import socket

CHECKS = []


def register(func):
    CHECKS.append(func)
    return func


def try_connect(host: str, port: int, timeout: int = 5) -> bool:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except:
        return False


def run_all_checks(host: str) -> list[dict]:
    findings = []
    for check in CHECKS:
        try:
            result = check(host)
            if result:
                findings.append(result)
        except Exception as e:
            pass
    return findings


@register
def check_ftp_anonymous(host: str) -> dict | None:
    if not try_connect(host, 21):
        return None
    return {
        "type": "low_hanging",
        "service": "FTP (21)",
        "check": "Anonymous login attempt",
        "command": f"curl ftp://{host} --user anonymous:anonymous -ls 2>/dev/null || echo 'FAILED'",
        "confidence": "medium",
        "description": "Check if FTP allows anonymous login",
    }


@register
def check_ssh_default_creds(host: str) -> dict | None:
    if not try_connect(host, 22):
        return None
    return {
        "type": "low_hanging",
        "service": "SSH (22)",
        "check": "Default credential test",
        "command": f'hydra -l root -P /usr/share/wordlists/rockyou.txt -t 4 ssh://{host} 2>/dev/null | head -5 || echo "Check rockyou path"',
        "confidence": "low",
        "description": "Check for weak SSH credentials (root:root, admin:admin)",
    }


@register
def check_smb_null_session(host: str) -> dict | None:
    if not try_connect(host, 445):
        return None
    return {
        "type": "low_hanging",
        "service": "SMB (445)",
        "check": "Null session / anonymous login",
        "command": f"smbclient -N -L //{host} 2>/dev/null",
        "confidence": "high",
        "description": "Check SMB null session authentication and list shares",
    }


@register
def check_nfs_exports(host: str) -> dict | None:
    if not try_connect(host, 2049):
        return None
    return {
        "type": "low_hanging",
        "service": "NFS (2049)",
        "check": "NFS exports enumeration",
        "command": f"showmount -e {host} 2>/dev/null",
        "confidence": "high",
        "description": "Enumerate NFS exports, check for no_root_squash",
    }


@register
def check_mysql_anonymous(host: str) -> dict | None:
    if not try_connect(host, 3306):
        return None
    return {
        "type": "low_hanging",
        "service": "MySQL (3306)",
        "check": "Anonymous root access",
        "command": f'mysql -h {host} -u root -e "show databases;" 2>/dev/null || echo "FAILED"',
        "confidence": "medium",
        "description": "Check if MySQL allows root with no password",
    }


@register
def check_postgres_anonymous(host: str) -> dict | None:
    if not try_connect(host, 5432):
        return None
    return {
        "type": "low_hanging",
        "service": "PostgreSQL (5432)",
        "check": "Default postgres access",
        "command": f'PGPASSWORD=postgres psql -h {host} -U postgres -c "\\l" 2>/dev/null || echo "FAILED"',
        "confidence": "medium",
        "description": "Check PostgreSQL default credentials (postgres:postgres)",
    }


@register
def check_redis_unauthorized(host: str) -> dict | None:
    if not try_connect(host, 6379):
        return None
    return {
        "type": "low_hanging",
        "service": "Redis (6379)",
        "check": "Unauthenticated access",
        "command": f'echo "INFO" | timeout 3 nc -n {host} 6379 2>/dev/null || echo "FAILED"',
        "confidence": "high",
        "description": "Check if Redis allows unauthenticated access (common CTF misconfig)",
    }


@register
def check_mongodb_unauthorized(host: str) -> dict | None:
    if not try_connect(host, 27017):
        return None
    payload = '{"find":"admin","filter":{},"limit":1}'
    return {
        "type": "low_hanging",
        "service": "MongoDB (27017)",
        "check": "Unauthenticated access",
        "command": f"echo '{payload}' | timeout 3 nc -n {host} 27017 2>/dev/null || echo 'FAILED'",
        "confidence": "high",
        "description": "Check if MongoDB allows unauthenticated access",
    }


@register
def check_winrm_default(host: str) -> dict | None:
    if not try_connect(host, 5985):
        return None
    return {
        "type": "low_hanging",
        "service": "WinRM (5985)",
        "check": "Default WinRM credentials",
        "command": f'crackmapexec winrm {host} -u administrator -p password123 2>/dev/null | head -3 || echo "FAILED"',
        "confidence": "low",
        "description": "Check WinRM with common credentials",
    }


@register
def check_ldap_anonymous(host: str) -> dict | None:
    if not try_connect(host, 389):
        return None
    return {
        "type": "low_hanging",
        "service": "LDAP (389)",
        "check": "Anonymous bind",
        "command": f"ldapsearch -x -h {host} -b \"dc=htb,dc=local\" 2>/dev/null | head -30 || ldapsearch -x -h {host} -s base namingcontexts 2>/dev/null || echo 'FAILED'",
        "confidence": "high",
        "description": "Check LDAP anonymous bind for information disclosure",
    }


@register
def check_tomcat_default(host: str) -> dict | None:
    checks = []
    for port in [80, 443, 8080, 8443]:
        if try_connect(host, port):
            checks.append({
                "type": "low_hanging",
                "service": f"HTTP ({port})",
                "check": "Tomcat manager default creds",
                "command": f'curl -s -o /dev/null -w "%{{http_code}}" -u tomcat:tomcat http://{host}:{port}/manager/html 2>/dev/null',
                "confidence": "medium",
                "description": "Check Tomcat manager with default credentials (tomcat:tomcat, admin:admin)",
            })
    return checks if checks else None
