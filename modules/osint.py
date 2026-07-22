import subprocess
import re
import json
import urllib.request
import urllib.parse
import socket
from datetime import datetime
from typing import Optional

try:
    from modules.tool_db import suggest_tools, search_tools, get_tools_by_category
    TOOL_DB_AVAILABLE = True
except ImportError:
    TOOL_DB_AVAILABLE = False

OSINT_TOOL_MAP = {
    "domain": ["theharvester", "recon-ng", "whois", "dig", "nslookup", "amass", "sublist3r", "dnsrecon", "dnsenum"],
    "subdomains": ["sublist3r", "amass", "subfinder", "assetfinder", "findomain", "dnsx", "altdns", "gobuster"],
    "dns": ["dnsrecon", "dnsenum", "dnsmap", "fierce", "nslookup", "dig", "host"],
    "whois": ["whois", "whois-client"],
    "email": ["theharvester", "holehe", "emailfinder", "h8mail", "infoga", "smtp-user-enum"],
    "username": ["sherlock", "maigret", "holehe", "social-analyzer", "whatsmyname"],
    "social": ["sherlock", "maigret", "recon-ng", "spiderfoot", "sn0int", "theharvester"],
    "metadata": ["exiftool", "mat2", "pdfinfo", "exif", "foremost", "binwalk"],
    "ip": ["whois", "geoiplookup", "nmap", "masscan", "shodan", "ipinfo"],
    "dork": ["pagodo", "go-dork", "dorkbot", "sn0int"],
    "web_archive": ["waybackpy", "cdx_toolkit"],
    "framework": ["recon-ng", "spiderfoot", "sn0int", "maltego", "theharvester", "datasploit"],
}


