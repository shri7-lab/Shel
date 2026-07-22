import random
import string


class TargetProfile:
    def __init__(self, name=None, role=None, organization=None, email=None, department=None):
        self.name = name
        self.role = role
        self.organization = organization
        self.email = email
        self.department = department
        self.phone = None
        self.linkedin = None
        self.manager_name = None
        self.manager_email = None
        self.team_members = []
        self.interests = []
        self.communication_style = "formal"
        self.language = "en"
        self.timezone = "UTC"
        self.trusted_platforms = ["email"]
        self.pain_points = []
        self.software_used = []
        self.recent_projects = []

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}

    def enrich_from_osint(self, osint_data):
        if isinstance(osint_data, dict):
            for key, value in osint_data.items():
                if hasattr(self, key) and value:
                    setattr(self, key, value)


class Persona:
    def __init__(self, name=None, role=None, organization=None):
        self.name = name or self._generate_name()
        self.role = role or self._generate_role()
        self.organization = organization or "Unknown Corp"
        self.email = f"{self.name.lower().replace(' ', '.')}@{self.organization.lower().replace(' ', '')}.com"
        self.phone = f"+1-555-{random.randint(100,999)}-{random.randint(1000,9999)}"
        self.personality = random.choice(["assertive", "friendly", "urgent", "authoritative", "sympathetic"])
        self.backstory = ""
        self.avatar_style = "professional"

    def _generate_name(self):
        firsts = ["Alex", "Jordan", "Morgan", "Casey", "Riley", "Taylor", "Avery",
                   "Quinn", "Sage", "Blake", "Cameron", "Drew", "Hayden", "Sydney"]
        lasts = ["Chen", "Patel", "Johnson", "Williams", "Kim", "Martinez",
                  "Thompson", "Garcia", "Robinson", "Lee", "Anderson", "Clark"]
        return f"{random.choice(firsts)} {random.choice(lasts)}"

    def _generate_role(self):
        roles = [
            "IT Security Manager", "Chief Information Officer", "Systems Administrator",
            "HR Director", "Executive Assistant", "VP of Engineering",
            "Head of Compliance", "Network Operations Lead", "Help Desk Supervisor",
            "Internal Audit Manager", "DevOps Team Lead", "Cloud Infrastructure Manager",
        ]
        return random.choice(roles)

    def generate_backstory(self, target_org=""):
        templates = [
            f"I've been with {'the company' if not target_org else target_org} for {random.randint(2,12)} years, leading the {random.choice(['security', 'infrastructure', 'compliance', 'operations'])} team.",
            f"As the {self.role}, I oversee all {random.choice(['digital transformation', 'security operations', 'IT compliance', 'cloud migration'])} initiatives.",
            f"I recently joined to help modernize our {random.choice(['security posture', 'IT infrastructure', 'compliance framework', 'incident response'])}.",
        ]
        self.backstory = random.choice(templates)
        return self.backstory

    def signature_block(self):
        return f"{'='*40}\n{self.name}\n{self.role}\n{self.organization}\n{self.email}\n{self.phone}"


