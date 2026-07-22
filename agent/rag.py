import re
import json
from pathlib import Path
from collections import defaultdict

KNOWLEDGE_DIR = Path(__file__).resolve().parent.parent / "knowledge"
WRITEUP_DIR = Path.home() / ".shel" / "writeups"


class RAGEngine:
    def __init__(self):
        self.index: dict[str, list[dict]] = {}
        self._build_index()

    def _build_index(self):
        KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)
        WRITEUP_DIR.mkdir(parents=True, exist_ok=True)

        for path in KNOWLEDGE_DIR.glob("*.md"):
            content = path.read_text(encoding="utf-8")
            chunks = self._chunk_markdown(content, path.stem)
            for chunk in chunks:
                for token in self._tokenize(chunk["text"]):
                    self.index.setdefault(token, []).append(chunk)

        for path in WRITEUP_DIR.glob("*.md"):
            content = path.read_text(encoding="utf-8", errors="replace")
            chunks = self._chunk_markdown(content, f"writeup:{path.stem}")
            for chunk in chunks:
                for token in self._tokenize(chunk["text"]):
                    self.index.setdefault(token, []).append(chunk)

    def _chunk_markdown(self, text: str, source: str) -> list[dict]:
        chunks = []
        lines = text.split("\n")
        current_section = "general"
        current_chunk = []
        current_chunk_len = 0

        for line in lines:
            if line.startswith("# "):
                if current_chunk and current_chunk_len > 50:
                    chunks.append({
                        "text": "\n".join(current_chunk),
                        "source": source,
                        "section": current_section,
                    })
                current_chunk = [line]
                current_chunk_len = len(line)
                current_section = line.lstrip("# ").strip()
            elif line.startswith("## "):
                if current_chunk and current_chunk_len > 50:
                    chunks.append({
                        "text": "\n".join(current_chunk),
                        "source": source,
                        "section": current_section,
                    })
                current_chunk = [line]
                current_chunk_len = len(line)
                current_section = line.lstrip("# ").strip()
            else:
                current_chunk.append(line)
                current_chunk_len += len(line)

        if current_chunk and current_chunk_len > 30:
            chunks.append({
                "text": "\n".join(current_chunk),
                "source": source,
                "section": current_section,
            })

        return chunks

    def _tokenize(self, text: str) -> set[str]:
        text = text.lower()
        tokens = set(re.findall(r"[a-z0-9_\-+./]+", text))
        return {t for t in tokens if len(t) > 2}

    def query(self, query: str, top_k: int = 5) -> list[dict]:
        tokens = self._tokenize(query)
        scores = defaultdict(float)

        for token in tokens:
            for chunk in self.index.get(token, []):
                key = (chunk["source"], chunk["section"], chunk["text"][:80])
                scores[key] += 1

        ranked = sorted(scores.items(), key=lambda x: -x[1])
        results = []
        seen = set()

        for (source, section, _), score in ranked:
            dedup_key = (source, section)
            if dedup_key in seen:
                continue
            seen.add(dedup_key)
            full_text = None
            for chunk in self.index.get(list(self.index.keys())[0], []):
                pass
            results.append({
                "source": source,
                "section": section,
                "relevance": score,
            })
            if len(results) >= top_k:
                break

        return results

    def get_section(self, source: str, section: str) -> str:
        path = KNOWLEDGE_DIR / f"{source}.md"
        if not path.exists():
            wpath = WRITEUP_DIR / f"{source.replace('writeup:', '')}.md"
            if wpath.exists():
                path = wpath
            else:
                return ""
        content = path.read_text(encoding="utf-8", errors="replace")
        lines = content.split("\n")
        in_section = False
        result = []
        for line in lines:
            if line.startswith("# ") and section in line:
                in_section = True
            elif line.startswith("## ") and section in line:
                in_section = True
            elif line.startswith("# ") and not section in line:
                if in_section:
                    break
            elif line.startswith("## ") and not section in line:
                if in_section:
                    break
            if in_section:
                result.append(line)
        return "\n".join(result[:100])

    def store_writeup(self, title: str, content: str):
        WRITEUP_DIR.mkdir(parents=True, exist_ok=True)
        safe_name = re.sub(r"[^\w\s-]", "", title).strip()[:50]
        path = WRITEUP_DIR / f"{safe_name}.md"
        path.write_text(content, encoding="utf-8")
        chunks = self._chunk_markdown(content, f"writeup:{safe_name}")
        for chunk in chunks:
            for token in self._tokenize(chunk["text"]):
                self.index.setdefault(token, []).append(chunk)
        return str(path)
