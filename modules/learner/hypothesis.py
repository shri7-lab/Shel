import random
from collections import defaultdict


class HypothesisGenerator:
    SERVICE_PATTERNS = {
        21: ["vsftpd", "ProFTPD", "Pure-FTPd", "Microsoft FTP", "FileZilla FTP"],
        22: ["OpenSSH", "Dropbear SSH", "libssh"],
        23: ["Telnet"],
        25: ["Postfix", "Exim", "Sendmail", "Exchange SMTP"],
        53: ["BIND", "dnsmasq", "Unbound", "PowerDNS"],
        80: ["Apache", "nginx", "IIS", "lighttpd", "Caddy", "Node.js"],
        110: ["Dovecot POP3", "Exchange POP3"],
        135: ["Windows RPC"],
        139: ["Samba", "Windows SMB"],
        143: ["Dovecot IMAP", "Exchange IMAP"],
        389: ["OpenLDAP", "Active Directory", "389 Directory Server"],
        443: ["Apache HTTPS", "nginx HTTPS", "IIS HTTPS", "Tomcat"],
        445: ["Samba", "Windows SMB"],
        1433: ["Microsoft SQL Server"],
        1521: ["Oracle Database"],
        2049: ["NFS"],
        2375: ["Docker API (unauthenticated)"],
        2376: ["Docker API (TLS)"],
        3306: ["MySQL", "MariaDB"],
        3389: ["RDP (Windows)"],
        5432: ["PostgreSQL"],
        5900: ["VNC"],
        5901: ["VNC"],
        5985: ["WinRM HTTP"],
        5986: ["WinRM HTTPS"],
        6379: ["Redis"],
        8080: ["Tomcat", "Jenkins", "nginx", "Node.js", "Java"],
        8443: ["Tomcat SSL", "Jenkins SSL"],
        9000: ["SonarQube", "PHP-FPM", "Portainer"],
        9090: ["Cockpit", "Prometheus", "Webmin"],
        9200: ["Elasticsearch"],
        9300: ["Elasticsearch cluster"],
        10000: ["Webmin", "Virtualmin"],
        11211: ["Memcached"],
        27017: ["MongoDB"],
        50070: ["Hadoop HDFS"],
        50075: ["Hadoop DataNode"],
    }

    KNOWN_VULNS = {
        21: ["anonymous_auth", "vsftpd_backdoor_234", "proftpd_mod_copy"],
        22: ["weak_creds", "libssh_auth_bypass", "ssh_enum_users"],
        23: ["default_creds", "unencrypted_traffic"],
        25: ["open_relay", "exim_rce", "sendmail_enum"],
        53: ["dns_zone_transfer", "dns_cache_poison", "dns_tunnel"],
        80: ["dir_listing", "lfi", "rfi", "sql_injection", "xss", "default_creds",
             "phpmyadmin", "wordpress", "joomla", "drupal", "shellshock"],
        110: ["weak_auth"],
        135: ["ms08_067"],
        139: ["smb_signing_disabled", "null_session", "eternalblue"],
        143: ["weak_auth"],
        389: ["ldap_anonymous", "ldap_simple_auth"],
        443: ["ssl_weak_ciphers", "heartbleed", "shellshock", "default_creds"],
        445: ["eternalblue", "smb_signing", "smb_null_session", "smb_relay"],
        1433: ["sa_default_pass", "sql_injection"],
        1521: ["default_passwords", "tns_poison"],
        2049: ["no_root_squash", "world_readable"],
        2375: ["docker_api_noauth"],
        3306: ["root_no_pass", "sql_injection", "default_creds"],
        3389: ["bluekeep", "rdp_man_in_the_middle", "weak_creds"],
        5432: ["default_creds", "pghba_misconfig"],
        5900: ["vnc_noauth", "vnc_weak_pass"],
        5985: ["winrm_creds", "winrm_psession"],
        5986: ["winrm_creds"],
        6379: ["redis_noauth", "redis_cron"],
        8080: ["tomcat_manager", "jenkins_script", "default_creds"],
        8443: ["tomcat_manager_ssl", "jenkins_script"],
        9000: ["default_creds"],
        9090: ["default_creds"],
        9200: ["elasticsearch_rce"],
        11211: ["memcached_noauth"],
        27017: ["mongo_noauth", "default_creds"],
    }

    EXPLOIT_MAP = {
        "eternalblue": {"tool": "msf", "module": "exploit/windows/smb/ms17_010_eternalblue"},
        "smb_null_session": {"tool": "smbclient", "command": "smbclient -L //target -N"},
        "anonymous_auth": {"tool": "ftp", "command": "ftp anonymous@target"},
        "tomcat_manager": {"tool": "msf", "module": "exploit/multi/http/tomcat_mgr_upload"},
        "docker_api_noauth": {"tool": "docker", "command": "docker -H tcp://target:2375 ps"},
        "redis_noauth": {"tool": "redis-cli", "command": "redis-cli -h target info"},
        "heartbleed": {"tool": "nmap", "command": "nmap -sV --script ssl-heartbleed target"},
        "shellshock": {"tool": "nmap", "command": "nmap -sV --script http-shellshock target"},
        "bluekeep": {"tool": "msf", "module": "exploit/windows/rdp/cve_2019_0708_bluekeep_rce"},
        "mongo_noauth": {"tool": "mongo", "command": "mongo target:27017"},
        "elasticsearch_rce": {"tool": "curl", "command": "curl -X GET target:9200/_nodes/process"},
    }

    def __init__(self):
        self.hypotheses = []
        self.rand = random.Random()

    def generate_hypotheses(self, open_ports, os_hint=None):
        hypotheses = []
        for port in open_ports:
            if port in self.SERVICE_PATTERNS:
                possible_services = self.SERVICE_PATTERNS[port]
                if "IIS" in possible_services and os_hint and "windows" in os_hint.lower():
                    hypotheses.append({
                        "port": port,
                        "hypothesis": f"Service is likely IIS (based on Windows hint)",
                        "service_guess": "IIS",
                        "confidence": 0.7,
                    })
                elif os_hint and "linux" in os_hint.lower():
                    linux_services = [s for s in possible_services if "IIS" not in s and "Windows" not in s]
                    if linux_services:
                        hypotheses.append({
                            "port": port,
                            "hypothesis": f"Service is likely {linux_services[0]} (based on Linux hint)",
                            "service_guess": linux_services[0],
                            "confidence": 0.6,
                        })

            if port in self.KNOWN_VULNS:
                for vuln in self.KNOWN_VULNS[port]:
                    exploit_info = self.EXPLOIT_MAP.get(vuln, {})
                    hypotheses.append({
                        "port": port,
                        "hypothesis": f"Vulnerability: {vuln} on port {port}",
                        "vuln": vuln,
                        "exploit_tool": exploit_info.get("tool", "unknown"),
                        "exploit_command": exploit_info.get("command", "") or exploit_info.get("module", ""),
                        "confidence": 0.4,
                    })

        self.hypotheses = hypotheses
        return hypotheses

    def test_hypothesis(self, hypothesis, result_success):
        if hypothesis in self.hypotheses:
            idx = self.hypotheses.index(hypothesis)
            self.hypotheses[idx]["tested"] = True
            self.hypotheses[idx]["result"] = "confirmed" if result_success else "refuted"
            if result_success:
                self.hypotheses[idx]["confidence"] = min(1.0, self.hypotheses[idx].get("confidence", 0.5) * 1.5)
            else:
                self.hypotheses[idx]["confidence"] = self.hypotheses[idx].get("confidence", 0.5) * 0.3
        return result_success

    def high_confidence_hypotheses(self, threshold=0.5):
        return [h for h in self.hypotheses if h.get("confidence", 0) >= threshold]

    def generate_attack_plan(self, open_ports, os_hint=None):
        hyps = self.generate_hypotheses(open_ports, os_hint)
        high_conf = self.high_confidence_hypotheses(0.5)
        plan = []
        for h in high_conf:
            vuln = h.get("vuln")
            if vuln and vuln in self.EXPLOIT_MAP:
                exploit = self.EXPLOIT_MAP[vuln]
                plan.append({
                    "port": h["port"],
                    "vulnerability": vuln,
                    "tool": exploit["tool"],
                    "command": exploit.get("command") or exploit.get("module", ""),
                    "confidence": h["confidence"],
                })
        for h in hyps:
            if h.get("service_guess") and not any(p["port"] == h["port"] for p in plan):
                plan.append({
                    "port": h["port"],
                    "service_guess": h["service_guess"],
                    "action": "enumerate",
                    "confidence": h["confidence"],
                })
        return plan

    def summarize(self):
        if not self.hypotheses:
            return "No hypotheses generated."
        lines = ["## Hypothesis Engine Summary", f"Total hypotheses: {len(self.hypotheses)}"]
        confirmed = sum(1 for h in self.hypotheses if h.get("result") == "confirmed")
        refuted = sum(1 for h in self.hypotheses if h.get("result") == "refuted")
        untested = sum(1 for h in self.hypotheses if not h.get("tested"))
        lines.append(f"Confirmed: {confirmed} | Refuted: {refuted} | Untested: {untested}")
        lines.append("")
        for h in sorted(self.hypotheses, key=lambda x: -x.get("confidence", 0))[:10]:
            status = "✓" if h.get("result") == "confirmed" else "✗" if h.get("result") == "refuted" else "?"
            lines.append(f"{status} [{h['port']}] {h['hypothesis']} (conf={h.get('confidence', 0):.1f})")
        return "\n".join(lines)


class BayesianUpdater:
    def __init__(self):
        self.beliefs = defaultdict(lambda: {"prior": 0.5, "likelihood_true": 0.7, "likelihood_false": 0.3})

    def update(self, port, technique, success):
        belief = self.beliefs[f"{port}:{technique}"]
        prior = belief["prior"]
        p_true = belief["likelihood_true"]
        p_false = belief["likelihood_false"]

        if success:
            posterior = (p_true * prior) / ((p_true * prior) + (p_false * (1 - prior)))
        else:
            posterior = ((1 - p_true) * prior) / (((1 - p_true) * prior) + ((1 - p_false) * (1 - prior)))
        self.beliefs[f"{port}:{technique}"]["prior"] = posterior
        return posterior

    def probability(self, port, technique):
        return self.beliefs[f"{port}:{technique}"]["prior"]

    def top_beliefs(self, n=10):
        sorted_beliefs = sorted(self.beliefs.items(), key=lambda x: -x[1]["prior"])
        return [{"key": k, "probability": v["prior"]} for k, v in sorted_beliefs[:n]]
