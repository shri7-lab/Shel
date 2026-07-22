import subprocess
import json
import urllib.request
import urllib.parse
import re
from pathlib import Path

TOOL_DEFINITIONS = [
    {
        "name": "bash",
        "description": "Execute a shell command on the local system. Use for running pentesting tools like nmap, curl, etc.",
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "The shell command to execute"},
            },
            "required": ["command"],
        },
    },
    {
        "name": "read_file",
        "description": "Read the contents of a file on the local system.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Absolute path to the file"},
            },
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": "Write content to a file on the local system. Use for saving scripts, payloads, and reports.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Absolute path to the file"},
                "content": {"type": "string", "description": "Content to write"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "search_web",
        "description": "Search the web for HTB writeups, exploit details, CVE info, or documentation.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "fetch_url",
        "description": "Fetch content from a URL. Use for reading writeups, exploit code, or documentation.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "URL to fetch"},
            },
            "required": ["url"],
        },
    },
    {
        "name": "generate_payload",
        "description": "Generate a payload using built-in modules. Types: reverse_shell, webshell, sqli, xss, encoder, msfvenom.",
        "input_schema": {
            "type": "object",
            "properties": {
                "payload_type": {
                    "type": "string",
                    "enum": ["reverse_shell", "webshell", "sqli", "xss", "encoder", "msfvenom"],
                    "description": "Type of payload to generate",
                },
                "params": {
                    "type": "object",
                    "description": "Parameters (e.g., lhost, lport, type, payload, format)",
                },
            },
            "required": ["payload_type", "params"],
        },
    },
    {
        "name": "query_knowledge",
        "description": "Search your built-in pentesting knowledge base for methodology, commands, and techniques.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "What to look up (e.g., 'SMB enumeration', 'Linux privesc', 'SQLi payloads')"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "store_writeup",
        "description": "Save a writeup or reference material into your knowledge base for future use.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Title of the writeup"},
                "content": {"type": "string", "description": "Full content of the writeup in markdown"},
            },
            "required": ["title", "content"],
        },
    },
    {
        "name": "docker_run",
        "description": "Run a command inside a Kali Linux Docker container with pentesting tools pre-installed (nmap, hydra, sqlmap, etc.).",
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "Command to run inside the container"},
            },
            "required": ["command"],
        },
    },
    {
        "name": "sub_agent",
        "description": "Delegate a specialized task to a sub-agent. Types: recon (scanning), exploit (exploitation), report (documentation).",
        "input_schema": {
            "type": "object",
            "properties": {
                "agent_type": {
                    "type": "string",
                    "enum": ["recon", "exploit", "report"],
                    "description": "Which sub-agent to use",
                },
                "task": {"type": "string", "description": "What to ask the sub-agent to do"},
            },
            "required": ["agent_type", "task"],
        },
    },
    {
        "name": "get_session_summary",
        "description": "Get a summary of the current session state including findings, completed actions, and pending steps.",
        "input_schema": {
            "type": "object",
            "properties": {},
        },
    },
    {
        "name": "suggest_tools",
        "description": "Suggest relevant BlackArch pentesting tools based on a task description. Example: 'scan ports' -> nmap, 'crack password' -> hashcat.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task": {"type": "string", "description": "Describe what you want to do (e.g., 'enumerate SMB shares', 'scan for SQL injection', 'crack NTLM hashes')"},
            },
            "required": ["task"],
        },
    },
    {
        "name": "search_tools",
        "description": "Search the BlackArch tool database by name or keyword to find a specific tool and its description.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Tool name or keyword to search for"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "execute_task",
        "description": "Universal task executor: describe any pentesting task and Shel will find the right tool and run it automatically. Use instead of bash when you know what to do but not which tool to use.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task": {"type": "string", "description": "What to do (e.g., 'enumerate SMB on 10.10.11.42', 'brute force SSH on 10.10.11.42:22 with user admin', 'scan web directory on http://10.10.11.42')"},
                "target": {"type": "string", "description": "Target IP or hostname"},
                "port": {"type": "integer", "description": "Target port (optional)"},
            },
            "required": ["task", "target"],
        },
    },
    {
        "name": "brain_goal",
        "description": "Add a goal to the Brain's autonomous decision queue. Brain will plan, execute, and learn from it automatically. Use when you want the autonomous loop to handle a task.",
        "input_schema": {
            "type": "object",
            "properties": {
                "objective": {"type": "string", "description": "Goal type: 'port scan', 'service enum', 'web recon', 'enum smb', 'enum ftp', 'enum ssh', 'enum ldap', 'enum nfs', 'enum mysql', 'enum redis', 'enum mongo', 'brute force', 'vuln scan', 'exploit search', 'crack hash', 'get foothold', 'privesc', 'lateral move'"},
                "target": {"type": "string", "description": "Target IP or hostname"},
                "port": {"type": "integer", "description": "Target port (optional)"},
                "priority": {"type": "integer", "description": "Priority 1-10 (10=critical, 5=normal, 1=optional). Defaults based on objective type."},
            },
            "required": ["objective", "target"],
        },
    },
    {
        "name": "brain_status",
        "description": "Get the Brain's current status: goal queue, learner statistics, blackboard state (targets, creds, findings found so far).",
        "input_schema": {
            "type": "object",
            "properties": {},
        },
    },
    {
        "name": "evasion_polymorph",
        "description": "Mutate a script payload using a polymorphic engine to evade signature-based detection. Supports python, powershell, bash, perl.",
        "input_schema": {
            "type": "object",
            "properties": {
                "code": {"type": "string", "description": "The original script code to mutate"},
                "lang": {"type": "string", "enum": ["python", "powershell", "bash", "perl"], "description": "Language of the script"},
                "encoding_rounds": {"type": "integer", "description": "Number of encoding layers to wrap (0-5, default 1)"},
            },
            "required": ["code", "lang"],
        },
    },
    {
        "name": "evasion_bypass",
        "description": "Generate AMSI bypass, ETW bypass, sandbox detection, or process injection PowerShell code for defense evasion.",
        "input_schema": {
            "type": "object",
            "properties": {
                "technique": {
                    "type": "string",
                    "enum": ["amsi_memory", "amsi_registry", "amsi_reflection", "etw", "sandbox_detect", "inject_crt", "inject_apc", "inject_hollow", "all"],
                    "description": "Which bypass technique to generate",
                },
            },
            "required": ["technique"],
        },
    },
    {
        "name": "evasion_lolbin",
        "description": "Generate fileless execution commands using Living-off-the-Land binaries (LOLBins). Supports download cradles, execution commands, and reverse shells.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["download", "execute", "reverse_shell", "find", "list", "summary"],
                    "description": "What to generate: download cradle, execution command, reverse shell, find by capability, list all, or summary",
                },
                "bin_name": {"type": "string", "description": "Name of the LOLBin (e.g., powershell, certutil, rundll32). Required for download/execute/reverse_shell."},
                "url": {"type": "string", "description": "URL for download cradle"},
                "payload_path": {"type": "string", "description": "Path to payload file for execution"},
                "lhost": {"type": "string", "description": "Listener IP for reverse shell"},
                "lport": {"type": "integer", "description": "Listener port for reverse shell"},
                "capability": {"type": "string", "description": "Filter by capability: execute, download, encode, bypass, reverse_shell, port_scan"},
                "platform": {"type": "string", "enum": ["windows", "linux"], "description": "Target platform (default: windows)"},
            },
            "required": ["action"],
        },
    },
    {
        "name": "supplychain_recon",
        "description": "Scan repository file contents for supply chain risks: dependency analysis, secret leaks, CI/CD workflow misconfigurations.",
        "input_schema": {
            "type": "object",
            "properties": {
                "files": {
                    "type": "object",
                    "description": "Dict of filename -> content for all repo files to scan",
                },
                "dependency_list": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of dependency names for confusion candidate detection",
                },
            },
            "required": ["files"],
        },
    },
    {
        "name": "supplychain_poison",
        "description": "Generate malicious packages for dependency confusion and typo-squatting attacks. Supports npm, pip, and cargo ecosystems.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["confusion_package", "typo_squat", "squat_list"],
                    "description": "What to generate: a malicious package, a single typo-squat, or a list of squats",
                },
                "package_name": {"type": "string", "description": "Original package name to target for confusion/squatting"},
                "ecosystem": {"type": "string", "enum": ["npm", "pip", "cargo"], "description": "Package ecosystem (default: npm)"},
                "payload_type": {"type": "string", "enum": ["reverse_shell", "env_leak", "cred_harvest", "crypto_miner", "backdoor"], "description": "Payload type for the malicious package"},
                "lhost": {"type": "string", "description": "Listener IP for reverse shell"},
                "lport": {"type": "integer", "description": "Listener port for reverse shell"},
                "count": {"type": "integer", "description": "Number of squat names to generate (default: 10)"},
            },
            "required": ["action"],
        },
    },
    {
        "name": "supplychain_cicd",
        "description": "Generate CI/CD workflow exploitation payloads: pull_request_target abuse, self-hosted runner compromise, token theft, dependency confusion in CI.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["generate", "techniques", "runner_registration", "dep_confusion_pip", "summary"],
                    "description": "Action to perform",
                },
                "technique": {
                    "type": "string",
                    "enum": ["pr_target", "self_hosted", "dependency_confusion", "token_theft", "approval_bypass"],
                    "description": "Attack technique for generate action",
                },
                "target_repo": {"type": "string", "description": "Target repo in format owner/repo"},
                "package_name": {"type": "string", "description": "Package name for dep confusion pip command"},
            },
            "required": ["action"],
        },
    },
    {
        "name": "social_engine",
        "description": "Social engineering campaign engine: create campaigns, set targets/objectives, manage personas, generate attack chains. Use for ceo_fraud, spear_phish, vishing, credential_harvest, malware_delivery, supply_chain attacks.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["campaign", "target_profile", "persona", "chains", "plan", "execute", "status", "vector_info"],
                    "description": "Action: campaign=create new, target_profile=analyze target, persona=generate persona, chains=show attack chain, plan=full campaign plan, execute=next stage, status=current state, vector_info=list vectors",
                },
                "objective": {"type": "string", "enum": ["credential_harvest", "malware_delivery", "ceo_fraud", "spear_phish", "vishing", "supply_chain"], "description": "Campaign objective"},
                "target_name": {"type": "string", "description": "Target's name"},
                "target_org": {"type": "string", "description": "Target's organization"},
                "target_email": {"type": "string", "description": "Target's email"},
                "target_role": {"type": "string", "description": "Target's role/job title"},
                "persona_name": {"type": "string", "description": "Persona name to impersonate"},
                "persona_role": {"type": "string", "description": "Persona role for impersonation"},
            },
            "required": ["action"],
        },
    },
    {
        "name": "social_phish",
        "description": "Generate phishing email/SMS templates, landing page HTML, and macro payloads for social engineering campaigns.",
        "input_schema": {
            "type": "object",
            "properties": {
                "style": {
                    "type": "string",
                    "enum": ["security_alert", "password_reset", "invoice", "doc_share", "docusign", "fedex", "voicemail", "calendar_invite", "compliance", "benefits", "it_notice", "hr_update", "linkedin", "teams_notification", "zoom_invite", "office365", "gmail", "generic", "okta", "vpn", "sms_urgent", "sms_delivery", "sms_banking", "macro_revshell", "macro_keylogger", "macro_credharvest"],
                    "description": "Template style or payload type",
                },
                "target_name": {"type": "string", "description": "Target's name for template personalization"},
                "target_email": {"type": "string", "description": "Target's email"},
                "org": {"type": "string", "description": "Organization name for branding"},
                "lhost": {"type": "string", "description": "Listener IP for reverse shell macros"},
                "lport": {"type": "integer", "description": "Listener port for reverse shell macros"},
            },
            "required": ["style"],
        },
    },
    {
        "name": "social_deepfake",
        "description": "Deepfake generation framework: orchestrate external ML tools (FaceSwap, Wav2Lip, Tortoise TTS, StyleGAN, Roop) for fake audio/video/image generation. Generate ready-to-run scripts.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["status", "script", "pipeline_voice", "pipeline_video", "persona_images", "report"],
                    "description": "Action to perform",
                },
                "tool": {"type": "string", "enum": ["faceswap", "wav2lip", "deepfacelab", "tortoise_tts", "stylegan3", "roop", "first_order_model", "so-vits-svc", "voice_cloner"], "description": "Deepfake tool for script generation"},
                "tool_action": {"type": "string", "description": "Tool-specific action (e.g., swap, train, convert, sync, generate)"},
                "source": {"type": "string", "description": "Source file path (face image, audio sample, etc.)"},
                "target": {"type": "string", "description": "Target file path (video, image, etc.)"},
                "output": {"type": "string", "description": "Output file path"},
                "script_text": {"type": "string", "description": "Speech text for voice pipelines"},
                "target_voice_sample": {"type": "string", "description": "Path to target voice sample for cloning"},
            },
            "required": ["action"],
        },
    },
    {
        "name": "stego_encode",
        "description": "Hide data using steganography. Supports text_whitespace (space/tab), text_homoglyph (Unicode lookalike chars), pixel_lsb (image bitmap), audio_lsb (WAV samples), http_header, dns_query, image_metadata, tcp_timestamp.",
        "input_schema": {
            "type": "object",
            "properties": {
                "technique": {
                    "type": "string",
                    "enum": ["text_whitespace", "text_homoglyph", "pixel_lsb", "audio_lsb", "http_header", "dns_query", "image_metadata", "tcp_timestamp"],
                    "description": "Steganography technique to use",
                },
                "payload": {"type": "string", "description": "The secret data to hide"},
                "cover": {"type": "string", "description": "Cover text for text stego techniques"},
                "cover_length": {"type": "integer", "description": "Generate cover of this length if no cover provided"},
            },
            "required": ["technique", "payload"],
        },
    },
    {
        "name": "stego_decode",
        "description": "Extract hidden data from steganography output. Use the matching technique to recover the original payload.",
        "input_schema": {
            "type": "object",
            "properties": {
                "technique": {"type": "string", "enum": ["text_whitespace", "text_homoglyph", "pixel_lsb", "audio_lsb", "http_header", "dns_query", "image_metadata", "tcp_timestamp"], "description": "Steganography technique used to encode"},
                "stego_data": {"type": "string", "description": "The stego text/data to decode"},
                "dns_queries": {"type": "array", "items": {"type": "string"}, "description": "DNS query list for dns_query decode"},
                "headers": {"type": "object", "description": "HTTP headers dict for http_header decode"},
            },
            "required": ["technique"],
        },
    },
    {
        "name": "c2_channel",
        "description": "Covert C2 channel management: generate beacon payloads, C2 server code, and channel configs for DNS/HTTP/Social/Blockchain C2.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["beacon", "implant", "server", "config", "info", "encode", "decode"],
                    "description": "Action: beacon=generate beacon request, implant=generate implant code, server=generate C2 server, config=channel config, info=channel descriptions, encode=encode command, decode=decode response",
                },
                "channel": {"type": "string", "enum": ["dns", "http", "https", "social", "blockchain", "icmp", "websocket", "tor"], "description": "C2 channel type (default: dns)"},
                "implant_type": {"type": "string", "enum": ["powershell", "bash", "python"], "description": "Implant language (default: powershell)"},
                "server_framework": {"type": "string", "enum": ["flask"], "description": "Server framework (default: flask)"},
                "c2_domain": {"type": "string", "description": "C2 domain (default: c2.example.com)"},
                "interval": {"type": "integer", "description": "Beacon interval in seconds (default: 60)"},
                "command": {"type": "string", "description": "Command to encode for C2"},
                "encoded": {"type": "string", "description": "Encoded command string to decode"},
            },
            "required": ["action"],
        },
    },
    {
        "name": "advanced_learn",
        "description": "Advanced continuous learning system: Q-learning strategy selection, skill memory, hypothesis engine, Bayesian inference. Initialize with 'init', then use 'q_select', 'q_learn', 'skill_save', 'skill_find', 'skill_exec', 'hypothesis', 'bayesian', or 'summary'.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["init", "q_select", "q_learn", "skill_save", "skill_find", "skill_exec", "skill_summary", "hypothesis", "attack_plan", "hypothesis_summary", "bayesian_top", "summary"],
                    "description": "Action to perform",
                },
                "target": {"type": "string", "description": "Target host for skill execution"},
                "ports": {"type": "array", "items": {"type": "integer"}, "description": "List of open ports for state encoding"},
                "services": {"type": "array", "items": {"type": "string"}, "description": "Service names for state encoding"},
                "os_type": {"type": "string", "description": "Target OS type for state encoding"},
                "findings": {"type": "array", "items": {"type": "string"}, "description": "Session findings for state encoding"},
                "skill_id": {"type": "string", "description": "Skill ID for execution or lookup"},
                "steps": {"type": "array", "description": "Skill steps (list of action dicts) for skill_save"},
                "port": {"type": "integer", "description": "Target port for Bayesian update"},
                "technique": {"type": "string", "description": "Technique name for Bayesian/Q-learning"},
                "tool": {"type": "string", "description": "Tool name for Q-learning"},
                "success": {"type": "boolean", "description": "Whether the action succeeded"},
                "duration": {"type": "number", "description": "Action duration in seconds"},
            },
            "required": ["action"],
        },
    },
    {
        "name": "compile_payload",
        "description": "Compile a native payload binary from source templates. Languages: rust, go, c. Supports cross-compilation to linux_amd64, windows_amd64, darwin_amd64, and more. Use list action to see available templates and toolchains.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["list", "compile", "status", "templates", "cross_targets"],
                    "description": "Action: list=available templates, compile=build a payload, status=toolchain status, templates=detailed template info, cross_targets=available cross-compile targets",
                },
                "language": {
                    "type": "string",
                    "enum": ["rust", "go", "c"],
                    "description": "Language filter for list/templates actions",
                },
                "template": {
                    "type": "string",
                    "description": "Template name (e.g., rust_reverse_shell, go_reverse_shell, c_reverse_shell_linux)",
                },
                "params": {
                    "type": "object",
                    "description": "Template parameters as key-value pairs (e.g., {'lhost': '10.10.14.1', 'lport': 4444})",
                },
                "cross_target": {
                    "type": "string",
                    "description": "Cross-compilation target (e.g., windows_amd64, linux_amd64, darwin_amd64)",
                },
                "strip": {
                    "type": "boolean",
                    "description": "Strip symbols from output (default: true)",
                },
                "optimize": {
                    "type": "boolean",
                    "description": "Optimize for size (default: true)",
                },
                "outfile": {
                    "type": "string",
                    "description": "Custom output filename (default: <template_name>[<cross_target>].ext)",
                },
            },
            "required": ["action"],
        },
    },
]

