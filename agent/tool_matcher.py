import re
import subprocess
import shlex
import json
from typing import Optional
from modules.tool_db import suggest_tools as db_suggest_tools
import agent.output_parser as output_parser

TOOL_COMMANDS = {
    "nmap": {
        "template": "nmap {flags} {target}",
        "profiles": {
            "quick": "-sC -sV -T4 --top-ports 1000",
            "full": "-sC -sV -T4 -p-",
            "vuln": "-sC -sV --script vuln -T4",
            "udp": "-sU --top-ports 100",
            "os": "-O -T4 --top-ports 500",
        },
        "default_profile": "quick",
        "parsers": ["nmap"],
    },
    "gobuster": {
        "template": "gobuster dir -u http://{target} -w {wordlist} {flags}",
        "profiles": {
            "dir": "-x php,txt,html,asp,aspx,jsp,do,action -t 50",
            "dns": "dns -d {target} -w {wordlist} -t 50",
            "vhost": "vhost -u http://{target} -w {wordlist} -t 50",
        },
        "default_profile": "dir",
        "defaults": {"wordlist": "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"},
        "parsers": ["gobuster"],
    },
    "ffuf": {
        "template": "ffuf -u http://{target}/FUZZ -w {wordlist} {flags}",
        "profiles": {
            "dir": "-c -t 50",
            "vhost": "-H \"Host: FUZZ.{target}\" -c -t 50",
            "params": "-c -t 50 -mode pitchfork",
        },
        "default_profile": "dir",
        "defaults": {"wordlist": "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"},
        "parsers": ["gobuster"],
    },
    "curl": {
        "template": "curl -s -L {target} {flags}",
        "profiles": {
            "head": "-I",
            "get": "",
            "post": "-X POST -d '{data}'",
            "cookies": "-b '{cookies}'",
        },
        "default_profile": "get",
        "parsers": ["curl"],
    },
    "whatweb": {
        "template": "whatweb -a 3 {target} {flags}",
        "profiles": {"default": "--color=never"},
        "default_profile": "default",
        "parsers": ["whatweb"],
    },
    "nikto": {
        "template": "nikto -h {target} {flags}",
        "profiles": {"default": "-Tuning 123456789 -ssl -timeout 10"},
        "default_profile": "default",
        "parsers": ["nikto"],
    },
    "smbclient": {
        "template": "smbclient -N -L //{target}/ 2>/dev/null {flags}",
        "profiles": {"default": "", "share": "-N '//{target}/{share}' -c ls 2>/dev/null"},
        "default_profile": "default",
        "parsers": ["smbclient"],
    },
    "smbmap": {
        "template": "smbmap -H {target} {flags}",
        "profiles": {"default": "", "recursive": "-R -q"},
        "default_profile": "default",
        "parsers": ["smbclient"],
    },
    "enum4linux": {
        "template": "enum4linux -a {target} 2>/dev/null {flags}",
        "profiles": {"default": "", "users": "-U", "shares": "-S"},
        "default_profile": "default",
        "parsers": ["enum4linux"],
    },
    "hydra": {
        "template": "hydra {flags} {target} {service}",
        "profiles": {
            "ssh": "-l {user} -P {wordlist} ssh",
            "ftp": "-l {user} -P {wordlist} ftp",
            "http-post": "-l {user} -P {wordlist} http-post-form \"{path}:{params}:{fail}\"",
            "smb": "-l {user} -P {wordlist} smb",
            "mysql": "-l {user} -P {wordlist} mysql",
            "rdp": "-l {user} -P {wordlist} rdp",
        },
        "defaults": {"user": "admin", "wordlist": "/usr/share/wordlists/rockyou.txt"},
        "default_profile": "ssh",
        "parsers": ["hydra"],
    },
    "sqlmap": {
        "template": "sqlmap -u {target} {flags}",
        "profiles": {
            "default": "--batch --random-agent --level 3 --risk 2",
            "dump": "--batch --random-agent --dump",
            "os-shell": "--batch --random-agent --os-shell",
        },
        "default_profile": "default",
        "parsers": ["sqlmap"],
    },
    "wpscan": {
        "template": "wpscan --url {target} {flags}",
        "profiles": {
            "default": "--random-user-agent --api-token ''",
            "enumerate": "--enumerate u,vp,vt,tt,cb,dbe",
            "passwords": "--passwords {wordlist} --usernames {user}",
        },
        "default_profile": "enumerate",
        "defaults": {"wordlist": "/usr/share/wordlists/rockyou.txt", "user": "admin"},
        "parsers": ["wpscan"],
    },
    "searchsploit": {
        "template": "searchsploit {query} {flags}",
        "profiles": {"default": "", "online": "-s"},
        "default_profile": "default",
    },
    "nuclei": {
        "template": "nuclei -u {target} {flags}",
        "profiles": {
            "default": "-severity low,medium,high,critical -t ~/nuclei-templates/",
            "tech": "-tags tech -json",
            "cves": "-severity high,critical",
        },
        "default_profile": "default",
        "parsers": ["nuclei"],
    },
    "dig": {
        "template": "dig {target} {flags} @{dns_server}",
        "profiles": {
            "any": "any +short",
            "axfr": "axfr",
            "mx": "mx +short",
            "ns": "ns +short",
        },
        "defaults": {"dns_server": "1.1.1.1"},
        "default_profile": "any",
    },
    "dnsrecon": {
        "template": "dnsrecon -d {target} {flags}",
        "profiles": {
            "default": "-t std",
            "bruteforce": "-t brt -D {wordlist}",
            "axfr": "-t axfr",
        },
        "defaults": {"wordlist": "/usr/share/wordlists/dns/subdomains-top1million-5000.txt"},
        "default_profile": "default",
        "parsers": ["dnsrecon"],
    },
    "ftp": {
        "template": "echo -e 'anonymous@\\n' | ftp -nv {target} 2>&1 {flags}",
        "profiles": {"default": "", "get": "-get {file}"},
        "default_profile": "default",
    },
    "redis-cli": {
        "template": "redis-cli -h {target} {flags}",
        "profiles": {
            "info": "INFO",
            "keys": "KEYS *",
            "dump": "--csv -c 'DUMP {key}'",
        },
        "default_profile": "info",
    },
    "mongosh": {
        "template": "mongosh --host {target} {flags}",
        "profiles": {
            "default": "--eval 'db.adminCommand(\"listDatabases\")' 2>/dev/null",
        },
        "default_profile": "default",
    },
    "showmount": {
        "template": "showmount -e {target} {flags}",
        "profiles": {"default": ""},
        "default_profile": "default",
    },
    "ldapsearch": {
        "template": "ldapsearch -H ldap://{target} -x -b \"{base}\" {flags}",
        "profiles": {
            "default": "-s base namingcontexts",
            "extract": "-x -h {target} -b \"{base}\"",
        },
        "defaults": {"base": ""},
        "default_profile": "default",
    },
    "msfconsole": {
        "template": "msfconsole -q -x 'use {module}; set RHOSTS {target}; {options}; run; exit' {flags}",
        "profiles": {
            "default": "",
        },
        "default_profile": "default",
    },
    "netcat": {
        "template": "nc -nzv {target} {port} {flags}",
        "profiles": {
            "default": "-w 3",
            "listen": "-lvnp {port}",
            "banner": "-nzv -w 3",
        },
        "default_profile": "banner",
    },
    "ssh": {
        "template": "ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 {user}@{target} {flags}",
        "profiles": {
            "default": "id 2>&1",
            "key": "-i {key_file} -o BatchMode=yes",
        },
        "defaults": {"user": "root"},
        "default_profile": "default",
    },
    "mysql": {
        "template": "mysql -h {target} -u {user} -p{pass} -e \"{query}\" {flags}",
        "profiles": {
            "default": "-e 'SHOW DATABASES;' 2>/dev/null",
            "tables": "-D {database} -e 'SHOW TABLES;' 2>/dev/null",
            "dump": "-D {database} -e 'SELECT * FROM {table};' 2>/dev/null",
        },
        "defaults": {"user": "root", "pass": "", "database": "mysql", "table": "user"},
        "default_profile": "default",
    },
    "psql": {
        "template": "PGPASSWORD={pass} psql -h {target} -U {user} -c \"{query}\" {flags}",
        "profiles": {
            "default": "-c '\\l' 2>/dev/null",
        },
        "defaults": {"user": "postgres", "pass": "postgres"},
        "default_profile": "default",
    },
    "evil-winrm": {
        "template": "evil-winrm -i {target} -u {user} -p {pass} {flags}",
        "profiles": {
            "default": "",
        },
        "defaults": {"user": "administrator", "pass": ""},
        "default_profile": "default",
    },
    "impacket-smbexec": {
        "template": "impacket-smbexec {domain}/{user}:{pass}@{target} {flags}",
        "profiles": {"default": ""},
        "defaults": {"domain": ".", "user": "administrator", "pass": ""},
        "default_profile": "default",
    },
    "impacket-psexec": {
        "template": "impacket-psexec {domain}/{user}:{pass}@{target} {flags}",
        "profiles": {"default": ""},
        "defaults": {"domain": ".", "user": "administrator", "pass": ""},
        "default_profile": "default",
    },
    "impacket-mssqlexec": {
        "template": "impacket-mssqlexec {domain}/{user}:{pass}@{target} {flags}",
        "profiles": {"default": ""},
        "defaults": {"domain": ".", "user": "sa", "pass": ""},
        "default_profile": "default",
    },
    "steghide": {
        "template": "steghide extract -sf {file} -p {pass} -f {flags}",
        "profiles": {"default": ""},
        "defaults": {"file": "", "pass": ""},
        "default_profile": "default",
    },
    "binwalk": {
        "template": "binwalk {file} {flags}",
        "profiles": {"default": "-Me"},
        "defaults": {"file": ""},
        "default_profile": "default",
    },
    "john": {
        "template": "john --format={format} --wordlist={wordlist} {hash_file} {flags}",
        "profiles": {
            "default": "",
            "single": "--single",
            "incremental": "--incremental",
        },
        "defaults": {"format": "", "wordlist": "/usr/share/wordlists/rockyou.txt", "hash_file": ""},
        "default_profile": "default",
    },
    "hashcat": {
        "template": "hashcat -m {mode} -a 0 {hash_file} {wordlist} {flags}",
        "profiles": {"default": "--force -O"},
        "defaults": {"mode": "0", "hash_file": "", "wordlist": "/usr/share/wordlists/rockyou.txt"},
        "default_profile": "default",
    },
    "wfuzz": {
        "template": "wfuzz -w {wordlist} {target}/FUZZ {flags}",
        "profiles": {"default": "-c -t 50 --hc 404"},
        "defaults": {"wordlist": "/usr/share/wordlists/wfuzz/general/common.txt"},
        "default_profile": "default",
    },
    "dirb": {
        "template": "dirb http://{target} {wordlist} {flags}",
        "profiles": {"default": "-w -r"},
        "defaults": {"wordlist": "/usr/share/wordlists/dirb/common.txt"},
        "default_profile": "default",
    },
    "zap-cli": {
        "template": "zap-cli quick-scan --self-contained {target} {flags}",
        "profiles": {"default": "-o -l low"},
        "default_profile": "default",
    },
    "wafw00f": {
        "template": "wafw00f {target} {flags}",
        "profiles": {"default": "-a"},
        "default_profile": "default",
    },
    "testssl": {
        "template": "testssl --quiet --color 0 {target} {flags}",
        "profiles": {"default": ""},
        "default_profile": "default",
    },
    "openssl": {
        "template": "openssl s_client -connect {target}:{port} -servername {target} 2>&1 {flags}",
        "profiles": {"default": ""},
        "defaults": {"port": "443"},
        "default_profile": "default",
    },
    "tcpdump": {
        "template": "tcpdump -i {interface} {flags}",
        "profiles": {
            "default": "-c 10 -nn",
            "port": "-i {interface} port {port} -c 10 -nn",
        },
        "defaults": {"interface": "eth0", "port": "80"},
        "default_profile": "default",
    },
    "responder": {
        "template": "responder -I {interface} {flags}",
        "profiles": {"default": "-dwPv"},
        "defaults": {"interface": "eth0"},
        "default_profile": "default",
    },
    "impacket-ntlmrelayx": {
        "template": "impacket-ntlmrelayx -tf {targets_file} -smb2support {flags}",
        "profiles": {"default": "-i", "socks": "-socks"},
        "defaults": {"targets_file": ""},
        "default_profile": "default",
    },
    "cewl": {
        "template": "cewl {target} -w {output} {flags}",
        "profiles": {"default": "-m 6 -d 2"},
        "defaults": {"output": "cewl_words.txt"},
        "default_profile": "default",
    },
}

