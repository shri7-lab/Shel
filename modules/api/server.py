import sys
import os
import json
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from config.settings import load_config, get_api_key
from agent.llm import LLM
from agent.state import SessionState
from agent.rag import RAGEngine
from agent.checkpoints import CheckpointGate
from agent.docker import DockerSandbox
from agent.tools import ToolRunner, TOOL_DEFINITIONS
from agent.sub_agent_runner import SubAgentRunner
from agent.autopilot import AutoPilot, PHASE_NAMES
from agent.system import build_system_prompt

app = FastAPI(title="Shel API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

shel_state = {}
shel_lock = threading.Lock()


class ChatRequest(BaseModel):
    message: str


class ToolRequest(BaseModel):
    name: str
    args: dict = {}


def init_shel():
    cfg = load_config()
    api_key = None
    try:
        api_key = get_api_key()
    except SystemExit:
        api_key = None

    llm = LLM()
    state = SessionState()
    rag = RAGEngine()
    checkpoint = CheckpointGate()
    docker = DockerSandbox()

    sub_agents = SubAgentRunner(llm=llm, tool_runner=None, state=state, console=None)
    tool_runner = ToolRunner(
        rag_engine=rag,
        checkpoint_gate=checkpoint,
        docker_sandbox=docker,
        sub_agents=sub_agents,
        state=state,
        brain=None,
    )
    sub_agents.tool_runner = tool_runner
    autopilot = AutoPilot(tool_runner=tool_runner, state=state, console=None)
    autopilot.set_swarm(sub_agents)

    return {
        "llm": llm,
        "state": state,
        "rag": rag,
        "checkpoint": checkpoint,
        "docker": docker,
        "tool_runner": tool_runner,
        "sub_agents": sub_agents,
        "autopilot": autopilot,
        "messages": [],
        "cfg": cfg,
    }


@app.on_event("startup")
async def startup():
    global shel_state
    shel_state = init_shel()


@app.get("/")
async def dashboard():
    templates_dir = Path(__file__).parent / "templates"
    index_path = templates_dir / "dashboard.html"
    if not index_path.exists():
        return JSONResponse({"error": "Dashboard template not found"}, status_code=404)
    return FileResponse(str(index_path))


@app.get("/api/status")
async def get_status():
    with shel_lock:
        s = shel_state
        state = s["state"]
        cfg = s["cfg"]
        autopilot = s["autopilot"]

        findings = state.findings
        actions = state.completed_actions
        has_brain = autopilot and autopilot.brain is not None
        phase_idx = autopilot.current_phase if autopilot and hasattr(autopilot, "current_phase") else -1
        phase_name = PHASE_NAMES[phase_idx] if phase_idx >= 0 and phase_idx < len(PHASE_NAMES) else "idle"
        target = state.targets[0] if state.targets else "none"

        recent = []
        for f in findings[-5:]:
            recent.append({
                "type": f.type,
                "description": f.detail[:120],
                "severity": f.confidence,
                "timestamp": f.timestamp,
            })

        status_data = {
            "provider": cfg.get("provider", "unknown"),
            "model": cfg.get("model", "unknown"),
            "mode": "autonomous" if phase_idx >= 0 else "interactive",
            "target": target,
            "phase": phase_idx if phase_idx >= 0 else "none",
            "phase_name": phase_name,
            "findings_count": len(findings),
            "actions_count": len(actions),
            "docker_available": s["docker"].available if s["docker"] else False,
            "recent_findings": recent,
            "events": state.session_log[-10:] if state.session_log else [],
        }
        return JSONResponse(status_data)


@app.get("/api/session")
async def get_session():
    with shel_lock:
        state = shel_state["state"]
        return JSONResponse({
            "target": state.targets[0] if state.targets else "",
            "targets": state.targets,
            "events": state.session_log[-50:] if state.session_log else [],
            "findings": [{"type": f.type, "detail": f.detail[:120], "confidence": f.confidence} for f in state.findings[-20:]],
            "phase": state.current_phase,
        })


@app.post("/api/chat")
async def chat(req: ChatRequest):
    user_msg = req.message.strip()
    if not user_msg:
        return JSONResponse({"error": "Empty message"}, status_code=400)

    with shel_lock:
        s = shel_state
        msg_list = s["messages"]
        llm = s["llm"]
        tool_runner = s["tool_runner"]
        state = s["state"]

        state.log_event("user_message", user_msg[:200])
        msg_list.append({"role": "user", "content": user_msg})

        if user_msg.startswith("/"):
            return handle_api_command(user_msg, s)

        try:
            system_prompt = build_system_prompt(state)
            resp = llm.send_with_tools(
                system_prompt, msg_list, TOOL_DEFINITIONS, tool_runner
            )
        except Exception as e:
            msg_list.pop()
            return JSONResponse({"error": str(e)}, status_code=500)

        response_blocks = []
        for block in resp.content:
            if block.type == "text":
                response_blocks.append({"type": "text", "content": block.text})
                state.log_event("assistant_response", block.text[:200])
            elif block.type == "tool_use":
                response_blocks.append({
                    "type": "tool_use",
                    "name": block.name,
                    "input": block.input,
                })

        return JSONResponse({
            "blocks": response_blocks,
            "messages": msg_list[-10:],
        })


@app.post("/api/tool")
async def run_tool(req: ToolRequest):
    with shel_lock:
        s = shel_state
        tool_runner = s["tool_runner"]
        state = s["state"]
        try:
            result = tool_runner.run(req.name, req.args)
            if state:
                state.add_finding("tool", f"Ran {req.name}", "info")
            return JSONResponse({"success": True, "result": str(result)})
        except Exception as e:
            return JSONResponse({"success": False, "error": str(e)}, status_code=500)


@app.get("/api/tools")
async def list_tools():
    return JSONResponse([{
        "name": t["name"],
        "description": t["description"],
    } for t in TOOL_DEFINITIONS])


def handle_api_command(cmd, s):
    lower = cmd.strip().lower()
    tool_runner = s["tool_runner"]
    from modules.payloads.compiler import Compiler, CROSS_TARGETS

    if lower == "/status":
        state = s["state"]
        target = state.targets[0] if state.targets else "none"
        content = f"Target: {target}\nPhase: {state.current_phase}\nFindings: {len(state.findings)}\nActions: {len(state.completed_actions)}\nEvents: {len(state.session_log)}"
        return JSONResponse({"blocks": [{"type": "text", "content": content}]})

    elif lower == "/help":
        from main import show_dashboard
        return JSONResponse({"blocks": [{"type": "text", "content": "Commands: /status, /help, /clear, /compile, /stego, /c2, /social, /evasion, /supplychain, /learn"}]})

    elif lower.startswith("/compile "):
        comp = Compiler()
        rest = cmd[9:].strip()
        parts = rest.split(maxsplit=1)
        if not parts or parts[0] == "list":
            lang = parts[1] if len(parts) > 1 and parts[1] in ("rust","go","c") else None
            templates = comp.list_templates(lang)
            return JSONResponse({"blocks": [{"type": "text", "content": json.dumps({k: {"language": v["language"], "params": list(v["params"].keys()), "description": v["description"]} for k, v in templates.items()}, indent=2)}]})
        tname = parts[0]
        params = {}
        if len(parts) > 1:
            for seg in parts[1].split():
                if "=" in seg:
                    k, v = seg.split("=", 1)
                    try: v = int(v)
                    except: pass
                    params[k] = v
        try:
            result = comp.compile(tname, params)
            if result["success"]:
                return JSONResponse({"blocks": [{"type": "text", "content": f"Compiled to {result['path']} ({result['size_kb']} KB)"}]})
            return JSONResponse({"blocks": [{"type": "text", "content": f"Failed: {result.get('stderr','')[:500]}"}]})
        except Exception as e:
            return JSONResponse({"blocks": [{"type": "text", "content": f"Error: {e}"}]})

    elif lower.startswith("/stego ") or lower.startswith("/c2 "):
        try:
            resp = tool_runner.run("stego_encode" if "/stego" in lower else "c2_channel", {"action": "info"})
            return JSONResponse({"blocks": [{"type": "text", "content": str(resp)[:2000]}]})
        except Exception as e:
            return JSONResponse({"blocks": [{"type": "text", "content": f"Error: {e}"}]})

    else:
        return JSONResponse({"blocks": [{"type": "text", "content": f"Unknown or non-API command: {cmd}"}]})


def start_server(host="127.0.0.1", port=8080):
    print(f"[+] Shel Web Dashboard: http://{host}:{port}")
    print("[+] Press Ctrl+C to stop")
    uvicorn.run(app, host=host, port=port, log_level="warning")
