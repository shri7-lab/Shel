#!/usr/bin/env python3
import sys
import time
import re
from pathlib import Path
from datetime import datetime
from agent.autopilot import PHASE_NAMES
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich.spinner import Spinner
from rich.text import Text
from rich.columns import Columns
from rich.syntax import Syntax
from rich.rule import Rule
from rich import box
from rich.style import Style
from rich.align import Align
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style as PtStyle

from config.settings import load_config, save_config, get_api_key
from agent.llm import LLM
from agent.tools import ToolRunner, TOOL_DEFINITIONS
from agent.system import build_system_prompt
from agent.state import SessionState
from agent.rag import RAGEngine
from agent.docker import DockerSandbox
from agent.checkpoints import CheckpointGate
from agent.sub_agent_runner import SubAgentRunner
from agent.autopilot import AutoPilot
from modules.osint import OSINTEngine

console = Console()
HISTORY_FILE = Path.home() / ".shel" / "history.txt"


def make_banner():
    logo = Text("""
    ╔══════════════════════════════════════╗
    ║  ███████ ██  ██ ███████ ██          ║
    ║  ██      ██  ██ ██      ██          ║
    ║  ███████ ███████ █████   ██          ║
    ║       ██ ██  ██ ██      ██          ║
    ║  ███████ ██  ██ ███████ ███████     ║
    ╚══════════════════════════════════════╝
""")
    logo.stylize("bold cyan")
    subtitle = Text(" Autonomous Pentesting AI Agent  |  v1.0  |  Attack-Tree Engine  |  RAG  |  Multi-Agent\n", style="dim white")
    return Columns([logo, subtitle])


def make_dashboard(state, cfg, docker, autopilot):
    target_str = ", ".join(state.targets[:2]) if state.targets else "none"
    findings_count = len(state.findings)
    provider = cfg.get("provider", "claude")
    model = cfg.get("model", "claude-sonnet-4-20250514")[:25]

    ap_status = "● Running" if autopilot and autopilot.running else "○ Idle"
    ap_color = "green" if autopilot and autopilot.running else "dim"

    swarm_agents = 0
    if autopilot and autopilot.swarm:
        s = autopilot.swarm.status()
        swarm_agents = s.get("completed", 0) + len(s.get("active", {}))

    grid = Table.grid(padding=(0, 2))
    grid.add_column()
    grid.add_column()
    grid.add_row(
        Text.assemble(
            (" Provider  ", "dim"), (f"{provider} ", "cyan"),
            (" Model  ", "dim"), (f"{model} ", "white"),
        ),
        Text.assemble(
            (" Docker  ", "dim"), ("✓ " if docker.available else "✗ ", "green" if docker.available else "red"),
            (" RAG  ", "dim"), ("✓ ", "green"),
            (" Shell  ", "dim"), ("✓ ", "green"),
        ),
    )
    grid.add_row(
        Text.assemble(
            (" Target(s)  ", "dim"), (f"{target_str} ", "yellow"),
            (" Findings  ", "dim"), (f"{findings_count} ", "white"),
            (" Swarm  ", "dim"), (f"{swarm_agents} agents ", "magenta"),
        ),
        Text.assemble(
            (" AutoPilot  ", "dim"), (f"{ap_status} ", ap_color),
            (" Session  ", "dim"), (f"{datetime.now().strftime('%H:%M:%S')} ", "dim"),
        ),
    )
    return grid


def show_dashboard(state, cfg, docker, autopilot):
    console.print(Rule(style="dim"))
    console.print(make_dashboard(state, cfg, docker, autopilot))
    console.print(Rule(style="dim"))


def print_banner():
    console.print()
    console.rule(style="bold cyan")
    b = make_banner()
    console.print(b)
    console.rule(style="bold cyan")


def show_help(state=None):
    categories = [
        ("Session", ["/help", "/clear", "/config", "/state", "/findings", "/log", "/reset", "/banner", "/exit"]),
        ("Target", ["/set-target <ip>", "/add-target <ip>"]),
        ("AI", ["/set-key", "/set-model", "/use-local", "/use-claude", "/shell-on", "/shell-off"]),
        ("OSINT", ["/osint <domain>", "/osint ip <ip>", "/osint email <email>", "/osint user <user>", "/osint dork <domain>", "/osint archive <domain>", "/osint tools <target>"]),
        ("Autonomous", ["/autoon <target>", "/autoon --fast <target>", "/autoon --deep <target>", "/autooff", "/status", "/brain"]),
        ("Swarm", ["/swarm launch <type> <task>", "/swarm chain", "/swarm status"]),
        ("Social", ["/social campaign|plan|chains <objective>", "/social phish <style> [name]", "/social deepfake status|script|pipeline", "/social vectors|target|persona"]),
        ("Steganography", ["/stego encode <technique> <payload>", "/stego decode <technique> <data>", "/stego techniques"]),
        ("C2", ["/c2 implant [channel] [type]", "/c2 beacon [channel]", "/c2 server", "/c2 encode|decode <cmd>"]),
        ("Learning", ["/learn init", "/learn summary", "/learn q_select [ports]", "/learn hypothesis|plan [ports...]", "/learn bayesian", "/learn skill_find|skill_summary"]),
        ("Supply Chain", ["/supplychain recon|cicd|poison <args>"]),
        ("Evasion", ["/evasion polymorph <lang> <code>", "/evasion bypass <type>", "/evasion lolbin <action> [args]"]),
        ("Compiler", ["/compile list|templates|status [lang]", "/compile <template> <params> [target]", "/compile cross_targets [lang]"]),
        ("Universal", ["/run <task> on <target>"]),
        ("Modules", ["/recon <task>", "/exploit <task>", "/report", "/docker-setup", "/docker <cmd>", "/benchmark"]),
    ]
    for cat, cmds in categories:
        table = Table(show_header=False, box=box.SIMPLE, padding=(0, 1))
        table.add_column("cmd", style="cyan")
        table.add_column("desc", style="white")
        for i, cmd in enumerate(cmds):
            name = cmd.split(" — ")
            table.add_row(name[0], name[1] if len(name) > 1 else "")
        if state:
            console.print(Panel(table, title=f"[bold]{cat}[/bold]", border_style="blue"))
        else:
            console.print(Panel(table, title=f"[bold]{cat}[/bold]", border_style="blue"))


def show_config():
    cfg = load_config()
    table = Table(box=box.SIMPLE)
    table.add_column("Setting", style="cyan")
    table.add_column("Value")
    for k, v in cfg.items():
        if k == "api_key":
            v = f"{v[:8]}...{v[-4:]}" if v else "(not set)"
        elif k == "ollama_model":
            table.add_row(k, str(v))
            continue
        table.add_row(k, str(v) if v is not None else "(not set)")
    console.print(Panel(table, title="Configuration", border_style="cyan"))


def show_session_state(state):
    text = state.to_prompt_block()
    text = text.replace("<attack_tree>", "").replace("</attack_tree>", "")
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    display = Text("\n".join(lines[:25]))
    if len(lines) > 25:
        display.append(f"\n... ({len(lines) - 25} more lines)")
    console.print(Panel(display, title="Session State", border_style="cyan"))


def show_findings(state):
    if not state.findings:
        console.print(Panel("[dim]No findings yet.[/dim]", title="Findings", border_style="yellow"))
        return
    table = Table(box=box.SIMPLE)
    table.add_column("#", style="dim")
    table.add_column("Type", style="cyan")
    table.add_column("Detail")
    table.add_column("Confidence")
    for i, f in enumerate(state.findings, 1):
        color = {"high": "red", "medium": "yellow", "low": "green"}.get(f.confidence, "white")
        ts = f.timestamp.split(".")[0] if hasattr(f, "timestamp") and f.timestamp else ""
        table.add_row(str(i), f.type, f.detail[:80], f"[{color}]{f.confidence}[/{color}]")
    console.print(Panel(table, title=f"Findings ({len(state.findings)})", border_style="green"))


