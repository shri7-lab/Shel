# Shel — Autonomous AI Pentesting Agent

**Shel** is a multi-agent autonomous pentesting AI that combines LLM-driven reasoning with a modular arsenal of specialized attack modules. It operates as an interactive REPL with a full dashboard, supporting autonomous goal-driven decision loops, multi-agent swarm coordination, polymorphic evasion, supply chain poisoning, social engineering campaigns, steganography, covert C2 channels, and continuous Q-learning—all from the command line.

```
╔══════════════════════════════════════╗
║  ███████ ██  ██ ███████ ██          ║
║  ██      ██  ██ ██      ██          ║
║  ███████ ███████ █████   ██          ║
║       ██ ██  ██ ██      ██          ║
║  ███████ ██  ██ ███████ ███████     ║
╚══════════════════════════════════════╝
 Autonomous Pentesting AI Agent  |  v1.0
```

---

## Table of Contents

- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Commands Reference](#commands-reference)
- [Capabilities](#capabilities)
  - [Autonomous Brain](#1-autonomous-brain)
  - [Multi-Agent Swarm](#2-multi-agent-swarm)
  - [Polymorphic Evasion](#3-polymorphic-evasion)
  - [Supply Chain Attacks](#4-supply-chain-attacks)
  - [Social Engineering](#5-social-engineering)
  - [Steganography & Covert C2](#6-steganography--covert-c2)
  - [Advanced Continuous Learning](#7-advanced-continuous-learning)
  - [OSINT](#8-osint)
  - [Payload Generation](#9-payload-generation)
- [LLM Tools Reference](#llm-tools-reference)
- [Attack Coverage](#attack-coverage-by-service)
- [Configuration](#configuration)
- [Module Reference](#module-reference)

---

## Architecture

```
main.py ────────────────── CLI REPL, dashboard, all /commands
  │
  ├── agent/ ───────────── Core intelligence
  │   ├── brain.py         Autonomous decision loop
  │   ├── learner.py       SQLite experience learner + advanced bridge
  │   ├── swarm.py         Multi-agent orchestrator
  │   ├── sub_agents.py    System prompts for 7 agent types
  │   ├── sub_agent_runner.py  Agent execution engine
  │   ├── autopilot.py     7-phase pipeline
  │   ├── tool_matcher.py  Task-to-tool mapping engine
  │   ├── tools.py         25 LLM tool definitions + ToolRunner
  │   ├── llm.py           Claude API / Ollama abstraction
  │   ├── rag.py           RAG knowledge base
  │   ├── state.py         Session state tracking
  │   ├── system.py        System prompt builder
  │   ├── docker.py        Kali Docker sandbox
  │   ├── checkpoints.py   Command approval gate
  │   └── output_parser.py Tool output parsers
  │
  ├── modules/ ─────────── Tactical capability modules
  │   ├── tool_db.py       2,856 BlackArch tools
  │   ├── osint.py         OSINT engine
  │   ├── low_hanging.py   Quick-win checks
  │   ├── evasion/         Polymorph, EDR bypass, LOLBins
  │   ├── supplychain/     Recon, poison, CI/CD
  │   ├── social/          Campaigns, phishing, deepfakes
  │   ├── stego/           Steganography, C2 channels
  │   ├── learner/         Q-learning, skills, hypotheses
  │   └── payloads/        Shells, webshells, encoders
  │
  ├── config/settings.py
  ├── knowledge/           7 methodology guides
  └── benchmark/           Challenge harness
```

---

## Quick Start

```bash
# Install
git clone https://github.com/yourusername/shel.git
cd shel
pip install -r requirements.txt

# Run with Claude (recommended)
python main.py

# Or use local models
# First set /use-local in the REPL, or:
# python main.py --local
```

On first launch you'll be prompted for your Anthropic API key. It's saved to `~/.shel/config.json`.

### Try it immediately

```
╭─[Shel]
╰─> /set-target 10.10.11.42

╭─[Shel]
╰─> /autoon 10.10.11.42

╭─[Shel]
╰─> /swarm chain
```

---

## Commands Reference

### Session

| Command | Description |
|---------|-------------|
| `/help` | Show help panel with all commands |
| `/clear` | Clear console, redisplay banner + dashboard |
| `/config` | Show current configuration |
| `/state` | Display session state |
| `/findings` | Show all findings in a table |
| `/log` | Print command execution log |
| `/reset` | Reset session state |
| `/banner` | Show splash banner |
| `/exit` | Exit Shel |

### Target

| Command | Description |
|---------|-------------|
| `/set-target <ip>` | Set primary target |
| `/add-target <ip>` | Add secondary target |

### AI / LLM

| Command | Description |
|---------|-------------|
| `/set-key` | Set Anthropic API key |
| `/set-model` | Set model name |
| `/use-local` | Switch to Ollama local inference |
| `/use-claude` | Switch to Claude API |
| `/shell-on` | Enable shell execution |
| `/shell-off` | Disable shell execution |

### OSINT

| Command | Description |
|---------|-------------|
| `/osint <domain>` | Full domain recon (DNS, WHOIS, subdomains, certs, dorks) |
| `/osint ip <ip>` | IP geolocation, ASN, reverse DNS |
| `/osint email <email>` | Email format and domain analysis |
| `/osint user <user>` | Username search across platforms |
| `/osint dork <domain>` | Google dorking (files, admin panels, exposed data) |
| `/osint archive <domain>` | Wayback Machine snapshot retrieval |
| `/osint tools <target>` | Tool recommendations per target |

### Autonomous Brain

| Command | Description |
|---------|-------------|
| `/autoon <target>` | Start brain (standard scan) |
| `/autoon --fast <target>` | Start brain (top 1000 ports) |
| `/autoon --deep <target>` | Start brain (full 65535 port range) |
| `/autooff` | Stop brain |
| `/status` | Brain/pipeline status dashboard |
| `/brain` | Brain dashboard with goal queue, learner stats, blackboard |

### Swarm

| Command | Description |
|---------|-------------|
| `/swarm launch <type> <task>` | Deploy sub-agent (recon/exploit/privesc/lateral/exfil/distraction/report) |
| `/swarm chain` | Deploy full chain on current target |
| `/swarm status` | Swarm status and findings |

### Social Engineering

| Command | Description |
|---------|-------------|
| `/social campaign <objective>` | Plan a campaign (credential_harvest/malware_delivery/ceo_fraud/spear_phish/vishing/supply_chain) |
| `/social chains <objective>` | Show 3-stage attack chain |
| `/social persona` | Generate attacker persona with backstory |
| `/social target <name>` | Build target profile |
| `/social vectors` | List 12 attack vectors |
| `/social phish <style> [name] [org]` | Generate email/SMS/landing page/macro |
| `/social deepfake status` | Show installed deepfake tools |
| `/social deepfake script <tool> <action>` | Generate tool script |
| `/social deepfake pipeline` | Full voice/video deepfake pipeline |

### Steganography

| Command | Description |
|---------|-------------|
| `/stego encode <technique> <payload>` | Hide data (whitespace/homoglyph/HTTP-header/DNS/metadata) |
| `/stego decode <technique> <data>` | Extract hidden data |
| `/stego techniques` | List all techniques |

### C2

| Command | Description |
|---------|-------------|
| `/c2 implant [channel] [type]` | Generate implant (powershell/bash/python) for 8 channels |
| `/c2 beacon [channel]` | Generate beacon request |
| `/c2 server` | Generate Flask C2 server |
| `/c2 config [channel]` | Generate channel configuration |
| `/c2 info` | C2 channel descriptions |
| `/c2 encode <cmd>` | Encode command for C2 |
| `/c2 decode <data>` | Decode C2 response |

### Supply Chain

| Command | Description |
|---------|-------------|
| `/supplychain recon <files>` | Scan for dependency risks, secrets, CI misconfigs |
| `/supplychain poison confusion <pkg>` | Generate dependency confusion package |
| `/supplychain poison squat <pkg>` | Generate typo-squat name |
| `/supplychain poison squat-list [count]` | Generate squat candidates |
| `/supplychain cicd techniques` | List CI/CD attack techniques |
| `/supplychain cicd generate <technique>` | Generate malicious workflow YAML |
| `/supplychain cicd runner` | Runner registration payload |

### Evasion

| Command | Description |
|---------|-------------|
| `/evasion polymorph <lang> <code>` | Mutate script (python/powershell/bash/perl) |
| `/evasion bypass <type>` | Generate bypass (amsi/etw/sandbox/injection) |
| `/evasion lolbin <action>` | LOLBin commands (list/find/revshell/download) |
| `/lolbins <action>` | LOLBin manager |

### Learning

| Command | Description |
|---------|-------------|
| `/learn init` | Initialize advanced learner |
| `/learn summary` | Show learner status |
| `/learn q_select [ports]` | Q-learning strategy selection |
| `/learn hypothesis [ports]` | Generate vulnerability hypotheses |
| `/learn plan [ports]` | Generate attack plan |
| `/learn bayesian` | Show Bayesian beliefs |
| `/learn skill_find [ports]` | Find matching skills |
| `/learn skill_summary` | Show skill library |

### Universal

| Command | Description |
|---------|-------------|
| `/run <task> on <target>[:port]` | Universal executor |
| `/recon <task>` | Recon sub-agent |
| `/exploit <task>` | Exploit sub-agent |
| `/report` | Generate pentest report |
| `/docker-setup` | Build Kali Docker image |
| `/docker <cmd>` | Run command in Docker |
| `/benchmark` | Show benchmark results |

---

## Capabilities

### 1. Autonomous Brain

The brain (`agent/brain.py`) is a goal-driven decision engine that plans, executes, and learns autonomously:

- **Priority Goal Queue** — goals with dynamic priority scoring based on port, service, and attack phase
- **Shared Blackboard** — targets, credentials, flags, and findings shared across all agents
- **Plan/Execute/Learn Loop** — picks highest-priority goal, selects the best tool (via learner), executes, records the outcome, adjusts Q-values
- **Auto-spawn** — findings automatically produce new goals (e.g., finding port 445 spawns "enum smb" and "vuln scan smb")
- **Learner Integration** — skips tools that fail 3x consecutively, ranks techniques by success rate per port/OS

```
Goal Queue:
  [1] port scan @ 10.10.11.42 (pri=10) — COMPLETED
  [2] enum smb @ 10.10.11.42:445 (pri=7) — IN PROGRESS
  [3] vuln scan @ 10.10.11.42:445 (pri=6) — PENDING
  [4] get foothold @ 10.10.11.42 (pri=9) — PENDING
```

### 2. Multi-Agent Swarm

The swarm coordinator (`agent/swarm.py` and `agent/sub_agent_runner.py`) deploys specialized agents in parallel:

| Agent Type | Role |
|------------|------|
| **recon** | Port scanning, service enumeration, OSINT |
| **exploit** | Vulnerability exploitation, credential attacks |
| **privesc** | Privilege escalation (kernel exploits, SUID, misconfigs) |
| **lateral** | Network pivoting, credential stuffing, share enumeration |
| **exfil** | Data extraction, flag hunting, sensitive file discovery |
| **distraction** | Noise generation, decoy attacks, IDS evasion |
| **report** | Engagement report generation from findings |

Features:
- **Parallel deployment** via `ThreadPoolExecutor`
- **Dependency-ordered chains** via `deploy_chain()` — recon → exploit → privesc → exfil → report
- **Shared blackboard** — agents write findings, credentials, and flags to a common store
- **Auto-extraction** — LLM responses are parsed for CVEs, credentials, and flags

### 3. Polymorphic Evasion

The evasion module (`modules/evasion/polymorph.py`) mutates scripts to evade signature-based detection:

- **Variable renaming** with word-boundary-aware regex (preserves module/import names)
- **Junk code injection** — random assignments, no-ops, dead branches
- **Multi-layer encoding** — base64, XOR (single-byte key), hex, reverse, split/shuffle
- **Per-language mutators** — Python, PowerShell, Bash, Perl
- **Stager generation** — download cradles, base64 stagers, `iex` invocations
- **Checksum tracking** — MD5 of each mutation to verify uniqueness

EDR bypass (`modules/evasion/edr.py`):

| Technique | Methods |
|-----------|---------|
| AMSI Bypass | Memory patch, registry, reflection |
| ETW Bypass | Provider nullification |
| Sandbox Detection | Debugger check, VM artifacts, sleep acceleration |
| Process Injection | CreateRemoteThread, APC, process hollowing |

LOLBin manager (`modules/evasion/lolbins.py`):

- **25 Windows** binaries: powershell, cscript, mshta, certutil, bitsadmin, regsvr32, rundll32, msiexec, wmic, msbuild, installutil, csc, and more
- **13 Linux** binaries: python, perl, bash, netcat, curl, wget, openssl, socat, nmap, gdb, awk, find, git
- Template-based download cradles, execution commands, and reverse shells

### 4. Supply Chain Attacks

The supply chain module (`modules/supplychain/`) targets the software supply chain:

**Recon** — Scans repositories for:
- Dependency analysis (npm/pip/cargo) — loose version pinning, wildcard deps, dangerous install scripts
- Secret leak detection — 14 patterns (AWS keys, GitHub tokens, SSH keys, JWTs, Slack tokens, PyPI tokens, etc.)
- CI/CD misconfigs — 9 patterns (pull_request_target, self-hosted runners, unpinned actions, GITHUB_TOKEN write-all, env injection, script injection, reusable workflows)

**Poison** — Generates:
- Typo-squatting — 5 strategies (swap, insert, omit, repeat, homoglyph)
- Dependency confusion packages — for npm/pip/cargo with payloads (reverse_shell, env_leak, cred_harvest, crypto_miner, backdoor)

**CI/CD** — Generates malicious workflow YAML for:
- PR_TARGET abuse with secret access
- Self-hosted runner compromise
- Dependency confusion in CI pipelines
- GITHUB_TOKEN theft via DNS exfiltration
- Environment approval bypass

### 5. Social Engineering

The social engineering module (`modules/social/`) orchestrates human-layer attacks:

**Campaign Engine** (`modules/social/engine.py`):
- Target profiling with OSINT enrichment
- Persona generator (name, role, backstory, signature block)
- 6 campaign types: credential_harvest, malware_delivery, ceo_fraud, spear_phish, vishing, supply_chain
- Multi-stage attack chains with status tracking
- Full campaign report generation

**Phishing Kit** (`modules/social/phishing.py`):
- 15 email templates: security_alert, password_reset, invoice, doc_share, docusign, fedex, voicemail, calendar_invite, compliance, benefits, it_notice, hr_update, linkedin, teams_notification, zoom_invite
- 7 SMS templates: urgent, delivery, banking, verification, missed_call, covid, payroll
- 5 landing page clones: Office 365, Gmail, Okta, VPN, generic login
- Macro payloads: reverse_shell, keylogger, cred_harvest
- SMTP configuration builder

**Deepfake Framework** (`modules/social/deepfake.py`):
- Orchestrates 9 external deepfake tools: FaceSwap, Wav2Lip, DeepFaceLab, So-VITS-SVC, Tortoise TTS, StyleGAN3, First Order Motion, Roop, Voice-Cloner
- Install detection and status reporting
- Ready-to-run script generation for each tool
- Full voice phishing pipeline (clone → generate → sync)
- Full deepfake video pipeline (animate → lipsync)
- Persona image generation via StyleGAN3

### 6. Steganography & Covert C2

**Steganography** (`modules/stego/stego.py`) — 8 techniques for hiding data:

| Technique | Method | Capacity |
|-----------|--------|----------|
| Text whitespace | Space=0, Tab=1 with magic header + terminator | Arbitrary (one bit per space) |
| Text homoglyph | Latin → Cyrillic Unicode lookalikes | One bit per substitutable char |
| Pixel LSB | LSB embedding in RGB pixel data | 3 bits per pixel |
| Audio LSB | LSB embedding in WAV samples | 1 bit per sample |
| HTTP header | Base64 payload in X-Stego header | Header size limited |
| DNS query | Base32 across subdomain queries | 20 chars per query |
| Image metadata | EXIF Artist/Comment fields | 200-255 chars |
| TCP timestamp | LSB in TCP TS values | 1 bit per timestamp |

**Covert C2** (`modules/stego/c2.py`) — 8 channel types:

| Channel | Method | Latency | Stealth |
|---------|--------|---------|---------|
| DNS | Subdomain queries + TXT responses | Slow | High |
| HTTP | API-style beaconing with UA rotation | Medium | High |
| HTTPS | TLS-encrypted HTTP beaconing | Medium | Very High |
| Social | Posts/comments on Twitter/Reddit/GitHub | High | Very High |
| Blockchain | Transaction memos on ETH/BTC/SOL | Very High | Maximum |
| ICMP | Echo request/reply payloads | Medium | Medium |
| WebSocket | Persistent bidirectional channel | Low | Medium |
| Tor | Onion-routed C2 | High | Maximum |

Implant generation: PowerShell (while loop), Bash (curl-based), Python (threaded with requests).
Server generation: Flask-based C2 with beacon/result endpoints and admin command queue.

### 7. Advanced Continuous Learning

The learning module (`modules/learner/`) upgrades the basic SQLite learner to a full reinforcement learning system:

**Q-Learning Selector** (`modules/learner/strategy.py`):
- ε-greedy action selection with configurable exploration rate
- State encoding: 15 binary features (ports present, services, OS, findings)
- Reward calculation: typed rewards (foothold=100, shell=150, privesc=120, etc.) with duration penalty and attempt bonus
- Adaptive epsilon decay (configurable decay rate and minimum)
- Full Q-table export and history tracking

**Skill Library** (`modules/learner/skills.py`):
- Store successful multi-step attack chains as reusable skills
- Find matching skills by port, OS, or tags with match scoring
- Skill generalization to new port/OS combinations
- 5 chain templates: enum, exploit, privesc, lateral, full
- Success rate tracking per skill

**Hypothesis Engine** (`modules/learner/hypothesis.py`):
- Service guessing: 44 ports with possible service fingerprints
- Vulnerability prediction: 80+ known vulns mapped to ports and exploit commands
- Bayesian updater: posterior probability tracking per port:technique pair
- Attack plan compiler: prioritizes high-confidence hypotheses into actionable steps

### 8. OSINT

The OSINT module (`modules/osint.py`) provides full-spectrum reconnaissance:

- **Domain recon**: DNS records (A/AAAA/MX/NS/TXT/SOA), WHOIS lookup, certificate transparency (crt.sh), subdomain discovery via common wordlist, Google dorking (6 categories), Wayback Machine archive
- **IP recon**: geolocation, ASN, hostname, reverse DNS
- **Email recon**: format analysis, domain validation
- **Username recon**: 9 platforms (GitHub, Twitter/X, Reddit, HackerNews, etc.)
- **Tool recommendations**: per-target-type BlackArch tool suggestions

### 9. Payload Generation

The payload generator (`modules/payloads/generator.py`) generates:

- **Reverse shells**: bash, python, php, nc, powershell
- **Webshells**: php simple, php隐蔽, asp, jsp
- **SQL injection**: time-based, error-based, union-based templates
- **XSS**: reflected, stored, DOM-based templates
- **Encoders**: base64, URL, hex, XOR
- **msfvenom wrapper**: generate staged/stageless Meterpreter payloads

---

## LLM Tools Reference

When chatting with Shel in natural language, the AI has access to these 25 tools:

| Tool | What it does |
|------|-------------|
| `bash` | Execute shell commands |
| `read_file` | Read file contents |
| `write_file` | Write/save files |
| `search_web` | DuckDuckGo web search |
| `fetch_url` | Fetch and parse web content |
| `generate_payload` | Generate shells, webshells, SQLi, XSS, encoders |
| `query_knowledge` | Search the built-in pentesting KB |
| `store_writeup` | Save a writeup into the KB |
| `docker_run` | Execute in Kali Docker container |
| `sub_agent` | Deploy recon/exploit/report sub-agents |
| `get_session_summary` | Current session state |
| `suggest_tools` | BlackArch tool recommendations |
| `search_tools` | BlackArch tool database search |
| `execute_task` | Universal task executor |
| `brain_goal` | Add goal to Brain queue |
| `brain_status` | Brain current status |
| `evasion_polymorph` | Polymorphic code mutation |
| `evasion_bypass` | AMSI/ETW bypass generation |
| `evasion_lolbin` | LOLBin download/execution |
| `supplychain_recon` | Supply chain risk scan |
| `supplychain_poison` | Dependency confusion packages |
| `supplychain_cicd` | CI/CD exploit workflows |
| `social_engine` | Campaign management |
| `social_phish` | Phishing templates |
| `social_deepfake` | Deepfake scripts/pipelines |
| `stego_encode` | Hide data via steganography |
| `stego_decode` | Extract hidden data |
| `c2_channel` | C2 beacon/implant/server |
| `advanced_learn` | Q-learning/skills/hypotheses |

---

## Attack Coverage by Service

| Port | Service | Techniques |
|------|---------|------------|
| 21 | FTP | anonymous auth, vsftpd backdoor, proftpd mod_copy |
| 22 | SSH | weak creds, libssh auth bypass, user enum |
| 23 | Telnet | default creds |
| 25 | SMTP | open relay, exim RCE, user enum |
| 53 | DNS | zone transfer, cache poison, tunnel |
| 80/443 | HTTP/S | dir enum, LFI/RFI, SQLi, XSS, shellshock, heartbleed, WordPress/Joomla/Drupal, phpMyAdmin, default creds |
| 110 | POP3 | weak auth |
| 135 | RPC | ms08_067 |
| 139/445 | SMB | null session, eternalblue, SMB signing, relay, enum shares/users |
| 143 | IMAP | weak auth |
| 389 | LDAP | anonymous bind, simple auth |
| 1433 | MSSQL | sa default pass, SQL injection |
| 1521 | Oracle | default passwords, TNS poison |
| 2049 | NFS | no_root_squash, world-readable shares |
| 2375 | Docker | unauthenticated API, container escape |
| 3306 | MySQL | root no pass, default creds, SQLi |
| 3389 | RDP | BlueKeep, MITM, weak creds |
| 5432 | PostgreSQL | default creds, pg_hba misconfig |
| 5900 | VNC | no-auth, weak pass |
| 5985/5986 | WinRM | creds, PS session |
| 6379 | Redis | no-auth, cron RCE |
| 8080/8443 | Tomcat/Jenkins | manager UI, script console, default creds |
| 9200 | Elasticsearch | RCE |
| 11211 | Memcached | no-auth |
| 27017 | MongoDB | no-auth, default creds |

---

## Configuration

Config is stored at `~/.shel/config.json`:

```json
{
    "api_key": "sk-ant-...",
    "provider": "claude",
    "model": "claude-sonnet-4-20250514",
    "ollama_model": "llama3.1",
    "ollama_url": "http://localhost:11434"
}
```

The learner database is at `~/.shel/learner.db` (SQLite).

---

## Module Reference

| Path | Lines | Purpose |
|------|-------|---------|
| `agent/brain.py` | 530 | Autonomous goal-driven reasoning loop |
| `agent/learner.py` | 323 | SQLite experience store + advanced bridge |
| `agent/swarm.py` | 292 | Multi-agent swarm orchestrator |
| `agent/sub_agents.py` | 131 | System prompts for 7 agent types |
| `agent/sub_agent_runner.py` | 261 | Agent execution engine |
| `agent/autopilot.py` | 424 | 7-phase linear pipeline |
| `agent/tool_matcher.py` | 680 | Task-to-tool mapping engine |
| `agent/tools.py` | 1,240 | 25 tool definitions + ToolRunner |
| `agent/llm.py` | 151 | Claude API / Ollama abstraction |
| `agent/rag.py` | 146 | RAG knowledge base |
| `agent/state.py` | 123 | Session state tracking |
| `agent/output_parser.py` | 230 | Tool output parsers |
| `agent/docker.py` | 76 | Docker sandbox |
| `agent/checkpoints.py` | 75 | Command approval gate |
| `modules/tool_db.py` | 14,627 | 2,856 BlackArch tools |
| `modules/osint.py` | 395 | OSINT engine |
| `modules/low_hanging.py` | 188 | Quick-win checks |
| `modules/evasion/polymorph.py` | 216 | Polymorphic engine |
| `modules/evasion/edr.py` | 111 | EDR bypass techniques |
| `modules/evasion/lolbins.py` | 282 | LOLBin manager |
| `modules/supplychain/recon.py` | 341 | Supply chain scanner |
| `modules/supplychain/poison.py` | 249 | Dependency poison |
| `modules/supplychain/cicd.py` | 306 | CI/CD exploitation |
| `modules/social/engine.py` | 367 | Campaign engine |
| `modules/social/phishing.py` | 426 | Phishing kit |
| `modules/social/deepfake.py` | 327 | Deepfake framework |
| `modules/stego/stego.py` | 251 | Steganography engine |
| `modules/stego/c2.py` | 282 | Covert C2 channels |
| `modules/learner/strategy.py` | 183 | Q-learning strategy |
| `modules/learner/skills.py` | 197 | Skill library |
| `modules/learner/hypothesis.py` | 212 | Hypothesis engine |
| `modules/payloads/generator.py` | 164 | Payload generator |
| `benchmark/runner.py` | 95 | Challenge benchmark |
| **Total** | **~25,000** | **50 Python files** |

---

## Requirements

```
anthropic>=0.30.0
rich>=13.0.0
pyyaml>=6.0
requests>=2.31.0
beautifulsoup4>=4.12.0
markdownify>=0.11.0
prompt-toolkit>=3.0.0
```

Optional: Docker Desktop (for sandboxed tool execution).

---

## License

MIT
