from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import datetime
import json


@dataclass
class Finding:
    type: str  # host, port, service, vuln, credential, flag, note
    detail: str
    confidence: str = "medium"  # high, medium, low
    source: str = ""
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


@dataclass
class Action:
    description: str
    status: str = "pending"  # pending, running, completed, failed
    result: str = ""
    command: str = ""
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


PHASES = [
    "recon",
    "enumeration",
    "vuln_analysis",
    "exploitation",
    "post_exploit",
    "privesc",
    "reporting",
]


class SessionState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.targets: list[str] = []
        self.current_phase: str = "recon"
        self.findings: list[Finding] = []
        self.completed_actions: list[Action] = []
        self.pending_actions: list[Action] = []
        self.current_action: Optional[Action] = None
        self.target_scope: list[str] = []
        self.session_log: list[dict] = []

    def add_finding(self, ftype: str, detail: str, confidence="medium", source=""):
        self.findings.append(Finding(ftype, detail, confidence, source))

    def add_pending(self, desc: str, command=""):
        self.pending_actions.append(Action(desc, "pending", command=command))

    def start_action(self, desc: str, command=""):
        a = Action(desc, "running", command=command)
        self.current_action = a
        return a

    def complete_action(self, result: str):
        if self.current_action:
            self.current_action.status = "completed"
            self.current_action.result = result
            self.completed_actions.append(self.current_action)
            self.current_action = None

    def fail_action(self, result: str):
        if self.current_action:
            self.current_action.status = "failed"
            self.current_action.result = result
            self.completed_actions.append(self.current_action)
            self.current_action = None

    def log_event(self, event_type: str, detail: str):
        self.session_log.append({
            "type": event_type,
            "detail": detail,
            "timestamp": datetime.now().isoformat(),
        })

    def to_prompt_block(self) -> str:
        lines = []
        lines.append("<attack_tree>")
        lines.append(f"Targets: {', '.join(self.targets) if self.targets else 'Not set'}")
        lines.append(f"Phase: {self.current_phase}")
        if self.target_scope:
            lines.append(f"Scope: {', '.join(self.target_scope)}")

        if self.findings:
            lines.append("\nFindings:")
            for f in self.findings[-15:]:
                lines.append(f"  [{f.confidence}] {f.type}: {f.detail[:120]}")

        if self.completed_actions:
            lines.append("\nCompleted actions (last 10):")
            for a in self.completed_actions[-10:]:
                status_mark = "✓" if a.status == "completed" else "✗"
                lines.append(f"  {status_mark} {a.description[:100]}")

        if self.pending_actions:
            lines.append("\nPending / suggested next steps:")
            for a in self.pending_actions:
                lines.append(f"  ☐ {a.description[:100]}")

        if self.current_action:
            lines.append(f"\nCurrently executing: {self.current_action.description[:100]}")

        lines.append("</attack_tree>")
        return "\n".join(lines)

    def advance_phase(self):
        idx = PHASES.index(self.current_phase) if self.current_phase in PHASES else 0
        if idx < len(PHASES) - 1:
            self.current_phase = PHASES[idx + 1]
