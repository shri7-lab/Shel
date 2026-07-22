import os
import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".shel"
CONFIG_FILE = CONFIG_DIR / "config.json"
DEFAULT_CONFIG = {
    "provider": "claude",
    "api_key": "",
    "model": "claude-sonnet-4-20250514",
    "ollama_url": "http://localhost:11434",
    "ollama_model": "llama3.1",
    "max_tokens": 8192,
    "temperature": 0.3,
    "shell_allow": True,
    "shell_ask": True,
    "shell_deny_commands": ["rm -rf /", "dd if=", "mkfs", "format"],
}


def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    return dict(DEFAULT_CONFIG)


def save_config(config):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


def get_api_key():
    config = load_config()
    if config.get("provider") == "ollama":
        return "ollama"
    key = config.get("api_key") or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        print("[!] No Anthropic API key found.")
        print("    Set ANTHROPIC_API_KEY env var, or run: /set-key")
        print("    Or switch to local models: /use-local")
        raise SystemExit(1)
    return key