class Campaign:
    def __init__(self, name=None):
        self.name = name or f"Op-{''.join(random.choices(string.ascii_uppercase, k=4))}-{random.randint(1000,9999)}"
        self.targets = []
        self.persona = None
        self.vector = "email"
        self.stages = []
        self.current_stage = 0
        self.objective = "credential_harvest"
        self.status = "draft"
        self.results = []

    def add_target(self, target):
        self.targets.append(target)
        return self

    def set_persona(self, persona):
        self.persona = persona
        return self

    def add_stage(self, name, content, delay_hours=0):
        self.stages.append({
            "name": name,
            "content": content,
            "delay_hours": delay_hours,
            "completed": False,
        })
        return self

    def generate_attack_chain(self, target, persona):
        chains = {
            "credential_harvest": [
                ("Initial Contact", self._phish_initial(target, persona)),
                ("Urgent Follow-up", self._phish_follow_up(target, persona, urgent=True)),
                ("Credential Harvest", self._credential_harvest_page(target)),
            ],
            "malware_delivery": [
                ("Trust Building", self._trust_building(target, persona)),
                ("Document Delivery", self._document_delivery(target)),
                ("Payload Execution", self._payload_execution(target)),
            ],
            "ceo_fraud": [
                ("Reconnaissance", self._recon_message(target)),
                ("Authority Request", self._ceo_authority(target, persona)),
                ("Wire Transfer", self._wire_transfer_request(target)),
            ],
            "spear_phish": [
                ("Contextual Hook", self._spear_initial(target, persona)),
                ("Info Gathering", self._spear_gather(target)),
                ("Final Lure", self._spear_final(target)),
            ],
            "vishing": [
                ("Pretext Call Script", self._vishing_script(target, persona)),
                ("Verification Bypass", self._vishing_verify(target)),
                ("Info Extraction", self._vishing_extract(target)),
            ],
            "supply_chain": [
                ("Vendor Impersonation", self._vendor_init(target, persona)),
                ("Invoice Request", self._vendor_invoice(target)),
                ("Payment Redirect", self._vendor_payment(target)),
            ],
        }
        return chains.get(self.objective, chains["credential_harvest"])

    def _phish_initial(self, target, persona):
        if isinstance(target, TargetProfile):
            name = target.name or "there"
        else:
            name = "there"
        return f"""Subject: Action Required: Security Verification

Dear {name},

Our security team has detected unusual login activity that requires immediate verification.
Please click here to confirm your account: https://secure-login-{target.organization.lower().replace(' ', '') if isinstance(target, TargetProfile) else 'verify'}.com

This request is time-sensitive. Failure to verify within 24 hours will result in account suspension.

{persona.signature_block() if persona else ''}"""

    def _phish_follow_up(self, target, persona, urgent=False):
        prefix = "URGENT: " if urgent else ""
        return f"""Subject: {prefix}Second Notice: Security Verification Required

This is your final notice. Your account has been flagged for unusual activity.
Verify immediately to prevent suspension: https://secure-login-verify.com

{persona.signature_block() if persona else ''}"""

    def _credential_harvest_page(self, target):
        org = target.organization if isinstance(target, TargetProfile) else "your organization"
        return f"""Landing Page: https://secure-login-{org.lower().replace(' ', '')}.com
Design: Clone of {org} login portal
Capture: username, password, 2FA code
Redirect: https://{org.lower().replace(' ', '')}.com/authenticated"""

    def _trust_building(self, target, persona):
        return f"""Subject: Introduction and Collaboration Opportunity

Hi,

I came across your profile and was impressed by your work in {target.department if isinstance(target, TargetProfile) and target.department else 'technology'}.
Would you be open to a brief discussion about industry trends?

{persona.signature_block() if persona else ''}"""

    def _document_delivery(self, target):
        return "Deliver macro-enabled document: Q4_Review_{target_name}.docm\nVector: Email attachment or Dropbox link\nPayload: Meterpreter shell via VBA macro"

    def _payload_execution(self, target):
        return "Execute staged payload via macro\nC2 callback to: https://c2-panel.attacker.com\nPersistence: Scheduled task"

    def _ceo_authority(self, target, persona):
        return f"""Subject: Urgent Wire Transfer Request

Hi {target.name if isinstance(target, TargetProfile) else 'Team'},

I'm in a confidential meeting and need a wire transfer processed immediately.
Amount: $48,500
Account: Chase Business - ****4832
Routing: 021000021
Please keep this confidential. Confirm receipt.

{persona.signature_block() if persona else ''}"""

    def _wire_transfer_request(self, target):
        return "Follow-up: Send updated banking details via encrypted email\nTarget amount: $95,000\nVendor: Strategic Partners LLC"

    def _spear_initial(self, target, persona):
        return f"""Subject: Regarding your recent {random.choice(['conference talk', 'publication', 'project', 'presentation'])}

Hi {target.name if isinstance(target, TargetProfile) else 'there'},

I read your recent {random.choice(['article', 'paper', 'post'])} and wanted to share some complementary research our team has been working on.

{persona.signature_block() if persona else ''}"""

    def _spear_gather(self, target):
        return "Engage target in technical discussion\nExtract: current tools, stack, pain points, upcoming projects\nChannel: LinkedIn DM or email thread"

    def _spear_final(self, target):
        return "Deliver targeted payload disguised as relevant resource\nFormat: PDF with embedded tracking or shared document\nC2: Beacon via DNS tunneling"

    def _vishing_script(self, target, persona):
        return f"""=== VISHING SCRIPT ===
Target: {target.name if isinstance(target, TargetProfile) else 'Unknown'}
Caller: {persona.name if persona else 'IT Support'}
Objective: Extract domain credentials

1. Caller: "Hi {target.name if isinstance(target, TargetProfile) else ''}, this is {persona.name if persona else 'Alex'} from IT. We're seeing some unusual login attempts from your account."
2. Target variation: Express concern, ask what's happening
3. Caller: "We need to verify your credentials to ensure your account hasn't been compromised. I'm sending you a one-time verification link."
4. Deliver link or request password reset codes
5. Capture credentials from verification page"""

    def _vishing_verify(self, target):
        return "Voice: Call back from spoofed internal number\nVerify: Ask employee ID or manager name\nEscalate: Transfer to 'senior security engineer'"

    def _vishing_extract(self, target):
        return "Extract: Domain admin credentials or VPN access\nPretext: Security audit compliance\nFallback: Leave callback number for urgency"

    def _vendor_init(self, target, persona):
        return f"""Subject: Updated Vendor Agreement - {target.organization if isinstance(target, TargetProfile) else 'Your Company'}

Dear AP Team,

Our banking information has changed effective immediately.
Please update our vendor profile with the attached new agreement.

Best,
{persona.name if persona else 'Vendor Representative'}"""

    def _vendor_invoice(self, target):
        return "Send inflated invoice with updated bank details\nTarget amount: 2x normal monthly invoice\nAttach: Fake purchase order"

    def _vendor_payment(self, target):
        return "Redirect: All future payments to new account\nConfirm: Request confirmation of first redirected payment\nCover: Claim accounting system migration"

    def _recon_message(self, target):
        return f"Pretext: Industry survey or benchmarking study\nGather: Org chart, reporting structure, financial approval chain"

    def plan(self, objective, target, persona):
        self.objective = objective
        if isinstance(target, dict):
            t = TargetProfile()
            t.enrich_from_osint(target)
            self.add_target(t)
        elif isinstance(target, TargetProfile):
            self.add_target(target)
        else:
            t = TargetProfile(name=str(target))
            self.add_target(t)
        self.set_persona(persona or Persona())
        chain = self.generate_attack_chain(self.targets[0], self.persona)
        for stage_name, stage_content in chain:
            self.add_stage(stage_name, stage_content)
        self.status = "planned"
        return self

    def execute_next_stage(self):
        if self.current_stage >= len(self.stages):
            return None, "Campaign complete"
        stage = self.stages[self.current_stage]
        self.current_stage += 1
        return stage["name"], stage["content"]

    def status_report(self):
        lines = [f"## Campaign: {self.name}", f"Objective: {self.objective}", f"Status: {self.status}",
                 f"Targets: {len(self.targets)}", f"Stages: {len(self.stages)} ({self.current_stage} completed)"]
        for i, stage in enumerate(self.stages):
            icon = "✓" if i < self.current_stage else "○" if i == self.current_stage else "·"
            lines.append(f"  {icon} Stage {i+1}: {stage['name']}")
        if self.persona:
            lines.append(f"\nPersona: {self.persona.name} ({self.persona.role})")
        if self.targets:
            t = self.targets[0]
            lines.append(f"Primary target: {t.name or 'Unknown'} (@ {t.organization or '?'})")
        return "\n".join(lines)

    def generate_report(self):
        lines = [f"# Social Engineering Campaign Report", f"## {self.name}", f"",
                 f"**Objective:** {self.objective}", f"**Vector:** {self.vector}", f"**Status:** {self.status}",
                 f"**Targets:** {len(self.targets)}", f"**Stages:** {len(self.stages)}", f""]
        for i, stage in enumerate(self.stages):
            status = "COMPLETED" if i < self.current_stage else "PENDING"
            lines.append(f"### Stage {i+1}: {stage['name']} [{status}]")
            lines.append(f"```")
            lines.append(stage["content"])
            lines.append(f"```")
            lines.append(f"")
        return "\n".join(lines)


