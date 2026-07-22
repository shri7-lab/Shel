import time
import uuid
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

from agent.sub_agents import SUB_AGENTS
from agent.tools import ToolRunner, TOOL_DEFINITIONS


AGENT_DEPENDENCIES = {
    "recon": [],
    "exploit": ["recon"],
    "privesc": ["exploit"],
    "lateral": ["exploit"],
    "exfil": ["exploit"],
    "distraction": ["recon"],
    "report": ["recon", "exploit", "privesc", "lateral", "exfil"],
}

AGENT_COLORS = {
    "recon": "cyan",
    "exploit": "red",
    "privesc": "yellow",
    "lateral": "magenta",
    "exfil": "green",
    "distraction": "blue",
    "report": "white",
}


class Swarm:
    def __init__(self, llm, tool_runner, state, console):
        self.llm = llm
        self.tool_runner = tool_runner
        self.state = state
        self.console = console

        self.blackboard = {
            "findings": [],
            "creds": [],
            "targets": {},
            "services": {},  # {target: {port: service_info}}
            "vulnerabilities": [],
            "footholds": [],
            "flags": [],
            "network_map": {},
            "agent_outputs": {},
        }
        self._lock = threading.Lock()
        self.active_agents = {}
        self.completed_agents = {}
        self.executor = ThreadPoolExecutor(max_workers=3)
        self.running = False

    def log(self, msg, agent_type="swarm"):
        ts = datetime.now().strftime("%H:%M:%S")
        color = AGENT_COLORS.get(agent_type, "white")
        if self.console:
            self.console.print(f"[dim][{ts}][/dim] [{color}][{agent_type.upper()}][/ {color}] {msg}")

    def read_blackboard(self, key=None):
        with self._lock:
            if key:
                return self.blackboard.get(key, [])
            return dict(self.blackboard)

    def write_blackboard(self, key, value):
        with self._lock:
            if key not in self.blackboard:
                self.blackboard[key] = []
            if isinstance(value, list):
                self.blackboard[key].extend(value)
            else:
                self.blackboard[key].append(value)

    def deploy(self, agent_type, task, target=None, depends_on=None, timeout=300):
        agent_id = f"{agent_type}_{uuid.uuid4().hex[:6]}"
        formatted_task = task
        if target:
            formatted_task = f"Target: {target}\n\n{task}"

        agent_info = {
            "id": agent_id,
            "type": agent_type,
            "task": task,
            "target": target,
            "status": "pending",
            "depends_on": depends_on or [],
            "started_at": None,
            "completed_at": None,
            "result": None,
        }

        with self._lock:
            self.active_agents[agent_id] = agent_info

        future = self.executor.submit(
            self._run_agent, agent_id, agent_type, formatted_task, timeout
        )
        agent_info["future"] = future
        agent_info["status"] = "queued"
        self.log(f"Deployed {agent_type} agent ({agent_id})", agent_type)
        return agent_id

    def _run_agent(self, agent_id, agent_type, task, timeout):
        with self._lock:
            if agent_id in self.active_agents:
                self.active_agents[agent_id]["status"] = "running"
                self.active_agents[agent_id]["started_at"] = time.time()

        system_prompt = SUB_AGENTS.get(agent_type, "")
        if not system_prompt:
            return {"error": f"No prompt for agent type: {agent_type}"}

        blackboard_snapshot = self.read_blackboard()
        context_parts = [f"## Swarm Blackboard Context\n"]
        if blackboard_snapshot.get("findings"):
            context_parts.append("### Active Findings")
            for f in blackboard_snapshot["findings"][-20:]:
                context_parts.append(f"- [{f.get('type','?')}] {str(f.get('detail',''))[:120]}")
        if blackboard_snapshot.get("creds"):
            context_parts.append("### Discovered Credentials")
            for c in blackboard_snapshot["creds"][-10:]:
                context_parts.append(f"- {c.get('user','?')}:{c.get('pass','?')} @ {c.get('target','?')}")
        if blackboard_snapshot.get("vulnerabilities"):
            context_parts.append("### Known Vulnerabilities")
            for v in blackboard_snapshot["vulnerabilities"][-10:]:
                context_parts.append(f"- {str(v)[:120]}")

        full_prompt = f"{system_prompt}\n\n{chr(10).join(context_parts)}\n\n## Current Task\n{task}"

        messages = [{"role": "user", "content": task}]

        try:
            resp = self.llm.send_with_tools(
                full_prompt,
                messages,
                TOOL_DEFINITIONS,
                self.tool_runner,
            )
            text_blocks = [b.text for b in resp.content if b.type == "text"]
            result_text = "\n\n".join(text_blocks) if text_blocks else "(no response)"

            extracted = self._extract_from_response(result_text, agent_type)

            with self._lock:
                if agent_id in self.active_agents:
                    self.active_agents[agent_id]["status"] = "completed"
                    self.active_agents[agent_id]["completed_at"] = time.time()
                    self.active_agents[agent_id]["result"] = {
                        "text": result_text,
                        **extracted,
                    }
                    self.completed_agents[agent_id] = dict(self.active_agents[agent_id])
                    del self.active_agents[agent_id]

            self.log(f"{agent_type} agent completed ({agent_id})", agent_type)
            return {"text": result_text, **extracted}

        except Exception as e:
            with self._lock:
                if agent_id in self.active_agents:
                    self.active_agents[agent_id]["status"] = "failed"
                    self.active_agents[agent_id]["completed_at"] = time.time()
                    self.active_agents[agent_id]["result"] = {"error": str(e)}
                    self.completed_agents[agent_id] = dict(self.active_agents[agent_id])
                    del self.active_agents[agent_id]
            self.log(f"{agent_type} agent failed: {e}", agent_type)
            return {"error": str(e)}

    def _extract_from_response(self, text, agent_type):
        extracted = {"findings": [], "creds": [], "vulnerabilities": []}
        if not text:
            return extracted

        import re

        cred_patterns = [
            r"(?:user|username)[:\s]+(\S+)[,\s]+(?:pass|password)[:\s]+(\S+)",
            r"(?:found|discovered).*?(?:cred|password|login)[:\s]*(\S+)[/\:](\S+)",
            r"(?:^|\s*[-]\s*)(\S+)[:/\\](\S+)(?:\s*@\s*(\S+))?\s*$",
        ]
        for pattern in cred_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
            for m in matches:
                if len(m) >= 2:
                    cred = {"user": m[0], "pass": m[1]}
                    if len(m) >= 3:
                        cred["target"] = m[2]
                    extracted["creds"].append(cred)

        vuln_patterns = [
            r"(CVE-\d{4}-\d{4,7})",
            r"(critical|high|medium)\s*(?:severity|vulnerability|risk)",
        ]
        for pattern in vuln_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for m in matches:
                extracted["vulnerabilities"].append(m)

        findings = self._parse_findings_from_text(text)
        extracted["findings"] = findings

        return extracted

    def _parse_findings_from_text(self, text):
        findings = []
        import re
        lines = text.split("\n")
        for line in lines:
            line = line.strip()
            if re.search(r"(?:found|discovered|detected|identified)\s*(?:\d+\s*)?(?:open\s*)?ports?", line, re.IGNORECASE):
                findings.append({"type": "port", "detail": line[:200], "confidence": "high"})
            if re.search(r"(?:user|username|account)\s*[:\s]", line, re.IGNORECASE) and len(line) < 100:
                if ":" in line and not line.startswith("http"):
                    parts = [p.strip() for p in line.split(":")]
                    findings.append({"type": "user", "detail": line[:150], "confidence": "medium"})
            if "flag{" in line.lower() or "htb{" in line.lower():
                findings.append({"type": "flag", "detail": line[:200], "confidence": "high"})
        return findings

    def wait_for_agent(self, agent_id, timeout=None):
        with self._lock:
            info = self.active_agents.get(agent_id) or self.completed_agents.get(agent_id)
        if not info:
            return None
        future = info.get("future")
        if future:
            try:
                future.result(timeout=timeout)
            except Exception:
                pass
        with self._lock:
            return self.completed_agents.get(agent_id) or self.active_agents.get(agent_id)

    def wait_for_all(self, timeout=None):
        with self._lock:
            agent_ids = list(self.active_agents.keys())
        for aid in agent_ids:
            self.wait_for_agent(aid, timeout)

    def deploy_chain(self, tasks):
        agent_ids = []
        for agent_type, task, target in tasks:
            deps = AGENT_DEPENDENCIES.get(agent_type, [])
            dep_ids = []
            for dep_type in deps:
                dep_ids.extend(
                    aid for aid in agent_ids
                    if aid.startswith(dep_type)
                )
            aid = self.deploy(agent_type, task, target, depends_on=dep_ids)
            agent_ids.append(aid)
        return agent_ids

    def get_findings(self, agent_type=None):
        all_findings = self.blackboard.get("findings", [])
        if agent_type:
            return [f for f in all_findings if f.get("source") == agent_type]
        return all_findings

    def get_creds(self):
        return self.blackboard.get("creds", [])

    def status(self):
        with self._lock:
            return {
                "active": {k: {"type": v["type"], "status": v["status"],
                               "task": v["task"][:80], "target": v.get("target")}
                          for k, v in self.active_agents.items()},
                "completed": len(self.completed_agents),
                "total_findings": len(self.blackboard.get("findings", [])),
                "total_creds": len(self.blackboard.get("creds", [])),
                "total_vulns": len(self.blackboard.get("vulnerabilities", [])),
            }

    def summary(self):
        s = self.status()
        lines = [
            "## Swarm Status",
            f"- **Active agents**: {len(s['active'])}",
            f"- **Completed agents**: {s['completed']}",
            f"- **Total findings**: {s['total_findings']}",
            f"- **Total credentials**: {s['total_creds']}",
            f"- **Total vulnerabilities**: {s['total_vulns']}",
        ]
        if s["active"]:
            lines.append("\n### Active Agents")
            for aid, info in s["active"].items():
                lines.append(f"- {info['type']}: {info['status']} — {info['task']}")
        return "\n".join(lines)
