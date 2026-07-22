import re
import json


class SupplyChainRecon:
    DEPENDENCY_FILES = {
        "package.json": "npm",
        "requirements.txt": "pip",
        "Pipfile": "pipenv",
        "Pipfile.lock": "pipenv",
        "Cargo.toml": "cargo",
        "Cargo.lock": "cargo",
        "go.mod": "go",
        "go.sum": "go",
        "Gemfile": "bundler",
        "Gemfile.lock": "bundler",
        "build.gradle": "gradle",
        "pom.xml": "maven",
        "composer.json": "composer",
        "yarn.lock": "yarn",
        " nuget.config": "nuget",
        "packages.config": "nuget",
    }

    CI_FILES = [
        ".github/workflows/",
        ".gitlab-ci.yml",
        "Jenkinsfile",
        ".circleci/config.yml",
        ".travis.yml",
        "azure-pipelines.yml",
        "bitbucket-pipelines.yml",
        "Dockerfile",
        ".dockerfile",
    ]

    SECRET_PATTERNS = {
        "AWS Access Key": r"(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}",
        "AWS Secret Key": r"(?i)aws(.{0,20})?(?-i)['\"][0-9a-zA-Z\/+]{40}['\"]",
        "GitHub Token": r"(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,}",
        "GitLab Token": r"glpat-[A-Za-z0-9\-_]{20,}",
        "Slack Token": r"xox[baprs]-[0-9a-zA-Z\-]{10,}",
        "Discord Token": r"[NM][A-Za-z\d]{23}\.[xz][A-Za-z\d]{6}\.[A-Za-z\d]{27}",
        "Generic API Key": r"(?i)(api[_-]?key|apikey|secret[_-]?key|secretkey)['\"]?\s*[:=]\s*['\"][0-9a-zA-Z_\-]{16,}['\"]",
        "Private SSH Key": r"-----BEGIN (RSA|DSA|EC|OPENSSH|PGP) PRIVATE KEY-----",
        "JWT Token": r"eyJ[A-Za-z0-9_\-]+\.eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+",
        "Google OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com",
        "Heroku API Key": r"(?i)heroku.{0,20}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}",
        "npm Token": r"npm_[A-Za-z0-9]{36}",
        "PyPI Token": r"pypi-[A-Za-z0-9]\.[A-Za-z0-9_-]+",
        "Slack Webhook": r"https://hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+/[A-Za-z0-9]+",
    }

    CI_MISCONFIG_PATTERNS = [
        {
            "id": "PR_TARGET_UNPINNED",
            "name": "pull_request_target with unpinned action",
            "severity": "high",
            "pattern": r"pull_request_target.*\n.*uses:\s+[^@#\n]+?(?:\n|$)",
            "description": "pull_request_target runs in the context of the base repo with access to secrets. Unpinned actions can be swapped by an attacker.",
        },
        {
            "id": "SELF_HOSTED_RUNNER",
            "name": "Self-hosted runner in workflow",
            "severity": "high",
            "pattern": r"runs-on:\s+self-hosted",
            "description": "Self-hosted runners have access to internal network and may not be isolated. PRs can execute arbitrary code on them.",
        },
        {
            "id": "CHECKOUT_ON_PR_TARGET",
            "name": "actions/checkout on PR ref in pull_request_target",
            "severity": "critical",
            "pattern": r"pull_request_target.*\n.*uses:\s+actions/checkout.*\n.*ref:\s+\$\{\{",
            "description": "Checking out PR code in pull_request_target context gives attackers full execution with secret access.",
        },
        {
            "id": "UNPINNED_ACTION",
            "name": "Action not pinned to SHA",
            "severity": "medium",
            "pattern": r"uses:\s+[A-Za-z0-9\-_]+/[A-Za-z0-9\-_]+@[a-z]+",
            "description": "Actions should be pinned to a full commit SHA instead of a tag/branch to prevent tag-mutation attacks.",
        },
        {
            "id": "GITHUB_TOKEN_WRITE",
            "name": "GITHUB_TOKEN with write permissions",
            "severity": "medium",
            "pattern": r"permissions:\s*write-all",
            "description": "GITHUB_TOKEN should follow least privilege. Write-all grants unintended push/delete access.",
        },
        {
            "id": "DANGEROUS_TRIGGER",
            "name": "Workflow triggers on pull_request_target or issue_comment",
            "severity": "high",
            "pattern": r"(issue_comment|pull_request_target|issues):",
            "description": "These triggers allow outside contributors to trigger workflows with secret access.",
        },
        {
            "id": "ENV_INJECTION",
            "name": "User-controlled input in env context",
            "severity": "high",
            "pattern": r"env:\s*\n.*\${{.*github\.event",
            "description": "GitHub event data can contain user-controlled content. Using it in env can lead to command injection.",
        },
        {
            "id": "SCRIPT_INJECTION",
            "name": "Event data in run command",
            "severity": "high",
            "pattern": r"run:.*\${{.*github\.event\.",
            "description": "Using github.event context in shell commands allows injection via PR body, title, or branch name.",
        },
        {
            "id": "REUSABLE_WORKFLOW",
            "name": "Reusable workflow from external repo",
            "severity": "medium",
            "pattern": r"uses:\s+[A-Za-z0-9\-_]+/[A-Za-z0-9\-_]+/.+@",
            "description": "Reusable workflows from external repos can be compromised. Pin to SHA.",
        },
    ]

    def __init__(self):
        self.findings = []

    def scan_dependency_file(self, content, filename=""):
        findings = []
        if not content:
            return findings
        ext = filename.split("/")[-1] if filename else ""
        system = self.DEPENDENCY_FILES.get(ext) or self._guess_package_manager(content)
        if system == "npm":
            findings.extend(self._scan_npm(content))
        elif system == "pip":
            findings.extend(self._scan_pip(content))
        elif system == "cargo":
            findings.extend(self._scan_cargo(content))
        findings.append({
            "type": "dependency_file",
            "system": system or "unknown",
            "file": filename,
            "severity": "info",
            "message": f"Found {system or 'unknown'} dependency file: {filename}",
        })
        return findings

    def _guess_package_manager(self, content):
        if '"dependencies"' in content or '"devDependencies"' in content:
            return "npm"
        if "==" in content and content.strip().startswith(("#", "")):
            return "pip"
        if "[dependencies]" in content:
            return "cargo"
        return "unknown"

    def _scan_npm(self, content):
        findings = []
        try:
            data = json.loads(content)
            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
            for name, version in deps.items():
                if version.startswith("*") or version.startswith(">=") or version.startswith("^0."):
                    findings.append({
                        "type": "loose_dependency",
                        "package": name,
                        "version": version,
                        "severity": "medium",
                        "message": f"Loose version pinning: {name}@{version} — risk of pulling compromised update",
                    })
                if version == "" or version == "*":
                    findings.append({
                        "type": "wildcard_dependency",
                        "package": name,
                        "version": version,
                        "severity": "high",
                        "message": f"Wildcard version: {name} — any version may be installed",
                    })
            scripts = data.get("scripts", {})
            for script_name, script_cmd in scripts.items():
                if any(kw in script_cmd.lower() for kw in ["curl", "wget", "bash", "eval", "exec", "download"]):
                    findings.append({
                        "type": "dangerous_script",
                        "script": script_name,
                        "command": script_cmd,
                        "severity": "high",
                        "message": f"Dangerous install script '{script_name}': {script_cmd}",
                    })
        except json.JSONDecodeError:
            pass
        return findings

    def _scan_pip(self, content):
        findings = []
        for line in content.split("\n"):
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("-"):
                continue
            if "==" in line:
                pkg, ver = line.split("==", 1)
                findings.append({
                    "type": "pinned_dependency",
                    "package": pkg.strip(),
                    "version": ver.strip(),
                    "severity": "low",
                    "message": f"Pinned: {pkg}=={ver}",
                })
            elif ">=" in line or ">" in line or "<=" in line or "<" in line:
                findings.append({
                    "type": "loose_dependency",
                    "package": line.split(">")[0].split("<")[0].strip(),
                    "version": line,
                    "severity": "medium",
                    "message": f"Loose pin: {line} — may pull compromised update",
                })
            else:
                pkg = line.split("[")[0].strip()
                findings.append({
                    "type": "unpinned_dependency",
                    "package": pkg,
                    "version": "any",
                    "severity": "high",
                    "message": f"Unpinned: {pkg} — any version may be installed",
                })
        return findings

    def _scan_cargo(self, content):
        findings = []
        in_deps = False
        for line in content.split("\n"):
            stripped = line.strip()
            if stripped.startswith("[dependencies"):
                in_deps = True
                continue
            if in_deps and stripped.startswith("["):
                in_deps = False
                continue
            if in_deps and "=" in stripped:
                parts = stripped.split("=", 1)
                pkg = parts[0].strip().strip('"')
                ver = parts[1].strip().strip('"').strip(',')
                if ver == "*" or ver.startswith(">") or ver == "":
                    findings.append({
                        "type": "loose_dependency",
                        "package": pkg,
                        "version": ver,
                        "severity": "medium",
                        "message": f"Loose pin: {pkg} = {ver}",
                    })
        return findings

    def scan_for_secrets(self, content, filename=""):
        findings = []
        if not content:
            return findings
        for secret_type, pattern in self.SECRET_PATTERNS.items():
            matches = re.findall(pattern, content)
            for m in matches[:5]:
                masked = m[:8] + "..." + m[-4:] if len(m) > 12 else m[:4] + "..."
                findings.append({
                    "type": "secret_leak",
                    "secret_type": secret_type,
                    "match": masked,
                    "file": filename,
                    "severity": "critical",
                    "message": f"Potential {secret_type} leak: {masked}",
                })
        return findings

    def scan_ci_workflow(self, content, filename=""):
        findings = []
        if not content:
            return findings
        for config in self.CI_MISCONFIG_PATTERNS:
            if re.search(config["pattern"], content, re.MULTILINE):
                findings.append({
                    "type": "ci_misconfig",
                    "id": config["id"],
                    "name": config["name"],
                    "file": filename,
                    "severity": config["severity"],
                    "message": config["description"],
                })
        findings.append({
            "type": "ci_file",
            "file": filename,
            "severity": "info",
            "message": f"Found CI/CD file: {filename}",
        })
        return findings

    def analyze_repo_structure(self, repo_files):
        all_findings = []
        for filepath, content in repo_files.items():
            for ci_prefix in self.CI_FILES:
                if filepath.startswith(ci_prefix) or filepath == ci_prefix.rstrip("/"):
                    all_findings.extend(self.scan_ci_workflow(content, filepath))
                    break
            if filepath.split("/")[-1] in self.DEPENDENCY_FILES:
                all_findings.extend(self.scan_dependency_file(content, filepath))
            all_findings.extend(self.scan_for_secrets(content, filepath))
        return all_findings

    def flag_confusion_candidates(self, dependency_list):
        candidates = []
        internal_patterns = [r'corp[.-]', r'internal[.-]', r'private[.-]', r'com[.][a-z]+\.[a-z]+']
        for dep_name in dependency_list:
            score = 0
            for pat in internal_patterns:
                if re.search(pat, dep_name, re.IGNORECASE):
                    score += 1
            if score > 0:
                candidates.append({
                    "name": dep_name,
                    "confidence": "high" if score >= 2 else "medium",
                    "reason": "Looks like an internal package name (possible dependency confusion target)",
                })
            if dep_name.count("-") >= 3 or dep_name.count("_") >= 3:
                candidates.append({
                    "name": dep_name,
                    "confidence": "low",
                    "reason": "Unusual naming pattern — possible private package",
                })
        return candidates

    def summarize(self, findings):
        if not findings:
            return "No findings."
        by_severity = {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0}
        by_type = {}
        for f in findings:
            by_severity[f["severity"]] = by_severity.get(f["severity"], 0) + 1
            ftype = f["type"]
            by_type[ftype] = by_type.get(ftype, 0) + 1
        lines = ["## Supply Chain Scan Summary"]
        lines.append(f"Total findings: {len(findings)}")
        lines.append(f"Critical: {by_severity.get('critical', 0)} | High: {by_severity.get('high', 0)} | Medium: {by_severity.get('medium', 0)} | Low: {by_severity.get('low', 0)}")
        lines.append("\n### By Type")
        for t, c in sorted(by_type.items(), key=lambda x: -x[1]):
            lines.append(f"- {t}: {c}")
        lines.append("\n### Critical & High")
        for f in findings:
            if f["severity"] in ("critical", "high"):
                lines.append(f"- [{f['severity'].upper()}] {f['message']}")
        return "\n".join(lines)
