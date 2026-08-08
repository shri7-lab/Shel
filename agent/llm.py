import json
import urllib.request
from config.settings import load_config, get_api_key


class LLM:
    def __init__(self):
        cfg = load_config()
        self.provider = cfg.get("provider", "claude")
        self.model = cfg["model"]
        self.max_tokens = cfg["max_tokens"]
        self.temperature = cfg["temperature"]

        if self.provider == "claude":
            self.api_key = get_api_key()
            from anthropic import Anthropic
            self.client = Anthropic(api_key=self.api_key)
        elif self.provider == "ollama":
            self.base_url = cfg.get("ollama_url", "http://localhost:11434")
            self.client = None

    def send(self, system, messages, tools):
        if self.provider == "claude":
            return self._send_claude(system, messages, tools)
        elif self.provider == "ollama":
            return self._send_ollama(system, messages, tools)
        raise ValueError(f"Unknown provider: {self.provider}")

    def _send_claude(self, system, messages, tools):
        return self.client.beta.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system,
            messages=messages,
            tools=tools,
        )

    def _send_ollama(self, system, messages, tools):
        formatted = self._format_for_ollama(system, messages, tools)
        data = json.dumps({
            "model": self.model,
            "messages": formatted,
            "stream": False,
            "options": {
                "num_predict": self.max_tokens,
                "temperature": self.temperature,
            },
        }).encode()
        req = urllib.request.Request(
            f"{self.base_url}/api/chat",
            data=data,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=900) as resp:
            result = json.loads(resp.read())

        return OllamaResponse(result, tools)

    def _block_text(self, c):
        if isinstance(c, dict):
            return c.get("text", "")
        return getattr(c, "text", "")

    def _format_for_ollama(self, system, messages, tools):
        formatted = [{"role": "system", "content": system}]
        tool_descriptions = []
        for t in tools:
            params = t.get("input_schema", {}).get("properties", {})
            param_str = ", ".join(
                f"{k}: {v.get('description', k)}" for k, v in params.items()
            )
            tool_descriptions.append(
                f"- {t['name']}({param_str}): {t['description']}"
            )
        if tool_descriptions:
            formatted[0]["content"] += (
                "\n\n## Available Tools\n" + "\n".join(tool_descriptions)
            )

        for msg in messages:
            if msg["role"] == "user":
                content = msg.get("content", "")
                if isinstance(content, list):
                    text_parts = [
                        self._block_text(c) for c in content
                    ]
                    content = "\n".join(text_parts)
                formatted.append({"role": "user", "content": content})
            elif msg["role"] == "assistant":
                content = msg.get("content", "")
                if isinstance(content, list):
                    text_parts = [self._block_text(c) for c in content]
                    content = "\n".join(text_parts)
                formatted.append({"role": "assistant", "content": content})

        return formatted

    def send_with_tools(self, system, messages, tools, tool_runner):
        if self.provider == "claude":
            return self._send_with_tools_claude(system, messages, tools, tool_runner)
        elif self.provider == "ollama":
            return self._send_with_tools_ollama(system, messages, tools, tool_runner)
        raise ValueError(f"Unknown provider: {self.provider}")

    def _send_with_tools_claude(self, system, messages, tools, tool_runner):
        while True:
            resp = self._send_claude(system, messages, tools)
            messages.append({"role": "assistant", "content": resp.content})

            stop_reason = resp.stop_reason
            if stop_reason == "end_turn":
                break

            if stop_reason == "tool_use":
                for block in resp.content:
                    if block.type == "tool_use":
                        result = tool_runner.run(block.name, block.input)
                        messages.append({
                            "role": "user",
                            "content": [{
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": str(result),
                            }],
                        })
                continue

            break
        return resp

    def _send_with_tools_ollama(self, system, messages, tools, tool_runner):
        resp = self._send_ollama(system, messages, tools)
        messages.append({"role": "assistant", "content": resp.content})
        return resp


class OllamaResponse:
    class ContentBlock:
        def __init__(self, text):
            self.type = "text"
            self.text = text

    def __init__(self, raw, tools):
        self.content = []
        self.stop_reason = "end_turn"

        if "message" in raw and "content" in raw["message"]:
            text = raw["message"]["content"]
            if text:
                text = text.strip()
                text = text.replace("```tool_code", "```bash")
                self.content.append(self.ContentBlock(text))