class ToolRunner:
    def __init__(self, rag_engine=None, checkpoint_gate=None, docker_sandbox=None, sub_agents=None, state=None, brain=None):
        self.rag_engine = rag_engine
        self.checkpoint_gate = checkpoint_gate
        self.docker_sandbox = docker_sandbox
        self.sub_agents = sub_agents
        self.state = state
        self.brain = brain
        self.allow_bash = True
        self.auto_mode = False

    def run(self, name, args):
        handlers = {
            "bash": self._bash,
            "read_file": self._read_file,
            "write_file": self._write_file,
            "search_web": self._search_web,
            "fetch_url": self._fetch_url,
            "generate_payload": self._generate_payload,
            "query_knowledge": self._query_knowledge,
            "store_writeup": self._store_writeup,
            "docker_run": self._docker_run,
            "sub_agent": self._sub_agent,
            "get_session_summary": self._get_session_summary,
            "suggest_tools": self._suggest_tools,
            "search_tools": self._search_tools,
            "execute_task": self._execute_task,
            "brain_goal": self._brain_goal,
            "brain_status": self._brain_status,
            "evasion_polymorph": self._evasion_polymorph,
            "evasion_bypass": self._evasion_bypass,
            "evasion_lolbin": self._evasion_lolbin,
            "supplychain_recon": self._supplychain_recon,
            "supplychain_poison": self._supplychain_poison,
            "supplychain_cicd": self._supplychain_cicd,
            "social_engine": self._social_engine,
            "social_phish": self._social_phish,
            "social_deepfake": self._social_deepfake,
            "stego_encode": self._stego_encode,
            "stego_decode": self._stego_decode,
            "c2_channel": self._c2_channel,
            "advanced_learn": self._advanced_learn,
            "compile_payload": self._compile_payload,
        }
        handler = handlers.get(name)
        if not handler:
            return f"Unknown tool: {name}"
        try:
            return handler(args)
        except Exception as e:
            import traceback
            return f"Error executing {name}: {e}\n{traceback.format_exc()}"

    def _bash(self, args):
        cmd = args["command"]
        if not self.allow_bash:
            return "Bash execution is disabled via /shell-off."
        if self.checkpoint_gate and not self.auto_mode:
            allowed, msg = self.checkpoint_gate.check_command(cmd)
            if not allowed:
                return msg
        if self.state:
            self.state.start_action(f"bash: {cmd[:100]}", command=cmd)
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=180
        )
        output = ""
        if result.stdout:
            output += result.stdout
        if result.stderr:
            output += f"\n[stderr]\n{result.stderr}"
        if result.returncode != 0:
            output += f"\n[exit code: {result.returncode}]"
        result_text = output or "(no output)"
        if self.state:
            self.state.complete_action(result_text[:500])
        if len(result_text) > 5000:
            result_text = result_text[:5000] + "\n... [truncated]"
        return result_text

    def _read_file(self, args):
        p = Path(args["path"]).expanduser()
        if not p.exists():
            return f"File not found: {args['path']}"
        content = p.read_text(encoding="utf-8", errors="replace")
        if len(content) > 8000:
            content = content[:8000] + "\n... [truncated]"
        return content

    def _write_file(self, args):
        p = Path(args["path"]).expanduser()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(args["content"])
        return f"Written to {p}"

    def _search_web(self, args):
        query = urllib.parse.quote(args["query"])
        url = f"https://html.duckduckgo.com/html/?q={query}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode()
            results = re.findall(
                r'<a rel="nofollow" class="result__a" href="([^"]+)".*?class="result__snippet">(.*?)</a>',
                html, re.DOTALL,
            )
            out = []
            for href, snippet in results[:6]:
                clean = re.sub(r"<[^>]+>", "", snippet).strip()
                out.append(f"{href}\n  {clean[:200]}")
            return "\n\n".join(out) if out else "No results found."
        except Exception as e:
            return f"Search failed: {e}"

    def _fetch_url(self, args):
        try:
            req = urllib.request.Request(
                args["url"], headers={"User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                html = resp.read().decode()
            try:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(html, "html.parser")
                for tag in soup(["script", "style", "nav", "footer", "header"]):
                    tag.decompose()
                text = soup.get_text(separator="\n", strip=True)
                lines = [l for l in text.split("\n") if len(l.strip()) > 40]
                return "\n".join(lines[:200])
            except ImportError:
                text = re.sub(r"<[^>]+>", " ", html)
                text = re.sub(r"\s+", " ", text).strip()
                return text[:5000]
        except Exception as e:
            return f"Fetch failed: {e}"

    def _generate_payload(self, args):
        from modules.payloads.generator import generate
        result = generate(args["payload_type"], args.get("params", {}))
        if self.state:
            self.state.add_finding("payload", f"Generated {args['payload_type']} payload", "low")
        return result

    def _compile_payload(self, args):
        from modules.payloads.compiler import Compiler, ToolchainError, CompilationError
        comp = Compiler()
        action = args.get("action", "list")

        if action == "status":
            s = comp.toolchain_status()
            lines = ["## Toolchain Status"]
            lines.append(f"Rust: {s.get('rust') or 'not found'}")
            lines.append(f"Go: {s.get('go') or 'not found'}")
            lines.append(f"GCC: {s.get('gcc') or 'not found'}")
            lines.append(f"GCC (Win cross): {s.get('gcc_win') or 'not found'}")
            lines.append(f"Rustup: {s.get('rustup') or 'not found'}")
            lines.append(f"\nNative compilers: {', '.join(s['native']) or 'none'}")
            lines.append(f"\nCross-compile targets ({len(s['cross_targets'])}):")
            for tgt, langs in s['cross_targets'].items():
                lines.append(f"  {tgt}: {', '.join(langs)}")
            return "\n".join(lines)

        elif action == "list":
            lang = args.get("language")
            templates = comp.list_templates(lang)
            if not templates:
                return "No templates found."
            lines = [f"## Templates ({len(templates)})"]
            for name, meta in templates.items():
                pdesc = ", ".join(f"{k}={v}" for k, v in meta["params"].items())
                lines.append(f"  {name}")
                lines.append(f"    language: {meta['language']}")
                lines.append(f"    {meta['description']}")
                lines.append(f"    params: {pdesc}")
            return "\n".join(lines)

        elif action == "templates":
            lang = args.get("language")
            templates = comp.list_templates(lang)
            import json
            return json.dumps(templates, indent=2, default=str)

        elif action == "cross_targets":
            lang = args.get("language")
            targets = comp.available_cross_targets(lang)
            lines = [f"## Cross-compile Targets ({len(targets)})"]
            for name, cfg in targets.items():
                langs = [k for k in ["go", "rust", "c"] if cfg and cfg.get(k)]
                lines.append(f"  {name}: {', '.join(langs)}")
            return "\n".join(lines)

        elif action == "compile":
            template = args.get("template")
            if not template:
                return "Error: 'template' is required for compile action."
            params = args.get("params", {})
            cross = args.get("cross_target")
            strip = args.get("strip", True)
            optimize = args.get("optimize", True)
            outfile = args.get("outfile")

            try:
                result = comp.compile(template, params, cross, strip, optimize, outfile)
            except (ToolchainError, CompilationError) as e:
                return f"Compilation failed: {e}"

            if result["success"]:
                msg = f"## Compilation Successful"
                msg += f"\nTemplate: {template}"
                msg += f"\nOutput: {result.get('path', 'unknown')}"
                msg += f"\nSize: {result.get('size_kb', 0)} KB"
                msg += f"\nTime: {result['elapsed']}s"
                msg += f"\nCommand: {result.get('cmd', 'N/A')}"
                if result.get("stdout"):
                    msg += f"\nStdout: {result['stdout'][:500]}"
                if self.state:
                    self.state.add_finding("payload", f"Compiled {template} binary ({result.get('size_kb',0)} KB)", "medium")
                return msg
            else:
                msg = f"## Compilation Failed"
                msg += f"\nTemplate: {template}"
                msg += f"\nCommand: {result.get('cmd', 'N/A')}"
                if result.get("stderr"):
                    msg += f"\nStderr:\n{result['stderr'][:1000]}"
                if result.get("stdout"):
                    msg += f"\nStdout:\n{result['stdout'][:500]}"
                return msg

        return f"Unknown action: {action}"

    def _query_knowledge(self, args):
        if not self.rag_engine:
            return "Knowledge base not available."
        results = self.rag_engine.query(args["query"])
        if not results:
            return "No relevant knowledge found. Try a web search instead."
        out = []
        for r in results[:3]:
            section_content = self.rag_engine.get_section(r["source"], r["section"])
            if section_content:
                out.append(f"## {r['source']} — {r['section']}\n{section_content[:500]}")
        return "\n\n".join(out) if out else "No detailed matches found."

    def _store_writeup(self, args):
        if not self.rag_engine:
            return "Knowledge base not available."
        path = self.rag_engine.store_writeup(args["title"], args["content"])
        if self.state:
            self.state.add_finding("writeup", f"Stored: {args['title']}", "low")
        return f"Writeup saved to {path}"

    def _docker_run(self, args):
        if not self.docker_sandbox or not self.docker_sandbox.available:
            return "Docker is not available. Install Docker Desktop or use bash tool instead."
        return self.docker_sandbox.run_command(args["command"])

    def _sub_agent(self, args):
        if not self.sub_agents:
            return "Sub-agent system not available."
        agent_type = args["agent_type"]
        task = args["task"]
        return self.sub_agents.run(agent_type, task, self.state)

    def _get_session_summary(self, args):
        if not self.state:
            return "No session state available."
        return self.state.to_prompt_block()

    def _suggest_tools(self, args):
        try:
            from modules.tool_db import suggest_tools
            results = suggest_tools(args["task"])
            if not results:
                return "No specific tools found for this task. Try searching the knowledge base or web."
            lines = [f"## Suggested tools for: {args['task']}"]
            seen = set()
            count = 0
            for category, tool in results:
                if tool['name'] in seen:
                    continue
                seen.add(tool['name'])
                lines.append(f"- **{tool['name']}** ({category.replace('blackarch-', '')}) - {tool['description'][:120]}")
                count += 1
                if count >= 15:
                    break
            if len(results) > 15:
                lines.append(f"\n... and {len(results) - 15} more tools.")
            return "\n".join(lines)
        except ImportError:
            return "Tool database not loaded."

    def _execute_task(self, args):
        from agent.tool_matcher import ToolMatcher
        matcher = ToolMatcher()
        task = args["task"]
        target = args["target"]
        port = args.get("port")

        if port:
            result = matcher.generic_run(task, f"{target}:{port}")
        else:
            result = matcher.generic_run(task, target)

        if result["status"] == "no_match":
            suggestions = result.get("suggestions", [])
            out = f"No tool found for: {task}\n"
            if suggestions:
                out += "Try these tools:\n"
                seen = set()
                for s in suggestions:
                    name = s.get("name", "")
                    if name.lower() not in seen:
                        seen.add(name.lower())
                        out += f"  - {name}: {s.get('description', '')[:100]}\n"
            return out

        lines = [f"## Task: {task}"]
        for r in result.get("results", []):
            lines.append(f"\n### {r['tool']}")
            lines.append(f"```\n{r['command']}\n```")
            output = r.get("output", "")
            if output and output != "(no output)":
                output_preview = output[:500]
                lines.append(f"**Output:**\n```\n{output_preview}\n```")
            parsed = r.get("parsed", {})
            if parsed:
                lines.append(f"**Parsed:** {json.dumps(parsed, indent=2)[:300]}")

        return "\n".join(lines)

    def _brain_goal(self, args):
        if not self.brain or not self.brain.running:
            return "Brain is not running. Start it with /autoon <target> first."
        objective = args.get("objective", "").strip().lower()
        target = args.get("target", "").strip()
        port = args.get("port")
        priority = args.get("priority")
        goal = self.brain.add_goal(objective, target, port=port, priority=priority)
        return f"Goal added: {objective} @ {target}:{port or '?'} (pri={goal.priority}, id={goal.id})"

    def _brain_status(self, args):
        if not self.brain or not self.brain.running:
            return "Brain is not running."
        s = self.brain.status()
        lines = [
            "## Brain Status",
            f"- **Status**: Running",
            f"- **Uptime**: {s['uptime']:.0f}s",
            f"- **Goals**: {s['total_goals']} total ({s['completed']} done, {s['failed']} failed, {s['pending']} pending)",
            f"- **Current goal**: {s.get('current') or 'standby'}",
            f"- **Targets**: {', '.join(s.get('targets', [])) or 'none'}",
            f"- **Credentials found**: {s['creds']}",
            f"- **Blackboard findings**: {s['findings']}",
            f"- **Learner experiences**: {s['learner_experiences']}",
        ]
        if s.get("learner_summary"):
            lines.append("\n### Learner: Top Techniques")
            for r in s["learner_summary"][:5]:
                rate = f"{r['success_rate']*100:.0f}%" if r.get("success_rate") is not None else "N/A"
                lines.append(f"- {r['technique_key']}: {r['success_count']} wins / {r['fail_count']} fails ({rate})")
        return "\n".join(lines)

    def _evasion_polymorph(self, args):
        from modules.evasion.polymorph import PolymorphicEngine
        eng = PolymorphicEngine()
        code = args["code"]
        lang = args.get("lang", "python")
        rounds = args.get("encoding_rounds", 1)
        result = eng.full_mutate(code, lang, encoding_rounds=rounds)
        checksum = eng.checksum(result)
        return f"# Polymorphic mutation complete\n# Lang: {lang} | Encoding rounds: {rounds}\n# MD5: {checksum}\n\n{result}"

    def _evasion_bypass(self, args):
        from modules.evasion.edr import EDREvasion
        edr = EDREvasion()
        technique = args["technique"]
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
            return f"Unknown technique: {technique}. Available: {', '.join(mapping.keys())}"
        return f"# {technique.replace('_', ' ').title()}\n\n{mapping[technique]()}"

    def _evasion_lolbin(self, args):
        from modules.evasion.lolbins import LOLBinManager
        platform = args.get("platform", "windows")
        lm = LOLBinManager(platform)
        action = args["action"]
        if action == "list":
            bins = lm.get_all()
            lines = [f"## LOLBins ({platform})", f"Total: {len(bins)} binaries\n"]
            for b in bins:
                caps = ", ".join(b["capabilities"])
                lines.append(f"- **{b['name']}** ({b['path']}): {caps}")
            return "\n".join(lines)
        elif action == "find":
            cap = args.get("capability", "execute")
            bins = lm.find_by_capability(cap)
            lines = [f"## LOLBins with capability: {cap}", f"Found: {len(bins)}\n"]
            for b in bins:
                lines.append(f"- **{b['name']}** ({b['path']}): {b['description']}")
            return "\n".join(lines)
        elif action == "summary":
            return lm.summarize()
        elif action == "download":
            bin_name = args.get("bin_name", "certutil")
            url = args.get("url", "http://example.com/payload")
            output = args.get("payload_path")
            return lm.generate_download_cradle(bin_name, url, output)
        elif action == "execute":
            bin_name = args.get("bin_name", "powershell")
            payload_path = args.get("payload_path", "payload.ps1")
            return lm.generate_execution(bin_name, payload_path)
        elif action == "reverse_shell":
            bin_name = args.get("bin_name", "powershell")
            lhost = args.get("lhost", "127.0.0.1")
            lport = args.get("lport", 4444)
            return lm.generate_reverse_shell(bin_name, lhost, lport)
        return f"Unknown action: {action}"

    def _supplychain_recon(self, args):
        from modules.supplychain.recon import SupplyChainRecon
        sc = SupplyChainRecon()
        files = args.get("files", {})
        findings = sc.analyze_repo_structure(files)
        dep_list = args.get("dependency_list", [])
        if dep_list:
            candidates = sc.flag_confusion_candidates(dep_list)
            findings.extend({"type": "confusion_candidate", **c} for c in candidates)
        return sc.summarize(findings)

    def _supplychain_poison(self, args):
        from modules.supplychain.poison import DependencyPoison
        dp = DependencyPoison()
        action = args["action"]
        ecosystem = args.get("ecosystem", "npm")

        if action == "confusion_package":
            name = args.get("package_name", "internal-lib")
            ptype = args.get("payload_type", "reverse_shell")
            lhost = args.get("lhost", "127.0.0.1")
            lport = args.get("lport", 4444)
            return dp.generate_confusion_package(name, ecosystem, ptype, lhost, lport)

        elif action == "typo_squat":
            name = args.get("package_name", "lodash")
            return dp.typo_squat(name)

        elif action == "squat_list":
            count = args.get("count", 10)
            squats = dp.generate_squat_list(ecosystem, count)
            lines = [f"## Typo-squatting candidates ({ecosystem})", ""]
            for s in squats:
                lines.append(f"- {s['original']} → [bold]{s['squat']}[/bold] ({s['strategy']})")
            return "\n".join(lines)
        return f"Unknown action: {action}"

    def _supplychain_cicd(self, args):
        from modules.supplychain.cicd import CICDExploit
        ce = CICDExploit()
        action = args["action"]

        if action == "techniques":
            return "\n".join(f"- **{tid}**: {info['description']}" for tid, info in ce.get_techniques().items())

        elif action == "summary":
            return ce.summarize()

        elif action == "generate":
            technique = args.get("technique", "pr_target")
            target = args.get("target_repo", "owner/repo")
            return ce.generate_malicious_workflow(target, technique)

        elif action == "runner_registration":
            return ce.generate_runner_registration()

        elif action == "dep_confusion_pip":
            name = args.get("package_name", "internal-lib")
            return ce.generate_dependency_confusion_pip(name, "https://pypi.org/simple/")

        return f"Unknown action: {action}"

    def _social_engine(self, args):
        from modules.social.engine import SocialEngine, Campaign, TargetProfile, Persona
        se = SocialEngine()
        action = args.get("action", "vector_info")

        if action == "vector_info":
            return se.vector_info()

        elif action == "target_profile":
            tp = TargetProfile(
                name=args.get("target_name"),
                role=args.get("target_role"),
                organization=args.get("target_org"),
                email=args.get("target_email"),
            )
            return se.generate_target_summary(tp)

        elif action == "persona":
            p = Persona(
                name=args.get("persona_name"),
                role=args.get("persona_role"),
                organization=args.get("target_org", "Target Corp"),
            )
            p.generate_backstory(args.get("target_org"))
            return f"## Persona: {p.name}\n**Role:** {p.role}\n**Email:** {p.email}\n**Phone:** {p.phone}\n**Personality:** {p.personality}\n**Backstory:** {p.backstory}\n\n{p.signature_block()}"

        elif action in ("campaign", "plan"):
            c = se.create_campaign()
            objective = args.get("objective", "credential_harvest")
            target_data = {
                "name": args.get("target_name", "Unknown"),
                "role": args.get("target_role", "Employee"),
                "organization": args.get("target_org", "Target Corp"),
                "email": args.get("target_email", ""),
            }
            persona = Persona(
                name=args.get("persona_name"),
                role=args.get("persona_role"),
            )
            c.plan(objective, target_data, persona)
            return c.status_report()

        elif action == "chains":
            objective = args.get("objective", "credential_harvest")
            target = TargetProfile(name=args.get("target_name", "User"), organization=args.get("target_org", "Org"))
            persona = Persona(name=args.get("persona_name", "Attacker"))
            c = Campaign()
            c.plan(objective, target, persona)
            lines = [f"## Attack Chain: {objective}"]
            for i, (name, content) in enumerate(c.generate_attack_chain(target, persona)):
                lines.append(f"\n### Stage {i+1}: {name}")
                lines.append(f"```\n{content}\n```")
            return "\n".join(lines)

        elif action == "status":
            if not se.campaigns:
                return "No campaigns created yet."
            return se.campaigns[-1].status_report()

        return f"Unknown action: {action}"

    def _social_phish(self, args):
        from modules.social.phishing import PhishingKit
        pk = PhishingKit()
        style = args.get("style", "security_alert")
        target_name = args.get("target_name", "User")
        target_email = args.get("target_email", "user@example.com")
        org = args.get("org", "Company")
        lhost = args.get("lhost", "127.0.0.1")
        lport = args.get("lport", 4444)

        if style.startswith("sms_"):
            sms_type = style[4:]
            return pk.sms_template(sms_type)

        elif style.startswith("macro_"):
            macro_type = style[6:]
            return pk.macro_payload(macro_type, lhost, lport)

        elif style in ("office365", "gmail", "generic", "okta", "vpn"):
            return pk.landing_page_html(style, org)

        else:
            return pk.email_template(style, target_name, target_email, org)

    def _social_deepfake(self, args):
        from modules.social.deepfake import DeepfakeFramework
        df = DeepfakeFramework()
        action = args.get("action")

        if action == "status":
            return df.status()

        elif action == "script":
            tool = args.get("tool", "roop")
            tool_action = args.get("tool_action", "swap")
            source = args.get("source")
            target = args.get("target")
            output = args.get("output")
            return df.generate_script(tool, tool_action, source, target, output)

        elif action == "pipeline_voice":
            voice_sample = args.get("target_voice_sample", "voice_sample.wav")
            script_text = args.get("script_text", "Hello, this is your CEO speaking.")
            output = args.get("output", "deepfake_call.mp4")
            return df.pipeline_phishing_call(voice_sample, script_text, output)

        elif action == "pipeline_video":
            source = args.get("source", "source_face.jpg")
            target = args.get("target", "driving_video.mp4")
            audio = args.get("target_voice_sample")
            return df.pipeline_deepfake_video(source, target, audio)

        elif action == "persona_images":
            count = int(args.get("count", 5))
            return df.generate_persona_images(count)

        elif action == "report":
            return df.generate_report()

        return f"Unknown action: {action}"

    def _stego_encode(self, args):
        from modules.stego.stego import StegoEngine
        se = StegoEngine()
        technique = args.get("technique", "text_whitespace")
        payload = args.get("payload", "secret")
        cover = args.get("cover")
        cover_len = args.get("cover_length", 100)

        if technique == "text_whitespace":
            if not cover:
                cover = se.random_cover_text(cover_len)
            result, bits = se.encode_text_whitespace(payload, cover)
            if result is None:
                return f"Error: {bits}"
            return f"# Whitespace Stego\nBits encoded: {bits}\n\nCover:\n{cover}\n\nStego:\n{result}"

        elif technique == "text_homoglyph":
            if not cover:
                cover = se.random_cover_text(cover_len)
            result, bits = se.encode_text_homoglyph(payload, cover)
            if result is None:
                return f"Error: {bits}"
            return f"# Homoglyph Stego\nBits encoded: {bits}\n\nCover:\n{cover}\n\nStego:\n{result}"

        elif technique == "pixel_lsb":
            pixels, w, h = se.random_cover_image(32, 32)
            result, bits = se.encode_pixel_lsb(payload, pixels)
            return f"# Pixel LSB Stego\nBits encoded: {bits}\nImage size: {w}x{h}x3\nPayload bytes: {len(payload)}\nData: {list(result[:64])}..."

        elif technique == "http_header":
            result = se.encode_http_header(payload)
            return json.dumps(result, indent=2)

        elif technique == "dns_query":
            queries = se.encode_dns_query(payload)
            return f"# DNS Stego\nQueries ({len(queries)}):\n" + "\n".join(queries)

        elif technique == "image_metadata":
            result = se.encode_image_metadata(payload)
            return json.dumps(result, indent=2)

        elif technique == "tcp_timestamp":
            result, bits = se.encode_tcp_timestamp(payload)
            return f"# TCP Timestamp Stego\nBits encoded: {bits}\nTimestamps: {result[:20]}..."

        return f"Unknown technique: {technique}"

    def _stego_decode(self, args):
        from modules.stego.stego import StegoEngine
        se = StegoEngine()
        technique = args.get("technique")

        if technique == "text_whitespace":
            stego = args.get("stego_data", "")
            return se.decode_text_whitespace(stego)

        elif technique == "text_homoglyph":
            stego = args.get("stego_data", "")
            return se.decode_text_homoglyph(stego)

        elif technique == "pixel_lsb":
            data = args.get("stego_data", "")
            return se.decode_pixel_lsb(eval(data) if isinstance(data, str) and data.startswith("[") else data.encode())

        elif technique == "http_header":
            headers = args.get("headers", {})
            result = se.decode_http_header(headers)
            return result or "No hidden data found in headers"

        elif technique == "dns_query":
            queries = args.get("dns_queries", [])
            return se.decode_dns_query(queries)

        elif technique == "image_metadata":
            meta = args.get("stego_data", {})
            if isinstance(meta, str):
                try:
                    meta = json.loads(meta)
                except json.JSONDecodeError:
                    return "Invalid metadata JSON"
            result = se.decode_image_metadata(meta)
            return result or "No hidden data found in metadata"

        elif technique == "tcp_timestamp":
            data = args.get("stego_data", "")
            timestamps = eval(data) if isinstance(data, str) else data
            return se.decode_tcp_timestamp(timestamps)

        return f"Unknown technique: {technique}"

    def _c2_channel(self, args):
        from modules.stego.c2 import C2Channel
        action = args.get("action")
        channel = args.get("channel", "http")
        domain = args.get("c2_domain", "c2.example.com")
        interval = args.get("interval", 60)

        c2 = C2Channel(channel, domain, interval)

        if action == "info":
            info = c2.channel_info()
            return "\n".join(f"- **{k}**: {v}" for k, v in info.items())

        elif action == "config":
            return c2.generate_channel_config(channel)

        elif action == "beacon":
            beacon = c2.beacon()
            return json.dumps(beacon, indent=2)

        elif action == "implant":
            implant_type = args.get("implant_type", "powershell")
            return f"# C2 Implant ({implant_type})\n# Channel: {channel} @ {domain}\n# Interval: {interval}s\n\n{c2.generate_c2_payload(implant_type)}"

        elif action == "server":
            framework = args.get("server_framework", "flask")
            return f"# C2 Server ({framework})\n# Domain: {domain}\n\n{c2.generate_c2_server(framework)}"

        elif action == "encode":
            command = args.get("command", "whoami")
            return c2.encode_command(command)

        elif action == "decode":
            encoded = args.get("encoded", "")
            result = c2.decode_command(encoded)
            return json.dumps(result, indent=2) if result else "Failed to decode"

        return f"Unknown action: {action}"

    def _advanced_learn(self, args):
        from agent.learner import Learner
        if not hasattr(self, '_learner') or not self._learner:
            self._learner = Learner()
        l = self._learner
        action = args.get("action")

        if action == "init":
            l.init_advanced()
            return l.advanced_summary()

        if action == "q_select":
            available = ["nmap:port_scan", "nmap:service_scan", "nmap:vuln_scan",
                          "gobuster:dir_enum", "searchsploit:cve_search", "hydra:brute_force",
                          "smbclient:enum_shares", "sqlmap:sql_injection", "nikto:web_scan",
                          "enum4linux:enum_users", "msfconsole:exploit"]
            result = l.q_select(
                ports=args.get("ports"),
                services=args.get("services"),
                os_type=args.get("os_type"),
                findings=args.get("findings"),
                available=available,
            )
            return f"Q-Learning selected: {result}"

        elif action == "q_learn":
            if not l.q_selector:
                return "Advanced learner not initialized. Run 'init' first."
            l.advanced_record(
                target=args.get("target", "unknown"),
                port=args.get("port", 0),
                service=args.get("service", ""),
                tool=args.get("tool", "unknown"),
                technique=args.get("technique", "unknown"),
                success=args.get("success", False),
                duration=args.get("duration", 0),
                ports=args.get("ports"),
                services=args.get("services"),
                os_type=args.get("os_type"),
                findings=args.get("findings"),
            )
            return "Recorded and learned from experience."

        elif action == "skill_save":
            l.init_advanced()
            steps = args.get("steps", [])
            target_info = {}
            if args.get("ports"):
                target_info["ports"] = args["ports"]
            if args.get("os_type"):
                target_info["os"] = args["os_type"]
            sid = l.skill_save_chain(steps, target_info)
            return f"Skill saved: {sid}"

        elif action == "skill_find":
            l.init_advanced()
            results = l.skill_find(
                ports=args.get("ports"),
                os_type=args.get("os_type"),
            )
            if not results:
                return "No matching skills found."
            lines = [f"## Matching Skills ({len(results)})"]
            for s in results:
                rate = f"{s.get('success_rate', 0)*100:.0f}%" if s.get("success_rate") else "N/A"
                lines.append(f"- **{s['name']}** ({s['id']}) match={s['match_score']} success={rate} steps={len(s['steps'])}")
            return "\n".join(lines)

        elif action == "skill_exec":
            l.init_advanced()
            l.set_tool_runner(self)
            result = l.skill_execute(args.get("skill_id", ""), args.get("target", ""))
            return json.dumps(result, indent=2)

        elif action == "skill_summary":
            return l.skill_summary() if l.skill_library else "Advanced learner not initialized."

        elif action == "hypothesis":
            l.init_advanced()
            hyps = l.hypothesis_generate(args.get("ports", []), args.get("os_type"))
            lines = [f"## Hypotheses ({len(hyps)})"]
            for h in hyps[:10]:
                lines.append(f"- [port {h['port']}] {h['hypothesis']} (conf={h.get('confidence',0):.2f})")
            return "\n".join(lines)

        elif action == "attack_plan":
            l.init_advanced()
            plan = l.hypothesis_attack_plan(args.get("ports", []), args.get("os_type"))
            if not plan:
                return "No attack plan generated."
            lines = [f"## Attack Plan ({len(plan)} steps)"]
            for p in plan:
                cmd = p.get("command") or p.get("action", "")
                lines.append(f"- [port {p['port']}] {p.get('vulnerability', p.get('service_guess', '?'))} → {cmd}")
            return "\n".join(lines)

        elif action == "hypothesis_summary":
            return l.hypothesis_summary() if l.hypothesis_gen else "Hypothesis engine not initialized."

        elif action == "bayesian_top":
            l.init_advanced()
            top = l.bayesian_top(10)
            if not top:
                return "No Bayesian data yet."
            lines = ["## Top Bayesian Probabilities"]
            for t in top:
                lines.append(f"- {t['key']}: {t['probability']:.2f}")
            return "\n".join(lines)

        elif action == "summary":
            return l.advanced_summary() if l.q_selector else "Advanced learner not initialized."

        return f"Unknown action: {action}"

    def _search_tools(self, args):
        try:
            from modules.tool_db import search_tools
            results = search_tools(args["query"])
            if not results:
                return f"No tools found matching '{args['query']}'."
            lines = [f"## Tools matching: {args['query']}"]
            seen = set()
            for category, tool in results:
                if tool['name'] in seen:
                    continue
                seen.add(tool['name'])
                lines.append(f"- **{tool['name']}** ({category.replace('blackarch-', '')}) - {tool['description'][:150]}")
            return "\n".join(lines[:25])
        except ImportError:
            return "Tool database not loaded."
