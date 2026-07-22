import re
from typing import Optional


def parse_nmap(output: str) -> dict:
    result = {
        "host": "",
        "hostname": "",
        "os": "",
        "ports": [],
        "services": [],
        "raw": output[:2000],
    }

    host_m = re.search(r"Nmap scan report for ([^\s]+(?:\s\([^)]+\))?)", output)
    if host_m:
        result["host"] = host_m.group(1).strip()

    os_m = re.search(r"OS details: (.+)", output)
    if os_m:
        result["os"] = os_m.group(1).strip()

    port_pattern = re.compile(
        r"^(\d+)/(tcp|udp)\s+(open|filtered|closed)\s+(\S+)(?:\s+(.+))?$", re.MULTILINE
    )
    for m in port_pattern.finditer(output):
        port_num = int(m.group(1))
        proto = m.group(2)
        state = m.group(3)
        service = m.group(4) if m.group(4) else "unknown"
        version = ""

        version_match = re.search(rf"^{port_num}/{proto}\s+{state}\s+(\S+)\s+(.+)$", output, re.MULTILINE)
        if version_match:
            version = version_match.group(2).strip()

        port_info = {
            "port": port_num,
            "protocol": proto,
            "state": state,
            "service": service.lower(),
            "version": version[:100] if version else "",
        }
        result["ports"].append(port_info)
        result["services"].append(f"{port_num}/{proto} ({service})")

    return result


def parse_gobuster(output: str) -> list:
    results = []
    for line in output.split("\n"):
        if "/" in line and "Status:" in line:
            m = re.search(r"(/\S+)\s+\(Status:\s*(\d+)\)", line)
            if m:
                results.append({
                    "path": m.group(1),
                    "status": int(m.group(2)),
                })
            else:
                parts = line.split()
                if len(parts) >= 2:
                    results.append({
                        "path": parts[0],
                        "status": parts[-1] if parts[-1].isdigit() else 0,
                    })
    return results


def parse_whatweb(output: str) -> dict:
    result = {"technologies": [], "server": "", "title": ""}
    for line in output.split("\n"):
        if "[" in line and "]" in line:
            techs = re.findall(r"\[([^\]]+)\]", line)
            for t in techs:
                if t not in ["200", "OK"]:
                    result["technologies"].append(t.strip())
        if "Server" in line or "server" in line:
            m = re.search(r"Server[:\s]+(.+)", line, re.IGNORECASE)
            if m:
                result["server"] = m.group(1).strip()
        if "Title" in line or "title" in line:
            m = re.search(r"(?:Title|title)[:\s]+(.+)", line)
            if m:
                result["title"] = m.group(1).strip()
    return result


def parse_nikto(output: str) -> list:
    vulns = []
    for line in output.split("\n"):
        if "+" in line and any(
            x in line.lower()
            for x in ["vuln", "cve", "xss", "sqli", "lfi", "rfi", "directory", "disclosure", "warning"]
        ):
            vulns.append(line.strip().lstrip("+ "))
    return vulns


def parse_smbclient(output: str) -> list:
    shares = []
    for line in output.split("\n"):
        line = line.strip()
        if line and not line.startswith("\\"):
            parts = line.split()
            if parts and parts[0].endswith("$"):
                shares.append(parts[0])
            elif parts and not any(x in line for x in ["Disk", "error", "failed"]):
                share_name = parts[0]
                if share_name not in ["session", "Server", "Comment", "------"] and not share_name.startswith("\\"):
                    shares.append(share_name)
    return shares