class OSINTEngine:
    def __init__(self):
        self.results = {}
        self._tool_suggestions = {}

    def run_cmd(self, cmd: str, timeout: int = 15) -> str:
        try:
            r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
            return (r.stdout + r.stderr)[:3000] or "(no output)"
        except subprocess.TimeoutExpired:
            return "(timeout)"
        except Exception as e:
            return f"(error: {e})"

    def web_get(self, url: str, timeout: int = 15) -> str:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode(errors="replace")[:5000]
        except Exception as e:
            return f"(fetch error: {e})"

    def _get_tools(self, task_type: str) -> list:
        if task_type in self._tool_suggestions:
            return self._tool_suggestions[task_type]

        tools = []
        preferred = OSINT_TOOL_MAP.get(task_type, [])

        if TOOL_DB_AVAILABLE:
            for name in preferred:
                results = search_tools(name)
                for cat, tool in results:
                    if tool["name"].lower() == name.lower():
                        tools.append({"name": tool["name"], "description": tool["description"], "category": cat})

            if not tools:
                results = suggest_tools(task_type.replace("_", " "))
                seen = set()
                for cat, tool in results:
                    if tool["name"] not in seen:
                        seen.add(tool["name"])
                        tools.append({"name": tool["name"], "description": tool["description"][:100], "category": cat})
                        if len(tools) >= 8:
                            break

        if not tools:
            for name in preferred[:5]:
                tools.append({"name": name, "description": f"Use `{name} --help` for usage", "category": "osint"})

        self._tool_suggestions[task_type] = tools
        return tools

    def _suggestions_block(self, task_type: str) -> str:
        tools = self._get_tools(task_type)
        if not tools:
            return ""
        lines = ["\n**Recommended tools:**"]
        for t in tools[:6]:
            cat = t.get("category", "").replace("blackarch-", "")
            lines.append(f"  - `{t['name']}` ({cat}) — {t.get('description', '')[:80]}")
        return "\n".join(lines)

    def domain_recon(self, domain: str) -> dict:
        result = {
            "domain": domain,
            "whois": "",
            "dns": {"a": [], "mx": [], "ns": [], "txt": [], "cname": []},
            "subdomains": [],
            "certificate": [],
            "technology": [],
            "tools": self._get_tools("domain"),
            "subdomain_tools": self._get_tools("subdomains"),
        }

        result["whois"] = self.run_cmd(f"whois {domain} 2>/dev/null", 20)[:2000]

        for rtype in ["a", "mx", "ns", "txt", "cname"]:
            out = self.run_cmd(f"dig +short {domain} {rtype} 2>/dev/null", 10)
            result["dns"][rtype] = [l.strip() for l in out.split("\n") if l.strip()]

        sub_out = self.run_cmd(
            f"curl -s 'https://crt.sh/?q=%25.{domain}&output=json' 2>/dev/null", 15,
        )
        if sub_out.startswith("["):
            try:
                certs = json.loads(sub_out)
                seen = set()
                for c in certs[:50]:
                    name = c.get("name_value", "")
                    for sub in name.split("\n"):
                        sub = sub.strip().lower()
                        if sub.endswith(domain) and sub not in seen:
                            seen.add(sub)
                            result["certificate"].append(sub)
                            if sub != domain:
                                result["subdomains"].append(sub)
            except:
                pass

        return result

    def ip_recon(self, ip: str) -> dict:
        result = {
            "ip": ip,
            "hostname": "",
            "asn": "",
            "location": "",
            "reverse_dns": [],
            "tools": self._get_tools("ip"),
        }

        try:
            result["hostname"] = socket.gethostbyaddr(ip)[0]
        except:
            result["hostname"] = ""

        whois_out = self.run_cmd(f"whois {ip} 2>/dev/null", 20)
        for line in whois_out.split("\n"):
            l = line.lower()
            if "origin" in l or "asn" in l:
                m = re.search(r"origin\s+(\S+)", line, re.IGNORECASE)
                if m:
                    result["asn"] = m.group(1)
            if "country" in l:
                m = re.search(r"country:\s+(\S+)", line, re.IGNORECASE)
                if m:
                    result["location"] = m.group(1)

        rdns_out = self.run_cmd(
            f"curl -s 'https://api.hackertarget.com/reverseiplookup/?q={ip}' 2>/dev/null", 15,
        )
        if rdns_out and "error" not in rdns_out.lower():
            result["reverse_dns"] = [l.strip() for l in rdns_out.split("\n") if l.strip() and not l.startswith("API")]

        return result

    def email_recon(self, email: str) -> dict:
        result = {
            "email": email,
            "domain": email.split("@")[-1] if "@" in email else "",
            "username": email.split("@")[0] if "@" in email else "",
            "domain_recon_result": None,
            "email_format": "",
            "tools": self._get_tools("email"),
        }

        if not result["domain"]:
            return result

        result["domain_recon_result"] = self.domain_recon(result["domain"])

        out = self.run_cmd(
            f"curl -s 'https://api.hackertarget.com/email-format/?q={email}' 2>/dev/null", 15,
        )
        if out and "error" not in out.lower():
            result["email_format"] = out.strip()

        return result

    def username_recon(self, username: str) -> dict:
        result = {
            "username": username,
            "profiles": [],
            "tools": self._get_tools("username"),
        }

        sites = {
            "github": f"https://github.com/{username}",
            "x.com": f"https://x.com/{username}",
            "reddit": f"https://www.reddit.com/user/{username}",
            "hackernews": f"https://news.ycombinator.com/user?id={username}",
            "keybase": f"https://keybase.io/{username}",
            "medium": f"https://medium.com/@{username}",
            "dev.to": f"https://dev.to/{username}",
            "replit": f"https://replit.com/@{username}",
            "hackthebox": f"https://app.hackthebox.com/profile/{username}",
        }

        for site, url in sites.items():
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                resp = urllib.request.urlopen(req, timeout=5)
                if resp.status == 200:
                    result["profiles"].append({"site": site, "url": url, "status": "found"})
                else:
                    result["profiles"].append({"site": site, "url": url, "status": "not found"})
            except:
                result["profiles"].append({"site": site, "url": url, "status": "not found"})

        return result

    def google_dork(self, domain: str, dork_type: str = "all") -> list:
        dorks = {
            "files": f"site:{domain} filetype:pdf OR filetype:doc OR filetype:xls OR filetype:sql",
            "admin": f"site:{domain} inurl:admin OR inurl:login OR inurl:wp-admin",
            "config": f"site:{domain} filetype:env OR filetype:cfg OR filetype:conf OR filetype:ini",
            "exposed": f"site:{domain} intitle:'index of' OR inurl:backup OR inurl:dump",
            "sql": f"site:{domain} inurl:.php?id= OR inurl:page_id=",
            "email": f"site:{domain} intext:@ OR intext:mail.",
            "all": f"site:{domain}",
        }

        categories = ["files", "admin", "config", "exposed", "sql", "email"] if dork_type == "all" else [dork_type]
        results = []
        tools = self._get_tools("dork")

        for t in categories:
            dork = dorks.get(t, f"site:{domain}")
            encoded = urllib.parse.quote(dork)
            out = self.web_get(f"https://html.duckduckgo.com/html/?q={encoded}", 15)
            links = re.findall(r'href="(https?://[^"]+)"', out)
            unique = list(dict.fromkeys([l for l in links if domain in l]))[:5]
            results.append({"type": t, "dork": dork, "results": unique, "tools": tools})

        return results

    def web_archive(self, domain: str) -> list:
        out = self.web_get(
            f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&limit=20", 20
        )
        snapshots = []
        try:
            data = json.loads(out) if out.startswith("[") else []
            for entry in data[1:21] if data else []:
                if len(entry) >= 6:
                    snapshots.append({
                        "url": entry[2] if len(entry) > 2 else "",
                        "timestamp": entry[1] if len(entry) > 1 else "",
                        "status": entry[4] if len(entry) > 4 else "",
                    })
        except:
            pass
        return snapshots

    def metadata_extract(self, file_path: str) -> dict:
        result = {"file": file_path, "metadata": "", "tools": self._get_tools("metadata")}
        result["metadata"] = self.run_cmd(f'exiftool "{file_path}" 2>/dev/null', 15)
        return result

    def full_recon(self, target: str) -> dict:
        results = {"target": target, "timestamp": datetime.now().isoformat(), "sections": {}}

        is_domain = "." in target and not target.replace(".", "").isdigit()
        is_ip = target.replace(".", "").isdigit() and target.count(".") == 3

        if is_domain:
            results["type"] = "domain"
            results["sections"]["domain"] = self.domain_recon(target)
            results["sections"]["dorks"] = self.google_dork(target)
            results["sections"]["archive"] = self.web_archive(target)
            if "@" in target:
                results["sections"]["email"] = self.email_recon(target)
        elif is_ip:
            results["type"] = "ip"
            results["sections"]["ip"] = self.ip_recon(target)
        else:
            results["type"] = "username"
            results["sections"]["username"] = self.username_recon(target)

        results["framework_tools"] = self._get_tools("framework")
        self.results[target] = results
        return results

    def format_report(self, target: str) -> str:
        if target not in self.results:
            return "No results for this target."

        data = self.results[target]
        lines = []
        lines.append(f"# OSINT Report: {target}")
        lines.append(f"Date: {data['timestamp']}")
        lines.append("")

        if "domain" in data.get("sections", {}):
            d = data["sections"]["domain"]
            lines.append("## DNS Records")
            for rtype in ["a", "mx", "ns", "txt", "cname"]:
                if d["dns"][rtype]:
                    lines.append(f"- **{rtype.upper()}**: {', '.join(d['dns'][rtype][:5])}")
            if d.get("subdomains"):
                lines.append(f"\n### Subdomains ({len(d['subdomains'])})")
                for s in sorted(d["subdomains"])[:20]:
                    lines.append(f"- {s}")
            lines.append(d.get("subdomain_tools", []) and self._suggestions_block("subdomains") or "")
            if d.get("whois"):
                lines.append(f"\n### WHOIS")
                lines.append(f"```\n{d['whois'][:500]}\n```")
            lines.append(self._suggestions_block("domain"))

        if "ip" in data.get("sections", {}):
            ip = data["sections"]["ip"]
            lines.append(f"\n## IP Recon: {ip['ip']}")
            lines.append(f"- **Hostname**: {ip.get('hostname', 'N/A')}")
            lines.append(f"- **ASN**: {ip.get('asn', 'N/A')}")
            lines.append(f"- **Location**: {ip.get('location', 'N/A')}")
            if ip.get("reverse_dns"):
                lines.append(f"- **Domains on this IP**: {', '.join(ip['reverse_dns'][:5])}")
            lines.append(self._suggestions_block("ip"))

        if "username" in data.get("sections", {}):
            u = data["sections"]["username"]
            found = [p for p in u["profiles"] if p["status"] == "found"]
            if found:
                lines.append(f"\n## Profiles Found for {u['username']}")
                for p in found:
                    lines.append(f"- [{p['site']}]({p['url']})")
            else:
                lines.append(f"\n## Profiles for {u['username']}: None found")
            lines.append(self._suggestions_block("username"))

        if "dorks" in data.get("sections", {}):
            lines.append("\n## Google Dorks")
            for d in data["sections"]["dorks"]:
                if d["results"]:
                    lines.append(f"- **{d['type']}**: {d['results'][0]}")
            lines.append(self._suggestions_block("dork"))

        if "archive" in data.get("sections", {}):
            snapshots = data["sections"]["archive"]
            if snapshots:
                lines.append(f"\n## Wayback Machine ({len(snapshots)} snapshots)")
                for s in snapshots[:5]:
                    lines.append(f"- [{s['timestamp']}] {s['url']} (HTTP {s['status']})")

        fw_tools = data.get("framework_tools", [])
        if fw_tools:
            lines.append("\n## Full OSINT Framework Tools")
            for t in fw_tools[:4]:
                cat = t.get("category", "").replace("blackarch-", "")
                lines.append(f"- **{t['name']}** ({cat}) — {t.get('description', '')[:80]}")

        return "\n".join(lines)

    def tool_recommendations_for_target(self, target: str) -> str:
        lines = ["## OSINT Tool Recommendations"]
        is_domain = "." in target and not target.replace(".", "").isdigit()
        is_ip = target.replace(".", "").isdigit() and target.count(".") == 3

        if is_domain:
            lines.append("\n### Domain Reconnaissance")
            for t in self._get_tools("domain")[:5]:
                lines.append(f"- `{t['name']}` — {t.get('description', '')[:80]}")
            lines.append("\n### Subdomain Enumeration")
            for t in self._get_tools("subdomains")[:5]:
                lines.append(f"- `{t['name']}` — {t.get('description', '')[:80]}")
            lines.append("\n### Google Dorking")
            for t in self._get_tools("dork")[:3]:
                lines.append(f"- `{t['name']}` — {t.get('description', '')[:80]}")

        elif is_ip:
            lines.append("\n### IP Reconnaissance")
            for t in self._get_tools("ip")[:5]:
                lines.append(f"- `{t['name']}` — {t.get('description', '')[:80]}")
        else:
            lines.append("\n### Username Search")
            for t in self._get_tools("username")[:5]:
                lines.append(f"- `{t['name']}` — {t.get('description', '')[:80]}")

        lines.append("\n### Full OSINT Frameworks")
        for t in self._get_tools("framework")[:4]:
            lines.append(f"- `{t['name']}` — {t.get('description', '')[:80]}")

        return "\n".join(lines)
