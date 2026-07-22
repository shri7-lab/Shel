# OSINT Methodology

## Domain Reconnaissance
- `whois <domain>` - Registration details
- `dig any <domain>` - All DNS records
- `dig mx <domain>` - Mail servers
- `dig txt <domain>` - SPF, DKIM, DMARC
- `dig ns <domain>` - Nameservers
- `curl -s https://crt.sh/?q=%.<domain>&output=json` - Certificate Transparency (subdomains)
- `theHarvester -d <domain> -b all` - Email + subdomain harvest
- `sublist3r -d <domain>` - Subdomain enumeration
- `amass enum -d <domain>` - Deep subdomain discovery

## IP Reconnaissance
- `whois <ip>` - ASN, netblock
- `nslookup <ip>` - PTR record
- `curl https://api.hackertarget.com/reverseiplookup/?q=<ip>` - Domains on same IP
- `shodan host <ip>` - Open ports, services (if API key)
- `curl https://ipinfo.io/<ip>/json` - Geolocation, ISP

## Email OSINT
- `curl https://api.hackertarget.com/email-format/?q=<email>` - Email format check
- Search in breach databases
- Google dork: `intext:@domain.com`
- GitHub dork: `@domain.com` in code

## Username OSINT
- `sherlock <username>` - Search 300+ social platforms
- Check: GitHub, Reddit, Twitter/X, Keybase, Medium, Dev.to, HTB

## Google Dorking
| Purpose | Dork |
|---------|------|
| Files | `site:domain filetype:pdf OR filetype:doc` |
| Admin panels | `site:domain inurl:admin OR inurl:login` |
| Config files | `site:domain filetype:env OR filetype:cfg` |
| Directory listing | `site:domain intitle:"index of"` |
| SQLi | `site:domain inurl:.php?id=` |
| Emails | `site:domain intext:@domain` |

## Web Archive
- `https://web.archive.org/cdx/search/cdx?url=<domain>/*&output=json` - List snapshots
- `https://web.archive.org/web/<timestamp>/<url>` - View cached version

## Metadata
- `exiftool <file>` - Extract metadata from documents, images
- `pdfinfo <file>` - PDF metadata
- `strings <file> | grep -i "@\|\.com\|http"` - Hidden data in binaries

## Tools (from BlackArch)
- theHarvester - Email/subdomain gathering
- sherlock - Username search
- holehe - Email-to-account mapping
- maigret - Profile search
- recon-ng - Full OSINT framework
- spiderfoot - Automated OSINT
- sn0int - OSINT/RECON framework
- photon - Crawler for OSINT