def handle_command(cmd, tool_runner, state, docker, sub_agents, rag, autopilot=None):
    cmd = cmd.strip()
    lower = cmd.lower()

    if lower == "/help":
        show_help(state)
        return True
    elif lower == "/clear":
        console.clear()
        print_banner()
        show_dashboard(state, load_config(), docker, autopilot)
        return True
    elif lower == "/config":
        show_config()
        return True
    elif lower == "/state":
        show_session_state(state)
        return True
    elif lower == "/findings":
        show_findings(state)
        return True
    elif lower == "/log":
        if tool_runner.checkpoint_gate:
            tool_runner.checkpoint_gate.print_summary()
        else:
            console.print(Panel("[dim]Logging not available.[/dim]", border_style="red"))
        return True
    elif lower == "/reset":
        state.reset()
        console.print(Panel("[green]Session state reset successfully.[/green]", border_style="green"))
        return True
    elif lower.startswith("/set-target "):
        target = cmd[12:].strip()
        state.targets = [target]
        state.target_scope = [target]
        state.add_finding("target", target, "high")
        console.print(Panel(f"[green]Target set to:[/green] [bold]{target}[/bold]", border_style="green"))
        return True
    elif lower.startswith("/add-target "):
        target = cmd[12:].strip()
        if target not in state.targets:
            state.targets.append(target)
            state.target_scope.append(target)
            console.print(Panel(f"[green]Added target:[/green] [bold]{target}[/bold]", border_style="green"))
        return True
    elif lower == "/shell-on":
        tool_runner.allow_bash = True
        console.print(Panel("[green]Shell execution enabled.[/green]", border_style="green"))
        return True
    elif lower == "/shell-off":
        tool_runner.allow_bash = False
        console.print(Panel("[yellow]Shell execution disabled.[/yellow]", border_style="yellow"))
        return True
    elif lower == "/set-key":
        key = Prompt.ask("Enter Anthropic API key", password=True)
        cfg = load_config()
        cfg["api_key"] = key
        save_config(cfg)
        console.print(Panel("[green]API key saved.[/green]", border_style="green"))
        return True
    elif lower == "/set-model":
        model = Prompt.ask("Enter model name", default="claude-sonnet-4-20250514")
        cfg = load_config()
        cfg["model"] = model
        save_config(cfg)
        console.print(Panel(f"[green]Model set to [bold]{model}[/bold][/green]", border_style="green"))
        console.print("[yellow]Restart Shel for the change to take effect.[/yellow]")
        return True
    elif lower == "/use-local":
        cfg = load_config()
        cfg["provider"] = "ollama"
        cfg["model"] = cfg.get("ollama_model", "llama3.1")
        save_config(cfg)
        console.print(Panel("[green]Switched to Ollama (local) mode.[/green]", border_style="green"))
        console.print("[yellow]Restart Shel for the change to take effect.[/yellow]")
        return True
    elif lower == "/use-claude":
        cfg = load_config()
        cfg["provider"] = "claude"
        cfg["model"] = "claude-sonnet-4-20250514"
        save_config(cfg)
        console.print(Panel("[green]Switched to Claude API mode.[/green]", border_style="green"))
        console.print("[yellow]Restart Shel for the change to take effect.[/yellow]")
        return True
    elif lower == "/docker-setup":
        if docker and docker.available:
            with console.status("[yellow]Building Docker image...", spinner="dots"):
                result = docker.build_image()
            console.print(Panel(result[:2000], title="Docker Build", border_style="green"))
        else:
            console.print(Panel("[red]Docker is not available. Install Docker Desktop.[/red]", border_style="red"))
        return True
    elif lower.startswith("/docker "):
        if docker and docker.available:
            command = cmd[8:].strip()
            with console.status("[yellow]Running in Docker sandbox...", spinner="dots"):
                result = docker.run_command(command)
            console.print(Panel(result[:3000], title=f"Docker: {command[:40]}", border_style="cyan"))
        else:
            console.print(Panel("[red]Docker is not available.[/red]", border_style="red"))
        return True
    elif lower.startswith("/recon "):
        if sub_agents:
            task = cmd[7:].strip()
            with console.status("[cyan]Recon sub-agent working...", spinner="dots"):
                result = sub_agents.run("recon", task, state)
            console.print(Panel(Markdown(result), title=f"Recon: {task[:40]}", border_style="cyan"))
        return True
    elif lower.startswith("/exploit "):
        if sub_agents:
            task = cmd[9:].strip()
            with console.status("[red]Exploit sub-agent working...", spinner="dots"):
                result = sub_agents.run("exploit", task, state)
            console.print(Panel(Markdown(result), title=f"Exploit: {task[:40]}", border_style="red"))
        return True
    elif lower == "/report":
        if sub_agents:
            with console.status("[green]Generating report...", spinner="dots"):
                result = sub_agents.run("report", "Generate a complete pentest report based on the current session state.", state)
            console.print(Panel(Markdown(result), title="Engagement Report", border_style="green"))
        return True
    elif lower == "/benchmark":
        try:
            from benchmark.runner import BenchmarkHarness
            b = BenchmarkHarness()
            b.load()
            console.print(Panel(Markdown(b.summary()), title="Benchmark Results", border_style="green"))
        except ImportError:
            console.print(Panel("[red]Benchmark module not available.[/red]", border_style="red"))
        return True
    elif lower.startswith("/osint "):
        rest = cmd[7:].strip()
        osint = OSINTEngine()

        if rest.startswith("tools "):
            target = rest[6:].strip()
            if not target:
                console.print(Panel("[red]Usage: /osint tools <target>[/red]", border_style="red"))
                return True
            with console.status("[cyan]Looking up OSINT tools...", spinner="dots"):
                result = osint.tool_recommendations_for_target(target)
            console.print(Panel(Markdown(result), title=f"OSINT Tools for {target}", border_style="cyan"))
            return True

        if rest.startswith("ip "):
            ip = rest[3:].strip()
            with console.status(f"[cyan]OSINT on IP {ip}...", spinner="dots"):
                r = osint.ip_recon(ip)
            panel = Panel(
                Text.assemble(
                    ("IP         ", "dim"), (f"{r['ip']}\n", "bold white"),
                    ("Hostname   ", "dim"), (f"{r.get('hostname', 'N/A')}\n", "white"),
                    ("ASN        ", "dim"), (f"{r.get('asn', 'N/A')}\n", "white"),
                    ("Location   ", "dim"), (f"{r.get('location', 'N/A')}\n", "white"),
                    ("Reverse DNS", "dim"), (", ".join(r.get("reverse_dns", [])[:3]) or "N/A", "white"),
                ),
                title=f"IP OSINT: {ip}", border_style="cyan",
            )
            console.print(panel)

        elif rest.startswith("email "):
            email = rest[6:].strip()
            with console.status(f"[cyan]OSINT on email {email}...", spinner="dots"):
                r = osint.email_recon(email)
            panel = Panel(
                Text.assemble(
                    ("Email    ", "dim"), (f"{r['email']}\n", "bold white"),
                    ("Domain   ", "dim"), (f"{r['domain']}\n", "white"),
                    ("Username ", "dim"), (f"{r['username']}\n", "white"),
                    ("Format   ", "dim"), (f"{r.get('email_format', 'N/A')}", "white"),
                ),
                title=f"Email OSINT: {email}", border_style="magenta",
            )
            console.print(panel)

        elif rest.startswith("user "):
            username = rest[5:].strip()
            with console.status(f"[cyan]Searching for {username}...", spinner="dots"):
                r = osint.username_recon(username)
            found = [p for p in r["profiles"] if p["status"] == "found"]
            if found:
                table = Table(box=box.SIMPLE)
                table.add_column("Platform", style="cyan")
                table.add_column("URL")
                for p in found:
                    table.add_row(p["site"], f"[link={p['url']}]{p['url']}[/link]")
                console.print(Panel(table, title=f"Profiles: {username}", border_style="green"))
            else:
                console.print(Panel(f"[yellow]No profiles found for [bold]{username}[/bold][/yellow]", border_style="yellow"))

        elif rest.startswith("dork "):
            domain = rest[5:].strip()
            with console.status(f"[cyan]Google dorking {domain}...", spinner="dots"):
                r = osint.google_dork(domain)
            for d in r:
                if d["results"]:
                    panel = Panel(
                        f"[bold]Dork:[/bold] {d['dork']}\n"
                        f"[bold]Results:[/bold]\n" + "\n".join(f"  [cyan]•[/cyan] {url}" for url in d["results"][:5]),
                        title=f"{d['type']}", border_style="green",
                    )
                    console.print(panel)

        elif rest.startswith("archive "):
            domain = rest[8:].strip()
            with console.status(f"[cyan]Fetching Wayback snapshots for {domain}...", spinner="dots"):
                r = osint.web_archive(domain)
            if r:
                table = Table(box=box.SIMPLE)
                table.add_column("Timestamp", style="dim")
                table.add_column("URL")
                table.add_column("Status")
                for s in r[:15]:
                    table.add_row(s.get("timestamp", ""), s.get("url", "")[:80], str(s.get("status", "")))
                console.print(Panel(table, title=f"Wayback: {domain}", border_style="cyan"))
            else:
                console.print(Panel(f"[yellow]No snapshots found for [bold]{domain}[/bold][/yellow]", border_style="yellow"))

        else:
            domain = rest
            with console.status(f"[green]Full OSINT on {domain}...", spinner="dots"):
                r = osint.full_recon(domain)
            console.print(Panel(Markdown(osint.format_report(domain)), title=f"OSINT: {domain}", border_style="cyan"))
            console.print()
            console.print(Panel(Markdown(osint.tool_recommendations_for_target(domain)), title="Tool Recommendations", border_style="cyan"))
        return True

    elif lower.startswith("/autoon "):
        if autopilot and autopilot.running:
            console.print(Panel("[red]AutoPilot is already running. Use /status or /autooff[/red]", border_style="red"))
            return True
        rest = cmd[8:].strip()
        scan_type = "standard"
        target = rest
        if rest.startswith("--fast "):
            scan_type = "fast"
            target = rest[7:].strip()
        elif rest.startswith("--deep "):
            scan_type = "deep"
            target = rest[7:].strip()
        if not target:
            console.print(Panel("[red]Usage: /autoon <target> | /autoon --fast <target> | /autoon --deep <target>[/red]", border_style="red"))
            return True
        tool_runner.auto_mode = True
        import threading
        t = threading.Thread(target=autopilot.start_brain, args=(target, scan_type), daemon=True)
        t.start()
        console.print(Panel(f"[bold green]Shel Brain engaged[/bold green] → [bold]{target}[/bold] ({scan_type})", border_style="green"))
        return True
    elif lower == "/autooff":
        if autopilot:
            autopilot.stop_brain()
            tool_runner.auto_mode = False
        console.print(Panel("[yellow]Brain stopped.[/yellow]", border_style="yellow"))
        return True
    elif lower == "/status":
        if autopilot and autopilot.brain and autopilot.brain.running:
            s = autopilot.brain_status()
            elapsed = s.get("uptime", 0)
            status_grid = Table.grid(padding=(0, 1))
            status_grid.add_column()
            status_grid.add_column()
            status_grid.add_row("[dim]Mode[/dim]", "[bold green]● Brain (autonomous loop)[/bold green]")
            status_grid.add_row("[dim]Target[/dim]", f"[bold]{autopilot.target}[/bold]")
            status_grid.add_row("[dim]Elapsed[/dim]", f"{elapsed:.0f}s")
            status_grid.add_row("[dim]Goals[/dim]", f"total={s['total_goals']} pending={s['pending']} active={s['in_progress']} done={s['completed']} failed={s['failed']}")
            status_grid.add_row("[dim]Current[/dim]", s.get("current") or "standby")
            status_grid.add_row("[dim]Findings[/dim]", str(len(autopilot.state.findings)))
            status_grid.add_row("[dim]Learner[/dim]", f"{s['learner_experiences']} experiences recorded")
            console.print(Panel(status_grid, title="Brain Status", border_style="green"))
            if s.get("goals"):
                goal_table = Table(box=box.SIMPLE)
                goal_table.add_column("ID", style="dim")
                goal_table.add_column("Objective")
                goal_table.add_column("Target")
                goal_table.add_column("Pri")
                goal_table.add_column("Status")
                for g in s["goals"]:
                    goal_table.add_row(g["id"], g["objective"], g["target"], str(g["priority"]), g["status"])
                console.print(Panel(goal_table, title="Goal Queue", border_style="cyan"))
        elif autopilot and autopilot.running:
            elapsed = time.time() - autopilot.start_time if autopilot.start_time else 0
            phase = autopilot.current_phase
            phase_name = PHASE_NAMES[phase] if phase < len(PHASE_NAMES) else "Complete"
            status_grid = Table.grid(padding=(0, 1))
            status_grid.add_column()
            status_grid.add_column()
            status_grid.add_row("[dim]Mode[/dim]", "[yellow]● Classic (phase pipeline)[/yellow]")
            status_grid.add_row("[dim]Target[/dim]", f"[bold]{autopilot.target}[/bold]")
            status_grid.add_row("[dim]Phase[/dim]", f"{phase + 1}/7 — {phase_name}")
            status_grid.add_row("[dim]Elapsed[/dim]", f"{elapsed:.0f}s")
            status_grid.add_row("[dim]Ports[/dim]", str(len(autopilot.parsed_ports)))
            status_grid.add_row("[dim]Findings[/dim]", str(len(autopilot.state.findings)))
            status_grid.add_row("[dim]Foothold[/dim]", autopilot.foothold_type or "[dim]None[/dim]")
            console.print(Panel(status_grid, title="AutoPilot Status", border_style="yellow"))
        else:
            console.print(Panel("[dim]Brain is idle. Use /autoon <target> to start.[/dim]", border_style="yellow"))
        return True
    elif lower == "/brain":
        if autopilot and autopilot.brain and autopilot.brain.running:
            s = autopilot.brain_status()
            elapsed = s.get("uptime", 0)
            info_grid = Table.grid(padding=(0, 1))
            info_grid.add_column()
            info_grid.add_column()
            info_grid.add_row("[dim]Status[/dim]", "[green]● Running[/green]")
            info_grid.add_row("[dim]Uptime[/dim]", f"{elapsed:.0f}s")
            info_grid.add_row("[dim]Goals[/dim]", f"{s['total_goals']} ({s['completed']} done, {s['failed']} failed)")
            info_grid.add_row("[dim]Active goal[/dim]", s.get("current") or "none")
            info_grid.add_row("[dim]Targets[/dim]", ", ".join(s.get("targets", [])) or "none")
            info_grid.add_row("[dim]Creds found[/dim]", str(s.get("creds", 0)))
            info_grid.add_row("[dim]Blackboard findings[/dim]", str(s.get("findings", 0)))
            info_grid.add_row("[dim]Learner experiences[/dim]", str(s.get("learner_experiences", 0)))
            console.print(Panel(info_grid, title="Brain Dashboard", border_style="magenta"))

            if s.get("goals"):
                gt = Table(box=box.SIMPLE)
                gt.add_column("ID", style="dim")
                gt.add_column("Objective")
                gt.add_column("Target:Port")
                gt.add_column("Pri")
                gt.add_column("Status")
                gt.add_column("Attempts")
                for g in s["goals"]:
                    tp = f"{g['target']}:{g['port']}" if g.get("port") else g["target"]
                    gt.add_row(g["id"], g["objective"], tp, str(g["priority"]), g["status"], str(g["attempts"]))
                console.print(Panel(gt, title="Goal Queue", border_style="cyan"))

            if s.get("learner_summary"):
                lt = Table(box=box.SIMPLE)
                lt.add_column("Technique")
                lt.add_column("Port")
                lt.add_column("Tool")
                lt.add_column("Success")
                lt.add_column("Fails")
                lt.add_column("Rate")
                for r in s["learner_summary"][:10]:
                    rate = f"{r['success_rate']*100:.0f}%" if r.get("success_rate") is not None else "N/A"
                    lt.add_row(r["technique_key"], str(r["port"]), r.get("tool", ""),
                               str(r["success_count"]), str(r["fail_count"]), rate)
                console.print(Panel(lt, title="Learner: Top Techniques", border_style="green"))
        else:
            console.print(Panel("[dim]Brain is idle. Run /autoon <target> first.[/dim]", border_style="yellow"))
        return True
    elif lower.startswith("/evasion ") or lower.startswith("/lolbins"):
        from modules.evasion.polymorph import PolymorphicEngine
        from modules.evasion.edr import EDREvasion
        from modules.evasion.lolbins import LOLBinManager

        if lower.startswith("/lolbins"):
            parts = cmd[8:].strip().split()
            action = parts[0] if parts else "summary"
            platform = parts[1] if len(parts) > 1 else "windows"
            lm = LOLBinManager(platform)
            if action == "list":
                bins = lm.get_all()
                table = Table(box=box.SIMPLE)
                table.add_column("Bin", style="cyan")
                table.add_column("Path")
                table.add_column("Capabilities")
                for b in bins:
                    table.add_row(b["name"], b["path"], ", ".join(b["capabilities"]))
                console.print(Panel(table, title=f"LOLBins ({platform})", border_style="green"))
            elif action == "find":
                cap = parts[1] if len(parts) > 1 else "execute"
                bins = lm.find_by_capability(cap)
                table = Table(box=box.SIMPLE)
                table.add_column("Bin", style="cyan")
                table.add_column("Path")
                table.add_column("Description")
                for b in bins:
                    table.add_row(b["name"], b["path"], b["description"])
                console.print(Panel(table, title=f"LOLBins with: {cap}", border_style="cyan"))
            else:
                console.print(Panel(lm.summarize(), title="LOLBin Summary", border_style="green"))
            return True

        rest = cmd[9:].strip()
        subparts = rest.split(maxsplit=2)
        if not subparts:
            console.print(Panel("[red]Usage: /evasion polymorph <lang> <code> | /evasion bypass <type> | /evasion lolbin <action> [args][/red]", border_style="red"))
            return True

        action = subparts[0].lower()

        if action == "polymorph":
            if len(subparts) < 3:
                console.print(Panel("[red]Usage: /evasion polymorph <lang> <code>[/red]", border_style="red"))
                return True
            lang = subparts[1].lower()
            code = subparts[2]
            eng = PolymorphicEngine()
            mutated = eng.full_mutate(code, lang)
            syntax = Syntax(mutated, lang, theme="monokai", word_wrap=True)
            console.print(Panel(syntax, title=f"Polymorphic Mutation ({lang})", border_style="green"))
            console.print(f"[dim]MD5: {eng.checksum(mutated)} | Seed: {eng.seed}[/dim]")

        elif action == "bypass":
            if len(subparts) < 2:
                console.print(Panel("[red]Usage: /evasion bypass <type>\nTypes: amsi_memory, amsi_registry, amsi_reflection, etw, sandbox_detect, inject_crt, inject_apc, inject_hollow, all[/red]", border_style="red"))
                return True
            technique = subparts[1].lower()
            edr = EDREvasion()
            mapping = {
                "amsi_memory": lambda: edr.amsi_bypass("memory"),
                "amsi_registry": lambda: edr.amsi_bypass("registry"),
                "amsi_reflection": lambda: edr.amsi_bypass("reflection"),
                "etw": lambda: edr.etw_bypass(),
                "sandbox_detect": lambda: edr.sandbox_detect(),
                "inject_crt": lambda: edr.process_injection("crt"),
                "inject_apc": lambda: edr.process_injection("apc"),
                "inject_hollow": lambda: edr.process_injection("hollow"),
                "all": lambda: edr.all_bypasses(),
            }
            if technique not in mapping:
                console.print(Panel(f"[red]Unknown technique: {technique}[/red]", border_style="red"))
                return True
            code = mapping[technique]()
            syntax = Syntax(code, "powershell", theme="monokai", word_wrap=True)
            console.print(Panel(syntax, title=f"{technique.replace('_', ' ').title()}", border_style="red"))

        elif action == "lolbin":
            if len(subparts) < 2:
                console.print(Panel("[red]Usage: /evasion lolbin <action> [args][/red]", border_style="red"))
                return True
            subaction = subparts[1].lower()
            lm = LOLBinManager("windows")
            if subaction == "list":
                bins = lm.get_all()
                table = Table(box=box.SIMPLE)
                table.add_column("Bin", style="cyan")
                table.add_column("Path")
                table.add_column("Capabilities")
                for b in bins:
                    table.add_row(b["name"], b["path"], ", ".join(b["capabilities"]))
                console.print(Panel(table, title="Windows LOLBins", border_style="green"))
            elif subaction == "revshell":
                bin_name = subparts[2] if len(subparts) > 2 else "powershell"
                lhost = subparts[3] if len(subparts) > 3 else "10.0.0.1"
                lport = int(subparts[4]) if len(subparts) > 4 else 4444
                code = lm.generate_reverse_shell(bin_name, lhost, lport)
                syntax = Syntax(code, "powershell", theme="monokai", word_wrap=True)
                console.print(Panel(syntax, title=f"Reverse Shell: {bin_name}", border_style="red"))
            elif subaction == "download":
                bin_name = subparts[2] if len(subparts) > 2 else "certutil"
                url = subparts[3] if len(subparts) > 3 else "http://example.com/payload.exe"
                code = lm.generate_download_cradle(bin_name, url)
                console.print(Panel(code, title=f"Download Cradle: {bin_name}", border_style="cyan"))
            else:
                console.print(Panel("[red]Sub-actions: list, revshell <bin> <lhost> <lport>, download <bin> <url>[/red]", border_style="red"))
        else:
            console.print(Panel(f"[red]Unknown evasion action: {action}[/red]", border_style="red"))
        return True

    elif lower.startswith("/supplychain "):
        from modules.supplychain.recon import SupplyChainRecon
        from modules.supplychain.poison import DependencyPoison
        from modules.supplychain.cicd import CICDExploit

        rest = cmd[13:].strip()
        parts = rest.split(maxsplit=1)
        if not parts:
            console.print(Panel("[red]Usage: /supplychain recon|cicd|poison <args>[/red]", border_style="red"))
            return True

        area = parts[0].lower()
        subargs = parts[1] if len(parts) > 1 else ""

        if area == "recon":
            if not subargs:
                console.print(Panel("[red]Provide file contents or use: /supplychain recon files <json>[/red]", border_style="red"))
                return True
            sc = SupplyChainRecon()
            files = {}
            sub_sub = subargs.split(maxsplit=1)
            if sub_sub[0] == "files" and len(sub_sub) > 1:
                files = {"scanned.txt": sub_sub[1]}
            findings = sc.analyze_repo_structure(files)
            console.print(Panel(sc.summarize(findings), title="Supply Chain Recon", border_style="cyan"))

        elif area == "poison":
            dp = DependencyPoison()
            subparts = subargs.split()
            if not subparts:
                console.print(Panel("[red]Usage: /supplychain poison confusion|squat|squat-list <pkg> [ecosystem] [payload_type][/red]", border_style="red"))
                return True
            subaction = subparts[0].lower()
            pkg = subparts[1] if len(subparts) > 1 else "lodash"
            eco = subparts[2] if len(subparts) > 2 else "npm"

            if subaction == "confusion":
                ptype = subparts[3] if len(subparts) > 3 else "reverse_shell"
                result = dp.generate_confusion_package(pkg, eco, ptype)
                console.print(Panel(Syntax(result, "python" if eco == "pip" else "javascript", theme="monokai"), title=f"Dependency Confusion: {pkg}", border_style="red"))

            elif subaction == "squat":
                result = dp.typo_squat(pkg)
                console.print(Panel(f"[green]{pkg}[/green] → [bold red]{result}[/bold red]", title="Typo-Squat", border_style="yellow"))

            elif subaction == "squat-list":
                count = int(subparts[2]) if len(subparts) > 2 and subparts[2].isdigit() else 10
                squats = dp.generate_squat_list(eco, count)
                table = Table(box=box.SIMPLE)
                table.add_column("Original", style="cyan")
                table.add_column("Squat", style="red")
                table.add_column("Strategy", style="dim")
                for s in squats:
                    table.add_row(s["original"], s["squat"], s["strategy"])
                console.print(Panel(table, title=f"Typo-Squats ({eco})", border_style="yellow"))

        elif area == "cicd":
            ce = CICDExploit()
            subparts = subargs.split()
            subaction = subparts[0].lower() if subparts else "summary"

            if subaction == "techniques":
                result = "\n".join(f"**{tid}** ({info['severity'].upper()}): {info['description']}" for tid, info in ce.get_techniques().items())
                console.print(Panel(Markdown(result), title="CI/CD Attack Techniques", border_style="red"))

            elif subaction == "summary":
                console.print(Panel(Markdown(ce.summarize()), title="CI/CD Attack Surface", border_style="cyan"))

            elif subaction == "generate":
                technique = subparts[1] if len(subparts) > 1 else "pr_target"
                repo = subparts[2] if len(subparts) > 2 else "owner/repo"
                result = ce.generate_malicious_workflow(repo, technique)
                console.print(Panel(Syntax(result, "yaml", theme="monokai"), title=f"CI/CD Exploit: {technique}", border_style="red"))

            elif subaction == "runner":
                result = ce.generate_runner_registration()
                console.print(Panel(Syntax(result, "bash", theme="monokai"), title="Runner Registration Payload", border_style="red"))

        else:
            console.print(Panel(f"[red]Unknown area: {area}. Use recon, poison, or cicd.[/red]", border_style="red"))
        return True

    elif lower.startswith("/social "):
        from modules.social.engine import SocialEngine, Campaign, TargetProfile, Persona
        from modules.social.phishing import PhishingKit
        from modules.social.deepfake import DeepfakeFramework

        rest = cmd[8:].strip()
        parts = rest.split(maxsplit=1)
        if not parts:
            console.print(Panel("[red]Usage:\n  /social campaign|plan|chains|target|persona|vectors\n  /social phish <style> [name] [org]\n  /social deepfake status|script|pipeline[/red]", border_style="red"))
            return True

        area = parts[0].lower()
        subargs = parts[1] if len(parts) > 1 else ""

        if area in ("campaign", "plan", "chains", "target", "persona", "vectors"):
            se = SocialEngine()
            if area == "vectors":
                console.print(Panel(Markdown(se.vector_info()), title="Attack Vectors", border_style="cyan"))
            elif area == "target":
                tp = TargetProfile(name=subargs or "Unknown", organization="Target")
                console.print(Panel(Markdown(se.generate_target_summary(tp)), title="Target Profile", border_style="yellow"))
            elif area == "persona":
                p = Persona(name=subargs or None)
                p.generate_backstory()
                info = f"**Name:** {p.name}\n**Role:** {p.role}\n**Email:** {p.email}\n**Phone:** {p.phone}\n**Style:** {p.personality}\n**Backstory:** {p.backstory}"
                console.print(Panel(Markdown(info), title="Generated Persona", border_style="green"))
                console.print(Panel(p.signature_block(), title="Signature Block", border_style="cyan"))
            elif area == "chains":
                subs = subargs.split(maxsplit=1)
                obj = subs[0] if subs else "credential_harvest"
                target_name = subs[1] if len(subs) > 1 else "John Doe"
                c = Campaign()
                c.plan(obj, {"name": target_name, "organization": "TargetCorp"}, Persona())
                for i, (name, content) in enumerate(c.generate_attack_chain(c.targets[0], c.persona)):
                    console.print(Panel(content, title=f"Stage {i+1}: {name}", border_style="red" if i == 2 else "yellow"))
            else:
                c = se.create_campaign()
                obj = subargs or "credential_harvest"
                c.plan(obj, {"name": "Target", "organization": "Org"}, Persona())
                console.print(Panel(Markdown(c.status_report()), title="Campaign Plan", border_style="green"))

        elif area == "phish":
            pk = PhishingKit()
            subparts = subargs.split()
            style = subparts[0] if subparts else "security_alert"
            target_name = subparts[1] if len(subparts) > 1 else "User"
            org = subparts[2] if len(subparts) > 2 else "Company"

            if style.startswith("sms_"):
                result = pk.sms_template(style[4:])
                console.print(Panel(result, title=f"SMS: {style}", border_style="yellow"))
            elif style.startswith("macro_"):
                result = pk.macro_payload(style[6:])
                console.print(Panel(Syntax(result, "vbscript", theme="monokai"), title=f"Macro: {style}", border_style="red"))
            elif style in ("office365", "gmail", "generic", "okta", "vpn"):
                result = pk.landing_page_html(style, org)
                console.print(Panel(Syntax(result, "html", theme="monokai"), title=f"Landing: {style}", border_style="red"))
            else:
                result = pk.email_template(style, target_name, org=org)
                console.print(Panel(result, title=f"Phishing Email: {style}", border_style="cyan"))

        elif area == "deepfake":
            df = DeepfakeFramework()
            subparts = subargs.split()
            subaction = subparts[0] if subparts else "status"

            if subaction == "status":
                console.print(Panel(Markdown(df.status()), title="Deepfake Framework", border_style="cyan"))
            elif subaction == "report":
                console.print(Panel(Markdown(df.generate_report()), title="Deepfake Guide", border_style="green"))
            elif subaction == "script":
                tool = subparts[1] if len(subparts) > 1 else "roop"
                tool_action = subparts[2] if len(subparts) > 2 else "swap"
                result = df.generate_script(tool, tool_action)
                console.print(Panel(Syntax(result, "bash", theme="monokai"), title=f"Deepfake: {tool} {tool_action}", border_style="magenta"))
            elif subaction == "pipeline":
                ptype = subparts[1] if len(subparts) > 1 else "voice"
                if ptype == "voice":
                    result = df.pipeline_phishing_call()
                else:
                    result = df.pipeline_deepfake_video()
                console.print(Panel(Syntax(result, "bash", theme="monokai"), title=f"Deepfake Pipeline", border_style="magenta"))
            else:
                console.print(Panel("[red]Sub-actions: status, report, script <tool> <action>, pipeline [voice|video][/red]", border_style="red"))

        else:
            console.print(Panel(f"[red]Unknown area: {area}[/red]", border_style="red"))
        return True

    elif lower.startswith("/stego "):
        from modules.stego.stego import StegoEngine
        import json

        rest = cmd[7:].strip()
        parts = rest.split(maxsplit=2)
        if not parts:
            console.print(Panel("[red]Usage:\n  /stego encode <technique> <payload> [cover]\n  /stego decode <technique> <data>\nTechniques: text_whitespace, text_homoglyph, pixel_lsb, http_header, dns_query, image_metadata", border_style="red"))
            return True

        se = StegoEngine()

        if parts[0] == "encode":
            technique = parts[1] if len(parts) > 1 else "text_whitespace"
            payload = parts[2] if len(parts) > 2 else "secret"
            cover = " ".join(parts[3:]) if len(parts) > 3 else se.random_cover_text(30)

            if technique == "text_whitespace":
                result, bits = se.encode_text_whitespace(payload, cover)
                if result is None:
                    console.print(Panel(f"[red]{bits}[/red]", border_style="red"))
                else:
                    console.print(Panel(f"[dim]Bits encoded: {bits}[/dim]\n\n{result}", title=f"Whitespace Stego", border_style="green"))
            elif technique == "text_homoglyph":
                result, bits = se.encode_text_homoglyph(payload, cover)
                if result is None:
                    console.print(Panel(f"[red]{bits}[/red]", border_style="red"))
                else:
                    console.print(Panel(result, title=f"Homoglyph Stego ({bits} bits)", border_style="cyan"))
            elif technique == "http_header":
                result = se.encode_http_header(payload)
                console.print(Panel(json.dumps(result, indent=2), title="HTTP Header Stego", border_style="yellow"))
            elif technique == "dns_query":
                queries = se.encode_dns_query(payload)
                console.print(Panel("\n".join(queries), title=f"DNS Queries ({len(queries)})", border_style="cyan"))
            elif technique == "image_metadata":
                result = se.encode_image_metadata(payload)
                console.print(Panel(json.dumps(result, indent=2), title="Image Metadata Stego", border_style="green"))
            else:
                console.print(Panel(f"[red]Unknown technique: {technique}[/red]", border_style="red"))

        elif parts[0] == "decode":
            technique = parts[1] if len(parts) > 1 else "text_whitespace"
            data = parts[2] if len(parts) > 2 else ""
            if technique == "text_whitespace":
                result = se.decode_text_whitespace(data)
            elif technique == "text_homoglyph":
                result = se.decode_text_homoglyph(data)
            else:
                result = f"Decode for {technique} not supported in CLI"
            console.print(Panel(result, title=f"Decoded: {technique}", border_style="green"))

        elif parts[0] == "techniques":
            techs = se.all_techniques()
            for t, desc in techs.items():
                console.print(f"[cyan]{t}[/cyan]: {desc}")

        else:
            console.print(Panel(f"[red]Unknown subcommand: {parts[0]}[/red]", border_style="red"))
        return True

    elif lower.startswith("/c2 "):
        from modules.stego.c2 import C2Channel
        import json

        rest = cmd[4:].strip()
        parts = rest.split()
        if not parts:
            console.print(Panel("[red]Usage:\n  /c2 implant [channel] [type] [domain]\n  /c2 beacon [channel] [domain]\n  /c2 server\n  /c2 config [channel]\n  /c2 info\n  /c2 encode <command>\n  /c2 decode <encoded>", border_style="red"))
            return True

        action = parts[0].lower()
        channel = parts[1] if len(parts) > 1 else "http"
        domain = parts[2] if len(parts) > 2 else "c2.example.com"
        if len(parts) > 3 and parts[3].startswith("http"):
            domain = parts[3]
            channel = parts[2] if len(parts) > 2 else "http"

        c2 = C2Channel(channel, domain, 60)

        if action == "info":
            info = c2.channel_info()
            for k, v in info.items():
                console.print(f"[cyan]{k}[/cyan]: {v}")
            return True

        if action == "implant":
            implant_type = parts[2] if len(parts) > 2 and parts[2] in ("powershell", "bash", "python") else "powershell"
            if implant_type in ("powershell", "bash", "python"):
                channel = parts[3] if len(parts) > 3 else "http"
                c2 = C2Channel(channel, parts[4] if len(parts) > 4 else domain, 60)
            result = c2.generate_c2_payload(implant_type)
            lang_map = {"powershell": "powershell", "bash": "bash", "python": "python"}
            console.print(Panel(Syntax(result, lang_map.get(implant_type, "powershell"), theme="monokai"), title=f"C2 Implant: {implant_type} @ {channel}", border_style="red"))

        elif action == "beacon":
            beacon = c2.beacon()
            console.print(Panel(json.dumps(beacon, indent=2), title=f"Beacon: {channel}", border_style="cyan"))

        elif action == "server":
            result = c2.generate_c2_server("flask")
            console.print(Panel(Syntax(result, "python", theme="monokai"), title="C2 Server (Flask)", border_style="green"))

        elif action == "config":
            result = c2.generate_channel_config(channel)
            console.print(Panel(Syntax(result, "json", theme="monokai"), title=f"C2 Config: {channel}", border_style="yellow"))

        elif action == "encode":
            command = " ".join(parts[1:]) if len(parts) > 1 else "whoami"
            result = c2.encode_command(command)
            console.print(Panel(result, title="Encoded Command", border_style="cyan"))

        elif action == "decode":
            encoded = parts[1] if len(parts) > 1 else ""
            result = c2.decode_command(encoded)
            if result:
                console.print(Panel(json.dumps(result, indent=2), title="Decoded Command", border_style="green"))
            else:
                console.print(Panel("[red]Failed to decode[/red]", border_style="red"))
        else:
            console.print(Panel(f"[red]Unknown action: {action}[/red]", border_style="red"))
        return True

    elif lower.startswith("/learn "):
        rest = cmd[7:].strip()
        parts = rest.split()
        if not parts:
            console.print(Panel("[red]Usage:\n  /learn init\n  /learn summary\n  /learn q_select [ports]\n  /learn skill_find [ports]\n  /learn hypothesis [ports...]\n  /learn plan [ports...]\n  /learn bayesian\n  /learn skill_summary", border_style="red"))
            return True

        from agent.learner import Learner
        if not hasattr(tool_runner, '_learner') or not tool_runner._learner:
            tool_runner._learner = Learner()
        l = tool_runner._learner

        action = parts[0].lower()
        if action == "init":
            l.init_advanced()
            result = l.advanced_summary()
            console.print(Panel(Markdown(result), title="Advanced Learner Initialized", border_style="green"))

        elif action == "summary":
            if l.q_selector:
                console.print(Panel(Markdown(l.advanced_summary()), title="Advanced Learner Status", border_style="cyan"))
            else:
                console.print(Panel(l.summary(), title="Basic Learner", border_style="cyan"))

        elif action == "q_select":
            l.init_advanced()
            ports = [int(p) for p in parts[1:]] if len(parts) > 1 else [80, 443]
            result = l.q_select(ports=ports)
            console.print(Panel(f"Q-Learning selected: [bold cyan]{result}[/bold cyan]", title="Strategy Selection", border_style="green"))

        elif action == "skill_find":
            l.init_advanced()
            ports = [int(p) for p in parts[1:]] if len(parts) > 1 else None
            results = l.skill_find(ports=ports)
            if results:
                table = Table(box=box.SIMPLE)
                table.add_column("Skill", style="cyan")
                table.add_column("Ports")
                table.add_column("Rate")
                table.add_column("Steps")
                for s in results[:10]:
                    rate = f"{s.get('success_rate', 0)*100:.0f}%" if s.get("success_rate") else "N/A"
                    ports_str = ",".join(str(p) for p in s.get("target_ports", [])) or "any"
                    table.add_row(s["name"][:30], ports_str, rate, str(len(s["steps"])))
                console.print(Panel(table, title="Matching Skills", border_style="cyan"))
            else:
                console.print(Panel("[yellow]No matching skills found[/yellow]", border_style="yellow"))

        elif action == "hypothesis":
            l.init_advanced()
            ports = [int(p) for p in parts[1:]] if len(parts) > 1 else [80, 443, 22]
            hyps = l.hypothesis_generate(ports)
            table = Table(box=box.SIMPLE)
            table.add_column("Port", style="dim")
            table.add_column("Hypothesis")
            table.add_column("Confidence")
            for h in hyps[:10]:
                conf = f"{h.get('confidence', 0):.0%}"
                table.add_row(str(h["port"]), h["hypothesis"][:60], conf)
            console.print(Panel(table, title=f"Hypotheses ({len(hyps)})", border_style="magenta"))

        elif action == "plan":
            l.init_advanced()
            ports = [int(p) for p in parts[1:]] if len(parts) > 1 else [80, 443, 22]
            plan = l.hypothesis_attack_plan(ports)
            if plan:
                table = Table(box=box.SIMPLE)
                table.add_column("Port", style="dim")
                table.add_column("Target")
                table.add_column("Command")
                table.add_column("Conf")
                for p in plan[:10]:
                    target = p.get("vulnerability", p.get("service_guess", "?"))
                    cmd = p.get("command", p.get("action", ""))[:40]
                    conf = f"{p.get('confidence', 0):.0%}"
                    table.add_row(str(p["port"]), target, cmd, conf)
                console.print(Panel(table, title="Attack Plan", border_style="red"))
            else:
                console.print(Panel("[yellow]No attack plan generated[/yellow]", border_style="yellow"))

        elif action == "bayesian":
            l.init_advanced()
            top = l.bayesian_top(10)
            if top:
                table = Table(box=box.SIMPLE)
                table.add_column("Port:Technique", style="cyan")
                table.add_column("Probability")
                for t in top:
                    table.add_row(t["key"], f"{t['probability']:.1%}")
                console.print(Panel(table, title="Bayesian Beliefs", border_style="green"))
            else:
                console.print(Panel("[yellow]No Bayesian data yet. Run some actions first.[/yellow]", border_style="yellow"))

        elif action == "skill_summary":
            result = l.skill_summary() if l.skill_library else "No skills."
            console.print(Panel(Markdown(result), title="Skill Library", border_style="cyan"))

        else:
            console.print(Panel(f"[red]Unknown action: {action}[/red]", border_style="red"))
        return True

    elif lower.startswith("/run "):
        rest = cmd[5:].strip()
        m = re.match(r"(.+?)\s+on\s+(.+?)(?::(\d+))?\s*$", rest)
        if not m:
            console.print(Panel("[red]Usage: /run <task> on <target>\n  e.g. /run scan SMB on 10.10.11.42\n  e.g. /run enumerate web on http://10.10.11.42:8080[/red]", border_style="red"))
            return True
        task = m.group(1).strip()
        target = m.group(2).strip()
        port = int(m.group(3)) if m.group(3) else None
        with console.status(f"[bold cyan]▶ Running:[/bold cyan] [white]{task}[/white] on [yellow]{target}[/yellow]", spinner="dots"):
            result = tool_runner.run("execute_task", {"task": task, "target": target, "port": port})
        if result.startswith("##"):
            console.print(Panel(Markdown(result), title=f"Run: {task}", border_style="green"))
        else:
            console.print(Panel(result, title=f"Run: {task}", border_style="cyan"))
        return True
    elif lower.startswith("/swarm "):
        rest = cmd[7:].strip()
        parts = rest.split(maxsplit=2)
        if not parts:
            console.print(Panel("[red]Usage: /swarm launch <type> <task> | /swarm chain | /swarm status[/red]", border_style="red"))
            return True

        if parts[0] == "status":
            if sub_agents:
                s = sub_agents.status()
                grid = Table.grid(padding=(0, 1))
                grid.add_column()
                grid.add_column()
                grid.add_row("[dim]Active agents[/dim]", str(len(s["active"])))
                grid.add_row("[dim]Completed agents[/dim]", str(s["completed"]))
                grid.add_row("[dim]Findings[/dim]", str(s["findings"]))
                grid.add_row("[dim]Credentials[/dim]", str(s["creds"]))
                console.print(Panel(grid, title="Swarm Status", border_style="cyan"))
                if s["active"]:
                    at = Table(box=box.SIMPLE)
                    at.add_column("Agent", style="cyan")
                    at.add_column("Status")
                    at.add_column("Task")
                    for aid, info in s["active"].items():
                        at.add_row(info["type"], info["status"], info["task"])
                    console.print(Panel(at, title="Active Agents", border_style="green"))
            else:
                console.print(Panel("[red]Swarm not initialized.[/red]", border_style="red"))
            return True

        elif parts[0] == "launch" and len(parts) >= 3:
            agent_type = parts[1].lower()
            task = parts[2]
            if agent_type not in ("recon", "exploit", "privesc", "lateral", "exfil", "distraction", "report"):
                console.print(Panel(f"[red]Unknown agent type: {agent_type}. Available: recon, exploit, privesc, lateral, exfil, distraction, report[/red]", border_style="red"))
                return True
            with console.status(f"[bold green]Swarm: deploying {agent_type} agent...", spinner="dots"):
                result = sub_agents.run(agent_type, task, wait=True, timeout=300)
            if isinstance(result, dict) and result.get("result"):
                text = result["result"].get("text", "")
                console.print(Panel(Markdown(text) if not text.startswith("Error") else text, title=f"Swarm: {agent_type}", border_style="green"))
            elif isinstance(result, str):
                console.print(Panel(Markdown(result) if not result.startswith("Error") else result, title=f"Swarm: {agent_type}", border_style="green"))
            return True

        elif parts[0] == "chain":
            if not autopilot or not autopilot.target:
                console.print(Panel("[yellow]Set a target first with /set-target or /autoon[/yellow]", border_style="yellow"))
                return True
            target = autopilot.target
            tasks = [
                ("recon", f"Full reconnaissance on {target}. Run port scan, service enum, OSINT.", target),
                ("exploit", f"Exploit any vulnerabilities found on {target}. Try credentials and known exploits.", target),
                ("privesc", f"Escalate privileges on {target}.", target),
                ("exfil", f"Extract flags and sensitive data from {target}.", target),
                ("report", f"Generate pentest report for engagement against {target}.", target),
            ]
            with console.status("[bold green]Swarm chain deploying agents...", spinner="dots"):
                aids = sub_agents.deploy_chain(tasks)
                for aid in aids:
                    sub_agents.wait_for(aid, timeout=600)
            console.print(Panel(f"[green]Swarm chain complete. {len(aids)} agents deployed.[/green]", border_style="green"))
            return True

        return True
    elif lower == "/banner":
        console.clear()
        print_banner()
        show_dashboard(state, load_config(), docker, autopilot)
        return True
    elif lower == "/exit" or lower == "/quit":
        console.print()
        console.rule(style="bold red")
        farewell = Text("\n  Goodbye, operator. Stay sharp.\n", style="bold red")
        console.print(Align.center(farewell))
        console.rule(style="bold red")
        sys.exit(0)
    elif lower.startswith("/compile "):
        from modules.payloads.compiler import Compiler, ToolchainError, CompilationError, CROSS_TARGETS
        CROSS_TARGET_NAMES = set(CROSS_TARGETS.keys())
        comp = Compiler()
        rest = cmd[9:].strip()
        parts = rest.split(maxsplit=1)
        if not parts or parts[0] in ("help", "--help"):
            console.print(Panel(
                "[red]Usage:\n"
                "  /compile list [rust|go|c] — list available templates\n"
                "  /compile templates [lang] — detailed template info (JSON)\n"
                "  /compile status — show toolchain status\n"
                "  /compile cross_targets [lang] — list cross-compile targets\n"
                "  /compile <template> <params> [target] — compile a payload\n"
                "\nExamples:\n"
                "  /compile rust_reverse_shell lhost=10.10.14.1 lport=4444\n"
                "  /compile go_reverse_shell lhost=10.10.14.1 lport=4444 windows_amd64\n"
                "  /compile c_reverse_shell_linux lhost=10.10.14.1 lport=4444[/red]",
                border_style="red"
            ))
            return True

        action = parts[0].lower()

        if action == "list":
            lang = parts[1].strip() if len(parts) > 1 and parts[1].strip() in ("rust", "go", "c") else None
            templates = comp.list_templates(lang)
            table = Table(box=box.SIMPLE)
            table.add_column("Template", style="cyan")
            table.add_column("Language")
            table.add_column("Parameters")
            table.add_column("Description")
            for name, meta in templates.items():
                pdesc = ", ".join(meta["params"].keys())
                table.add_row(name, meta["language"], pdesc, meta["description"][:60])
            console.print(Panel(table, title=f"Templates ({len(templates)})", border_style="green"))

        elif action == "status":
            s = comp.toolchain_status()
            table = Table(box=box.SIMPLE)
            table.add_column("Toolchain", style="cyan")
            table.add_column("Version/Status")
            table.add_row("Rust (rustc)", s.get("rust") or "[red]not found[/red]")
            table.add_row("Go (go)", s.get("go") or "[red]not found[/red]")
            table.add_row("C (gcc)", s.get("gcc") or "[red]not found[/red]")
            table.add_row("C Win cross", s.get("gcc_win") or "[red]not found[/red]")
            table.add_row("Rustup", s.get("rustup") or "[red]not found[/red]")
            table.add_row("Native compilers", ", ".join(s["native"]) or "[red]none[/red]")
            if s["cross_targets"]:
                ct_rows = "\n".join(f"  {t}: {', '.join(l)}" for t, l in s["cross_targets"].items())
                table.add_row("Cross targets", ct_rows)
            console.print(Panel(table, title="Compiler Toolchain Status", border_style="cyan"))

        elif action == "templates":
            lang = None
            if len(parts) > 1 and parts[1].strip() in ("rust", "go", "c"):
                lang = parts[1].strip()
            templates = comp.list_templates(lang)
            console.print(Panel(
                json.dumps({k: {"language": v["language"], "params": v["params"], "description": v["description"]} for k, v in templates.items()}, indent=2),
                title="Template Details",
                border_style="green"
            ))

        elif action == "cross_targets":
            lang = None
            if len(parts) > 1 and parts[1].strip() in ("rust", "go", "c"):
                lang = parts[1].strip()
            targets = comp.available_cross_targets(lang)
            table = Table(box=box.SIMPLE)
            table.add_column("Target", style="cyan")
            table.add_column("Supported Languages")
            for name, cfg in targets.items():
                langs = [k for k in ["go", "rust", "c"] if cfg and cfg.get(k)]
                table.add_row(name, ", ".join(langs))
            console.print(Panel(table, title=f"Cross-compile Targets ({len(targets)})", border_style="cyan"))

        else:
            template = action
            raw = parts[1] if len(parts) > 1 else ""
            cross = None
            params = {}

            segs = raw.split()
            i = 0
            while i < len(segs):
                if "=" in segs[i]:
                    k, v = segs[i].split("=", 1)
                    v2 = v.strip("\"'")
                    try:
                        v2 = int(v2)
                    except ValueError:
                        pass
                    params[k.strip()] = v2
                elif segs[i] in CROSS_TARGET_NAMES:
                    cross = segs[i]
                i += 1

            meta = comp.list_templates().get(template)
            if not meta:
                console.print(Panel(f"[red]Unknown template: {template}[/red]", border_style="red"))
                return True

            missing = [k for k in meta["params"] if k not in params]
            if missing:
                console.print(Panel(f"[red]Missing params: {', '.join(missing)}[/red]", border_style="red"))
                return True

            with console.status(f"[bold yellow]Compiling {template}..."):
                try:
                    result = comp.compile(template, params, cross)
                except (ToolchainError, CompilationError) as e:
                    console.print(Panel(f"[red]Compilation failed: {e}[/red]", border_style="red"))
                    return True

            if result["success"]:
                table = Table(box=box.SIMPLE)
                table.add_column("Property", style="cyan")
                table.add_column("Value")
                table.add_row("Template", template)
                table.add_row("Output", str(result.get("path", "N/A")))
                table.add_row("Size", f"{result.get('size_kb', 0)} KB")
                table.add_row("Time", f"{result['elapsed']}s")
                table.add_row("Command", result.get("cmd", "N/A")[:80])
                console.print(Panel(table, title="Compilation Successful", border_style="green"))
                if result.get("stderr"):
                    console.print(Panel(result["stderr"][:500], title="Warnings", border_style="yellow"))
            else:
                msg = f"[red]Compilation failed[/red]\n"
                msg += f"Command: {result.get('cmd', 'N/A')}\n"
                if result.get("stderr"):
                    msg += f"\nStderr:\n{result['stderr'][:1000]}"
                console.print(Panel(Markdown(msg), title="Compilation Error", border_style="red"))

        return True

    elif lower.startswith("/"):
        console.print(Panel(f"[red]Unknown command: {cmd}\nType /help for available commands.[/red]", border_style="red"))
        return True
    return False