def parse_enum4linux(output: str) -> dict:
    result = {"users": [], "shares": [], "os": "", "policy": {}}
    in_users = False
    in_shares = False

    for line in output.split("\n"):
        if "index:" in line and "/" in line:
            m = re.search(r"index:\s+\d+/\d+\s+[+-]{3}\s+(.+)", line)
            if m:
                result["users"].append(m.group(1).strip())

        if "Sharename" in line or "Share name" in line:
            in_shares = True
            continue
        if in_shares and line.strip() and not line.startswith("-"):
            parts = line.split()
            if parts and parts[0] not in ["---", "------"]:
                result["shares"].append(parts[0])
        if in_shares and "---" in line and len(line.strip()) < 10:
            in_shares = False

        if "OS:" in line or "os:" in line:
            m = re.search(r"OS[:\s]+(.+)", line, re.IGNORECASE)
            if m:
                result["os"] = m.group(1).strip()

        if "Password policy" in line:
            in_policy = True
            continue

    return result


def parse_hydra(output: str) -> list:
    creds = []
    for line in output.split("\n"):
        if "login:" in line and "password:" in line:
            m = re.search(r"login:\s+(\S+)\s+password:\s+(\S+)", line)
            if m:
                creds.append({"username": m.group(1), "password": m.group(2)})
        elif "host:" in line and "login" in line:
            m = re.search(r"host:\s+\S+\s+login:\s+(\S+)\s+password:\s+(\S+)", line)
            if m:
                creds.append({"username": m.group(1), "password": m.group(2)})
    return creds


def parse_sqlmap(output: str) -> list:
    findings = []
    for line in output.split("\n"):
        if "Parameter:" in line and "GET" in line:
            m = re.search(r"Parameter:\s+(\S+)\s+\(GET\)", line)
            if m:
                findings.append({"type": "sqli", "param": m.group(1), "method": "GET"})
        elif "Parameter:" in line and "POST" in line:
            m = re.search(r"Parameter:\s+(\S+)\s+\(POST\)", line)
            if m:
                findings.append({"type": "sqli", "param": m.group(1), "method": "POST"})
        elif "Type:" in line and "boolean" in line:
            if findings:
                findings[-1]["technique"] = "boolean-based blind"
        elif "Type:" in line and "error" in line:
            if findings:
                findings[-1]["technique"] = "error-based"
        elif "Type:" in line and "time" in line:
            if findings:
                findings[-1]["technique"] = "time-based blind"
        elif "Type:" in line and "UNION" in line:
            if findings:
                findings[-1]["technique"] = "union-based"
    return findings


def parse_nuclei(output: str) -> list:
    findings = []
    for line in output.split("\n"):
        if "[critical]" in line or "[high]" in line or "[medium]" in line or "[low]" in line:
            m = re.search(r"\[(critical|high|medium|low)\]\s+(\S+)", line)
            if m:
                findings.append({
                    "severity": m.group(1),
                    "template": m.group(2),
                    "matched": line,
                })
    return findings


PARSERS = {
    "nmap": parse_nmap,
    "gobuster": parse_gobuster,
    "whatweb": parse_whatweb,
    "nikto": parse_nikto,
    "smbclient": parse_smbclient,
    "enum4linux": parse_enum4linux,
    "hydra": parse_hydra,
    "sqlmap": parse_sqlmap,
    "nuclei": parse_nuclei,
}


def detect_tool(output: str) -> Optional[str]:
    signatures = {
        "nmap": ["Nmap scan report for", "Nmap done:", "PORT     STATE"],
        "gobuster": ["Gobuster", "Status:", "Progress:"],
        "whatweb": ["WhatWeb", "http://", "https://", "["],
        "nikto": ["Nikto", "+ Server:", "+ Target IP:"],
        "smbclient": ["smbclient", "Sharename", "tree connect failed"],
        "enum4linux": ["enum4linux", "index:", "Workgroup:"],
        "hydra": ["Hydra", "login:", "password:"],
        "sqlmap": ["sqlmap", "Parameter:", "URL:"],
        "nuclei": ["Nuclei", "[critical]", "[high]"],
    }
    for tool_name, sigs in signatures.items():
        if all(s in output for s in sigs[:2]) or any(s in output for s in sigs):
            return tool_name
    return None