class SocialEngine:
    ATTACK_VECTORS = [
        "spear_phish", "whaling", "ceo_fraud", "credential_harvest",
        "malware_delivery", "vishing", "smishing", "supply_chain",
        "water_hole", "tech_support", "hr_impersonation", "it_impersonation",
    ]

    def __init__(self):
        self.campaigns = []

    def create_campaign(self, name=None):
        c = Campaign(name)
        self.campaigns.append(c)
        return c

    def generate_target_summary(self, target_info):
        if isinstance(target_info, dict):
            tp = TargetProfile()
            tp.enrich_from_osint(target_info)
            target_info = tp
        if isinstance(target_info, TargetProfile):
            lines = [f"## Target Profile", f"**Name:** {target_info.name or 'Unknown'}",
                     f"**Role:** {target_info.role or 'Unknown'}", f"**Organization:** {target_info.organization or 'Unknown'}",
                     f"**Email:** {target_info.email or 'Unknown'}", f"**Department:** {target_info.department or 'Unknown'}",
                     f"**Manager:** {target_info.manager_name or 'Unknown'}", f"**Phone:** {target_info.phone or 'Unknown'}",
                     f"**Language:** {target_info.language}", f"**Comm Style:** {target_info.communication_style}",
                     f"**Platforms:** {', '.join(target_info.trusted_platforms)}"]
            if target_info.interests:
                lines.append(f"**Interests:** {', '.join(target_info.interests)}")
            if target_info.pain_points:
                lines.append(f"**Pain Points:** {', '.join(target_info.pain_points)}")
            if target_info.software_used:
                lines.append(f"**Software:** {', '.join(target_info.software_used)}")
            if target_info.recent_projects:
                lines.append(f"**Projects:** {', '.join(target_info.recent_projects)}")
            if target_info.team_members:
                lines.append(f"**Team:** {', '.join(target_info.team_members)}")
            return "\n".join(lines)
        return f"## Target\n{str(target_info)}"

    def vector_info(self):
        lines = ["## Social Engineering Attack Vectors"]
        descriptions = {
            "spear_phish": "Targeted email phishing with contextual lures based on target research",
            "whaling": "Phishing targeting executives/C-suite with business-related pretexts",
            "ceo_fraud": "Impersonation of CEO/executive to authorize fraudulent transactions",
            "credential_harvest": "Clone login pages to capture credentials and 2FA codes",
            "malware_delivery": "Deliver payloads via macro documents, malicious attachments",
            "vishing": "Voice phishing — phone calls impersonating IT/HR/support",
            "smishing": "SMS phishing with urgent messages and malicious links",
            "supply_chain": "Vendor impersonation to redirect payments or deliver poisoned updates",
            "water_hole": "Compromise sites the target frequently visits",
            "tech_support": "Pretend to be IT support to extract credentials or install remote access",
            "hr_impersonation": "HR-themed phishing (benefits, payroll, policy updates)",
            "it_impersonation": "IT-themed phishing (password reset, security alert, software update)",
        }
        for v in self.ATTACK_VECTORS:
            lines.append(f"- **{v}**: {descriptions.get(v, '')}")
        return "\n".join(lines)