def main():
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    try:
        api_key = get_api_key()
    except SystemExit:
        key = Prompt.ask("Enter your Anthropic API key", password=True)
        cfg = load_config()
        cfg["api_key"] = key
        save_config(cfg)
        api_key = key

    llm = LLM()
    state = SessionState()
    rag = RAGEngine()
    checkpoint = CheckpointGate()
    docker = DockerSandbox()
    sub_agents = SubAgentRunner(
        llm=llm,
        tool_runner=None,
        state=state,
        console=console,
    )
    tool_runner = ToolRunner(
        rag_engine=rag,
        checkpoint_gate=checkpoint,
        docker_sandbox=docker,
        sub_agents=sub_agents,
        state=state,
        brain=None,
    )

    sub_agents.tool_runner = tool_runner

    autopilot = AutoPilot(tool_runner=tool_runner, state=state, console=console)
    autopilot.set_swarm(sub_agents)
    messages = []

    pt_style = PtStyle.from_dict({
        "prompt": "bold cyan",
    })
    session = PromptSession(history=FileHistory(str(HISTORY_FILE)), style=pt_style)

    cfg = load_config()
    console.clear()
    print_banner()
    show_dashboard(state, cfg, docker, autopilot)
    console.print()

    while True:
        try:
            user_input = session.prompt("╭─[bold cyan]Shel[/bold cyan]\n╰─> ", style="")
        except (EOFError, KeyboardInterrupt):
            console.print("\n")
            console.rule(style="bold red")
            farewell = Text("  Goodbye, operator. Stay sharp.\n", style="bold red")
            console.print(Align.center(farewell))
            console.rule(style="bold red")
            break

        if not user_input.strip():
            continue

        console.print(Rule(style="dim"))
        if user_input.startswith("/"):
            handle_command(user_input, tool_runner, state, docker, sub_agents, rag, autopilot)
            if user_input.lower() not in ("/clear", "/banner"):
                show_dashboard(state, load_config(), docker, autopilot)
            continue

        state.log_event("user_message", user_input[:200])
        messages.append({"role": "user", "content": user_input})

        with console.status("[bold cyan]Shel is strategizing...", spinner="dots"):
            try:
                system_prompt = build_system_prompt(state)
                resp = llm.send_with_tools(
                    system_prompt, messages, TOOL_DEFINITIONS, tool_runner
                )
            except Exception as e:
                console.print(Panel(f"[red]{e}[/red]", title="Error", border_style="red"))
                state.log_event("error", str(e))
                messages.pop()
                continue

        for block in resp.content:
            if block.type == "text":
                console.print(Panel(Markdown(block.text), title="Shel", border_style="cyan"))
                state.log_event("assistant_response", block.text[:200])

        show_dashboard(state, load_config(), docker, autopilot)


if __name__ == "__main__":
    import sys

    if "--use-local" in sys.argv:
        from config.settings import load_config, save_config
        cfg = load_config()
        cfg["provider"] = "ollama"
        cfg["model"] = cfg.get("ollama_model", "dolphin-llama3:8b")
        save_config(cfg)

    if "--web" in sys.argv:
        from modules.api.server import start_server
        host = "127.0.0.1"
        port = 8080
        for i, a in enumerate(sys.argv):
            if a == "--host" and i + 1 < len(sys.argv):
                host = sys.argv[i + 1]
            if a == "--port" and i + 1 < len(sys.argv):
                port = int(sys.argv[i + 1])
        start_server(host=host, port=port)
    else:
        main()
