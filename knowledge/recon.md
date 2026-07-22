# Reconnaissance Methodology

## nmap scans
- Quick scan: `nmap -sC -sV -O -T4 <target>`
- Full port scan: `nmap -p- -T4 <target>`
- UDP scan: `nmap -sU --top-ports 100 <target>`
- Script scan: `nmap --script vuln <target>`
- Output formats: `-oN <file> -oX <file> -oG <file>`

## Web Enumeration
- Directory busting: `gobuster dir -u <url> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
- Subdomain: `gobuster vhost -u <url> -w <wordlist>`
- Tech stack: `whatweb <url>`
- Screenshots: `gowitness single <url>`

## DNS
- Forward: `nslookup <domain>`
- Reverse: `nslookup <ip>`
- Zone transfer: `dig axfr @<ns> <domain>`

## SMB
- Share listing: `smbclient -L //<target>`
- Recursive: `smbclient //<target>/share -c "recurse; ls"`

## LDAP
- `ldapsearch -x -H ldap://<target> -b "dc=..."`

## SNMP
- `snmpwalk -v2c -c public <target>`
