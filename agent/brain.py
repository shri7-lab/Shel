import time
import uuid
import threading
from datetime import datetime
from collections import defaultdict

from agent.tool_matcher import ToolMatcher
from agent.learner import Learner

GOAL_TEMPLATES = {
    "discover targets": {"priority": 9, "description": "Find live hosts and open ports"},
    "port scan": {"priority": 9, "description": "Scan target for open ports"},
    "service enum": {"priority": 8, "description": "Enumerate service version and config"},
    "web recon": {"priority": 8, "description": "Reconnaissance on web services"},
    "web directory": {"priority": 7, "description": "Discover web directories and files"},
    "vuln scan": {"priority": 7, "description": "Scan for vulnerabilities"},
    "exploit search": {"priority": 7, "description": "Search for public exploits"},
    "brute force": {"priority": 6, "description": "Brute force authentication"},
    "enum smb": {"priority": 8, "description": "Enumerate SMB shares and users"},
    "enum ftp": {"priority": 7, "description": "Enumerate FTP service"},
    "enum ssh": {"priority": 7, "description": "Enumerate SSH service"},
    "enum ldap": {"priority": 8, "description": "Enumerate LDAP directory"},
    "enum nfs": {"priority": 8, "description": "Enumerate NFS exports"},
    "enum mysql": {"priority": 8, "description": "Enumerate MySQL database"},
    "enum mssql": {"priority": 8, "description": "Enumerate MSSQL database"},
    "enum redis": {"priority": 8, "description": "Enumerate Redis service"},
    "enum mongo": {"priority": 8, "description": "Enumerate MongoDB service"},
    "enum dns": {"priority": 7, "description": "Enumerate DNS records"},
    "enum smtp": {"priority": 6, "description": "Enumerate SMTP service"},
    "crack hash": {"priority": 5, "description": "Crack captured hashes"},
    "get foothold": {"priority": 9, "description": "Establish initial access"},
    "privesc": {"priority": 9, "description": "Escalate privileges to root/admin"},
    "lateral move": {"priority": 8, "description": "Move to adjacent hosts"},
    "dump creds": {"priority": 8, "description": "Dump credentials from compromised host"},
    "exfil data": {"priority": 5, "description": "Exfiltrate target data"},
    "cleanup": {"priority": 3, "description": "Remove traces of activity"},
}

TECHNIQUE_MAP = {
    "smb": [
        ("smbclient", "null_session"),
        ("smbmap", "enum_shares"),
        ("enum4linux", "all"),
        ("crackmapexec", "smb_enum"),
        ("hydra", "smb_brute"),
    ],
    "http": [
        ("whatweb", "detect_cms"),
        ("gobuster", "dir_scan"),
        ("nikto", "vuln_scan"),
        ("nuclei", "template_scan"),
        ("wpscan", "wp_enum"),
    ],
    "ftp": [
        ("ftp", "anonymous_login"),
        ("nmap", "ftp_script"),
        ("hydra", "ftp_brute"),
    ],
    "ssh": [
        ("ssh", "banner_grab"),
        ("nmap", "ssh_script"),
        ("hydra", "ssh_brute"),
    ],
    "mysql": [
        ("mysql", "no_password_root"),
        ("nmap", "mysql_script"),
        ("hydra", "mysql_brute"),
    ],
    "redis": [
        ("redis-cli", "info_grab"),
        ("nmap", "redis_script"),
    ],
    "ldap": [
        ("ldapsearch", "anonymous_bind"),
        ("nmap", "ldap_script"),
    ],
    "nfs": [
        ("showmount", "list_exports"),
        ("nmap", "nfs_script"),
    ],
    "dns": [
        ("dnsrecon", "std_enum"),
        ("dig", "any_record"),
    ],
    "port_scan": [
        ("nmap", "quick_scan"),
        ("nmap", "full_scan"),
    ],
}


class Goal:
    def __init__(self, objective, target, port=None, service=None,
                 priority=5, depends_on=None, max_attempts=2):
        self.id = str(uuid.uuid4())[:8]
        self.objective = objective
        self.target = target
        self.port = port
        self.service = service
        self.priority = priority
        self.depends_on = depends_on or []
        self.max_attempts = max_attempts
        self.status = "pending"
        self.created_at = time.time()
        self.completed_at = None
        self.result = {}
        self.attempts = 0
        self.error = None

    def key(self):
        return f"{self.objective}:{self.target}:{self.port}"

    def __lt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return f"Goal({self.objective} @ {self.target}:{self.port or '?'} pri={self.priority} status={self.status})"


class Brain:
    def __init__(self, tool_runner, state, console, learner=None):
        self.tool_runner = tool_runner
        self.matcher = ToolMatcher()
        self.state = state
        self.console = console
        self.learner = learner or Learner()

        self.goals = []
        self.blackboard = {
            "targets": set(),
            "ports": {},       # {target: {port: {service, version, state}}}
            "creds": [],       # [{user, pass, service, target}]
            "findings": [],    # [{type, detail, confidence}]
            "hosts": {},       # {target: {os, hostname, arch}}
            "subnets": set(),  # CIDR ranges discovered
            "footholds": [],   # [{target, user, method}]
        }
        self.running = False
        self._thread = None
        self._lock = threading.Lock()
        self.current_goal = None
        self.start_time = None

    def log(self, msg, style="info"):
        ts = datetime.now().strftime("%H:%M:%S")
        s_map = {
            "info": "cyan", "found": "green", "vuln": "red",
            "phase": "yellow", "creds": "magenta", "success": "bold green",
            "fail": "red", "goal": "white", "brain": "bold magenta",
        }
        s = s_map.get(style, "white")
        if self.console:
            self.console.print(f"[dim][{ts}][/dim] [{s}]{msg}[/{s}]")

    def add_goal(self, objective, target, port=None, service=None,
                 priority=None, depends_on=None, max_attempts=2):
        if objective in GOAL_TEMPLATES:
            template = GOAL_TEMPLATES[objective]
            if priority is None:
                priority = template["priority"]
        else:
            if priority is None:
                priority = 5

        with self._lock:
            for g in self.goals:
                if (g.objective == objective and g.target == target
                        and g.port == port and g.status in ("pending", "in_progress")):
                    return g

            goal = Goal(objective, target, port, service, priority, depends_on, max_attempts)
            self.goals.append(goal)
            self.goals.sort(key=lambda g: -g.priority)
            self.log(f"Goal added: {objective} @ {target}:{port or '?'} (pri={priority})", "goal")
            return goal

    def get_goal(self, goal_id):
        for g in self.goals:
            if g.id == goal_id:
                return g
        return None

    def remove_goal(self, goal_id):
        with self._lock:
            self.goals = [g for g in self.goals if g.id != goal_id]

    def _next_goal(self):
        ready = [g for g in self.goals
                 if g.status == "pending"
                 and all(self.get_goal(d) and self.get_goal(d).status == "completed"
                         for d in g.depends_on)]
        ready.sort(key=lambda g: -g.priority)
        return ready[0] if ready else None

    def start(self, target=None):
        self.running = True
        self.start_time = time.time()
        self.log("Brain initialized — autonomous reasoning loop engaged", "brain")

        if target:
            self.add_goal("discover targets", target)
            self.blackboard["targets"].add(target)

        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()
        return self

    def stop(self):
        self.running = False
        if self.current_goal:
            self.current_goal.status = "failed"
            self.current_goal.error = "stopped by user"
        elapsed = time.time() - self.start_time if self.start_time else 0
        self.log(f"Brain stopped after {elapsed:.0f}s — {len(self.goals)} goals processed", "brain")

    def wait(self, timeout=None):
        if self._thread:
            self._thread.join(timeout=timeout)

    def _run_loop(self):
        while self.running:
            try:
                goal = self._next_goal()
                if goal is None:
                    if all(g.status in ("completed", "failed") for g in self.goals):
                        self.log("All goals complete — Brain entering standby", "brain")
                        break
                    time.sleep(1)
                    continue

                self.current_goal = goal
                goal.status = "in_progress"
                goal.attempts += 1
                self.state.current_phase = f"brain_{goal.objective}"
                self.log(f"Working on: {goal.objective} @ {goal.target}:{goal.port or '?'}", "brain")

                actions = self._plan(goal)
                success = False

                for action in actions:
                    if not self.running:
                        break
                    result = self._execute(goal, action)
                    self._learn(goal, action, result)
                    self._update_blackboard(result)

                    if result.get("success"):
                        success = True
                        findings_for_goal = result.get("findings", [])
                        for f in findings_for_goal:
                            self._spawn_goals_from_finding(f)
                        break

                if success:
                    goal.status = "completed"
                    goal.completed_at = time.time()
                    self.log(f"Goal completed: {goal.objective} @ {goal.target}", "success")
                else:
                    if goal.attempts < goal.max_attempts:
                        goal.status = "pending"
                        goal.priority = max(1, goal.priority - 1)
                        self.log(f"Goal retrying: {goal.objective} (attempt {goal.attempts}/{goal.max_attempts})", "fail")
                    else:
                        goal.status = "failed"
                        goal.completed_at = time.time()
                        self.log(f"Goal failed: {goal.objective} @ {goal.target}", "fail")

                self.current_goal = None
                self.goals.sort(key=lambda g: -g.priority)

            except Exception as e:
                self.log(f"Brain error: {e}", "fail")
                if self.current_goal:
                    self.current_goal.error = str(e)
                    self.current_goal.status = "failed"
                    self.current_goal = None
                time.sleep(1)

    def _plan(self, goal):
        if goal.port and goal.service:
            svc = goal.service.lower()
        elif goal.port:
            port_svc = {21: "ftp", 22: "ssh", 80: "http", 443: "https",
                        445: "smb", 389: "ldap", 3306: "mysql", 6379: "redis",
                        27017: "mongo", 2049: "nfs", 53: "dns"}
            svc = port_svc.get(goal.port, "unknown")
        else:
            svc = None

        techniques = TECHNIQUE_MAP.get(svc, [])
        if not techniques and goal.objective == "port scan":
            techniques = TECHNIQUE_MAP.get("port_scan", [])

        if not techniques:
            default_obj_tech = {
                "discover targets": [("nmap", "quick_scan")],
                "vuln scan": [("nuclei", "template_scan"), ("nikto", "vuln_scan")],
                "brute force": [("hydra", "ssh_brute")],
                "exploit search": [("searchsploit", "search")],
                "crack hash": [("hashcat", "auto"), ("john", "auto")],
                "get foothold": [("ssh", "try_creds"), ("hydra", "ssh_brute")],
                "privesc": [("ssh", "enum_sudo"), ("ssh", "enum_suid")],
            }
            techniques = default_obj_tech.get(goal.objective, [])

        if goal.target in self.blackboard.get("targets", set()):
            target_os = self.blackboard.get("hosts", {}).get(goal.target, {}).get("os")
        else:
            target_os = None

        ranked = []
        for tool, technique in techniques:
            skip = self.learner.should_skip(tool, technique, goal.port or 0, target_os)
            best = self.learner.best_technique(goal.port or 0, target_os)
            rank = 1.0

            for b in best:
                if b.get("tool") == tool and b.get("technique") == technique:
                    rank = b.get("success_rate", 0.5)
                    break

            ranked.append((rank, tool, technique, skip))

        ranked.sort(key=lambda x: -x[0])

        actions = []
        for rank, tool, technique, skip in ranked:
            if skip:
                continue
            match = self.matcher.match_tools(tool, goal.target, port=goal.port, service=svc)
            for m in match[:1]:
                actions.append({
                    "tool": tool,
                    "technique": technique,
                    "command": m.get("command", ""),
                    "target": goal.target,
                    "port": goal.port,
                    "service": svc,
                    "parsers": m.get("parsers", []),
                })

        return actions

    def _execute(self, goal, action):
        start = time.time()
        tool = action["tool"]
        cmd = action["command"]
        target = action["target"]
        technique = action["technique"]

        self.log(f"  [{tool}] {technique} on {target}", "info")

        if self.state:
            self.state.start_action(f"brain: {tool} {technique} on {target}")

        if self.tool_runner and cmd:
            try:
                output = self.tool_runner.run("bash", {"command": cmd})
            except Exception as e:
                output = f"error: {e}"
        else:
            output = "(no command generated)"

        duration = time.time() - start
        output_str = str(output) if output else ""

        findings = self._extract_findings(action, output_str)
        success = bool(findings) or ("error" not in output_str.lower()[:30]
                                      and output_str
                                      and "(no output)" not in output_str
                                      and output_str != "error executing bash")

        if self.state:
            self.state.complete_action(output_str[:500])

        result = {
            "tool": tool,
            "technique": technique,
            "target": target,
            "command": cmd[:200],
            "output": output_str[:2000],
            "duration": duration,
            "success": success,
            "findings": findings,
        }
        return result

    def _extract_findings(self, action, output):
        findings = []
        if not output or "(no output)" in output:
            return findings
        tool = action["tool"]
        port = action.get("port")
        svc = action.get("service")

        parsed = self.matcher._try_parse(output, action.get("parsers", []), tool)
        if isinstance(parsed, dict):
            for key, val in parsed.items():
                if isinstance(val, list) and val:
                    for item in val[:5]:
                        findings.append({
                            "type": key,
                            "detail": str(item)[:150],
                            "confidence": "high",
                            "tool": tool,
                            "port": port,
                        })
                elif isinstance(val, str) and val:
                    findings.append({
                        "type": key,
                        "detail": val[:150],
                        "confidence": "high",
                        "tool": tool,
                        "port": port,
                    })
        return findings

    def _update_blackboard(self, result):
        for f in result.get("findings", []):
            self.blackboard.setdefault("findings", []).append(f)
            if self.state:
                self.state.add_finding(
                    f.get("type", "brain"),
                    f.get("detail", ""),
                    f.get("confidence", "medium"),
                    f.get("tool", "brain"),
                )
            port = f.get("port")
            ftype = f.get("type", "")
            detail = f.get("detail", "")

            if ftype == "user" and detail:
                self.blackboard.setdefault("creds", []).append({
                    "user": detail.split(":")[0] if ":" in detail else detail,
                    "source": result.get("tool", "?"),
                    "target": result.get("target", "?"),
                })
            if ftype == "cred" or ftype == "password":
                parts = detail.split(":")
                if len(parts) >= 2:
                    self.blackboard.setdefault("creds", []).append({
                        "user": parts[0],
                        "pass": ":".join(parts[1:]),
                        "target": result.get("target", "?"),
                        "service": result.get("tool", "?"),
                    })
            if ftype == "os" and detail:
                target = result.get("target", "").split(":")[0]
                self.blackboard.setdefault("hosts", {})[target] = {
                    "os": detail,
                    "source": result.get("tool", "brain"),
                }

    def _spawn_goals_from_finding(self, finding):
        ftype = finding.get("type", "")
        detail = finding.get("detail", "")
        port = finding.get("port")

        if ftype == "port" and detail:
            for g in self.goals:
                if g.objective == "service enum" and g.port == port:
                    return

        if ftype in ("cred", "password"):
            target = self.blackboard.get("targets")
            for t in list(target)[:1]:
                self.add_goal("get foothold", t)

        if ftype == "smb_share":
            target = list(self.blackboard.get("targets", set()))[:1]
            if target:
                self.add_goal("get foothold", target[0])

        if ftype == "foothold" and detail:
            for t in list(self.blackboard.get("targets", set()))[:1]:
                self.add_goal("privesc", t)

    def _learn(self, goal, action, result):
        target = goal.target
        target_os = self.blackboard.get("hosts", {}).get(target, {}).get("os")
        port = goal.port or 0
        svc = goal.service or action.get("service", "")
        tool = action["tool"]
        technique = action["technique"]
        success = result.get("success", False)
        duration = result.get("duration", 0)
        output = result.get("output", "")

        self.learner.record(
            target=target,
            target_os=target_os,
            port=port,
            service=svc,
            tool=tool,
            technique=technique,
            success=success,
            duration=duration,
            output=output,
        )

    def status(self):
        return {
            "running": self.running,
            "total_goals": len(self.goals),
            "pending": sum(1 for g in self.goals if g.status == "pending"),
            "in_progress": sum(1 for g in self.goals if g.status == "in_progress"),
            "completed": sum(1 for g in self.goals if g.status == "completed"),
            "failed": sum(1 for g in self.goals if g.status == "failed"),
            "current": str(self.current_goal) if self.current_goal else None,
            "goals": [{"id": g.id, "objective": g.objective, "target": g.target,
                        "port": g.port, "priority": g.priority, "status": g.status,
                        "attempts": g.attempts} for g in self.goals],
            "targets": list(self.blackboard.get("targets", set())),
            "creds": len(self.blackboard.get("creds", [])),
            "findings": len(self.blackboard.get("findings", [])),
            "learner_experiences": self.learner.total_experiences(),
            "learner_summary": self.learner.summary(),
            "uptime": time.time() - self.start_time if self.start_time else 0,
        }

    def add_to_blackboard(self, key, value):
        with self._lock:
            if key == "targets":
                self.blackboard.setdefault("targets", set()).add(value)
            elif key == "creds":
                self.blackboard.setdefault("creds", []).append(value)
            elif key == "findings":
                self.blackboard.setdefault("findings", []).append(value)
            else:
                self.blackboard[key] = value
