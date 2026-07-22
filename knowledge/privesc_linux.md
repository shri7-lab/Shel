# Linux Privilege Escalation Checklist

## Enumeration Commands
```bash
whoami; id; hostname; uname -a
cat /etc/os-release
sudo -l
find / -perm -4000 -type f 2>/dev/null
cat /etc/crontab
ls -la /etc/cron*
cat /etc/passwd | grep -v nologin
ps aux
netstat -tlnp
ss -tlnp
find / -writable -type f 2>/dev/null | grep -v proc
cat /etc/fstab
cat ~/.bash_history
echo '' > ~/.bash_history
```

## Interesting Files
- `/etc/shadow` - Password hashes
- `/etc/ssh/sshd_config` - SSH config
- `*.kdbx` - KeePass databases
- `*.id_rsa` - SSH keys
- `.git/config` - Git repos
- `.env` - Environment variables (creds)

## SUID Binaries (GTFOBins)
- Check each SUID binary against https://gtfobins.github.io/
- Common privesc SUIDs: `nmap`, `vim`, `less`, `more`, `bash`, `awk`, `python`, `perl`, `find`

## Kernel Exploits
- `uname -a` → search for kernel CVEs
- Tools: `linux-exploit-suggester.sh`, `dirtycow`, `pwnkit`
