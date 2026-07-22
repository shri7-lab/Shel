import subprocess
import shutil
import tempfile
from pathlib import Path


DOCKER_IMAGE = "shel-tools"
DOCKERFILE_CONTENT = """FROM kalilinux/kali-rolling:latest
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \\
    nmap hydra gobuster dirb wfuzz sqlmap nikto enum4linux \\
    smbclient ldapscripts dnsutils curl wget netcat-openbsd \\
    iproute2 python3-pip openssh-client whois dnsrecon \\
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --quiet pwntools requests beautifulsoup4
WORKDIR /workspace
"""


class DockerSandbox:
    def __init__(self):
        self.available = self._check_docker()

    def _check_docker(self):
        docker_path = shutil.which("docker")
        if not docker_path:
            return False
        try:
            subprocess.run(
                ["docker", "info"],
                capture_output=True, text=True, timeout=10,
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError, OSError):
            return False

    def build_image(self):
        if not self.available:
            return "Docker is not available."
        with tempfile.TemporaryDirectory() as tmpdir:
            dockerfile = Path(tmpdir) / "Dockerfile"
            dockerfile.write_text(DOCKERFILE_CONTENT)
            result = subprocess.run(
                ["docker", "build", "-t", DOCKER_IMAGE, tmpdir],
                capture_output=True, text=True, timeout=300,
            )
            if result.returncode != 0:
                return f"Build failed:\n{result.stderr}"
            return "Image built successfully with Kali tools (nmap, hydra, sqlmap, etc.)."

    def run_command(self, command: str, timeout: int = 120) -> str:
        if not self.available:
            return "Docker is not available. Install Docker Desktop and try again."

        cmd = [
            "docker", "run", "--rm",
            "-v", f"{Path.cwd()}:/workspace",
            DOCKER_IMAGE,
            "bash", "-c", command,
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            output = ""
            if result.stdout:
                output += result.stdout
            if result.stderr:
                output += f"\n[stderr]\n{result.stderr}"
            if result.returncode != 0:
                output += f"\n[exit code: {result.returncode}]"
            return output or "(no output)"
        except subprocess.TimeoutExpired:
            return f"Command timed out after {timeout}s."
        except Exception as e:
            return f"Docker error: {e}"

    def run_interactive(self, command: str) -> str:
        return self.run_command(command)
