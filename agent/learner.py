import sqlite3
import json
import time
import random
from pathlib import Path
from datetime import datetime


DB_PATH = Path.home() / ".shel" / "learner.db"


class Learner:
    def __init__(self, db_path=None):
        self.db_path = Path(db_path or DB_PATH)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self.db_path))
        self._conn.row_factory = sqlite3.Row
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self._init_db()
        self.q_selector = None
        self.skill_library = None
        self.hypothesis_gen = None
        self.bayesian = None

    def init_advanced(self):
        from modules.learner.strategy import QLearningSelector, StateEncoder, RewardCalculator, AdaptiveScheduler
        from modules.learner.skills import SkillLibrary, ChainBuilder, SkillExecutor
        from modules.learner.hypothesis import HypothesisGenerator, BayesianUpdater
        self.q_selector = QLearningSelector()
        self.state_encoder = StateEncoder()
        self.reward_calc = RewardCalculator()
        self.scheduler = AdaptiveScheduler()
        self.skill_library = SkillLibrary()
        self.chain_builder = ChainBuilder()
        self.hypothesis_gen = HypothesisGenerator()
        self.bayesian = BayesianUpdater()
        self.skill_executor = None
        return self

    def set_tool_runner(self, tool_runner):
        if self.skill_library:
            from modules.learner.skills import SkillExecutor
            self.skill_executor = SkillExecutor(self.skill_library, tool_runner)

    def _init_db(self):
        self._conn.executescript("""
            CREATE TABLE IF NOT EXISTS experiences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT,
                target_os TEXT,
                port INTEGER,
                service TEXT,
                tool TEXT,
                technique TEXT,
                success INTEGER,
                duration REAL,
                output_preview TEXT,
                created_at TEXT,
                session_id TEXT
            );
            CREATE INDEX IF NOT EXISTS idx_exp_port ON experiences(port);
            CREATE INDEX IF NOT EXISTS idx_exp_tool ON experiences(tool);
            CREATE INDEX IF NOT EXISTS idx_exp_technique ON experiences(technique);
            CREATE INDEX IF NOT EXISTS idx_exp_os ON experiences(target_os);

            CREATE TABLE IF NOT EXISTS technique_rankings (
                technique_key TEXT PRIMARY KEY,
                port INTEGER,
                service TEXT,
                target_os TEXT,
                tool TEXT,
                technique TEXT,
                success_count INTEGER DEFAULT 0,
                fail_count INTEGER DEFAULT 0,
                avg_duration REAL DEFAULT 0,
                last_used TEXT,
                consecutive_fails INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                started_at TEXT,
                ended_at TEXT,
                total_actions INTEGER DEFAULT 0,
                successful_actions INTEGER DEFAULT 0
            );
        """)
        self._conn.commit()
        self._conn.execute(
            "INSERT OR IGNORE INTO sessions (id, started_at) VALUES (?, ?)",
            (self.session_id, datetime.now().isoformat()),
        )
        self._conn.commit()

    def record(self, target, target_os, port, service, tool, technique, success, duration, output=""):
        now = datetime.now().isoformat()
        self._conn.execute(
            """INSERT INTO experiences
               (target, target_os, port, service, tool, technique, success, duration, output_preview, created_at, session_id)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (target, target_os or "", port or 0, service or "",
             tool, technique, 1 if success else 0, duration,
             (output or "")[:500], now, self.session_id),
        )

        technique_key = f"{port}:{tool}:{technique}:{target_os or 'any'}"
        existing = self._conn.execute(
            "SELECT * FROM technique_rankings WHERE technique_key = ?", (technique_key,)
        ).fetchone()

        if existing:
            sc = existing["success_count"] + (1 if success else 0)
            fc = existing["fail_count"] + (0 if success else 1)
            total = sc + fc
            avg_dur = ((existing["avg_duration"] * (total - 1)) + duration) / total if total > 0 else duration
            consec = (existing["consecutive_fails"] + 1) if not success else 0
            self._conn.execute(
                """UPDATE technique_rankings
                   SET success_count=?, fail_count=?, avg_duration=?, last_used=?, consecutive_fails=?
                   WHERE technique_key=?""",
                (sc, fc, avg_dur, now, consec, technique_key),
            )
        else:
            self._conn.execute(
                """INSERT INTO technique_rankings
                   (technique_key, port, service, target_os, tool, technique, success_count, fail_count, avg_duration, last_used, consecutive_fails)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (technique_key, port, service, target_os or "", tool, technique,
                 1 if success else 0, 0 if success else 1, duration, now, 0 if success else 1),
            )

        self._conn.commit()

    def best_technique(self, port, target_os=None):
        rows = self._conn.execute(
            """SELECT tool, technique, success_count, fail_count,
                      CAST(success_count AS REAL) / MAX((success_count + fail_count), 1) AS success_rate
               FROM technique_rankings
               WHERE port = ? AND (? IS NULL OR target_os = ?)
               ORDER BY success_rate DESC, (success_count + fail_count) DESC
               LIMIT 5""",
            (port, target_os, target_os),
        ).fetchall()
        return [dict(r) for r in rows]

    def should_skip(self, tool, technique, port, target_os=None):
        key = f"{port}:{tool}:{technique}:{target_os or 'any'}"
        row = self._conn.execute(
            "SELECT consecutive_fails, fail_count FROM technique_rankings WHERE technique_key = ?",
            (key,),
        ).fetchone()
        if row and row["consecutive_fails"] >= 3:
            return True
        if row and row["fail_count"] >= 5 and row["consecutive_fails"] >= 2:
            return True
        return False

    def best_tools_for_port(self, port, target_os=None, top_n=3):
        rows = self._conn.execute(
            """SELECT tool, technique, success_rate, sample_size FROM (
                   SELECT tool, technique,
                          CAST(SUM(success) AS REAL) / MAX(CAST(COUNT(*) AS REAL), 1) AS success_rate,
                          COUNT(*) AS sample_size
                   FROM experiences
                   WHERE port = ? AND (? IS NULL OR target_os = target_os)
                   GROUP BY tool, technique
               ) ORDER BY success_rate DESC, sample_size DESC
               LIMIT ?""",
            (port, target_os, top_n),
        ).fetchall()
        return [dict(r) for r in rows]

    def failure_count(self, tool, technique, port, target_os=None):
        key = f"{port}:{tool}:{technique}:{target_os or 'any'}"
        row = self._conn.execute(
            "SELECT fail_count FROM technique_rankings WHERE technique_key = ?", (key,)
        ).fetchone()
        return row["fail_count"] if row else 0

    def summary(self):
        rows = self._conn.execute(
            """SELECT technique_key, port, tool, technique, success_count, fail_count,
                      CAST(success_count AS REAL) / MAX((success_count + fail_count), 1) AS success_rate
               FROM technique_rankings
               ORDER BY (success_count + fail_count) DESC
               LIMIT 20"""
        ).fetchall()
        return [dict(r) for r in rows]

    def total_experiences(self):
        row = self._conn.execute("SELECT COUNT(*) AS c FROM experiences").fetchone()
        return row["c"] if row else 0

    def session_stats(self):
        row = self._conn.execute(
            "SELECT COUNT(*) AS total, SUM(success) AS successes FROM experiences WHERE session_id = ?",
            (self.session_id,),
        ).fetchone()
        return {"total": row["total"], "successes": row["successes"] or 0} if row else {"total": 0, "successes": 0}

    def advanced_record(self, target, port, service, tool, technique, success, duration=0,
                        ports=None, services=None, os_type=None, findings=None):
        self.record(target, os_type, port, service, tool, technique, success, duration)
        if not self.q_selector:
            return
        state = self.state_encoder.encode(ports, services, os_type, findings)
        action = f"{tool}:{technique}"
        reward = self.reward_calc.calculate(
            "failed_exploit" if not success else "foothold",
            duration,
        )
        next_state = self.state_encoder.encode(ports, services, os_type, findings)
        self.q_selector.learn(state, action, reward, next_state)
        if self.bayesian:
            self.bayesian.update(port, technique, success)

    def q_select(self, ports=None, services=None, os_type=None, findings=None, available=None):
        if not self.q_selector:
            self.init_advanced()
        state = self.state_encoder.encode(ports, services, os_type, findings)
        return self.q_selector.select_action(state, available or [])

    def q_best(self, ports=None, services=None, os_type=None, findings=None):
        if not self.q_selector:
            return None
        state = self.state_encoder.encode(ports, services, os_type, findings)
        return self.q_selector.best_action(state)

    def skill_save_chain(self, steps, target_info=None):
        if not self.skill_library:
            self.init_advanced()
        return self.skill_library.add_from_chain(steps, target_info)

    def skill_find(self, ports=None, os_type=None, tags=None):
        if not self.skill_library:
            return []
        return self.skill_library.find_matching(ports, os_type, tags)

    def skill_execute(self, skill_id, target):
        if not self.skill_executor:
            return {"status": "error", "message": "Skill executor not initialized. Call set_tool_runner()"}
        return self.skill_executor.execute(skill_id, target)

    def skill_summary(self):
        if not self.skill_library:
            return "Advanced learning not initialized. Run /learn init first."
        return self.skill_library.summary()

    def hypothesis_generate(self, ports=None, os_hint=None):
        if not self.hypothesis_gen:
            self.init_advanced()
        return self.hypothesis_gen.generate_hypotheses(ports or [], os_hint)

    def hypothesis_attack_plan(self, ports=None, os_hint=None):
        if not self.hypothesis_gen:
            self.init_advanced()
        return self.hypothesis_gen.generate_attack_plan(ports or [], os_hint)

    def hypothesis_summary(self):
        if not self.hypothesis_gen:
            return "Hypothesis engine not initialized."
        return self.hypothesis_gen.summarize()

    def hypothesis_test(self, hypothesis, result):
        if not self.hypothesis_gen:
            return False
        return self.hypothesis_gen.test_hypothesis(hypothesis, result)

    def bayesian_probability(self, port, technique):
        if not self.bayesian:
            return 0.5
        return self.bayesian.probability(port, technique)

    def bayesian_top(self, n=10):
        if not self.bayesian:
            return []
        return self.bayesian.top_beliefs(n)

    def advanced_summary(self):
        if not self.q_selector:
            return "Advanced learning not initialized. Run /learn init"
        parts = [f"## Advanced Learner Summary",
                 f"Q-Table size: {len(self.q_selector.q_table)} states",
                 f"Epsilon: {self.q_selector.epsilon:.3f}",
                 f"Bayesian beliefs: {len(self.bayesian.beliefs) if self.bayesian else 0}",
                 f"Skills: {len(self.skill_library.skills) if self.skill_library else 0}",
                 f"Hypotheses: {len(self.hypothesis_gen.hypotheses) if self.hypothesis_gen else 0}"]
        if self.bayesian:
            top = self.bayesian_top(5)
            if top:
                parts.append("\n### Top Bayesian Probabilities")
                for t in top:
                    parts.append(f"- {t['key']}: {t['probability']:.2f}")
        if self.q_selector:
            export = self.q_selector.export()
            if export["history_size"] > 0:
                parts.append(f"\n### Q-Learning History")
                last = export["history"][-5:] if len(export["history"]) > 5 else export["history"]
            parts.append(f"\n### Best Action by State")
            shown = 0
            for state_id, actions in sorted(export["q_table"].items(), key=lambda x: -len(x[1]))[:5]:
                if actions:
                    best = max(actions, key=actions.get)
                    parts.append(f"- State {state_id}: {best} (Q={actions[best]:.2f})")
                    shown += 1
        return "\n".join(parts)

    def close(self):
        self._conn.execute(
            "UPDATE sessions SET ended_at=?, total_actions=?, successful_actions=? WHERE id=?",
            (datetime.now().isoformat(),
             self.session_stats()["total"],
             self.session_stats()["successes"],
             self.session_id),
        )
        self._conn.commit()
        self._conn.close()

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass
