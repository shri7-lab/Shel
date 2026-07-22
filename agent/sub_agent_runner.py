import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from agent.llm import LLM
from agent.sub_agents import SUB_AGENTS
from agent.tools import TOOL_DEFINITIONS

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
    "recon": "cyan", "exploit": "red", "privesc": "yellow",
    "lateral": "magenta", "exfil": "green", "distraction": "blue",
    "report": "white",
}


class SubAgentRunner:
    def __init__(self, llm, tool_runner=None, state=None, console=None):
        self.llm = llm
        self.tool_runner = tool_runner
        self.state = state
        self.console = console
        self.executor = ThreadPoolExecutor(max_workers=4)
        self._lock = threading.Lock()
        self.active = {}
        self.completed = {}
        self.blackboard = {
            "findings": [],
            "creds": [],
            "targets": {},
            "vulnerabilities": [],
            "footholds": [],
            "flags": [],
        }

    def log(self, msg, agent_type="swarm"):
        ts = datetime.now().strftime("%H:%M:%S")
        color = AGENT_COLORS.get(agent_type, "white")
        if self.console:
            self.console.print(f"[dim][{ts}][/dim] [{color}][{agent_type.upper()}][/] {msg}")

    def read_blackboard(self, key=None):
        with self._lock:
            if key:
                return list(self.blackboard.get(key, []))
            return dict(self.blackboard)

    def write_blackboard(self, key, value):
        with self._lock:
            if key not in self.blackboard:
                self.blackboard[key] = []
            if isinstance(value, list):
                self.blackboard[key].extend(value)
            else:
                self.blackboard[key].append(value)

    def run(self, agent_type, task, target=None, depends_on=None, wait=True, timeout=300):
        if wait:
            return self._run_sync(agent_type, task, target, depends_on, timeout)
        else:
            return self._run_async(agent_type, task, target, depends_on)

    def _run_sync(self, agent_type, task, target=None, depends_on=None, timeout=300):
        aid = self._run_async(agent_type, task, target, depends_on)
        result = self.wait_for(aid, timeout)
        return result

    def _run_async(self, agent_type, task, target=None, depends_on=None):
        aid = f"{agent_type}_{threading.get_ident()}_{id(task)}"
        full_task = f"Target: {target}\n\n{task}" if target else task

        info = {
            "id": aid, "type": agent_type, "task": task, "target": target,
            "status": "queued", "depends_on": depends_on or [],
            "started_at": None, "completed_at": None, "result": None,
        }
        with self._lock:
            self.active[aid] = info

        future = self.executor.submit(self._execute, aid, agent_type, full_task, timeout=300)
        info["future"] = future
        self.log(f"Deployed {agent_type} agent", agent_type)
        return aid

    def _execute(self, agent_id, agent_type, task, timeout=300):
        with self._lock:
            if agent_id in self.active:
                self.active[agent_id]["status"] = "running"
                self.active[agent_id]["started_at"] = time.time()

        system_prompt = SUB_AGENTS.get(agent_type, "")
        if not system_prompt:
            return {"error": f"No prompt for agent type: {agent_type}"}

        context = self._build_context(agent_type)
        full_prompt = f"{system_prompt}\n\n{context}\n\n## Task\n{task}"
        messages = [{"role": "user", "content": task}]

        try:
            resp = self.llm.send_with_tools(
                full_prompt, messages, TOOL_DEFINITIONS, self.tool_runner,
            )
            text_blocks = [b.text for b in resp.content if b.type == "text"]
            result_text = "\n\n".join(text_blocks) if text_blocks else "(no response)"

            extracted = self._extract_findings(result_text)

            for f in extracted.get("findings", []):
                self.write_blackboard("findings", f)
            for c in extracted.get("creds", []):
                self.write_blackboard("creds", c)
            for v in extracted.get("vulnerabilities", []):
                self.write_blackboard("vulnerabilities", v)

            with self._lock:
                if agent_id in self.active:
                    self.active[agent_id]["status"] = "completed"
                    self.active[agent_id]["completed_at"] = datetime.now().isoformat()
                    self.active[agent_id]["result"] = {"text": result_text, **extracted}
                    self.completed[agent_id] = dict(self.active[agent_id])
                    del self.active[agent_id]

            self.log(f"{agent_type} agent completed", agent_type)
            return result_text

        except Exception as e:
            with self._lock:
                if agent_id in self.active:
                    self.active[agent_id]["status"] = "failed"
                    self.active[agent_id]["completed_at"] = datetime.now().isoformat()
                    self.active[agent_id]["result"] = {"error": str(e)}
                    self.completed[agent_id] = dict(self.active[agent_id])
                    del self.active[agent_id]
            self.log(f"{agent_type} agent failed: {e}", agent_type)
            return f"Error: {e}"

    def _build_context(self, agent_type):
        import re
        parts = ["## Swarm Blackboard Context"]
        b = self.read_blackboard()

        if b.get("findings"):
            parts.append("\n### Active Findings")
            for f in b["findings"][-15:]:
                detail = str(f.get("detail", ""))[:100]
                parts.append(f"- [{f.get('type','?')}] {detail}")
        if b.get("creds"):
            parts.append("\n### Discovered Credentials")
            for c in b["creds"][-10:]:
                parts.append(f"- {c.get('user','?')}:{c.get('pass','?')} @ {c.get('target','?')}")
        if b.get("flags"):
            parts.append("\n### Flags Captured")
            for flag in b["flags"][-5:]:
                parts.append(f"- {str(flag)[:100]}")
        if b.get("vulnerabilities"):
            parts.append("\n### Known Vulnerabilities")
            for v in b["vulnerabilities"][-10:]:
                parts.append(f"- {str(v)[:100]}")

        return "\n".join(parts)

    def _extract_findings(self, text):
        import re
        extracted = {"findings": [], "creds": [], "vulnerabilities": []}
        if not text:
            return extracted

        cred_pats = [
            r"(?:user|username)[:\s]+(\S+)[,\s]+(?:pass|password)[:\s]+(\S+)",
            r"(?:^|\s*[-]\s*)(\S+)[:/\\](\S+)(?:\s*@\s*(\S+))?\s*$",
        ]
        for pat in cred_pats:
            for m in re.findall(pat, text, re.IGNORECASE | re.MULTILINE):
                cred = {"user": m[0], "pass": m[1]}
                if len(m) >= 3:
                    cred["target"] = m[2]
                extracted["creds"].append(cred)

        for m in re.findall(r"(CVE-\d{4}-\d{4,7})", text, re.IGNORECASE):
            extracted["vulnerabilities"].append(m)

        for line in text.split("\n"):
            line = line.strip()
            if not line:
                continue
            if re.search(r"(?:found|discovered|detected)\s*(?:\d+\s*)?(?:open\s*)?ports?", line, re.IGNORECASE):
                extracted["findings"].append({"type": "port", "detail": line[:200], "confidence": "high"})
            if "flag{" in line.lower() or "htb{" in line.lower():
                extracted["findings"].append({"type": "flag", "detail": line[:200], "confidence": "high"})
                extracted["flags"] = extracted.get("flags", []) + [line[:200]]

        return extracted

    def wait_for(self, agent_id, timeout=None):
        with self._lock:
            info = self.active.get(agent_id)
        if info and "future" in info:
            try:
                info["future"].result(timeout=timeout)
            except Exception:
                pass
        with self._lock:
            return self.completed.get(agent_id)

    def run_parallel(self, tasks):
        aids = []
        for agent_type, task, target in tasks:
            aid = self._run_async(agent_type, task, target)
            aids.append(aid)
        results = {}
        for aid in aids:
            self.wait_for(aid)
            with self._lock:
                if aid in self.completed:
                    results[aid] = self.completed[aid].get("result", {})
        return results

    def status(self):
        with self._lock:
            return {
                "active": {k: {"type": v["type"], "status": v["status"],
                               "task": v.get("task", "")[:60]}
                          for k, v in self.active.items()},
                "completed": len(self.completed),
                "findings": len(self.blackboard.get("findings", [])),
                "creds": len(self.blackboard.get("creds", [])),
            }

    def summary(self):
        s = self.status()
        lines = [f"## Swarm Status",
                 f"- **Active agents**: {len(s['active'])}",
                 f"- **Completed agents**: {s['completed']}",
                 f"- **Findings**: {s['findings']}",
                 f"- **Credentials**: {s['creds']}"]
        if s["active"]:
            lines.append("\n### Active")
            for aid, info in s["active"].items():
                lines.append(f"- {info['type']}: {info['status']} — {info['task']}")
        return "\n".join(lines)

    def deploy_chain(self, tasks):
        aids = []
        for agent_type, task, target in tasks:
            deps = AGENT_DEPENDENCIES.get(agent_type, [])
            dep_ids = [aid for dep in deps for aid in aids if aid.startswith(dep)]
            aid = self._run_async(agent_type, task, target)
            aids.append(aid)
        return aids


import time
