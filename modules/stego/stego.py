import base64
import random
import string
import struct
import hashlib


class StegoEngine:
    def __init__(self, seed=None):
        self.rand = random.Random(seed)
        self.bit_order = "lsb"

    MAGIC = "0100101101100011011001010111100101010011"  # "KeyS" in binary

    TERMINATOR = "11111111"

    def encode_text_whitespace(self, payload, cover_text):
        header = self.MAGIC + "0010110110101111"
        binary = header + self._to_binary(payload) + self.TERMINATOR
        spaces = [i for i, ch in enumerate(cover_text) if ch in (" ", "\t")]
        if len(binary) > len(spaces):
            return None, f"Need {len(binary)} whitespace positions, only {len(spaces)} available"

        result = list(cover_text)
        for bit_idx, pos in enumerate(spaces):
            if bit_idx < len(binary):
                result[pos] = "\t" if binary[bit_idx] == "1" else " "
        return "".join(result), len(binary) - len(self.TERMINATOR)

    def decode_text_whitespace(self, stego_text):
        binary = ""
        for ch in stego_text:
            if ch == "\t":
                binary += "1"
            elif ch == " ":
                binary += "0"
        sep_start = binary.find("0010110110101111")
        if sep_start == -1:
            return self._from_binary(binary)
        payload_start = sep_start + 16
        term_end = binary.find(self.TERMINATOR, payload_start)
        if term_end == -1:
            return self._from_binary(binary[payload_start:])
        return self._from_binary(binary[payload_start:term_end])

    def encode_text_homoglyph(self, payload, cover_text):
        binary = self._to_binary(payload)
        homoglyphs = {"a": ["а"], "e": ["е"], "o": ["о"], "c": ["с"],
                       "p": ["р"], "x": ["х"], "y": ["у"], "i": ["і"],
                       "m": ["м"], "n": ["п"], "t": ["т"], "b": ["ь"],
                       "k": ["к"], "h": ["н"], "u": ["и"]}
        candidates = [(i, ch) for i, ch in enumerate(cover_text.lower()) if ch in homoglyphs]
        if len(binary) > len(candidates):
            return None, f"Need {len(binary)} homoglyph positions, only {len(candidates)} available"

        result = list(cover_text)
        for bit_idx, (pos, ch) in enumerate(candidates[:len(binary)]):
            if binary[bit_idx] == "1":
                result[pos] = self.rand.choice(homoglyphs[ch])
        return "".join(result), len(binary)

    def decode_text_homoglyph(self, stego_text):
        homoglyph_map = {}
        for latin, cyrillics in {"a": ["а"], "e": ["е"], "o": ["о"], "c": ["с"],
                                  "p": ["р"], "x": ["х"], "y": ["у"], "i": ["і"],
                                  "m": ["м"], "n": ["п"], "t": ["т"], "b": ["ь"],
                                  "k": ["к"], "h": ["н"], "u": ["и"]}.items():
            for cyr in cyrillics:
                homoglyph_map[cyr] = latin

        binary = ""
        for char in stego_text.lower():
            if char in homoglyph_map:
                binary += "1"  # replaced
            else:
                pass
        return self._from_binary(binary)

    def encode_pixel_lsb(self, payload, pixel_data, channels=3):
        binary = self._to_binary(payload) + "11111111"
        data_len = len(binary)
        if data_len > len(pixel_data) * channels:
            return None, f"Payload too large: need {data_len} bits, pixel capacity {len(pixel_data) * channels}"

        flat = bytearray(pixel_data)
        for i in range(data_len):
            flat[i] = (flat[i] & 0xFE) | int(binary[i])
        return bytes(flat), data_len

    def decode_pixel_lsb(self, stego_data, channels=3):
        flat = bytearray(stego_data) if isinstance(stego_data, bytes) else stego_data
        binary = ""
        for byte in flat:
            binary += str(byte & 1)
            if binary[-8:] == "11111111":
                return self._from_binary(binary[:-8])
        return self._from_binary(binary)

    def encode_audio_lsb(self, payload, audio_samples, bits_per_sample=16):
        binary = self._to_binary(payload) + "11111111"
        if len(binary) > len(audio_samples):
            return None, f"Payload too large: need {len(binary)} bits, {len(audio_samples)} available"

        encoded = list(audio_samples)
        for i in range(len(binary)):
            encoded[i] = (encoded[i] & ~1) | int(binary[i])
        return encoded, len(binary)

    def decode_audio_lsb(self, stego_samples):
        binary = ""
        for sample in stego_samples:
            binary += str(sample & 1)
            if binary[-8:] == "11111111":
                return self._from_binary(binary[:-8])
        return self._from_binary(binary)

    def encode_http_header(self, payload):
        encoded = base64.b64encode(payload.encode() if isinstance(payload, str) else payload).decode()
        headers = {
            "X-Cache": f"HIT from proxy-{self.rand.randint(100,999)}",
            "X-Request-ID": f"req-{hashlib.md5(encoded.encode()).hexdigest()[:16]}",
            "X-Content-Duration": f"{self.rand.randint(100,9999)}",
            "X-Powered-By": f"Express/{self.rand.randint(4,8)}.{self.rand.randint(0,9)}.{self.rand.randint(0,9)}",
            "X-Runtime": f"{self.rand.random() * 2:.6f}",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "X-Forwarded-For": f"{self.rand.randint(1,255)}.{self.rand.randint(1,255)}.{self.rand.randint(1,255)}.{self.rand.randint(1,255)}",
        }
        header_name = self.rand.choice(list(headers.keys()))
        return {header_name: headers[header_name], "X-Stego": encoded}

    def decode_http_header(self, headers):
        encoded = headers.get("X-Stego", "")
        if not encoded:
            return None
        try:
            return base64.b64decode(encoded).decode()
        except Exception:
            return None

    def encode_dns_query(self, payload, domain="example.com"):
        encoded = base64.b32encode(payload.encode() if isinstance(payload, str) else payload).decode().lower().rstrip("=")
        chunk_size = 20
        queries = []
        for i in range(0, len(encoded), chunk_size):
            chunk = encoded[i:i+chunk_size]
            subdomain = f"{chunk}.{self.rand.choice(['stg','cdn','api','cdn','static'])}.{domain}"
            queries.append(subdomain)
        return queries

    def decode_dns_query(self, queries, domain="example.com"):
        combined = ""
        for q in queries:
            for suffix in [f".stg.{domain}", f".cdn.{domain}", f".api.{domain}", f".static.{domain}"]:
                if suffix in q:
                    combined += q.split(".")[0]
                    break
        padding = 8 - (len(combined) % 8) if len(combined) % 8 else 0
        combined += "=" * padding
        try:
            return base64.b32decode(combined.upper()).decode(errors="replace")
        except Exception:
            return combined

    def encode_image_metadata(self, payload, existing_metadata=None):
        fields = {
            "Artist": payload[:255] if len(payload) <= 255 else base64.b64encode(payload.encode()).decode()[:255],
            "Copyright": f"© {self.rand.randint(2000, 2026)} {hashlib.md5(payload.encode()).hexdigest()[:16]}",
            "Description": f"Generated by {self.rand.choice(['Adobe','Canon','Nikon','Phase One'])} {self.rand.choice(['Photoshop','Capture One','Lightroom'])}",
            "Comment": f"PLIST:{base64.b64encode(payload.encode()).decode()[:200]}",
        }
        chosen = self.rand.choice(list(fields.keys()))
        return {chosen: fields[chosen]}

    def decode_image_metadata(self, metadata):
        for key, value in metadata.items():
            if key == "Artist" and value:
                try:
                    return base64.b64decode(value).decode(errors="replace")
                except Exception:
                    return value
            if key == "Comment" and value.startswith("PLIST:"):
                try:
                    return base64.b64decode(value[6:]).decode(errors="replace")
                except Exception:
                    return value[6:]
        return None

    def encode_tcp_timestamp(self, payload, timestamps=None):
        binary = self._to_binary(payload) + "11111111"
        if timestamps is None:
            timestamps = [self.rand.randint(100000, 999999) for _ in range(len(binary))]
        encoded = []
        for i, ts in enumerate(timestamps):
            if i < len(binary):
                encoded.append((ts & ~1) | int(binary[i]))
            else:
                encoded.append(ts)
        return encoded, len(binary)

    def decode_tcp_timestamp(self, timestamps):
        binary = ""
        for ts in timestamps:
            binary += str(ts & 1)
            if binary[-8:] == "11111111":
                return self._from_binary(binary[:-8])
        return self._from_binary(binary)

    def random_cover_image(self, width=64, height=64):
        pixels = bytearray(width * height * 3)
        for i in range(len(pixels)):
            pixels[i] = self.rand.randint(0, 255)
        return pixels, width, height

    def random_cover_text(self, word_count=50):
        words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "it",
                  "for", "not", "on", "with", "he", "as", "you", "do", "at", "this",
                  "but", "his", "by", "from", "they", "we", "say", "her", "she", "or",
                  "an", "will", "my", "one", "all", "would", "there", "their", "what",
                  "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
                  "when", "make", "can", "like", "time", "no", "just", "him", "know",
                  "take", "people", "into", "year", "your", "good", "some", "could",
                  "them", "see", "other", "than", "then", "now", "look", "only", "come",
                  "its", "over", "think", "also", "back", "after", "use", "two", "how",
                  "our", "work", "first", "well", "way", "even", "new", "want", "because",
                  "any", "these", "give", "day", "most", "us"]
        return " ".join(self.rand.choice(words) for _ in range(word_count))

    def all_techniques(self):
        return {
            "text_whitespace": "Hide data in whitespace (space=0, tab=1) of arbitrary text",
            "text_homoglyph": "Replace Latin chars with Cyrillic homoglyphs (visually identical)",
            "pixel_lsb": "Least Significant Bit embedding in pixel data (BMP/PNG)",
            "audio_lsb": "LSB embedding in raw audio samples (WAV)",
            "http_header": "Encode payload as X-Stego HTTP header value",
            "dns_query": "Split payload across DNS subdomain queries (base32 encoded)",
            "image_metadata": "Bury payload in EXIF metadata fields (Artist, Comment)",
            "tcp_timestamp": "LSB in TCP timestamp values",
        }

    def _to_binary(self, data):
        if isinstance(data, str):
            data = data.encode("utf-8")
        return "".join(format(b, "08b") for b in data)

    def _from_binary(self, binary):
        chars = []
        for i in range(0, len(binary) - 7, 8):
            byte = int(binary[i:i+8], 2)
            chars.append(byte)
        return bytes(chars).decode("utf-8", errors="replace")
