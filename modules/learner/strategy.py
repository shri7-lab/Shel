import json
import random
import hashlib
from collections import defaultdict


class StateEncoder:
    def encode(self, ports=None, services=None, os_type=None, findings=None):
        features = {}
        if ports:
            features["port_count"] = min(len(ports), 20)
            features["has_web"] = 1 if any(p in (80, 443, 8080, 8443) for p in ports) else 0
            features["has_smb"] = 1 if any(p in (139, 445) for p in ports) else 0
            features["has_ssh"] = 1 if 22 in ports else 0
            features["has_ftp"] = 1 if 21 in ports else 0
            features["has_rdp"] = 1 if 3389 in ports else 0
            features["has_mssql"] = 1 if 1433 in ports else 0
            features["has_mysql"] = 1 if 3306 in ports else 0
            features["has_redis"] = 1 if 6379 in ports else 0
            features["has_mongo"] = 1 if 27017 in ports else 0
            features["has_ldap"] = 1 if 389 in ports else 0
            features["has_nfs"] = 1 if 2049 in ports else 0
            features["has_dns"] = 1 if 53 in ports else 0

        if services:
            svc_lower = [s.lower() for s in services if s]
            if "http" in " ".join(svc_lower) or "nginx" in " ".join(svc_lower) or "apache" in " ".join(svc_lower):
                features["has_http_service"] = 1
            if any("iis" in s for s in svc_lower):
                features["has_iis"] = 1
            if any("tomcat" in s for s in svc_lower):
                features["has_java"] = 1

        if os_type:
            os_lower = os_type.lower()
            if "windows" in os_lower:
                features["os_windows"] = 1
            elif "linux" in os_lower:
                features["os_linux"] = 1

        if findings:
            features["finding_count"] = min(len(findings), 10)
            has_creds = any("cred" in f.lower() for f in findings if isinstance(f, str))
            has_vuln = any("cve" in f.lower() or "vuln" in f.lower() for f in findings if isinstance(f, str))
            features["has_credentials"] = 1 if has_creds else 0
            features["has_vulnerability"] = 1 if has_vuln else 0

        return frozenset(features.items())

    def state_key(self, features):
        sorted_items = sorted(features)
        raw = json.dumps(sorted_items)
        return hashlib.md5(raw.encode()).hexdigest()[:16]


class QLearningSelector:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.rand = random.Random()
        self.history = []

    def select_action(self, state, available_actions):
        state_id = self._state_id(state)
        if not available_actions:
            return None
        if self.rand.random() < self.epsilon:
            return self.rand.choice(available_actions)
        q_values = {a: self.q_table[state_id][a] for a in available_actions}
        max_q = max(q_values.values()) if q_values else 0
        best = [a for a, q in q_values.items() if q == max_q]
        return self.rand.choice(best)

    def learn(self, state, action, reward, next_state, available_actions=None):
        state_id = self._state_id(state)
        next_id = self._state_id(next_state) if next_state is not None else state_id
        max_next_q = 0
        if available_actions:
            next_qs = [self.q_table[next_id][a] for a in available_actions]
            max_next_q = max(next_qs) if next_qs else 0
        current_q = self.q_table[state_id][action]
        td_target = reward + self.gamma * max_next_q
        td_error = td_target - current_q
        self.q_table[state_id][action] = current_q + self.alpha * td_error
        self.history.append({
            "state": state_id,
            "action": action,
            "reward": reward,
            "td_error": td_error,
        })

    def _state_id(self, state):
        if isinstance(state, frozenset):
            sorted_items = sorted(state)
            raw = json.dumps(sorted_items)
            return hashlib.md5(raw.encode()).hexdigest()[:16]
        return str(state)

    def best_action(self, state):
        state_id = self._state_id(state)
        if not self.q_table[state_id]:
            return None
        return max(self.q_table[state_id], key=self.q_table[state_id].get)

    def q_value(self, state, action):
        return self.q_table[self._state_id(state)][action]

    def adjust_epsilon(self, decay=0.995, min_epsilon=0.01):
        self.epsilon = max(min_epsilon, self.epsilon * decay)

    def export(self):
        return {
            "q_table": {k: dict(v) for k, v in self.q_table.items()},
            "alpha": self.alpha,
            "gamma": self.gamma,
            "epsilon": self.epsilon,
            "history_size": len(self.history),
        }


class RewardCalculator:
    REWARDS = {
        "foothold": 100.0,
        "credential": 80.0,
        "shell": 150.0,
        "privesc": 120.0,
        "cve_found": 60.0,
        "port_found": 10.0,
        "service_enum": 15.0,
        "web_vuln": 40.0,
        "file_read": 30.0,
        "lateral_move": 90.0,
        "exfil": 70.0,
        "failed_port": -5.0,
        "failed_exploit": -20.0,
        "failed_enum": -2.0,
        "timeout": -10.0,
        "detected": -50.0,
        "noop": -1.0,
    }

    @classmethod
    def calculate(cls, outcome_type, duration=None, attempts=1):
        base = cls.REWARDS.get(outcome_type, 0.0)
        if duration and duration > 0:
            time_penalty = -duration * 0.1
        else:
            time_penalty = 0
        attempt_bonus = max(0, (10 - attempts) * 2)
        return base + time_penalty + attempt_bonus

    @classmethod
    def from_finding(cls, finding_type, severity):
        severity_map = {"critical": 1.5, "high": 1.0, "medium": 0.5, "low": 0.2}
        mult = severity_map.get(severity, 0.1)
        base = cls.REWARDS.get(finding_type, 10.0) if finding_type in cls.REWARDS else 10.0
        return base * mult


class AdaptiveScheduler:
    def __init__(self, base_interval=1.0):
        self.base_interval = base_interval
        self.consecutive_failures = 0
        self.consecutive_successes = 0
        self.backoff_factor = 2.0

    def next_interval(self, success):
        if success:
            self.consecutive_successes += 1
            self.consecutive_failures = 0
            return max(self.base_interval * 0.5, self.base_interval - self.consecutive_successes * 0.1)
        self.consecutive_failures += 1
        self.consecutive_successes = 0
        return self.base_interval * (self.backoff_factor ** self.consecutive_failures)

    def should_retry(self, max_retries=3):
        return self.consecutive_failures < max_retries

    def reset(self):
        self.consecutive_failures = 0
        self.consecutive_successes = 0
