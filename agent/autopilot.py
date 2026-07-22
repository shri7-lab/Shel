import time
import subprocess
import threading
from datetime import datetime

from agent.tool_matcher import ToolMatcher
from agent.brain import Brain
from agent.learner import Learner

PHASE_NAMES = [
    "Reconnaissance",
    "Service Enumeration",
    "Vulnerability Analysis",
    "Exploitation",
    "Post-Exploitation",
    "Privilege Escalation",
    "Reporting",
]


class AutoPilot:
    def __init__(self, tool_runner, state, console, suppress_output=False):
        self.tool_runner = tool_runner
        self.state = state
        self.console = console
        self.suppress_output = suppress_output
        self.matcher = ToolMatcher()

        self.current_phase = 0
        self.target = ""
        self.running = False
        self.parsed_ports = []
        self.discovered_creds = []
        self.foothold_type = None
        self.foothold_info = {}
        self.start_time = None
        self.completed_phases = set()

        self.brain = None
        self.learner = None
        self.swarm = None

    def set_swarm(self, sub_agents):
        self.swarm = sub_agents

    def start_brain(self, target, scan_type="standard"):
        self.target = target
        self.running = True
        self.start_time = time.time()
        self.learner = Learner()

        from agent.sub_agent_runner import SubAgentRunner
        if self.swarm is None:
            from agent.llm import LLM
            self.swarm = SubAgentRunner(
                llm=LLM(),
                tool_runner=self.tool_runner,
                state=self.state,
                console=self.console,
            )

        self.brain = Brain(
            tool_runner=self.tool_runner,
            state=self.state,
            console=self.console,
            learner=self.learner,
        )
        self.state.targets = [target]
        self.state.add_finding("target", target, "high", "user")
        self.log("Brain mode engaged — autonomous reasoning loop", "phase")

        if scan_type == "fast":
            self.brain.add_goal("port scan", target, priority=9)
        elif scan_type == "deep":
            deep_goal = self.brain.add_goal("port scan", target, priority=9)
            deep_goal.max_attempts = 3
        else:
            self.brain.add_goal("port scan", target, priority=9)

        self.brain.start(target)
        self.tool_runner.brain = self.brain
        return self.brain

    def stop_brain(self):
        self.running = False
        if self.brain:
            self.brain.stop()
        if self.tool_runner:
            self.tool_runner.brain = None
        self.log("Brain stopped", "fail")

    def brain_status(self):
        if self.brain and self.brain.running:
            return self.brain.status()
        return {"running": False}

    def log(self, msg, style="white"):
        if not self.suppress_output:
            ts = datetime.now().strftime("%H:%M:%S")
            s = {
                "info": "cyan", "found": "green", "vuln": "red",
                "phase": "yellow", "creds": "magenta",
                "success": "bold green", "fail": "red",
            }.get(style, "white")
            self.console.print(f"[dim][{ts}][/dim] [{s}]{msg}[/{s}]")

    def run_bash(self, cmd, timeout=180):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
            return (result.stdout + result.stderr).strip() or "(no output)"
        except subprocess.TimeoutExpired:
            return "(timeout)"
        except Exception as e:
            return f"(error: {e})"

    def start(self, target, scan_type="standard"):
        self.target = target
        self.running = True
        self.start_time = time.time()
        self.state.targets = [target]
        self.state.add_finding("target", target, "high", "user")

        self._header(f"AutoPilot engaged — Target: {target}")

        self._phase_recon(scan_type)
        if not self.running: return
        self._phase_enumeration()
        if not self.running: return
        self._phase_vuln_analysis()
        if not self.running: return
        self._phase_exploitation()
        if not self.running: return
        self._phase_post_exploit()
        if not self.running: return
        self._phase_privesc()
        if not self.running: return
        self._phase_reporting()

        elapsed = time.time() - self.start_time
        self.log(f"AutoPilot complete in {elapsed:.0f}s", "success")

    def stop(self):
        self.running = False
        self.log("AutoPilot stopped by user", "fail")

    def _header(self, msg):
        if not self.suppress_output:
            self.console.rule(f"[bold yellow]{msg}[/bold yellow]")

    def _next_phase(self):
        self.current_phase += 1
        if self.current_phase < len(PHASE_NAMES):
            self.log(f"Phase {self.current_phase + 1}/{len(PHASE_NAMES)}: {PHASE_NAMES[self.current_phase]}", "phase")
            self.state.current_phase = PHASE_NAMES[self.current_phase].lower().replace(" ", "_")

    # ═══════════════════════════════════════════════
    # PHASE 1: RECONNAISSANCE
    # ═══════════════════════════════════════════════

    def _phase_recon(self, scan_type):
        self._next_phase()
        self.completed_phases.add(0)

        if scan_type == "fast":
            nmap_cmd = f"nmap -sC -sV -T4 --top-ports 1000 {self.target}"
        elif scan_type == "deep":
            nmap_cmd = f"nmap -sC -sV -T4 -p- {self.target}"
        else:
            nmap_cmd = f"nmap -sC -sV -T4 {self.target}"

        self.log(f"Running: {nmap_cmd}", "info")
        output = self.run_bash(nmap_cmd, 300)
        self.parsed_ports = []
        self.service_versions = {}

        from agent.output_parser import parse_nmap
        parsed = parse_nmap(output)
        self.parsed_ports = parsed["ports"]

        if parsed["os"]:
            self.log(f"OS Detection: {parsed['os']}", "found")
            self.state.add_finding("os", parsed["os"], "high", "nmap")
        if parsed["hostname"]:
            self.log(f"Hostname: {parsed['hostname']}", "info")

        if not parsed["ports"]:
            self.log("No open ports found. Trying full port scan...", "fail")
            fallback = self.run_bash(f"nmap -p- -T4 {self.target}", 600)
            parsed = parse_nmap(fallback)
            self.parsed_ports = parsed["ports"]
            if not parsed["ports"]:
                self.log("Target appears to be down or firewalled.", "fail")
                self.running = False
                return

        for p in parsed["ports"]:
            extra = f" - {p['version']}" if p.get("version") else ""
            self.log(f"  Port {p['port']}/{p['protocol']}: {p['service']}{extra}", "info")
            self.state.add_finding("port", f"Port {p['port']}/{p['protocol']}: {p['service']}{extra}",
                                   "high" if p["state"] == "open" else "medium", "nmap")
        self.log(f"Found {len(parsed['ports'])} open ports", "found")

    # ═══════════════════════════════════════════════
    # PHASE 2: SERVICE ENUMERATION (UNIVERSAL)
    # ═══════════════════════════════════════════════

    def _phase_enumeration(self):
        self._next_phase()
        self.completed_phases.add(1)

        for pinfo in self.parsed_ports:
            if not self.running:
                return
            self._enumerate_service(pinfo)

    def _enumerate_service(self, pinfo):
        port = pinfo["port"]
        service = pinfo["service"]
        self.log(f"Enumerating port {port} ({service})...", "info")

        matches = self.matcher.execute_match(self.target, port, service)

        for m in matches:
            if not self.running:
                return
            tool = m["tool"]
            cmd = m["command"]
            raw = m.get("raw", "")
            parsed = m.get("parsed", {})

            if cmd and raw:
                self.log(f"  [{tool}]: ran command", "info")
            if parsed:
                self._record_parsed_findings(tool, port, parsed)

    def _record_parsed_findings(self, tool, port, parsed):
        if not isinstance(parsed, dict):
            return
        for key, val in parsed.items():
            if isinstance(val, list) and val:
                self.log(f"  [{tool}] {key}: {', '.join(str(v)[:60] for v in val[:5])}", "found")
                for item in val[:10]:
                    self.state.add_finding(tool, f"port {port}: {item}", "high", tool)
            elif isinstance(val, str) and val:
                self.log(f"  [{tool}] {key}: {val[:120]}", "found")
                self.state.add_finding(tool, f"port {port}: {key}={val[:80]}", "high", tool)

    # ═══════════════════════════════════════════════
    # PHASE 3: VULNERABILITY ANALYSIS
    # ═══════════════════════════════════════════════

    def _phase_vuln_analysis(self):
        self._next_phase()
        self.completed_phases.add(2)

        self.log("Running low-hanging fruit checks...", "info")
        try:
            from modules.low_hanging import run_all_checks
            checks = run_all_checks(self.target)
            for c in checks:
                items = c if isinstance(c, list) else [c]
                for item in items:
                    self.log(f"  [+] {item['description']}", "found")
                    self.state.add_finding("low_hanging", item["description"], item["confidence"], item["service"])
        except ImportError:
            self.log("  Low-hanging checks module not available", "info")

        self.log("Running nuclei vulnerability scan...", "info")
        nuclei_out = self.run_bash(
            f"nuclei -u http://{self.target} -severity critical,high,medium -silent 2>/dev/null | head -20", 120
        )
        if nuclei_out and nuclei_out.strip() and "(no output)" not in nuclei_out:
            from agent.output_parser import parse_nuclei
            for f in parse_nuclei(nuclei_out)[:10]:
                sev = f.get("severity", "?")
                self.log(f"  Nuclei: [{sev}] {f.get('template', '?')}", "vuln")
                self.state.add_finding("nuclei", f"{sev}: {f.get('template', '?')}", sev, "nuclei")

        self._run_universal_vuln_scan()

    def _run_universal_vuln_scan(self):
        for pinfo in self.parsed_ports[:3]:
            if not self.running:
                return
            port = pinfo["port"]
            service = pinfo["service"]
            matches = self.matcher.match_tools("vulnerability scan", self.target, port=port, service=service)
            for m in matches[:2]:
                cmd = m["command"]
                self.log(f"  Running vuln scan on port {port} via {m['tool']}", "info")
                out = self.run_bash(cmd, 120)
                parsed = self.matcher._try_parse(out, m["parsers"], m["tool"])
                self._record_parsed_findings(m["tool"], port, parsed)

    # ═══════════════════════════════════════════════
    # PHASE 4: EXPLOITATION (UNIVERSAL)
    # ═══════════════════════════════════════════════

    def _phase_exploitation(self):
        self._next_phase()
        self.completed_phases.add(3)

        for pinfo in self.parsed_ports:
            if not self.running:
                return
            port = pinfo["port"]
            service = pinfo["service"]
            version = pinfo.get("version", "")
            if not version:
                continue

            self.log(f"Searching exploits for {service} {version} on port {port}...", "info")
            matches = self.matcher.match_tools("exploit search", version, port=port, service=service)
            for m in matches[:2]:
                out = self.run_bash(m["command"], 30)
                if out and "(no output)" not in out and "error" not in out.lower()[:60]:
                    self.log(f"  [{m['tool']}] {out[:200]}", "info")
                    self.state.add_finding("exploit", f"{service} {version}: {out[:100]}", "high", m["tool"])

        self._try_ssh_with_discovered_creds()

    def _try_ssh_with_discovered_creds(self):
        if not self.discovered_creds or self.foothold_type:
            return
        for cred in self.discovered_creds:
            self.log(f"  Trying {cred['user']}:{cred['pass']} via SSH ({self.target}:22)...", "info")
            out = self.run_bash(
                f'sshpass -p "{cred["pass"]}" ssh -o StrictHostKeyChecking=no {cred["user"]}@{self.target} "id; hostname" 2>/dev/null',
                20,
            )
            if out and "error" not in out.lower()[:60] and out.strip():
                self.log(f"  SSH login SUCCESS with {cred['user']}:{cred['pass']}!", "success")
                self.foothold_type = "ssh"
                self.foothold_info = {"user": cred["user"], "pass": cred["pass"], "target": self.target}
                self.state.add_finding("foothold", f"SSH: {cred['user']}@{self.target} pass:{cred['pass']}", "high", "autopilot")
                break

    # ═══════════════════════════════════════════════
    # PHASE 5: POST-EXPLOITATION
    # ═══════════════════════════════════════════════

    def _phase_post_exploit(self):
        self._next_phase()
        self.completed_phases.add(4)
        if not self.foothold_type:
            self.log("No foothold — skipping post-exploit", "info")
            return

        self.log(f"Foothold: {self.foothold_type} — {self.foothold_info.get('user', '?')}@{self.target}", "success")
        if self.foothold_type == "ssh":
            u = self.foothold_info["user"]
            p = self.foothold_info["pass"]
            ssh_cmd = f'sshpass -p "{p}" ssh -o StrictHostKeyChecking=no {u}@{self.target}'

            out = self.run_bash(
                f'{ssh_cmd} "cat ~/user.txt ~/Desktop/user.txt ~/Documents/user.txt 2>/dev/null; '
                f'find /home -name user.txt -exec cat {{}} \\; 2>/dev/null"', 20
            )
            if out:
                for line in out.split("\n"):
                    line = line.strip()
                    if line and len(line) > 10:
                        self.log(f"  FLAG: {line}", "success")
                        self.state.add_finding("flag", line, "high", "post_exploit")

            root_out = self.run_bash(f'{ssh_cmd} "cat /root/flag.txt 2>/dev/null; find /root -name flag.txt -exec cat {{}} \\; 2>/dev/null"', 15)
            if root_out:
                for line in root_out.split("\n"):
                    line = line.strip()
                    if line and len(line) > 10:
                        self.log(f"  ROOT FLAG: {line}", "success")
                        self.state.add_finding("flag", line, "high", "post_exploit")

    # ═══════════════════════════════════════════════
    # PHASE 6: PRIVILEGE ESCALATION
    # ═══════════════════════════════════════════════

    def _phase_privesc(self):
        self._next_phase()
        self.completed_phases.add(5)
        if not self.foothold_type:
            self.log("No foothold — skipping privesc", "info")
            return

        self.log("Running Linux privesc enumeration...", "info")
        if self.foothold_type == "ssh":
            u = self.foothold_info["user"]
            p = self.foothold_info["pass"]
            ssh_cmd = f'sshpass -p "{p}" ssh -o StrictHostKeyChecking=no {u}@{self.target}'
            out = self.run_bash(
                f'{ssh_cmd} "uname -a; id; sudo -l 2>/dev/null; '
                f'find / -perm -4000 -type f 2>/dev/null | head -10"', 20
            )
            if out:
                if "root" in out and "NOPASSWD" in out:
                    self.log("  User has sudo (NOPASSWD) — potential privesc!", "vuln")
                    self.state.add_finding("privesc", "sudo NOPASSWD access", "high", "autopilot")
                if "python" in out or "perl" in out:
                    self.log("  SUID binaries like python/perl found — check GTFOBins", "vuln")

    # ═══════════════════════════════════════════════
    # PHASE 7: REPORTING
    # ═══════════════════════════════════════════════

    def _phase_reporting(self):
        self._next_phase()
        self.completed_phases.add(6)
        elapsed = time.time() - self.start_time

        self._header("Engagement Summary")
        self.log(f"Target: {self.target}", "info")
        self.log(f"Duration: {elapsed:.0f}s", "info")
        self.log(f"Phases completed: {len(self.completed_phases)}/7", "info")
        self.log(f"Open ports found: {len(self.parsed_ports)}", "info")
        self.log(f"Findings: {len(self.state.findings)}", "info")
        self.log(f"Foothold: {'YES (' + self.foothold_type + ')' if self.foothold_type else 'Not established'}", "success" if self.foothold_type else "fail")

        key_findings = [f for f in self.state.findings if f.confidence in ("high", "medium")]
        if key_findings:
            self.log("Key findings:", "phase")
            for f in key_findings[-15:]:
                self.log(f"  [{f.confidence}] {f.type}: {f.detail[:100]}", "info")

        self.log("AutoPilot mission complete.", "success")
