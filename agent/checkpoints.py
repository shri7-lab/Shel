from rich.prompt import Confirm, Prompt
from rich.console import Console
from pathlib import Path

console = Console()

DESTRUCTIVE_PATTERNS = [
    "rm -rf", "dd if=", "mkfs", "format", "fdisk", "mke2fs",
    "chmod 000", "> /dev/sd", "> /dev/nvme",
    "drop database", "drop table", "truncate",
    "shutdown", "reboot", "poweroff",
]

SENSITIVE_PATTERNS = [
    "sqlmap", "metasploit", "msfconsole", "msfvenom",
    "hydra", "medusa", "hashcat", "john",
    "exploit", "shell", "reverse",
]


class CheckpointGate:
    def __init__(self):
        self.session_log_path = Path.home() / ".shel" / "session_log.txt"
        self.session_log_path.parent.mkdir(parents=True, exist_ok=True)
        self.command_count = 0
        self.approved_targets = set()

    def set_targets(self, targets: list[str]):
        self.approved_targets = set(targets)

    def check_command(self, command: str) -> tuple[bool, str]:
        self.command_count += 1
        cmd_lower = command.lower()

        self._log(f"[{self.command_count}] CMD: {command}")

        for pattern in DESTRUCTIVE_PATTERNS:
            if pattern in cmd_lower:
                self._log(f"[{self.command_count}] DESTRUCTIVE: {command}")
                console.print(f"\n[bold red]⚠ DESTRUCTIVE COMMAND DETECTED[/bold red]")
                console.print(f"[yellow]{command}[/yellow]")
                allowed = Confirm.ask("[red]Allow this command?[/red]", default=False)
                if allowed:
                    self._log(f"[{self.command_count}] APPROVED (destructive): {command}")
                    return True, "approved"
                self._log(f"[{self.command_count}] DENIED (destructive): {command}")
                return False, "denied: destructive command rejected by user"

        for pattern in SENSITIVE_PATTERNS:
            if pattern in cmd_lower:
                self._log(f"[{self.command_count}] SENSITIVE: {command}")
                console.print(f"\n[bold yellow]⚠ Sensitive command:[/bold yellow]")
                console.print(f"[cyan]{command}[/cyan]")
                allowed = Confirm.ask("Allow?", default=True)
                if allowed:
                    self._log(f"[{self.command_count}] APPROVED: {command}")
                    return True, "approved"
                self._log(f"[{self.command_count}] DENIED: {command}")
                return False, "denied by user"
        self._log(f"[{self.command_count}] AUTO-APPROVED: {command}")
        return True, "approved"

    def _log(self, line: str):
        with open(self.session_log_path, "a", encoding="utf-8") as f:
            f.write(line + "\n")

    def print_summary(self):
        if not self.session_log_path.exists():
            console.print("[dim]No session log yet.[/dim]")
            return
        content = self.session_log_path.read_text(encoding="utf-8")
        lines = [l for l in content.split("\n") if l.strip()]
        console.print(f"\n[bold]Session Log ({len(lines)} commands)[/bold]")
        for l in lines[-20:]:
            console.print(f"  [dim]{l}[/dim]")
