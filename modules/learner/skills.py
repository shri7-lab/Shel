import json
import hashlib
import time
from collections import defaultdict


class SkillLibrary:
    def __init__(self, storage_path=None):
        self.skills = {}
        self.usage_stats = defaultdict(lambda: {"uses": 0, "successes": 0, "failures": 0})

    def add_skill(self, name, steps, target_ports=None, target_os=None, prerequisites=None, tags=None):
        skill_id = hashlib.md5(name.encode()).hexdigest()[:12]
        skill = {
            "id": skill_id,
            "name": name,
            "steps": steps,
            "target_ports": target_ports or [],
            "target_os": target_os,
            "prerequisites": prerequisites or [],
            "tags": tags or [],
            "created": time.time(),
            "last_used": 0,
            "success_count": 0,
            "fail_count": 0,
            "avg_duration": 0.0,
        }
        self.skills[skill_id] = skill
        return skill_id

    def add_from_chain(self, chain_steps, target_info=None):
        if not chain_steps:
            return None
        first = chain_steps[0]
        desc = first.get("objective", "auto") if isinstance(first, dict) else str(first)
        ports = []
        os_type = None
        if target_info:
            ports = target_info.get("ports", [])
            os_type = target_info.get("os")
        name = f"chain_{desc[:20]}_{int(time.time())}"
        return self.add_skill(name, chain_steps, ports, os_type)

    def find_matching(self, ports=None, os_type=None, tags=None):
        matches = []
        for skill in self.skills.values():
            score = 0
            if ports and skill["target_ports"]:
                shared = set(ports) & set(skill["target_ports"])
                if shared:
                    score += len(shared) * 10
                else:
                    continue
            if os_type and skill["target_os"]:
                if os_type.lower() == skill["target_os"].lower():
                    score += 20
                else:
                    continue
            if tags and skill["tags"]:
                shared_tags = set(tags) & set(skill["tags"])
                score += len(shared_tags) * 5
            if score > 0 or not (ports or os_type or tags):
                success_rate = 0
                total = skill["success_count"] + skill["fail_count"]
                if total > 0:
                    success_rate = skill["success_count"] / total
                matches.append({**skill, "match_score": score, "success_rate": success_rate})
        return sorted(matches, key=lambda x: -x["match_score"])

    def record_use(self, skill_id, success=True, duration=0):
        if skill_id not in self.skills:
            return
        skill = self.skills[skill_id]
        skill["last_used"] = time.time()
        total = skill["success_count"] + skill["fail_count"]
        skill["avg_duration"] = ((skill["avg_duration"] * total) + duration) / (total + 1)
        if success:
            skill["success_count"] += 1
        else:
            skill["fail_count"] += 1
        stat = self.usage_stats[skill_id]
        stat["uses"] += 1
        if success:
            stat["successes"] += 1
        else:
            stat["failures"] += 1

    def generalize(self, skill_id, new_ports=None, new_os=None):
        if skill_id not in self.skills:
            return None
        original = self.skills[skill_id]
        generalized = {**original}
        gen_id = hashlib.md5(f"{skill_id}_gen_{int(time.time())}".encode()).hexdigest()[:12]
        generalized["id"] = gen_id
        generalized["parent_id"] = skill_id
        generalized["generalization_count"] = original.get("generalization_count", 0) + 1
        if new_ports:
            generalized["target_ports"] = list(set(original["target_ports"] + new_ports))
        if new_os:
            generalized["target_os"] = new_os
        self.skills[gen_id] = generalized
        return gen_id

    def summary(self):
        if not self.skills:
            return "No skills recorded."
        lines = [f"## Skill Library ({len(self.skills)} skills)"]
        for sid, skill in sorted(self.skills.items(), key=lambda x: -x[1]["success_count"]):
            total = skill["success_count"] + skill["fail_count"]
            rate = f"{skill['success_count']/total*100:.0f}%" if total > 0 else "N/A"
            ports = f"ports={skill['target_ports']}" if skill["target_ports"] else "any"
            lines.append(f"- **{skill['name']}** ({sid}) | {rate} | {ports} | steps={len(skill['steps'])}")
        return "\n".join(lines)


class ChainBuilder:
    def __init__(self):
        self.chains = []

    def build(self, objective, target_data):
        chains = {
            "service_enum": self._enum_chain,
            "exploit": self._exploit_chain,
            "privesc": self._privesc_chain,
            "lateral": self._lateral_chain,
            "full": self._full_chain,
        }
        builder = chains.get(objective, self._enum_chain)
        return builder(target_data)

    def _enum_chain(self, target):
        steps = [
            {"action": "port_scan", "params": {"target": target, "ports": "top1000"}, "objective": "discover_ports"},
            {"action": "service_scan", "params": {"target": target}, "objective": "identify_services"},
            {"action": "os_detect", "params": {"target": target}, "objective": "os_fingerprint"},
        ]
        return steps

    def _exploit_chain(self, target):
        return [
            {"action": "vuln_scan", "params": {"target": target}, "objective": "find_vulnerabilities"},
            {"action": "search_exploit", "params": {"target": target}, "objective": "find_exploit_code"},
            {"action": "run_exploit", "params": {"target": target}, "objective": "gain_foothold"},
            {"action": "verify_access", "params": {"target": target}, "objective": "confirm_foothold"},
        ]

    def _privesc_chain(self, target):
        return [
            {"action": "enum_users", "params": {"target": target}, "objective": "list_users"},
            {"action": "check_suid", "params": {"target": target}, "objective": "find_suid_binaries"},
            {"action": "check_kernel", "params": {"target": target}, "objective": "kernel_version_check"},
            {"action": "check_configs", "params": {"target": target}, "objective": "find_misconfigs"},
        ]

    def _lateral_chain(self, target):
        return [
            {"action": "enum_shares", "params": {"target": target}, "objective": "find_network_shares"},
            {"action": "dump_creds", "params": {"target": target}, "objective": "collect_credentials"},
            {"action": "try_creds", "params": {"target": target}, "objective": "credential_stuffing"},
        ]

    def _full_chain(self, target):
        return self._enum_chain(target) + self._exploit_chain(target) + self._privesc_chain(target)


class SkillExecutor:
    def __init__(self, skill_library, tool_runner=None):
        self.library = skill_library
        self.tool_runner = tool_runner

    def execute(self, skill_id, target, adapt=True):
        if skill_id not in self.library.skills:
            return {"status": "error", "message": f"Skill {skill_id} not found"}
        skill = self.library.skills[skill_id]
        results = []
        total_duration = 0
        all_success = True

        for step in skill["steps"]:
            action = step.get("action")
            params = {**step.get("params", {}), "target": target}
            if self.tool_runner and action:
                result = self.tool_runner.run(action, params)
            else:
                result = f"[simulated] {action} on {target}"
            success = "Error" not in str(result)[:10]
            duration = 1.0
            total_duration += duration
            results.append({"step": action, "success": success, "result": str(result)[:200]})
            if not success:
                all_success = False
                if not adapt:
                    break

        self.library.record_use(skill_id, all_success, total_duration)
        return {"status": "complete", "skill": skill["name"], "all_success": all_success,
                "steps": len(skill["steps"]), "completed": len(results), "results": results}