TASK_MAP = {
    "port scan": ["nmap"],
    "portscan": ["nmap"],
    "scan ports": ["nmap"],
    "service scan": ["nmap"],
    "vulnerability scan": ["nuclei", "nikto", "nmap"],
    "web recon": ["whatweb", "wafw00f", "curl", "wpscan"],
    "web directory": ["gobuster", "ffuf", "dirb", "wfuzz"],
    "directory brute": ["gobuster", "ffuf", "dirb", "wfuzz"],
    "dir bust": ["gobuster", "ffuf"],
    "dns recon": ["dnsrecon", "dig"],
    "dns enumeration": ["dnsrecon", "dig"],
    "subdomain": ["dnsrecon", "gobuster"],
    "smb enum": ["smbclient", "smbmap", "enum4linux"],
    "smb enumeration": ["smbclient", "smbmap", "enum4linux"],
    "snb": ["smbclient", "smbmap", "enum4linux"],
    "enumerate smb": ["smbclient", "smbmap", "enum4linux"],
    "enum smb": ["smbclient", "smbmap", "enum4linux"],
    "smb scan": ["smbclient", "smbmap", "enum4linux"],
    "scan smb": ["smbclient", "smbmap", "enum4linux"],
    "enumerate web": ["whatweb", "gobuster", "nikto", "curl"],
    "scan web": ["whatweb", "nikto", "nuclei"],
    "web scan": ["whatweb", "nikto", "nuclei"],
    "search web dir": ["gobuster", "ffuf", "dirb"],
    "web dir scan": ["gobuster", "ffuf", "dirb"],
    "dir scan": ["gobuster", "ffuf", "dirb"],
    "brute force": ["hydra"],
    "bruteforce": ["hydra"],
    "crack password": ["hydra", "john", "hashcat"],
    "password crack": ["john", "hashcat"],
    "hash crack": ["hashcat", "john"],
    "exploit search": ["searchsploit"],
    "search exploit": ["searchsploit"],
    "sql injection": ["sqlmap"],
    "sql": ["sqlmap"],
    "wordpress": ["wpscan"],
    "wp scan": ["wpscan"],
    "enum ftp": ["ftp", "nmap"],
    "enumerate ftp": ["ftp", "nmap"],
    "ftp enum": ["ftp", "nmap"],
    "ftp enumeration": ["ftp", "nmap"],
    "enum ssh": ["ssh", "nmap"],
    "enumerate ssh": ["ssh", "nmap"],
    "ssh enum": ["ssh", "nmap"],
    "ssh enumeration": ["nmap"],
    "redis enum": ["redis-cli"],
    "redis enumeration": ["redis-cli"],
    "mongo enum": ["mongosh"],
    "mongodb enum": ["mongosh"],
    "mysql enum": ["mysql"],
    "mysql enumeration": ["mysql"],
    "nfs enum": ["showmount"],
    "nfs enumeration": ["showmount"],
    "ldap enum": ["ldapsearch"],
    "ldap enumeration": ["ldapsearch"],
    "web app scan": ["nikto", "nuclei", "zap-cli", "wpscan"],
    "ssl scan": ["testssl", "openssl"],
    "ssl tls": ["testssl", "openssl"],
    "cms detect": ["whatweb", "wpscan"],
    "waf detect": ["wafw00f"],
    "wordlist gen": ["cewl"],
    "wordlist generate": ["cewl"],
    "packet capture": ["tcpdump"],
    "responder": ["responder"],
    "relay": ["impacket-ntlmrelayx"],
    "winrm": ["evil-winrm"],
    "psexec": ["impacket-psexec"],
    "smbexec": ["impacket-smbexec"],
    "steghide": ["steghide"],
    "binwalk": ["binwalk"],
    "hydra": ["hydra"],
    "nikto": ["nikto"],
    "gobuster": ["gobuster"],
    "ffuf": ["ffuf"],
    "sqlmap": ["sqlmap"],
    "nuclei": ["nuclei"],
    "wpscan": ["wpscan"],
    "dnsrecon": ["dnsrecon"],
    "dig": ["dig"],
    "smbclient": ["smbclient"],
    "smbmap": ["smbmap"],
    "enum4linux": ["enum4linux"],
    "showmount": ["showmount"],
    "ldapsearch": ["ldapsearch"],
    "redis-cli": ["redis-cli"],
    "mongosh": ["mongosh"],
    "mysql": ["mysql"],
    "psql": ["psql"],
    "impacket-psexec": ["impacket-psexec"],
    "impacket-smbexec": ["impacket-smbexec"],
    "impacket-mssqlexec": ["impacket-mssqlexec"],
    "evil-winrm": ["evil-winrm"],
    "testssl": ["testssl"],
    "openssl": ["openssl"],
    "wafw00f": ["wafw00f"],
    "whatweb": ["whatweb"],
    "curl": ["curl"],
    "zap-cli": ["zap-cli"],
    "cewl": ["cewl"],
    "john": ["john"],
    "hashcat": ["hashcat"],
    "wpscan": ["wpscan"],
    "wp-scan": ["wpscan"],
    "dirb": ["dirb"],
    "wfuzz": ["wfuzz"],
    "tcpdump": ["tcpdump"],
    "responder": ["responder"],
    "impacket-ntlmrelayx": ["impacket-ntlmrelayx"],
    "steghide": ["steghide"],
    "binwalk": ["binwalk"],
    "nmap": ["nmap"],
    "ftp": ["ftp"],
    "msfconsole": ["msfconsole"],
    "netcat": ["netcat"],
    "searchsploit": ["searchsploit"],
    "ssh": ["ssh"],
}

