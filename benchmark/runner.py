import json
import time
import subprocess
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict


@dataclass
class BenchmarkResult:
    challenge: str
    success: bool
    duration_seconds: float
    cost_estimate: float
    commands_run: int
    findings_count: int
    errors: list[str] = field(default_factory=list)
    notes: str = ""
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


class BenchmarkHarness:
    def __init__(self):
        self.results: list[BenchmarkResult] = []
        self.results_file = Path.home() / ".shel" / "benchmark_results.json"
        self.results_file.parent.mkdir(parents=True, exist_ok=True)

    def run_challenge(self, challenge_name: str, target: str, prompt_file: Path) -> BenchmarkResult:
        prompt = prompt_file.read_text(encoding="utf-8") if prompt_file.exists() else f"Hack the target: {target}"
        errors = []
        commands_run = 0
        start = time.time()

        try:
            result = subprocess.run(
                ["python", "-m", "shel_cli", prompt],
                capture_output=True, text=True, timeout=300,
                cwd=str(Path(__file__).resolve().parent.parent),
            )
            if result.returncode != 0:
                errors.append(f"Exit code: {result.returncode}")
            commands_run = result.stdout.count("$ ")
        except subprocess.TimeoutExpired:
            errors.append("Timed out after 300s")
        except Exception as e:
            errors.append(str(e))

        duration = time.time() - start
        success = len(errors) == 0
        result = BenchmarkResult(
            challenge=challenge_name,
            success=success,
            duration_seconds=round(duration, 1),
            cost_estimate=round(duration * 0.0001, 4),
            commands_run=commands_run,
            findings_count=0,
            errors=errors,
        )
        self.results.append(result)
        self._save()
        return result

    def _save(self):
        data = [asdict(r) for r in self.results]
        self.results_file.write_text(json.dumps(data, indent=2))

    def load(self):
        if self.results_file.exists():
            data = json.loads(self.results_file.read_text())
            self.results = [BenchmarkResult(**d) for d in data]

    def summary(self) -> str:
        if not self.results:
            return "No benchmark results yet."
        total = len(self.results)
        successes = sum(1 for r in self.results if r.success)
        avg_duration = sum(r.duration_seconds for r in self.results) / total if total else 0
        avg_cost = sum(r.cost_estimate for r in self.results) / total if total else 0
        lines = [
            "## Benchmark Summary",
            f"Challenges: {total}",
            f"Success rate: {successes}/{total} ({successes/total*100:.0f}%)",
            f"Avg duration: {avg_duration:.1f}s",
            f"Avg cost: ${avg_cost:.4f}",
            "",
            "### Results",
        ]
        for r in self.results:
            status = "✓" if r.success else "✗"
            lines.append(f"  {status} {r.challenge} ({r.duration_seconds}s, ${r.cost_estimate:.4f})")
        return "\n".join(lines)