TOOL_NAMES = {name.lower(): name for name in TOOL_COMMANDS}


class ToolMatcher:
    def __init__(self):
        self.parser = output_parser

    def expand_target(self, target, port=None, service=None, profile=None):
        t = target
        if port and profile and profile in TOOL_COMMANDS.get("nmap", {}).get("profiles", {}):
            t = f"{target}:{port}" if ":" not in target else target
        return t

    def _extract_tool_name(self, task):
        task_lower = task.lower().strip()
        if task_lower in TASK_MAP:
            return TASK_MAP[task_lower]
        for pattern, tools in sorted(TASK_MAP.items(), key=lambda x: -len(x[0])):
            if pattern in task_lower:
                return tools
        return None

    def _format_command(self, tool_name, target, profile=None, **kwargs):
        tool_name_lower = tool_name.lower()
        if tool_name_lower not in TOOL_COMMANDS:
            return None, None

        config = TOOL_COMMANDS[tool_name_lower]
        template = config["template"]

        if profile is None:
            profile = config.get("default_profile", "default")

        profiles = config.get("profiles", {})
        flags = profiles.get(profile, profiles.get("default", ""))

        defaults = config.get("defaults", {})
        combined = {**defaults, **kwargs, "target": target, "flags": flags}

        try:
            cmd = template.format(**combined)
        except KeyError as e:
            cmd = template.replace(f"{{{e.args[0]}}}", "").format(**combined)
        while True:
            try:
                cmd = cmd.format(**combined)
                break
            except KeyError as e:
                cmd = cmd.replace(f"{{{e.args[0]}}}", "")

        return cmd, config.get("parsers", [])

    def match_tools(self, task, target, port=None, service=None, ip=None):
        task_lower = task.lower().strip()

        matched_tools = self._extract_tool_name(task)

        if matched_tools is None:
            suggested = db_suggest_tools(task)[:10]
            matched_tools = []
            for cat, tool_entry in suggested:
                name = tool_entry.get("name", "").lower()
                if name in TOOL_COMMANDS:
                    matched_tools.append(name)
            if not matched_tools:
                return []

        results = []
        for tool_name in matched_tools:
            tgt = target
            tool_config = TOOL_COMMANDS.get(tool_name, {})
            if port and "{port}" not in tool_config.get("template", ""):
                tgt = f"{target}:{port}"
            profiles = list(tool_config.get("profiles", {}).keys())
            for prof in profiles if len(profiles) > 1 else [None]:
                cmd, parsers = self._format_command(tool_name, tgt, profile=prof)
                if cmd:
                    results.append({
                        "tool": tool_name,
                        "command": cmd,
                        "parsers": parsers,
                        "profile": prof or "default",
                        "target": tgt,
                    })
        return results

    def execute_match(self, target, port, service, task=None):
        if task is None:
            task = self._task_for_port(port, service)
        matches = self.match_tools(task, target, port=port, service=service)
        outputs = []
        for m in matches[:3]:
            out = self._run_command(m["command"], timeout=120)
            parsed = self._try_parse(out, m["parsers"], m["tool"])
            outputs.append({
                "tool": m["tool"],
                "command": m["command"],
                "raw": out[:2000],
                "parsed": parsed,
            })
        return outputs

    def _task_for_port(self, port, service):
        port = int(port) if port else 0
        if port == 21:
            return "ftp enum"
        elif port == 22:
            return "ssh enum"
        elif port in (80, 443, 8080, 8443):
            return "web recon"
        elif port == 139 or port == 445:
            return "smb enum"
        elif port == 389 or port == 636:
            return "ldap enum"
        elif port == 2049:
            return "nfs enum"
        elif port == 3306:
            return "mysql enum"
        elif port == 5432:
            return "psql enum"
        elif port == 6379:
            return "redis enum"
        elif port == 27017:
            return "mongodb enum"
        elif port == 25:
            return "smtp enum"
        elif port == 53:
            return "dns recon"
        elif port == 88:
            return "kerberos enum"
        elif port == 161:
            return "snmp enum"
        elif port == 1433:
            return "mssql enum"
        elif port == 5985 or port == 5986:
            return "winrm"
        elif port == 3389:
            return "rdp enum"
        elif port == 110 or port == 143 or port == 993 or port == 995:
            return "email enum"
        elif service:
            return f"{service} enum"
        return "port scan"

    def _run_command(self, cmd, timeout=120):
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            out = result.stdout + result.stderr
            return out.strip()
        except subprocess.TimeoutExpired:
            return "[TIMEOUT]"
        except FileNotFoundError:
            return "[TOOL NOT INSTALLED]"
        except Exception as e:
            return f"[ERROR] {e}"

    def _try_parse(self, output, parsers, tool_name):
        if not output or output.startswith("[") or len(output) < 10:
            return {}
        tool = output_parser.detect_tool(output)
        if tool and tool in output_parser.PARSERS:
            try:
                return output_parser.PARSERS[tool](output)
            except Exception:
                pass
        # try each available parser
        for parser_name in parsers:
            mapper = {
                "nmap": output_parser.parse_nmap,
                "gobuster": output_parser.parse_gobuster,
                "whatweb": output_parser.parse_whatweb,
                "nikto": output_parser.parse_nikto,
                "smbclient": output_parser.parse_smbclient,
                "enum4linux": output_parser.parse_enum4linux,
                "hydra": output_parser.parse_hydra,
                "sqlmap": output_parser.parse_sqlmap,
                "nuclei": output_parser.parse_nuclei,
            }
            fn = mapper.get(parser_name)
            if fn:
                try:
                    result = fn(output)
                    if result and (isinstance(result, dict) and any(v for v in result.values())):
                        return result
                except Exception:
                    continue
        return {}

    def generic_run(self, task, target, **kwargs):
        matches = self.match_tools(task, target)
        if not matches:
            all_suggestions = db_suggest_tools(task)[:10]
            return {"status": "no_match", "task": task, "suggestions": [t for _, t in all_suggestions]}

        results = []
        for m in matches[:3]:
            cmd = m["command"]
            out = self._run_command(cmd)
            parsed = self._try_parse(out, m["parsers"], m["tool"])
            results.append({
                "tool": m["tool"],
                "command": cmd,
                "output": out[:2000] if len(out) > 2000 else out,
                "parsed": parsed,
            })
        return {"status": "done", "task": task, "results": results}
