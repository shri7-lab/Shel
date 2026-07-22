"""
BlackArch Tool Database - Comprehensive penetration testing tool repository.

This module provides access to the BlackArch Linux penetration testing
tool database, organized by category with search and suggestion capabilities.
"""

TOOL_DATABASE = {
    # Web Application (319 tools)
    'blackarch-webapp': [
        {
            'name': '0d1n',
            'description': "Web security tool to make fuzzing at HTTP inputs, made in C with libCurl.",
            'aliases': ["0d1n", "0d1n"],
        },
        {
            'name': 'abuse-ssl-bypass-waf',
            'description': "Bypassing WAF by abusing SSL/TLS Ciphers.",
            'aliases': ["abuse-ssl-bypass-waf", "abuse ssl bypass waf"],
        },
        {
            'name': 'adfind',
            'description': "Simple admin panel finder for php,js,cgi,asp and aspx admin panels.",
            'aliases': ["adfind", "adfind"],
        },
        {
            'name': 'adminpagefinder',
            'description': "This python script looks for a large amount of possible administrative interfaces on a given site.",
            'aliases': ["adminpagefinder", "adminpagefinder"],
        },
        {
            'name': 'albatar',
            'description': "A SQLi exploitation framework in Python.",
            'aliases': ["albatar", "albatar"],
        },
        {
            'name': 'anti-xss',
            'description': "A XSS vulnerability scanner.",
            'aliases': ["anti-xss", "anti xss"],
        },
        {
            'name': 'arachni',
            'description': "A feature-full, modular, high-performance Ruby framework aimed towards helping penetration testers and administrators evaluate the security of web applications.",
            'aliases': ["arachni", "arachni"],
        },
        {
            'name': 'astra',
            'description': "Automated Security Testing For REST API\'s.",
            'aliases': ["astra", "astra"],
        },
        {
            'name': 'atlas',
            'description': "Open source tool that can suggest sqlmap tampers to bypass WAF/IDS/IPS.",
            'aliases': ["atlas", "atlas"],
        },
        {
            'name': 'badministration',
            'description': "A tool which interfaces with management or administration applications from an offensive standpoint.",
            'aliases': ["badministration", "badministration"],
        },
        {
            'name': 'badsecrets',
            'description': "A library for detecting known secrets across many web frameworks.",
            'aliases': ["badsecrets", "badsecrets"],
        },
        {
            'name': 'bbqsql',
            'description': "SQL injection exploit tool.",
            'aliases': ["bbqsql", "bbq sql", "blind sql"],
        },
        {
            'name': 'bbscan',
            'description': "A tiny Batch web vulnerability Scanner.",
            'aliases': ["bbscan", "bbscan"],
        },
        {
            'name': 'bing-lfi-rfi',
            'description': "Python script for searching Bing for sites that may have local and remote file inclusion vulnerabilities.",
            'aliases': ["bing-lfi-rfi", "bing lfi rfi"],
        },
        {
            'name': 'blisqy',
            'description': "Exploit Time-based blind-SQL injection in HTTP-Headers (MySQL/MariaDB).",
            'aliases': ["blisqy", "blisqy"],
        },
        {
            'name': 'brutemap',
            'description': "Penetration testing tool that automates testing accounts to the site\'s login page.",
            'aliases': ["brutemap", "brutemap"],
        },
        {
            'name': 'brutexss',
            'description': "Cross-Site Scripting Bruteforcer.",
            'aliases': ["brutexss", "brutexss"],
        },
        {
            'name': 'bsqlbf',
            'description': "Blind SQL Injection Brute Forcer.",
            'aliases': ["bsqlbf", "bsqlbf"],
        },
        {
            'name': 'bsqlinjector',
            'description': "Blind SQL injection exploitation tool written in ruby.",
            'aliases': ["bsqlinjector", "bsqlinjector"],
        },
        {
            'name': 'burpsuite',
            'description': "An integrated platform for attacking web applications (community edition) + SHELLING plugin.",
            'aliases': ["burp", "burpsuite", "burp suite"],
        },
        {
            'name': 'c5scan',
            'description': "Vulnerability scanner and information gatherer for the Concrete5 CMS.",
            'aliases': ["c5scan", "c5scan"],
        },
        {
            'name': 'caido-cli',
            'description': "Intercepting proxy to replay, inject, scan and fuzz HTTP requests.",
            'aliases': ["caido-cli", "caido cli"],
        },
        {
            'name': 'caido-desktop',
            'description': "Intercepting proxy to replay, inject, scan and fuzz HTTP requests.",
            'aliases': ["caido-desktop", "caido desktop"],
        },
        {
            'name': 'cansina',
            'description': "A python-based Web Content Discovery Tool.",
            'aliases': ["cansina", "cansina"],
        },
        {
            'name': 'cariddi',
            'description': "Take a list of domains, crawl urls and scan for endpoints, secrets, api keys, file extensions, token.",
            'aliases': ["cariddi", "cariddi"],
        },
        {
            'name': 'cent',
            'description': "Community edition nuclei templates.",
            'aliases': ["cent", "cent"],
        },
        {
            'name': 'chankro',
            'description': "Tool that generates a PHP capable of run a custom binary (like a meterpreter) or a bash script (p.e. reverse shell) bypassing disable_functions & open_basedir).",
            'aliases': ["chankro", "chankro"],
        },
        {
            'name': 'cjexploiter',
            'description': "Drag and Drop ClickJacking exploit development assistance tool.",
            'aliases': ["cjexploiter", "cjexploiter"],
        },
        {
            'name': 'clairvoyance',
            'description': "Obtain GraphQL API Schema even if the introspection is not enabled.",
            'aliases': ["clairvoyance", "clairvoyance"],
        },
        {
            'name': 'cloudget',
            'description': "Python script to bypass cloudflare from command line. Built upon cfscrape module.",
            'aliases': ["cloudget", "cloudget"],
        },
        {
            'name': 'cms-few',
            'description': "Joomla, Mambo, PHP-Nuke, and XOOPS CMS SQL injection vulnerability scanning tool written in Python.",
            'aliases': ["cms-few", "cms few"],
        },
        {
            'name': 'cmseek',
            'description': "CMS (Content Management Systems) Detection and Exploitation suite.",
            'aliases': ["cmseek", "cmseek"],
        },
        {
            'name': 'cmsfuzz',
            'description': "Fuzzer for wordpress, cold fusion, drupal, joomla, and phpnuke.",
            'aliases': ["cmsfuzz", "cmsfuzz"],
        },
        {
            'name': 'cmsscan',
            'description': "CMS scanner to identify and find vulnerabilities for Wordpress, Drupal, Joomla, vBulletin.",
            'aliases': ["cmsscan", "cmsscan"],
        },
        {
            'name': 'cmsscanner',
            'description': "CMS Scanner Framework.",
            'aliases': ["cmsscanner", "cmsscanner"],
        },
        {
            'name': 'comission',
            'description': "WhiteBox CMS analysis.",
            'aliases': ["comission", "comission"],
        },
        {
            'name': 'commentor',
            'description': "Extract all comments from the specified URL resource.",
            'aliases': ["commentor", "commentor"],
        },
        {
            'name': 'commix',
            'description': "Automated All-in-One OS Command Injection and Exploitation Tool.",
            'aliases': ["commix", "commix"],
        },
        {
            'name': 'corscanner',
            'description': "Fast CORS misconfiguration vulnerabilities scanner.",
            'aliases': ["corscanner", "corscanner"],
        },
        {
            'name': 'corsy',
            'description': "CORS Misconfiguration Scanner.",
            'aliases': ["corsy", "corsy"],
        },
        {
            'name': 'crabstick',
            'description': "Automatic remote/local file inclusion vulnerability analysis and exploit tool.",
            'aliases': ["crabstick", "crabstick"],
        },
        {
            'name': 'crackql',
            'description': "GraphQL password brute-force and fuzzing utility",
            'aliases': ["crackql", "crackql"],
        },
        {
            'name': 'crawlic',
            'description': "Web recon tool (find temporary files, parse robots.txt, search folders, google dorks and search domains hosted on same server).",
            'aliases': ["crawlic", "crawlic"],
        },
        {
            'name': 'crlfuzz',
            'description': "A fast tool to scan CRLF vulnerability written in Go.",
            'aliases': ["crlfuzz", "crlfuzz"],
        },
        {
            'name': 'csrftester',
            'description': "The OWASP CSRFTester Project attempts to give developers the ability to test their applications for CSRF flaws.",
            'aliases': ["csrftester", "csrftester"],
        },
        {
            'name': 'cybercrowl',
            'description': "A Python Web path scanner tool.",
            'aliases': ["cybercrowl", "cybercrowl"],
        },
        {
            'name': 'dalfox',
            'description': "Powerful open-source XSS scanner and utility focused on automation.",
            'aliases': ["dalfox", "dal fox", "dalifox"],
        },
        {
            'name': 'darkdump',
            'description': "Open Source Intelligence interface for Deep Web scraping.",
            'aliases': ["darkdump", "darkdump"],
        },
        {
            'name': 'darkjumper',
            'description': "This tool will try to find every website that host at the same server at your target.",
            'aliases': ["darkjumper", "darkjumper"],
        },
        {
            'name': 'darkscrape',
            'description': "OSINT Tool For Scraping Dark Websites.",
            'aliases': ["darkscrape", "darkscrape"],
        },
        {
            'name': 'davscan',
            'description': "Fingerprints servers, finds exploits, scans WebDAV.",
            'aliases': ["davscan", "davscan"],
        },
        {
            'name': 'dawnscanner',
            'description': "A static analysis security scanner for ruby written web applications.",
            'aliases': ["dawnscanner", "dawnscanner"],
        },
        {
            'name': 'dff-scanner',
            'description': "Tool for finding path of predictable resource locations.",
            'aliases': ["dff-scanner", "dff scanner"],
        },
        {
            'name': 'dirble',
            'description': "Fast directory scanning and scraping tool.",
            'aliases': ["dirble", "dirble"],
        },
        {
            'name': 'dirbuster-ng',
            'description': "C CLI implementation of the Java dirbuster tool.",
            'aliases': ["dirbuster-ng", "dirbuster ng"],
        },
        {
            'name': 'dirhunt',
            'description': "Find web directories without bruteforce.",
            'aliases': ["dirhunt", "dirhunt"],
        },
        {
            'name': 'dirscraper',
            'description': "OSINT Scanning tool which discovers and maps directories found in javascript files hosted on a website.",
            'aliases': ["dirscraper", "dirscraper"],
        },
        {
            'name': 'dirsearch',
            'description': "HTTP(S) directory/file brute forcer.",
            'aliases': ["dirsearch", "dirsearch"],
        },
        {
            'name': 'docem',
            'description': "Uility to embed XXE and XSS payloads in docx,odt,pptx,etc (OXML_XEE on steroids).",
            'aliases': ["docem", "docem"],
        },
        {
            'name': 'domi-owned',
            'description': "A tool used for compromising IBM/Lotus Domino servers.",
            'aliases': ["domi-owned", "domi owned"],
        },
        {
            'name': 'dontgo403',
            'description': "Tool to bypass 40X response codes..",
            'aliases': ["dontgo403", "dontgo403"],
        },
        {
            'name': 'doork',
            'description': "Passive Vulnerability Auditor.",
            'aliases': ["doork", "doork"],
        },
        {
            'name': 'dorknet',
            'description': "Selenium powered Python script to automate searching for vulnerable web apps.",
            'aliases': ["dorknet", "dorknet"],
        },
        {
            'name': 'droopescan',
            'description': "A plugin-based scanner that aids security researchers in identifying issues with several CMSs, mainly Drupal & Silverstripe.",
            'aliases': ["droopescan", "droope scan"],
        },
        {
            'name': 'drupal-module-enum',
            'description': "Enumerate on drupal modules.",
            'aliases': ["drupal-module-enum", "drupal module enum"],
        },
        {
            'name': 'drupalscan',
            'description': "Simple non-intrusive Drupal scanner.",
            'aliases': ["drupalscan", "drupalscan"],
        },
        {
            'name': 'drupwn',
            'description': "Drupal enumeration & exploitation tool.",
            'aliases': ["drupwn", "drupwn"],
        },
        {
            'name': 'dsfs',
            'description': "A fully functional File inclusion vulnerability scanner (supporting GET and POST parameters) written in under 100 lines of code.",
            'aliases': ["dsfs", "dsfs"],
        },
        {
            'name': 'dsjs',
            'description': "A fully functional JavaScript library vulnerability scanner written in under 100 lines of code.",
            'aliases': ["dsjs", "dsjs"],
        },
        {
            'name': 'dsss',
            'description': "A fully functional SQL injection vulnerability scanner (supporting GET and POST parameters) written in under 100 lines of code.",
            'aliases': ["dsss", "dsss"],
        },
        {
            'name': 'dsstore-crawler',
            'description': "A parser + crawler for .DS_Store files exposed publically.",
            'aliases': ["dsstore-crawler", "dsstore crawler"],
        },
        {
            'name': 'dsxs',
            'description': "A fully functional Cross-site scripting vulnerability scanner (supporting GET and POST parameters) written in under 100 lines of code.",
            'aliases': ["dsxs", "dsxs"],
        },
        {
            'name': 'eos',
            'description': "Enemies Of Symfony - Debug mode Symfony looter.",
            'aliases': ["eos", "eos"],
        },
        {
            'name': 'epicwebhoneypot',
            'description': "Tool which aims to lure attackers using various types of web vulnerability scanners by tricking them into believing that they have found a vulnerability on a host.",
            'aliases': ["epicwebhoneypot", "epicwebhoneypot"],
        },
        {
            'name': 'evine',
            'description': "Interactive CLI Web Crawler.",
            'aliases': ["evine", "evine"],
        },
        {
            'name': 'extended-ssrf-search',
            'description': "Smart ssrf scanner using different methods like parameter brute forcing in post and get.",
            'aliases': ["extended-ssrf-search", "extended ssrf search"],
        },
        {
            'name': 'eyewitness',
            'description': "Designed to take screenshots of websites, provide some server header info, and identify default credentials if possible.",
            'aliases': ["eyewitness", "eyewitness"],
        },
        {
            'name': 'fbht',
            'description': "A Facebook Hacking Tool",
            'aliases': ["fbht", "fbht"],
        },
        {
            'name': 'fdsploit',
            'description': "A File Inclusion & Directory Traversal fuzzing, enumeration & exploitation tool.",
            'aliases': ["fdsploit", "fdsploit"],
        },
        {
            'name': 'feroxbuster',
            'description': "A fast, simple, recursive content discovery tool written in Rust.",
            'aliases': ["feroxbuster", "feroxbuster"],
        },
        {
            'name': 'ffuf',
            'description': "Fast web fuzzer written in Go.",
            'aliases': ["ffuf", "fuzz faster u fool"],
        },
        {
            'name': 'fhttp',
            'description': "This is a framework for HTTP related attacks. It is written in Perl with a GTK interface, has a proxy for debugging and manipulation, proxy chaining, evasion rules, and more.",
            'aliases': ["fhttp", "fhttp"],
        },
        {
            'name': 'filebuster',
            'description': "An extremely fast and flexible web fuzzer.",
            'aliases': ["filebuster", "filebuster"],
        },
        {
            'name': 'filegps',
            'description': "A tool that help you to guess how your shell was renamed after the server-side script of the file uploader saved it.",
            'aliases': ["filegps", "filegps"],
        },
        {
            'name': 'fimap',
            'description': "A little tool for local and remote file inclusion auditing and exploitation.",
            'aliases': ["fimap", "fimap"],
        },
        {
            'name': 'fingerprinter',
            'description': "CMS/LMS/Library etc Versions Fingerprinter.",
            'aliases': ["fingerprinter", "fingerprinter"],
        },
        {
            'name': 'flask-session-cookie-manager2',
            'description': "Decode and encode Flask session cookie.",
            'aliases': ["flask-session-cookie-manager2", "flask session cookie manager2"],
        },
        {
            'name': 'flask-session-cookie-manager3',
            'description': "Decode and encode Flask session cookie.",
            'aliases': ["flask-session-cookie-manager3", "flask session cookie manager3"],
        },
        {
            'name': 'fockcache',
            'description': "Tool to make cache poisoning by trying X-Forwarded-Host and X-Forwarded-Scheme headers on web pages.",
            'aliases': ["fockcache", "fockcache"],
        },
        {
            'name': 'fuxploider',
            'description': "Tool that automates the process of detecting and exploiting file upload forms flaws.",
            'aliases': ["fuxploider", "fuxploider"],
        },
        {
            'name': 'gau',
            'description': "Fetch known URLs from AlienVault\'s Open Threat Exchange, the Wayback Machine, and Common Crawl.",
            'aliases': ["gau", "getallurls", "get all urls"],
        },
        {
            'name': 'ghauri',
            'description': "An advanced cross-platform tool that automates the process of detecting and exploiting SQL injection security flaws.",
            'aliases': ["ghauri", "ghauri"],
        },
        {
            'name': 'ghost-py',
            'description': "Webkit based webclient (relies on PyQT).",
            'aliases': ["ghost-py", "ghost py"],
        },
        {
            'name': 'gitdump',
            'description': "A pentesting tool that dumps the source code from .git even when the directory traversal is disabled.",
            'aliases': ["gitdump", "gitdump"],
        },
        {
            'name': 'gittools',
            'description': "A repository with 3 tools for pwn\'ing websites with .git repositories available\'.",
            'aliases': ["gittools", "gittools"],
        },
        {
            'name': 'golismero',
            'description': "Opensource web security testing framework.",
            'aliases': ["golismero", "golismero"],
        },
        {
            'name': 'goop-dump',
            'description': "Tool to dump a git repository from a website, focused on as-complete-as-possible dumps and handling weird edge-cases.",
            'aliases': ["goop-dump", "goop dump"],
        },
        {
            'name': 'gopherus',
            'description': "Tool generates gopher link for exploiting SSRF and gaining RCE in various servers.",
            'aliases': ["gopherus", "gopherus"],
        },
        {
            'name': 'gospider',
            'description': "Fast web spider written in Go.",
            'aliases': ["gospider", "gospider"],
        },
        {
            'name': 'gowitness',
            'description': "A golang, web screenshot utility using Chrome Headless.",
            'aliases': ["gowitness", "gowitness"],
        },
        {
            'name': 'grabber',
            'description': "A web application scanner. Basically it detects some kind of vulnerabilities in your website.",
            'aliases': ["grabber", "grabber"],
        },
        {
            'name': 'graphql-path-enum',
            'description': "Tool that lists the different ways of reaching a given type in a GraphQL schema.",
            'aliases': ["graphql-path-enum", "graphql path enum"],
        },
        {
            'name': 'graphqlmap',
            'description': "Scripting engine to interact with a graphql endpoint for pentesting purposes.",
            'aliases': ["graphqlmap", "graphqlmap"],
        },
        {
            'name': 'graphw00f',
            'description': "GraphQL endpoint detection and engine fingerprinting.",
            'aliases': ["graphw00f", "graphw00f"],
        },
        {
            'name': 'grpc-pentest-suite',
            'description': "Set of tools for pentesting gRPC-Web Applications.",
            'aliases': ["grpc-pentest-suite", "grpc pentest suite"],
        },
        {
            'name': 'h2csmuggler',
            'description': "HTTP Request Smuggling over HTTP/2 Cleartext (h2c).",
            'aliases': ["h2csmuggler", "h2csmuggler"],
        },
        {
            'name': 'h2t',
            'description': "Scans a website and suggests security headers to apply.",
            'aliases': ["h2t", "h2t"],
        },
        {
            'name': 'hakrawler',
            'description': "Simple, fast web crawler designed for easy, quick discovery of endpoints and assets within a web application.",
            'aliases': ["hakrawler", "hakrawler"],
        },
        {
            'name': 'hetty',
            'description': "HTTP toolkit for security research. Aims to become an open source alternative to commercial software like Burp Suite Pro.",
            'aliases': ["hetty", "hetty"],
        },
        {
            'name': 'hookshot',
            'description': "Integrated web scraper and email account data breach comparison tool.",
            'aliases': ["hookshot", "hookshot"],
        },
        {
            'name': 'htcap',
            'description': "A web application analysis tool for detecting communications between javascript and the server.",
            'aliases': ["htcap", "htcap"],
        },
        {
            'name': 'http2smugl',
            'description': "Http2Smugl - Tool to detect and exploit HTTP request smuggling in cases it can be achieved via HTTP/2 -> HTTP/1.1 conversion.",
            'aliases': ["http2smugl", "http2smugl"],
        },
        {
            'name': 'httpforge',
            'description': "A set of shell tools that let you manipulate, send, receive, and analyze HTTP messages. These tools can be used to test, discover, and assert the security of Web servers, apps, and sites. An accompanying Python library is available for extensions.",
            'aliases': ["httpforge", "httpforge"],
        },
        {
            'name': 'httpgrep',
            'description': "Async HTTP(S) scanner that greps response bodies and headers for strings or regex across hosts, ports, CIDR/ranges and TLS-cert vhosts.",
            'aliases': ["httpgrep", "httpgrep"],
        },
        {
            'name': 'httppwnly',
            'description': "\"Repeater\" style XSS post-exploitation tool for mass browser control.",
            'aliases': ["httppwnly", "httppwnly"],
        },
        {
            'name': 'httpx',
            'description': "A fast and multi-purpose HTTP toolkit allow to run multiple probers using retryablehttp library.",
            'aliases': ["httpx", "http probe"],
        },
        {
            'name': 'identywaf',
            'description': "Blind WAF identification tool.",
            'aliases': ["identywaf", "identywaf"],
        },
        {
            'name': 'injectus',
            'description': "CRLF and open redirect fuzzer.",
            'aliases': ["injectus", "injectus"],
        },
        {
            'name': 'interactsh-client',
            'description': "Open-Source Solution for Out of band Data Extraction.",
            'aliases': ["interactsh-client", "interactsh client"],
        },
        {
            'name': 'ipsourcebypass',
            'description': "This Python script can be used to bypass IP source restrictions using HTTP headers.",
            'aliases': ["ipsourcebypass", "ipsourcebypass"],
        },
        {
            'name': 'jaeles',
            'description': "The Swiss Army knife for automated Web Application Testing.",
            'aliases': ["jaeles", "jaeles"],
        },
        {
            'name': 'jaidam',
            'description': "Penetration testing tool that would take as input a list of domain names, scan them, determine if wordpress or joomla platform was used and finally check them automatically, for web vulnerabilities using two well-known open source tools,",
            'aliases': ["jaidam", "jaidam"],
        },
        {
            'name': 'jast',
            'description': "Just Another Screenshot Tool.",
            'aliases': ["jast", "jast"],
        },
        {
            'name': 'jboss-autopwn',
            'description': "A JBoss script for obtaining remote shell access.",
            'aliases': ["jboss-autopwn", "jboss autopwn"],
        },
        {
            'name': 'jdeserialize',
            'description': "A library that interprets Java serialized objects. It also comes with a command-line tool that can generate compilable class declarations, extract block data, and print textual representations of instance values.",
            'aliases': ["jdeserialize", "jdeserialize"],
        },
        {
            'name': 'jexboss',
            'description': "Jboss verify and Exploitation Tool.",
            'aliases': ["jexboss", "jexboss"],
        },
        {
            'name': 'jira-scan',
            'description': "A simple remote scanner for Atlassian Jira",
            'aliases': ["jira-scan", "jira scan"],
        },
        {
            'name': 'jok3r',
            'description': "Network and Web Pentest Framework.",
            'aliases': ["jok3r", "jok3r"],
        },
        {
            'name': 'jomplug',
            'description': "This php script fingerprints a given Joomla system and then uses Packet Storm\'s archive to check for bugs related to the installed components.",
            'aliases': ["jomplug", "jomplug"],
        },
        {
            'name': 'jooforce',
            'description': "A Joomla password brute force tester.",
            'aliases': ["jooforce", "jooforce"],
        },
        {
            'name': 'joomlascan',
            'description': "Joomla scanner scans for known vulnerable remote file inclusion paths and files.",
            'aliases': ["joomlascan", "joomlascan"],
        },
        {
            'name': 'joomlavs',
            'description': "A black box, Ruby powered, Joomla vulnerability scanner.",
            'aliases': ["joomlavs", "joomlavs"],
        },
        {
            'name': 'joomscan',
            'description': "Detects file inclusion, sql injection, command execution vulnerabilities of a target Joomla! web site.",
            'aliases': ["joomscan", "joomla scan"],
        },
        {
            'name': 'jshell',
            'description': "Get a JavaScript shell with XSS.",
            'aliases': ["jshell", "jshell"],
        },
        {
            'name': 'jsonbee',
            'description': "A ready to use JSONP endpoints/payloads to help bypass content security policy (CSP).",
            'aliases': ["jsonbee", "jsonbee"],
        },
        {
            'name': 'jsparser',
            'description': "Parse javascript using Tornado and JSBeautifier to discover interesting enpoints.",
            'aliases': ["jsparser", "jsparser"],
        },
        {
            'name': 'jsql-injection',
            'description': "A Java application for automatic SQL database injection.",
            'aliases': ["jsql-injection", "jsql injection"],
        },
        {
            'name': 'jstillery',
            'description': "Advanced JavaScript Deobfuscation via Partial Evaluation.",
            'aliases': ["jstillery", "jstillery"],
        },
        {
            'name': 'juumla',
            'description': "Python tool created to identify Joomla version, scan for vulnerabilities and search for config files.",
            'aliases': ["juumla", "juumla"],
        },
        {
            'name': 'jwt-hack',
            'description': "A tool for hacking / security testing to JWT.",
            'aliases': ["jwt-hack", "jwt hack"],
        },
        {
            'name': 'kadimus',
            'description': "LFI Scan & Exploit Tool.",
            'aliases': ["kadimus", "kadimus"],
        },
        {
            'name': 'katana-pd',
            'description': "Crawling and spidering framework.",
            'aliases': ["katana-pd", "katana pd"],
        },
        {
            'name': 'kiterunner',
            'description': "Contextual Content Discovery Tool.",
            'aliases': ["kiterunner", "kiterunner"],
        },
        {
            'name': 'konan',
            'description': "Advanced Web Application Dir Scanner.",
            'aliases': ["konan", "konan"],
        },
        {
            'name': 'kubolt',
            'description': "Utility for scanning public kubernetes clusters.",
            'aliases': ["kubolt", "kubolt"],
        },
        {
            'name': 'lfi-exploiter',
            'description': "This perl script leverages /proc/self/environ to attempt getting code execution out of a local file inclusion vulnerability..",
            'aliases': ["lfi-exploiter", "lfi exploiter"],
        },
        {
            'name': 'lfi-fuzzploit',
            'description': "A simple tool to help in the fuzzing for, finding, and exploiting of local file inclusion vulnerabilities in Linux-based PHP applications.",
            'aliases': ["lfi-fuzzploit", "lfi fuzzploit"],
        },
        {
            'name': 'lfi-image-helper',
            'description': "A simple script to infect images with PHP Backdoors for local file inclusion attacks.",
            'aliases': ["lfi-image-helper", "lfi image helper"],
        },
        {
            'name': 'lfi-sploiter',
            'description': "This tool helps you exploit LFI (Local File Inclusion) vulnerabilities. Post discovery, simply pass the affected URL and vulnerable parameter to this tool. You can also use this tool to scan a URL for LFI vulnerabilities.",
            'aliases': ["lfi-sploiter", "lfi sploiter"],
        },
        {
            'name': 'lfifreak',
            'description': "A unique automated LFi Exploiter with Bind/Reverse Shells.",
            'aliases': ["lfifreak", "lfifreak"],
        },
        {
            'name': 'lfimap',
            'description': "Local file inclusion discovery and exploitation tool.",
            'aliases': ["lfimap", "lfimap"],
        },
        {
            'name': 'liffy',
            'description': "A Local File Inclusion Exploitation tool.",
            'aliases': ["liffy", "liffy"],
        },
        {
            'name': 'lightbulb',
            'description': "Python framework for auditing web applications firewalls.",
            'aliases': ["lightbulb", "lightbulb"],
        },
        {
            'name': 'linkfinder',
            'description': "Discovers endpoint and their parameters in JavaScript files.",
            'aliases': ["linkfinder", "linkfinder"],
        },
        {
            'name': 'list-urls',
            'description': "Extracts links from webpage.",
            'aliases': ["list-urls", "list urls"],
        },
        {
            'name': 'log4j-bypass',
            'description': "Log4j web app tester that includes WAF bypasses.",
            'aliases': ["log4j-bypass", "log4j bypass"],
        },
        {
            'name': 'log4j-scan',
            'description': "A fully automated, accurate, and extensive scanner for finding log4j RCE CVE-44228.",
            'aliases': ["log4j-scan", "log4j scan"],
        },
        {
            'name': 'lorsrf',
            'description': "Find the parameters that can be used to find SSRF or Out-of-band resource load.",
            'aliases': ["lorsrf", "lorsrf"],
        },
        {
            'name': 'lulzbuster',
            'description': "A multithreaded, very fast and smart HTTP(S) directory and file bruteforcer written in C on top of libcurl.",
            'aliases': ["lulzbuster", "lulzbuster"],
        },
        {
            'name': 'magescan',
            'description': "Scan a Magento site for information.",
            'aliases': ["magescan", "magescan"],
        },
        {
            'name': 'malicious-pdf',
            'description': "Generate a bunch of malicious pdf files with phone-home functionality.",
            'aliases': ["malicious-pdf", "malicious pdf"],
        },
        {
            'name': 'mando.me',
            'description': "Web Command Injection Tool.",
            'aliases': ["mando.me", "mando.me"],
        },
        {
            'name': 'maryam',
            'description': "OSINT Framework",
            'aliases': ["maryam", "maryam"],
        },
        {
            'name': 'meg',
            'description': "Fetch many paths for many hosts - without killing the hosts.",
            'aliases': ["meg", "meg"],
        },
        {
            'name': 'metoscan',
            'description': "Tool for scanning the HTTP methods supported by a webserver.",
            'aliases': ["metoscan", "metoscan"],
        },
        {
            'name': 'monsoon',
            'description': "A fast HTTP enumerator that allows you to execute a large number of HTTP requests.",
            'aliases': ["monsoon", "monsoon"],
        },
        {
            'name': 'mooscan',
            'description': "A scanner for Moodle LMS.",
            'aliases': ["mooscan", "mooscan"],
        },
        {
            'name': 'morxtraversal',
            'description': "Path Traversal checking tool.",
            'aliases': ["morxtraversal", "morxtraversal"],
        },
        {
            'name': 'multiinjector',
            'description': "Automatic SQL injection utility using a lsit of URI addresses to test parameter manipulation.",
            'aliases': ["multiinjector", "multiinjector"],
        },
        {
            'name': 'nosqli',
            'description': "NoSQL scanner and injector.",
            'aliases': ["nosqli", "nosqli"],
        },
        {
            'name': 'nosqlmap',
            'description': "Automated Mongo database and NoSQL web application exploitation tool",
            'aliases': ["nosqlmap", "nosqlmap"],
        },
        {
            'name': 'novahot',
            'description': "A webshell framework for penetration testers.",
            'aliases': ["novahot", "novahot"],
        },
        {
            'name': 'okadminfinder',
            'description': "Tool to find admin panels / admin login pages.",
            'aliases': ["okadminfinder", "okadminfinder"],
        },
        {
            'name': 'onionsearch',
            'description': "Script that scrapes urls on different .onion search engines.",
            'aliases': ["onionsearch", "onionsearch"],
        },
        {
            'name': 'opendoor',
            'description': "OWASP WEB Directory Scanner.",
            'aliases': ["opendoor", "opendoor"],
        },
        {
            'name': 'owasp-bywaf',
            'description': "A web application penetration testing framework (WAPTF).",
            'aliases': ["owasp-bywaf", "owasp bywaf"],
        },
        {
            'name': 'owtf',
            'description': "The Offensive (Web) Testing Framework.",
            'aliases': ["owtf", "owtf"],
        },
        {
            'name': 'pappy-proxy',
            'description': "An intercepting proxy for web application testing.",
            'aliases': ["pappy-proxy", "pappy proxy"],
        },
        {
            'name': 'parameth',
            'description': "This tool can be used to brute discover GET and POST parameters.",
            'aliases': ["parameth", "parameth"],
        },
        {
            'name': 'parampampam',
            'description': "This tool for brute discover GET and POST parameters.",
            'aliases': ["parampampam", "parampampam"],
        },
        {
            'name': 'paramspider',
            'description': "Mining URLs from dark corners of Web Archives for bug hunting/fuzzing/further probing.",
            'aliases': ["paramspider", "param spider"],
        },
        {
            'name': 'paros',
            'description': "Java-based HTTP/HTTPS proxy for assessing web app vulnerabilities. Supports editing/viewing HTTP messages on-the-fly, spiders, client certificates, proxy-chaining, intelligent scanning for XSS and SQLi, etc.",
            'aliases': ["paros", "paros"],
        },
        {
            'name': 'payloadmask',
            'description': "Web Payload list editor to use techniques to try bypass web application firewall.",
            'aliases': ["payloadmask", "payloadmask"],
        },
        {
            'name': 'peepingtom',
            'description': "A tool to take screenshots of websites. Much like eyewitness.",
            'aliases': ["peepingtom", "peepingtom"],
        },
        {
            'name': 'phantomcollect',
            'description': "Lightweight stealth web data collection framework for ethical security testing.",
            'aliases': ["phantomcollect", "phantomcollect"],
        },
        {
            'name': 'photon',
            'description': "Incredibly fast crawler which extracts urls, emails, files, website accounts and much more.",
            'aliases': ["photon", "photon"],
        },
        {
            'name': 'php-findsock-shell',
            'description': "A Findsock Shell implementation in PHP + C.",
            'aliases': ["php-findsock-shell", "php findsock shell"],
        },
        {
            'name': 'php-malware-finder',
            'description': "Detect potentially malicious PHP files.",
            'aliases': ["php-malware-finder", "php malware finder"],
        },
        {
            'name': 'phpggc',
            'description': "A library of PHP unserialize() payloads along with a tool to generate them, from command line or programmatically.",
            'aliases': ["phpggc", "phpggc"],
        },
        {
            'name': 'phpsploit',
            'description': "Stealth post-exploitation framework.",
            'aliases': ["phpsploit", "phpsploit"],
        },
        {
            'name': 'pinkerton',
            'description': "JavaScript file crawler and secret finder.",
            'aliases': ["pinkerton", "pinkerton"],
        },
        {
            'name': 'pixload',
            'description': "Image Payload Creating/Injecting tools.",
            'aliases': ["pixload", "pixload"],
        },
        {
            'name': 'plecost',
            'description': "Wordpress finger printer Tool.",
            'aliases': ["plecost", "plecost"],
        },
        {
            'name': 'plown',
            'description': "A security scanner for Plone CMS.",
            'aliases': ["plown", "plown"],
        },
        {
            'name': 'poly',
            'description': "Polymorphic webshells.",
            'aliases': ["poly", "poly"],
        },
        {
            'name': 'pown',
            'description': "Security testing and exploitation toolkit built on top of Node.js and NPM.",
            'aliases': ["pown", "pown"],
        },
        {
            'name': 'ppfuzz',
            'description': "A fast tool to scan client-side prototype pollution vulnerability written in Rust.",
            'aliases': ["ppfuzz", "ppfuzz"],
        },
        {
            'name': 'ppmap',
            'description': "A scanner/exploitation tool written in GO, which leverages client-side Prototype Pollution to XSS by exploiting known gadgets.",
            'aliases': ["ppmap", "ppmap"],
        },
        {
            'name': 'proxenet',
            'description': "THE REAL hacker friendly proxy for web application pentests.",
            'aliases': ["proxenet", "proxenet"],
        },
        {
            'name': 'pwndrop',
            'description': "Self-deployable file hosting service for red teamers, allowing to easily upload and share payloads over HTTP and WebDAV.",
            'aliases': ["pwndrop", "pwndrop"],
        },
        {
            'name': 'pyfiscan',
            'description': "Free web-application vulnerability and version scanner.",
            'aliases': ["pyfiscan", "pyfiscan"],
        },
        {
            'name': 'python-witnessme',
            'description': "Web Inventory tool, takes screenshots of webpages using Pyppeteer.",
            'aliases': ["python-witnessme", "python witnessme"],
        },
        {
            'name': 'python2-jsbeautifier',
            'description': "JavaScript unobfuscator and beautifier.",
            'aliases': ["python2-jsbeautifier", "python2 jsbeautifier"],
        },
        {
            'name': 'rabid',
            'description': "A CLI tool and library allowing to simply decode all kind of BigIP cookies.",
            'aliases': ["rabid", "rabid"],
        },
        {
            'name': 'rapidscan',
            'description': "The Multi-Tool Web Vulnerability Scanner.",
            'aliases': ["rapidscan", "rapidscan"],
        },
        {
            'name': 'recollapse',
            'description': "Tool for black-box regex fuzzing to bypass validations and discover normalizations in web applications.",
            'aliases': ["recollapse", "recollapse"],
        },
        {
            'name': 'remot3d',
            'description': "An Simple Exploit for PHP Language.",
            'aliases': ["remot3d", "remot3d"],
        },
        {
            'name': 'restler-fuzzer',
            'description': "First stateful REST API fuzzing tool for automatically testing cloud services through their REST APIs and finding security and reliability bugs in these services.",
            'aliases': ["restler-fuzzer", "restler fuzzer"],
        },
        {
            'name': 'riwifshell',
            'description': "Web backdoor - infector - explorer.",
            'aliases': ["riwifshell", "riwifshell"],
        },
        {
            'name': 'rookie',
            'description': "Load cookies from your web browsers.",
            'aliases': ["rookie", "rookie"],
        },
        {
            'name': 'ruler',
            'description': "A tool to abuse Exchange services.",
            'aliases': ["ruler", "ruler"],
        },
        {
            'name': 'rustbuster',
            'description': "DirBuster for Rust.",
            'aliases': ["rustbuster", "rustbuster"],
        },
        {
            'name': 'rww-attack',
            'description': "Performs a dictionary attack against a live Microsoft Windows Small Business Server.",
            'aliases': ["rww-attack", "rww attack"],
        },
        {
            'name': 'sawef',
            'description': "Send Attack Web Forms.",
            'aliases': ["sawef", "sawef"],
        },
        {
            'name': 'scanqli',
            'description': "SQLi scanner to detect SQL vulns.",
            'aliases': ["scanqli", "scanqli"],
        },
        {
            'name': 'scrying',
            'description': "Collect RDP, web, and VNC screenshots smartly.",
            'aliases': ["scrying", "scrying"],
        },
        {
            'name': 'second-order',
            'description': "Second-order subdomain takeover scanner.",
            'aliases': ["second-order", "second order"],
        },
        {
            'name': 'secretfinder',
            'description': "A python script to find sensitive data (apikeys, accesstoken, jwt,..) in javascript files.",
            'aliases': ["secretfinder", "secret finder"],
        },
        {
            'name': 'secscan',
            'description': "Web Apps Scanner and Much more utilities.",
            'aliases': ["secscan", "secscan"],
        },
        {
            'name': 'see-surf',
            'description': "Security tool to find potential vulnerable Server Side Request Forgery (SSRF) parameters.",
            'aliases': ["see-surf", "see surf"],
        },
        {
            'name': 'serializationdumper',
            'description': "A tool to dump Java serialization streams in a more human readable form.",
            'aliases': ["serializationdumper", "serializationdumper"],
        },
        {
            'name': 'shortfuzzy',
            'description': "A web fuzzing script written in perl.",
            'aliases': ["shortfuzzy", "shortfuzzy"],
        },
        {
            'name': 'shuffledns',
            'description': "A wrapper around massdns written in GO.",
            'aliases': ["shuffledns", "shuffle dns"],
        },
        {
            'name': 'sitadel',
            'description': "Web Application Security Scanner.",
            'aliases': ["sitadel", "sitadel"],
        },
        {
            'name': 'sitediff',
            'description': "Fingerprint a web app using local files as the fingerprint sources.",
            'aliases': ["sitediff", "sitediff"],
        },
        {
            'name': 'sj',
            'description': "A tool for auditing endpoints defined in exposed (Swagger/OpenAPI) definition files.",
            'aliases': ["sj", "sj"],
        },
        {
            'name': 'skipfish',
            'description': "A fully automated, active web application security reconnaissance tool.",
            'aliases': ["skipfish", "skipfish"],
        },
        {
            'name': 'smplshllctrlr',
            'description': "PHP Command Injection exploitation tool.",
            'aliases': ["smplshllctrlr", "smplshllctrlr"],
        },
        {
            'name': 'smuggler',
            'description': "An HTTP Request Smuggling / Desync testing tool written in Python 3.",
            'aliases': ["smuggler", "smuggler"],
        },
        {
            'name': 'smuggler-py',
            'description': "Python tool used to test for HTTP Desync/Request Smuggling attacks.",
            'aliases': ["smuggler-py", "smuggler py"],
        },
        {
            'name': 'snallygaster',
            'description': "Tool to scan for secret files on HTTP servers.",
            'aliases': ["snallygaster", "snallygaster"],
        },
        {
            'name': 'snuck',
            'description': "Automatic XSS filter bypass.",
            'aliases': ["snuck", "snuck"],
        },
        {
            'name': 'sourcemapper',
            'description': "Extract JavaScript source trees from Sourcemap files.",
            'aliases': ["sourcemapper", "sourcemapper"],
        },
        {
            'name': 'spaf',
            'description': "Static Php Analysis and Fuzzer.",
            'aliases': ["spaf", "spaf"],
        },
        {
            'name': 'sparty',
            'description': "An open source tool written in python to audit web applications using sharepoint and frontpage architecture.",
            'aliases': ["sparty", "sparty"],
        },
        {
            'name': 'spiga',
            'description': "Configurable web resource scanner.",
            'aliases': ["spiga", "spiga"],
        },
        {
            'name': 'spike-proxy',
            'description': "A Proxy for detecting vulnerabilities in web applications",
            'aliases': ["spike-proxy", "spike proxy"],
        },
        {
            'name': 'spipscan',
            'description': "SPIP (CMS) scanner for penetration testing purpose written in Python.",
            'aliases': ["spipscan", "spipscan"],
        },
        {
            'name': 'sprayingtoolkit',
            'description': "Scripts to make password spraying attacks against Lync/S4B & OWA a lot quicker, less painful and more efficient.",
            'aliases': ["sprayingtoolkit", "sprayingtoolkit"],
        },
        {
            'name': 'sqid',
            'description': "A SQL injection digger.",
            'aliases': ["sqid", "sqid"],
        },
        {
            'name': 'ssrf-sheriff',
            'description': "A simple SSRF-testing sheriff written in Go.",
            'aliases': ["ssrf-sheriff", "ssrf sheriff"],
        },
        {
            'name': 'ssrfmap',
            'description': "Automatic SSRF fuzzer and exploitation tool.",
            'aliases': ["ssrfmap", "ssrfmap"],
        },
        {
            'name': 'stews',
            'description': "A Security Tool for Enumerating WebSockets.",
            'aliases': ["stews", "stews"],
        },
        {
            'name': 'striker',
            'description': "An offensive information and vulnerability scanner.",
            'aliases': ["striker", "striker"],
        },
        {
            'name': 'subjs',
            'description': "Fetches javascript file from a list of URLS or subdomains.",
            'aliases': ["subjs", "subjs"],
        },
        {
            'name': 'themole',
            'description': "Automatic SQL injection exploitation tool.",
            'aliases': ["themole", "themole"],
        },
        {
            'name': 'tidos-framework',
            'description': "Offensive Web Application Penetration Testing Framework.",
            'aliases': ["tidos-framework", "tidos framework"],
        },
        {
            'name': 'tinja',
            'description': "CLI tool for testing web pages for template injection vulnerabilities.",
            'aliases': ["tinja", "tinja"],
        },
        {
            'name': 'torcrawl',
            'description': "Crawl and extract (regular or onion) webpages through TOR network.",
            'aliases': ["torcrawl", "torcrawl"],
        },
        {
            'name': 'tplmap',
            'description': "Automatic Server-Side Template Injection Detection and Exploitation Tool.",
            'aliases': ["tplmap", "tplmap"],
        },
        {
            'name': 'typo3scan',
            'description': "Enumerate Typo3 version and extensions.",
            'aliases': ["typo3scan", "typo3scan"],
        },
        {
            'name': 'uncaptcha2',
            'description': "Defeating the latest version of ReCaptcha with 91% accuracy.",
            'aliases': ["uncaptcha2", "uncaptcha2"],
        },
        {
            'name': 'uppwn',
            'description': "A script that automates detection of security flaws on websites\' file upload systems\'.",
            'aliases': ["uppwn", "uppwn"],
        },
        {
            'name': 'urlcrazy',
            'description': "Generate and test domain typos and variations to detect and perform typo squatting, URL hijacking, phishing, and corporate espionage.",
            'aliases': ["urlcrazy", "urlcrazy"],
        },
        {
            'name': 'urldigger',
            'description': "A python tool to extract URL addresses from different HOT sources and/or detect SPAM and malicious code",
            'aliases': ["urldigger", "urldigger"],
        },
        {
            'name': 'urlextractor',
            'description': "Information gathering & website reconnaissance.",
            'aliases': ["urlextractor", "urlextractor"],
        },
        {
            'name': 'urx',
            'description': "Extracts URLs from OSINT Archives for Security Insights.",
            'aliases': ["urx", "urx"],
        },
        {
            'name': 'vane',
            'description': "A vulnerability scanner which checks the security of WordPress installations using a black box approach.",
            'aliases': ["vane", "vane"],
        },
        {
            'name': 'vanguard',
            'description': "A comprehensive web penetration testing tool written in Perl thatidentifies vulnerabilities in web applications.",
            'aliases': ["vanguard", "vanguard"],
        },
        {
            'name': 'vbscan',
            'description': "A black box vBulletin vulnerability scanner written in perl.",
            'aliases': ["vbscan", "vbscan"],
        },
        {
            'name': 'vega',
            'description': "An open source platform to test the security of web applications.",
            'aliases': ["vega", "vega"],
        },
        {
            'name': 'vsvbp',
            'description': "Black box tool for Vulnerability detection in web applications.",
            'aliases': ["vsvbp", "vsvbp"],
        },
        {
            'name': 'vulnerabilities-spider',
            'description': "A tool to scan for web vulnerabilities.",
            'aliases': ["vulnerabilities-spider", "vulnerabilities spider"],
        },
        {
            'name': 'vulnx',
            'description': "Cms and vulnerabilites detector & An intelligent bot auto shell injector.",
            'aliases': ["vulnx", "vulnx"],
        },
        {
            'name': 'w13scan',
            'description': "Passive Security Scanner.",
            'aliases': ["w13scan", "w13scan"],
        },
        {
            'name': 'wafninja',
            'description': "A tool which contains two functions to attack Web Application Firewalls.",
            'aliases': ["wafninja", "wafninja"],
        },
        {
            'name': 'wafp',
            'description': "An easy to use Web Application Finger Printing tool written in ruby using sqlite3 databases for storing the fingerprints.",
            'aliases': ["wafp", "wafp"],
        },
        {
            'name': 'wafpass',
            'description': "Analysing parameters with all payloads\' bypass methods, aiming at benchmarking security solutions like WAF.",
            'aliases': ["wafpass", "wafpass"],
        },
        {
            'name': 'wapiti',
            'description': "A vulnerability scanner for web applications.",
            'aliases': ["wapiti", "wapiti"],
        },
        {
            'name': 'wascan',
            'description': "Web Application Scanner.",
            'aliases': ["wascan", "wascan"],
        },
        {
            'name': 'waybackpack',
            'description': "Download the entire Wayback Machine archive for a given URL.",
            'aliases': ["waybackpack", "waybackpack"],
        },
        {
            'name': 'wayparam',
            'description': "Fetch and normalize parameterized URLs from the Wayback CDX API.",
            'aliases': ["wayparam", "wayparam"],
        },
        {
            'name': 'wcvs',
            'description': "Web Cache Vulnerability Scanner is a Go-based CLI tool for testing for web cache poisoning.",
            'aliases': ["wcvs", "wcvs"],
        },
        {
            'name': 'web-soul',
            'description': "A plugin based scanner for attacking and data mining web sites written in Perl.",
            'aliases': ["web-soul", "web soul"],
        },
        {
            'name': 'webanalyze',
            'description': "Port of Wappalyzer (uncovers technologies used on websites) in go to automate scanning.",
            'aliases': ["webanalyze", "webanalyze"],
        },
        {
            'name': 'webborer',
            'description': "A directory-enumeration tool written in Go.",
            'aliases': ["webborer", "webborer"],
        },
        {
            'name': 'webhandler',
            'description': "A handler for PHP system functions & also an alternative \'netcat\' handler.",
            'aliases': ["webhandler", "webhandler"],
        },
        {
            'name': 'webkiller',
            'description': "Tool Information Gathering Write By Python.",
            'aliases': ["webkiller", "webkiller"],
        },
        {
            'name': 'webshells',
            'description': "Web Backdoors.",
            'aliases': ["webshells", "webshells"],
        },
        {
            'name': 'webslayer',
            'description': "A tool designed for brute forcing Web Applications.",
            'aliases': ["webslayer", "webslayer"],
        },
        {
            'name': 'webtech',
            'description': "Identify technologies used on websites.",
            'aliases': ["webtech", "webtech"],
        },
        {
            'name': 'webxploiter',
            'description': "An OWASP Top 10 Security scanner.",
            'aliases': ["webxploiter", "webxploiter"],
        },
        {
            'name': 'weevely',
            'description': "Weaponized web shell.",
            'aliases': ["weevely", "weevely"],
        },
        {
            'name': 'weirdaal',
            'description': "AWS Attack Library.",
            'aliases': ["weirdaal", "weirdaal"],
        },
        {
            'name': 'whatwaf',
            'description': "Detect and bypass web application firewalls and protection systems.",
            'aliases': ["whatwaf", "whatwaf"],
        },
        {
            'name': 'whichcdn',
            'description': "Tool to detect if a given website is protected by a Content Delivery Network.",
            'aliases': ["whichcdn", "whichcdn"],
        },
        {
            'name': 'wig',
            'description': "WebApp Information Gatherer.",
            'aliases': ["wig", "wig"],
        },
        {
            'name': 'witchxtool',
            'description': "A perl script that consists of a port scanner, LFI scanner, MD5 bruteforcer, dork SQL injection scanner, fresh proxy scanner, and a dork LFI scanner.",
            'aliases': ["witchxtool", "witchxtool"],
        },
        {
            'name': 'wordpress-exploit-framework',
            'description': "A Ruby framework for developing and using modules which aid in the penetration testing of WordPress powered websites and systems.",
            'aliases': ["wordpress-exploit-framework", "wordpress exploit framework"],
        },
        {
            'name': 'wpforce',
            'description': "Wordpress Attack Suite.",
            'aliases': ["wpforce", "wpforce"],
        },
        {
            'name': 'wpintel',
            'description': "Chrome extension designed for WordPress Vulnerability Scanning and information gathering.",
            'aliases': ["wpintel", "wpintel"],
        },
        {
            'name': 'wpprobe',
            'description': "A fast WordPress plugin enumeration tool.",
            'aliases': ["wpprobe", "wpprobe"],
        },
        {
            'name': 'wpseku',
            'description': "Simple Wordpress Security Scanner.",
            'aliases': ["wpseku", "wpseku"],
        },
        {
            'name': 'ws-attacker',
            'description': "A modular framework for web services penetration testing.",
            'aliases': ["ws-attacker", "ws attacker"],
        },
        {
            'name': 'wssip',
            'description': "Application for capturing, modifying and sending custom WebSocket data from client to server and vice versa.",
            'aliases': ["wssip", "wssip"],
        },
        {
            'name': 'wuzz',
            'description': "Interactive cli tool for HTTP inspection.",
            'aliases': ["wuzz", "wuzz"],
        },
        {
            'name': 'x8',
            'description': "Hidden parameters discovery suite.",
            'aliases': ["x8", "x8"],
        },
        {
            'name': 'xmlrpc-bruteforcer',
            'description': "An XMLRPC brute forcer targeting Wordpress written in Python 3.",
            'aliases': ["xmlrpc-bruteforcer", "xmlrpc bruteforcer"],
        },
        {
            'name': 'xspear',
            'description': "Powerful XSS Scanning and Parameter analysis tool&gem.",
            'aliases': ["xspear", "xspear"],
        },
        {
            'name': 'xsrfprobe',
            'description': "The Prime Cross Site Request Forgery Audit and Exploitation Toolkit.",
            'aliases': ["xsrfprobe", "xsrfprobe"],
        },
        {
            'name': 'xss-freak',
            'description': "An XSS scanner fully written in Python3 from scratch.",
            'aliases': ["xss-freak", "xss freak"],
        },
        {
            'name': 'xsscon',
            'description': "Simple XSS Scanner tool.",
            'aliases': ["xsscon", "xsscon"],
        },
        {
            'name': 'xsscrapy',
            'description': "XSS spider - 66/66 wavsep XSS detected.",
            'aliases': ["xsscrapy", "xsscrapy"],
        },
        {
            'name': 'xsser',
            'description': "A penetration testing tool for detecting and exploiting XSS vulnerabilites.",
            'aliases': ["xsser", "xsser.py", "cross site scripter"],
        },
        {
            'name': 'xssless',
            'description': "An automated XSS payload generator written in python.",
            'aliases': ["xssless", "xssless"],
        },
        {
            'name': 'xsspy',
            'description': "Web Application XSS Scanner.",
            'aliases': ["xsspy", "xsspy"],
        },
        {
            'name': 'xsss',
            'description': "A brute force cross site scripting scanner.",
            'aliases': ["xsss", "xsss"],
        },
        {
            'name': 'xssscan',
            'description': "Command line tool for detection of XSS attacks in URLs. Based on ModSecurity rules from OWASP CRS.",
            'aliases': ["xssscan", "xssscan"],
        },
        {
            'name': 'xsssniper',
            'description': "An automatic XSS discovery tool",
            'aliases': ["xsssniper", "xsssniper"],
        },
        {
            'name': 'xsstrike',
            'description': "An advanced XSS detection and exploitation suite.",
            'aliases': ["xsstrike", "xsstrike"],
        },
        {
            'name': 'xssya',
            'description': "A Cross Site Scripting Scanner & Vulnerability Confirmation.",
            'aliases': ["xssya", "xssya"],
        },
        {
            'name': 'xwaf',
            'description': "Automatic WAF bypass tool.",
            'aliases': ["xwaf", "xwaf"],
        },
        {
            'name': 'xxxpwn',
            'description': "A tool Designed for blind optimized XPath 1 injection attacks.",
            'aliases': ["xxxpwn", "xxxpwn"],
        },
        {
            'name': 'xxxpwn-smart',
            'description': "A fork of xxxpwn adding further optimizations and tweaks.",
            'aliases': ["xxxpwn-smart", "xxxpwn smart"],
        },
        {
            'name': 'yaaf',
            'description': "Yet Another Admin Finder.",
            'aliases': ["yaaf", "yaaf"],
        },
        {
            'name': 'yasuo',
            'description': "A ruby script that scans for vulnerable & exploitable 3rd-party web applications on a network.",
            'aliases': ["yasuo", "yasuo"],
        },
        {
            'name': 'yawast',
            'description': "The YAWAST Antecedent Web Application Security Toolkit.",
            'aliases': ["yawast", "yawast"],
        },
        {
            'name': 'ycrawler',
            'description': "A web crawler that is useful for grabbing all user supplied input related to a given website and will save the output. It has proxy and log file support.",
            'aliases': ["ycrawler", "ycrawler"],
        },
        {
            'name': 'ysoserial',
            'description': "A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization.",
            'aliases': ["ysoserial", "ysoserial"],
        },
    ],

    # Scanner (309 tools)
    'blackarch-scanner': [
        {
            'name': '0trace',
            'description': "A hop enumeration tool.",
            'aliases': ["0trace", "0trace"],
        },
        {
            'name': 'a2sv',
            'description': "Auto Scanning to SSL Vulnerability.",
            'aliases': ["a2sv", "a2sv"],
        },
        {
            'name': 'admsnmp',
            'description': "ADM SNMP audit scanner.",
            'aliases': ["admsnmp", "admsnmp"],
        },
        {
            'name': 'allthevhosts',
            'description': "A vhost discovery tool that scrapes various web applications.",
            'aliases': ["allthevhosts", "allthevhosts"],
        },
        {
            'name': 'amap',
            'description': "Next-generation tool for assisting network penetration testing.",
            'aliases': ["amap", "amap"],
        },
        {
            'name': 'amass',
            'description': "In-depth subdomain enumeration written in Go.",
            'aliases': ["amass", "amass enum"],
        },
        {
            'name': 'anubis-netsec',
            'description': "Subdomain enumeration and information gathering tool.",
            'aliases': ["anubis-netsec", "anubis netsec"],
        },
        {
            'name': 'apache-users',
            'description': "This perl script will enumerate the usernames on a unix system that use the apache module UserDir.",
            'aliases': ["apache-users", "apache users"],
        },
        {
            'name': 'apachetomcatscanner',
            'description': "Apache Tomcat vulnerability scanner.",
            'aliases': ["apachetomcatscanner", "apachetomcatscanner"],
        },
        {
            'name': 'arjun',
            'description': "HTTP parameter discovery suite.",
            'aliases': ["arjun", "arjun"],
        },
        {
            'name': 'assassingo',
            'description': "Web pentest framework for information gathering and vulnerability scanning.",
            'aliases': ["assassingo", "assassingo"],
        },
        {
            'name': 'assetfinder',
            'description': "Find domains and subdomains potentially related to a given domain.",
            'aliases': ["assetfinder", "assetfinder"],
        },
        {
            'name': 'athena-ssl-scanner',
            'description': "A SSL cipher scanner that checks all cipher codes. It can identify about 150 different ciphers.",
            'aliases': ["athena-ssl-scanner", "athena ssl scanner"],
        },
        {
            'name': 'atscan',
            'description': "Server, Site and Dork Scanner.",
            'aliases': ["atscan", "atscan"],
        },
        {
            'name': 'attk',
            'description': "Trend Micro Anti-Threat Toolkit.",
            'aliases': ["attk", "attk"],
        },
        {
            'name': 'aws-extender-cli',
            'description': "Script to test S3 buckets as well as Google Storage buckets and Azure Storage containers for common misconfiguration issues.",
            'aliases': ["aws-extender-cli", "aws extender cli"],
        },
        {
            'name': 'aws-iam-privesc',
            'description': "AWS IAM policy scanner that helps determine where privilege escalation can be achieved.",
            'aliases': ["aws-iam-privesc", "aws iam privesc"],
        },
        {
            'name': 'barmie',
            'description': "Java RMI enumeration and attack tool.",
            'aliases': ["barmie", "barmie"],
        },
        {
            'name': 'bashscan',
            'description': "A port scanner built to utilize /dev/tcp for network and service discovery.",
            'aliases': ["bashscan", "bashscan"],
        },
        {
            'name': 'belati',
            'description': "The Traditional Swiss Army Knife for OSINT.",
            'aliases': ["belati", "belati"],
        },
        {
            'name': 'bingoo',
            'description': "A Linux bash based Bing and Google Dorking Tool.",
            'aliases': ["bingoo", "bingoo"],
        },
        {
            'name': 'birp',
            'description': "A tool that will assist in the security assessment of mainframe applications served over TN3270.",
            'aliases': ["birp", "birp"],
        },
        {
            'name': 'blackbox-scanner',
            'description': "Dork scanner & bruteforcing & hash cracker with blackbox framework.",
            'aliases': ["blackbox-scanner", "blackbox scanner"],
        },
        {
            'name': 'bleah',
            'description': "A BLE scanner for \"smart\" devices hacking.",
            'aliases': ["bleah", "bleah"],
        },
        {
            'name': 'blindy',
            'description': "Simple script to automate brutforcing blind sql injection vulnerabilities.",
            'aliases': ["blindy", "blindy"],
        },
        {
            'name': 'bluto',
            'description': "Recon, Subdomain Bruting, Zone Transfers.",
            'aliases': ["bluto", "bluto"],
        },
        {
            'name': 'braa',
            'description': "A mass snmp scanner.",
            'aliases': ["braa", "braa"],
        },
        {
            'name': 'cameradar',
            'description': "Hacks its way into RTSP videosurveillance cameras.",
            'aliases': ["cameradar", "cameradar"],
        },
        {
            'name': 'camscan',
            'description': "A tool which will analyze the CAM table of Cisco switches to look for anamolies.",
            'aliases': ["camscan", "camscan"],
        },
        {
            'name': 'cangibrina',
            'description': "Dashboard Finder.",
            'aliases': ["cangibrina", "cangibrina"],
        },
        {
            'name': 'cecster',
            'description': "A tool to perform security testing against the HDMI CEC (Consumer Electronics Control) and HEC (HDMI Ethernet Channel) protocols.",
            'aliases': ["cecster", "cecster"],
        },
        {
            'name': 'cero',
            'description': "Scrape domain names from SSL certificates of arbitrary hosts.",
            'aliases': ["cero", "cero"],
        },
        {
            'name': 'changeme',
            'description': "A default credential scanner.",
            'aliases': ["changeme", "change me"],
        },
        {
            'name': 'check-weak-dh-ssh',
            'description': "Debian OpenSSL weak client Diffie-Hellman Exchange checker.",
            'aliases': ["check-weak-dh-ssh", "check weak dh ssh"],
        },
        {
            'name': 'chiron',
            'description': "An all-in-one IPv6 Penetration Testing Framework.",
            'aliases': ["chiron", "chiron"],
        },
        {
            'name': 'cipherscan',
            'description': "A very simple way to find out which SSL ciphersuites are supported by a target.",
            'aliases': ["cipherscan", "cipherscan"],
        },
        {
            'name': 'ciscos',
            'description': "Scans class A, B, and C networks for cisco routers which have telnet open and have not changed the default password from cisco.",
            'aliases': ["ciscos", "ciscos"],
        },
        {
            'name': 'clair',
            'description': "Vulnerability Static Analysis for Containers.",
            'aliases': ["clair", "clair"],
        },
        {
            'name': 'climber',
            'description': "Check UNIX/Linux systems for privilege escalation.",
            'aliases': ["climber", "climber"],
        },
        {
            'name': 'cloudflare-enum',
            'description': "Cloudflare DNS Enumeration Tool for Pentesters.",
            'aliases': ["cloudflare-enum", "cloudflare enum"],
        },
        {
            'name': 'cloudsploit',
            'description': "AWS security scanning checks.",
            'aliases': ["cloudsploit", "cloudsploit"],
        },
        {
            'name': 'cmsmap',
            'description': "A python open source Content Management System scanner that automates the process of detecting security flaws of the most popular CMSs.",
            'aliases': ["cmsmap", "cmsmap"],
        },
        {
            'name': 'configpush',
            'description': "This is a tool to span /8-sized networks quickly sending snmpset requests with default or otherwise specified community string to Cisco devices.",
            'aliases': ["configpush", "configpush"],
        },
        {
            'name': 'corstest',
            'description': "A simple CORS misconfigurations checker.",
            'aliases': ["corstest", "corstest"],
        },
        {
            'name': 'cpfinder',
            'description': "Simple script that looks for administrative web interfaces.",
            'aliases': ["cpfinder", "cpfinder"],
        },
        {
            'name': 'crackmapexec',
            'description': "A swiss army knife for pentesting Windows/Active Directory environments.",
            'aliases': ["crackmapexec", "cme", "crack map exec", "netexec"],
        },
        {
            'name': 'ct-exposer',
            'description': "An OSINT tool that discovers sub-domains by searching Certificate Transparency logs.",
            'aliases': ["ct-exposer", "ct exposer"],
        },
        {
            'name': 'cvechecker',
            'description': "The goal of cvechecker is to report about possible vulnerabilities on your system, by scanning the installed software and matching the results with the CVE database.",
            'aliases': ["cvechecker", "cvechecker"],
        },
        {
            'name': 'd-tect',
            'description': "Pentesting the Modern Web.",
            'aliases': ["d-tect", "d tect"],
        },
        {
            'name': 'darkbing',
            'description': "A tool written in python that leverages bing for mining data on systems that may be susceptible to SQL injection.",
            'aliases': ["darkbing", "darkbing"],
        },
        {
            'name': 'davtest',
            'description': "Tests WebDAV enabled servers by uploading test executable files, and then (optionally) uploading files which allow for command execution or other actions directly on the target.",
            'aliases': ["davtest", "davtest"],
        },
        {
            'name': 'dbusmap',
            'description': "Simple utility for enumerating D-Bus endpoints, an nmap for D-Bus.",
            'aliases': ["dbusmap", "dbusmap"],
        },
        {
            'name': 'dcrawl',
            'description': "Simple, but smart, multi-threaded web crawler for randomly gathering huge lists of unique domain names.",
            'aliases': ["dcrawl", "dcrawl"],
        },
        {
            'name': 'deblaze',
            'description': "Performs method enumeration and interrogation against flash remoting end points.",
            'aliases': ["deblaze", "deblaze"],
        },
        {
            'name': 'delldrac',
            'description': "DellDRAC and Dell Chassis Discovery and Brute Forcer.",
            'aliases': ["delldrac", "delldrac"],
        },
        {
            'name': 'dhcpig',
            'description': "Enhanced DHCPv4 and DHCPv6 exhaustion and fuzzing script written in python using scapy network library.",
            'aliases': ["dhcpig", "dhcpig"],
        },
        {
            'name': 'dirb',
            'description': "A web content scanner, brute forceing for hidden files.",
            'aliases': ["dirb", "dirbuster"],
        },
        {
            'name': 'dirbuster',
            'description': "An application designed to brute force directories and files names on web/application servers",
            'aliases': ["dirbuster", "dirbuster"],
        },
        {
            'name': 'dirscanner',
            'description': "This is a python script that scans webservers looking for administrative directories, php shells, and more.",
            'aliases': ["dirscanner", "dirscanner"],
        },
        {
            'name': 'dirstalk',
            'description': "Modern alternative to dirbuster/dirb.",
            'aliases': ["dirstalk", "dirstalk"],
        },
        {
            'name': 'dmitry',
            'description': "Deepmagic Information Gathering Tool.",
            'aliases': ["dmitry", "dmitry"],
        },
        {
            'name': 'dnmap',
            'description': "The distributed nmap framework.",
            'aliases': ["dnmap", "dnmap"],
        },
        {
            'name': 'dns2geoip',
            'description': "A simple python script that brute forces DNS and subsequently geolocates the found subdomains.",
            'aliases': ["dns2geoip", "dns2geoip"],
        },
        {
            'name': 'dnsa',
            'description': "A dns security swiss army knife.",
            'aliases': ["dnsa", "dnsa"],
        },
        {
            'name': 'dnsbf',
            'description': "Search for available domain names in an IP range.",
            'aliases': ["dnsbf", "dnsbf"],
        },
        {
            'name': 'dnscan',
            'description': "A python wordlist-based DNS subdomain scanner.",
            'aliases': ["dnscan", "dnscan"],
        },
        {
            'name': 'dnsgoblin',
            'description': "Nasty creature constantly searching for DNS servers. It uses standard dns querys and waits for the replies.",
            'aliases': ["dnsgoblin", "dnsgoblin"],
        },
        {
            'name': 'dnspredict',
            'description': "DNS prediction.",
            'aliases': ["dnspredict", "dnspredict"],
        },
        {
            'name': 'dnstwist',
            'description': "Domain name permutation engine for detecting typo squatting, phishing and corporate espionage.",
            'aliases': ["dnstwist", "dns twist"],
        },
        {
            'name': 'dockerscan',
            'description': "Docker security analysis & hacking tools.",
            'aliases': ["dockerscan", "dockerscan"],
        },
        {
            'name': 'dorkbot',
            'description': "Command-line tool to scan Google search results for vulnerabilities.",
            'aliases': ["dorkbot", "dorkbot"],
        },
        {
            'name': 'dorkme',
            'description': "Tool designed with the purpose of making easier the searching of vulnerabilities with Google Dorks, such as SQL Injection vulnerabilities.",
            'aliases': ["dorkme", "dorkme"],
        },
        {
            'name': 'dpscan',
            'description': "Drupal Vulnerability Scanner.",
            'aliases': ["dpscan", "dpscan"],
        },
        {
            'name': 'dripper',
            'description': "A fast, asynchronous DNS scanner; it can be used for enumerating subdomains and enumerating boxes via reverse DNS.",
            'aliases': ["dripper", "dripper"],
        },
        {
            'name': 'dvcs-ripper',
            'description': "Rip web accessible (distributed) version control systems: SVN/GIT/BZR/CVS/HG.",
            'aliases': ["dvcs-ripper", "dvcs ripper"],
        },
        {
            'name': 'eazy',
            'description': "This is a small python tool that scans websites to look for PHP shells, backups, admin panels, and more.",
            'aliases': ["eazy", "eazy"],
        },
        {
            'name': 'enum-shares',
            'description': "Tool that enumerates shared folders across the network and under a custom user account.",
            'aliases': ["enum-shares", "enum shares"],
        },
        {
            'name': 'enumiax',
            'description': "An IAX enumerator.",
            'aliases': ["enumiax", "enum iax"],
        },
        {
            'name': 'eternal-scanner',
            'description': "An internet scanner for exploit CVE-0144 (Eternal Blue).",
            'aliases': ["eternal-scanner", "eternal scanner"],
        },
        {
            'name': 'faradaysec',
            'description': "Collaborative Penetration Test and Vulnerability Management Platform.",
            'aliases': ["faradaysec", "faradaysec"],
        },
        {
            'name': 'fernmelder',
            'description': "Asynchronous mass DNS scanner.",
            'aliases': ["fernmelder", "fernmelder"],
        },
        {
            'name': 'fgscanner',
            'description': "An advanced, opensource URL scanner.",
            'aliases': ["fgscanner", "fgscanner"],
        },
        {
            'name': 'fi6s',
            'description': "IPv6 network scanner designed to be fast.",
            'aliases': ["fi6s", "fi6s"],
        },
        {
            'name': 'find-dns',
            'description': "A tool that scans networks looking for DNS servers.",
            'aliases': ["find-dns", "find dns"],
        },
        {
            'name': 'flashscanner',
            'description': "Flash XSS Scanner.",
            'aliases': ["flashscanner", "flashscanner"],
        },
        {
            'name': 'flunym0us',
            'description': "A Vulnerability Scanner for Wordpress and Moodle.",
            'aliases': ["flunym0us", "flunym0us"],
        },
        {
            'name': 'forkingportscanner',
            'description': "Simple and fast forking port scanner written in perl. Can only scan on host at a time, the forking is done on the specified port range. Or on the default range of 1. Has the ability to scan UDP or TCP, defaults to tcp.",
            'aliases': ["forkingportscanner", "forkingportscanner"],
        },
        {
            'name': 'fortiscan',
            'description': "A high performance FortiGate SSL-VPN vulnerability scanning and exploitation tool.",
            'aliases': ["fortiscan", "fortiscan"],
        },
        {
            'name': 'fs-nyarl',
            'description': "A network takeover & forensic analysis tool - useful to advanced PenTest tasks & for fun and profit.",
            'aliases': ["fs-nyarl", "fs nyarl"],
        },
        {
            'name': 'fscan',
            'description': "A Security Auditing Tool.",
            'aliases': ["fscan", "fscan"],
        },
        {
            'name': 'fsnoop',
            'description': "A tool to monitor file operations on GNU/Linux systems by using the Inotify mechanism. Its primary purpose is to help detecting file race condition vulnerabilities and since version 3, to exploit them with loadable DSO modules (also called \"payload modules\" or \"paymods\").",
            'aliases': ["fsnoop", "fsnoop"],
        },
        {
            'name': 'ftp-spider',
            'description': "FTP investigation tool - Scans ftp server for the following: reveal entire directory tree structures, detect anonymous access, detect directories with write permissions, find user specified data within repository.",
            'aliases': ["ftp-spider", "ftp spider"],
        },
        {
            'name': 'ftpscout',
            'description': "Scans ftps for anonymous access.",
            'aliases': ["ftpscout", "ftpscout"],
        },
        {
            'name': 'garak',
            'description': "The LLM vulnerability scanner.",
            'aliases': ["garak", "garak"],
        },
        {
            'name': 'gcpbucketbrute',
            'description': "A script to enumerate Google Storage buckets, determine what access you have to them, and determine if they can be privilege escalated.",
            'aliases': ["gcpbucketbrute", "gcpbucketbrute"],
        },
        {
            'name': 'gethsploit',
            'description': "Finding Ethereum nodes which are vulnerable to RPC-attacks.",
            'aliases': ["gethsploit", "gethsploit"],
        },
        {
            'name': 'gggooglescan',
            'description': "A Google scraper which performs automated searches and returns results of search queries in the form of URLs or hostnames.",
            'aliases': ["gggooglescan", "gggooglescan"],
        },
        {
            'name': 'ghost-phisher',
            'description': "GUI suite for phishing and penetration attacks.",
            'aliases': ["ghost-phisher", "ghost phisher"],
        },
        {
            'name': 'git-dump',
            'description': "Dump the contents of a remote git repository without directory listing enabled.",
            'aliases': ["git-dump", "git dump"],
        },
        {
            'name': 'git-dumper',
            'description': "A tool to dump a git repository from a website.",
            'aliases': ["git-dumper", "git dumper"],
        },
        {
            'name': 'gitrob',
            'description': "Reconnaissance tool for GitHub organizations.",
            'aliases': ["gitrob", "git rob"],
        },
        {
            'name': 'gloom',
            'description': "Linux Penetration Testing Framework.",
            'aliases': ["gloom", "gloom"],
        },
        {
            'name': 'glpwnme',
            'description': "GLPI vulnerabilities checking tool.",
            'aliases': ["glpwnme", "glpwnme"],
        },
        {
            'name': 'grabbb',
            'description': "Clean, functional, and fast banner scanner.",
            'aliases': ["grabbb", "grabbb"],
        },
        {
            'name': 'graphql-cop',
            'description': "GraphQL vulnerability scanner.",
            'aliases': ["graphql-cop", "graphql cop"],
        },
        {
            'name': 'grepforrfi',
            'description': "Simple script for parsing web logs for RFIs and Webshells v1.2",
            'aliases': ["grepforrfi", "grepforrfi"],
        },
        {
            'name': 'grype',
            'description': "A vulnerability scanner for container images and filesystems.",
            'aliases': ["grype", "grype"],
        },
        {
            'name': 'gtp-scan',
            'description': "A small python script that scans for GTP (GPRS tunneling protocol) speaking hosts.",
            'aliases': ["gtp-scan", "gtp scan"],
        },
        {
            'name': 'h2buster',
            'description': "A threaded, recursive, web directory brute-force scanner over HTTP/2.",
            'aliases': ["h2buster", "h2buster"],
        },
        {
            'name': 'habu',
            'description': "Python Network Hacking Toolkit.",
            'aliases': ["habu", "habu"],
        },
        {
            'name': 'hakku',
            'description': "Simple framework that has been made for penetration testing tools.",
            'aliases': ["hakku", "hakku"],
        },
        {
            'name': 'halberd',
            'description': "Halberd discovers HTTP load balancers. It is useful for web application security auditing and for load balancer configuration testing.",
            'aliases': ["halberd", "halberd"],
        },
        {
            'name': 'hbad',
            'description': "This tool allows you to test clients on the heartbleed bug.",
            'aliases': ["hbad", "hbad"],
        },
        {
            'name': 'hellraiser',
            'description': "Vulnerability Scanner.",
            'aliases': ["hellraiser", "hellraiser"],
        },
        {
            'name': 'hexhttp',
            'description': "Perform tests on HTTP headers and analyze the results to identify vulnerabilities and interesting behaviors.",
            'aliases': ["hexhttp", "hexhttp"],
        },
        {
            'name': 'hikpwn',
            'description': "A simple scanner for Hikvision devices with basic vulnerability scanning capabilities written in Python 3.8.",
            'aliases': ["hikpwn", "hikpwn"],
        },
        {
            'name': 'homepwn',
            'description': "Swiss Army Knife for Pentesting of IoT Devices.",
            'aliases': ["homepwn", "homepwn"],
        },
        {
            'name': 'hoppy',
            'description': "A python script which tests http methods for configuration issues leaking information or just to see if they are enabled.",
            'aliases': ["hoppy", "hoppy"],
        },
        {
            'name': 'host-extract',
            'description': "Ruby script tries to extract all IP/Host patterns in page response of a given URL and JavaScript/CSS files of that URL.",
            'aliases': ["host-extract", "host extract"],
        },
        {
            'name': 'hsecscan',
            'description': "A security scanner for HTTP response headers.",
            'aliases': ["hsecscan", "hsecscan"],
        },
        {
            'name': 'http-enum',
            'description': "A tool to enumerate the enabled HTTP methods supported on a webserver.",
            'aliases': ["http-enum", "http enum"],
        },
        {
            'name': 'httprobe',
            'description': "Take a list of domains and probe for working HTTP and HTTPS servers",
            'aliases': ["httprobe", "http probe"],
        },
        {
            'name': 'httpsscanner',
            'description': "A tool to test the strength of a SSL web server.",
            'aliases': ["httpsscanner", "httpsscanner"],
        },
        {
            'name': 'iaxscan',
            'description': "A Python based scanner for detecting live IAX/2 hosts and then enumerating (by bruteforce) users on those hosts.",
            'aliases': ["iaxscan", "iax scan"],
        },
        {
            'name': 'icmpquery',
            'description': "Send and receive ICMP queries for address mask and current time.",
            'aliases': ["icmpquery", "icmpquery"],
        },
        {
            'name': 'iis-shortname-scanner',
            'description': "An IIS shortname Scanner.",
            'aliases': ["iis-shortname-scanner", "iis shortname scanner"],
        },
        {
            'name': 'ike-scan',
            'description': "A tool that uses IKE protocol to discover, fingerprint and test IPSec VPN servers.",
            'aliases': ["ike-scan", "ike scan"],
        },
        {
            'name': 'ilo4-toolbox',
            'description': "Toolbox for HPE iLO4 analysis.",
            'aliases': ["ilo4-toolbox", "ilo4 toolbox"],
        },
        {
            'name': 'infip',
            'description': "A python script that checks output from netstat against RBLs from Spamhaus.",
            'aliases': ["infip", "infip"],
        },
        {
            'name': 'inurlbr',
            'description': "Advanced search in the search engines - Inurl scanner, dorker, exploiter.",
            'aliases': ["inurlbr", "inurlbr"],
        },
        {
            'name': 'ipscan',
            'description': "A very fast IP address and port scanner.",
            'aliases': ["ipscan", "ipscan"],
        },
        {
            'name': 'iptv',
            'description': "Search and brute force illegal iptv server.",
            'aliases': ["iptv", "iptv"],
        },
        {
            'name': 'ipv6toolkit',
            'description': "SI6 Networks\' IPv6 Toolkit.",
            'aliases': ["ipv6toolkit", "ipv6toolkit"],
        },
        {
            'name': 'jaadas',
            'description': "Joint Advanced Defect assEsment for android applications.",
            'aliases': ["jaadas", "jaadas"],
        },
        {
            'name': 'knock',
            'description': "Subdomain scanner.",
            'aliases': ["knock", "knock"],
        },
        {
            'name': 'knxmap',
            'description': "KNXnet/IP scanning and auditing tool for KNX home automation installations.",
            'aliases': ["knxmap", "knxmap"],
        },
        {
            'name': 'krbrelayx',
            'description': "Kerberos relaying and unconstrained delegation abuse toolkit.",
            'aliases': ["krbrelayx", "krbrelayx"],
        },
        {
            'name': 'kscan',
            'description': "Asset mapping tool that can perform port scanning, TCP fingerprinting and banner capture for specified assets.",
            'aliases': ["kscan", "kscan"],
        },
        {
            'name': 'kube-hunter',
            'description': "Hunt for security weaknesses in Kubernetes clusters.",
            'aliases': ["kube-hunter", "kube hunter"],
        },
        {
            'name': 'kubesploit',
            'description': "Cross-platform post-exploitation HTTP/2 Command & Control server.",
            'aliases': ["kubesploit", "kubesploit"],
        },
        {
            'name': 'kubestriker',
            'description': "A Blazing fast Security Auditing tool for Kubernetes.",
            'aliases': ["kubestriker", "kubestriker"],
        },
        {
            'name': 'laf',
            'description': "Login Area Finder: scans host/s for login panels.",
            'aliases': ["laf", "laf"],
        },
        {
            'name': 'leaklooker',
            'description': "Find open databases with Shodan.",
            'aliases': ["leaklooker", "leaklooker"],
        },
        {
            'name': 'letmefuckit-scanner',
            'description': "Scanner and Exploit Magento.",
            'aliases': ["letmefuckit-scanner", "letmefuckit scanner"],
        },
        {
            'name': 'leviathan',
            'description': "A mass audit toolkit which has wide range service discovery, brute force, SQL injection detection and running custom exploit capabilities.",
            'aliases': ["leviathan", "leviathan"],
        },
        {
            'name': 'lfi-scanner',
            'description': "This is a simple perl script that enumerates local file inclusion attempts when given a specific target.",
            'aliases': ["lfi-scanner", "lfi scanner"],
        },
        {
            'name': 'lfisuite',
            'description': "Totally Automatic LFI Exploiter (+ Reverse Shell) and Scanner.",
            'aliases': ["lfisuite", "lfisuite"],
        },
        {
            'name': 'linenum',
            'description': "Scripted Local Linux Enumeration & Privilege Escalation Checks",
            'aliases': ["linenum", "linenum"],
        },
        {
            'name': 'linux-smart-enumeration',
            'description': "Linux enumeration tool for pentesting and CTFs with verbosity levels.",
            'aliases': ["linux-smart-enumeration", "linux smart enumeration"],
        },
        {
            'name': 'littleblackbox',
            'description': "Penetration testing tool, search in a collection of thousands of private SSL keys extracted from various embedded devices.",
            'aliases': ["littleblackbox", "littleblackbox"],
        },
        {
            'name': 'locasploit',
            'description': "Local enumeration and exploitation framework.",
            'aliases': ["locasploit", "locasploit"],
        },
        {
            'name': 'logmepwn',
            'description': "A fully automated, reliable, super-fast, mass scanning and validation toolkit for the Log4J RCE CVE-44228 vulnerability.",
            'aliases': ["logmepwn", "logmepwn"],
        },
        {
            'name': 'lotophagi',
            'description': "a relatively compact Perl script designed to scan remote hosts for default (or common) Lotus NSF and BOX databases.",
            'aliases': ["lotophagi", "lotophagi"],
        },
        {
            'name': 'lunar',
            'description': "A UNIX security auditing tool based on several security frameworks.",
            'aliases': ["lunar", "lunar"],
        },
        {
            'name': 'maligno',
            'description': "An open source penetration testing tool written in python, that serves Metasploit payloads. It generates shellcode with msfvenom and transmits it over HTTP or HTTPS.",
            'aliases': ["maligno", "maligno"],
        },
        {
            'name': 'manspider',
            'description': "Spider entire networks for juicy files sitting on SMB shares. Search filenames or file content - regex supported!",
            'aliases': ["manspider", "manspider"],
        },
        {
            'name': 'mantra',
            'description': "Hunt down API key leaks in JS files and pages.",
            'aliases': ["mantra", "mantra toolkit"],
        },
        {
            'name': 'mitm6',
            'description': "Pwning IPv4 via IPv6.",
            'aliases': ["mitm6", "mitm6"],
        },
        {
            'name': 'modscan',
            'description': "A new tool designed to map a SCADA MODBUS TCP based network.",
            'aliases': ["modscan", "modscan"],
        },
        {
            'name': 'mongoaudit',
            'description': "A powerful MongoDB auditing and pentesting tool .",
            'aliases': ["mongoaudit", "mongoaudit"],
        },
        {
            'name': 'mqtt-pwn',
            'description': "A one-stop-shop for IoT Broker penetration-testing and security assessment operations.",
            'aliases': ["mqtt-pwn", "mqtt pwn"],
        },
        {
            'name': 'msmailprobe',
            'description': "Office 365 and Exchange Enumeration tool.",
            'aliases': ["msmailprobe", "msmailprobe"],
        },
        {
            'name': 'mssqlscan',
            'description': "A small multi-threaded tool that scans for Microsoft SQL Servers.",
            'aliases': ["mssqlscan", "mssqlscan"],
        },
        {
            'name': 'multiscanner',
            'description': "Modular file scanning/analysis framework.",
            'aliases': ["multiscanner", "multiscanner"],
        },
        {
            'name': 'naabu',
            'description': "A fast port scanner written in go with focus on reliability and simplicity.",
            'aliases': ["naabu", "naabu scanner"],
        },
        {
            'name': 'navgix',
            'description': "Multi-threaded golang tool that will check for nginx alias traversal vulnerabilities.",
            'aliases': ["navgix", "navgix"],
        },
        {
            'name': 'netbios-share-scanner',
            'description': "This tool could be used to check windows workstations and servers if they have accessible shared resources.",
            'aliases': ["netbios-share-scanner", "netbios share scanner"],
        },
        {
            'name': 'netexec',
            'description': "A Windows / Active Directory environments pentest tool.",
            'aliases': ["netexec", "nxc", "crackmapexec replacement"],
        },
        {
            'name': 'netscan',
            'description': "Tcp/Udp/Tor port scanner with: synpacket, connect TCP/UDP and socks5 (tor connection).",
            'aliases': ["netscan", "netscan"],
        },
        {
            'name': 'netscan2',
            'description': "Active / passive network scanner.",
            'aliases': ["netscan2", "netscan2"],
        },
        {
            'name': 'netz',
            'description': "Discover internet-wide misconfigurations while drinking coffee.",
            'aliases': ["netz", "netz"],
        },
        {
            'name': 'nili',
            'description': "Tool for Network Scan, Man in the Middle, Protocol Reverse Engineering and Fuzzing.",
            'aliases': ["nili", "nili"],
        },
        {
            'name': 'nimux',
            'description': "Pure-Nim network enumeration and remote execution toolkit.",
            'aliases': ["nimux", "nimux"],
        },
        {
            'name': 'nmbscan',
            'description': "Tool to scan the shares of a SMB/NetBIOS network, using the NMB/SMB/NetBIOS protocols.",
            'aliases': ["nmbscan", "nmbscan"],
        },
        {
            'name': 'nox-framework',
            'description': "OSINT & CTI Framework with 120+ sources, async performance, identity pivoting, and automated risk analysis.",
            'aliases': ["nox-framework", "nox framework"],
        },
        {
            'name': 'nray',
            'description': "Distributed port scanner.",
            'aliases': ["nray", "nray"],
        },
        {
            'name': 'ntlm-challenger',
            'description': "Parse NTLM over HTTP challenge messages.",
            'aliases': ["ntlm-challenger", "ntlm challenger"],
        },
        {
            'name': 'ntlm-scanner',
            'description': "A simple python tool based on Impacket that tests servers for various known NTLM vulnerabilities.",
            'aliases': ["ntlm-scanner", "ntlm scanner"],
        },
        {
            'name': 'ntlmrecon',
            'description': "A tool to enumerate information from NTLM authentication enabled web endpoints.",
            'aliases': ["ntlmrecon", "ntlmrecon"],
        },
        {
            'name': 'nuclei',
            'description': "A fast tool for configurable targeted scanning based on templates offering massive extensibility and ease of use.",
            'aliases': ["nuclei", "nuclei scanner"],
        },
        {
            'name': 'nuclei-templates',
            'description': "Community curated list of template files for the nuclei engine.",
            'aliases': ["nuclei-templates", "nuclei templates"],
        },
        {
            'name': 'o-saft',
            'description': "A tool to show informations about SSL certificate and tests the SSL connection according given list of ciphers and various SSL configurations.",
            'aliases': ["o-saft", "o saft"],
        },
        {
            'name': 'ocs',
            'description': "Compact mass scanner for Cisco routers with default telnet/enable passwords.",
            'aliases': ["ocs", "ocs"],
        },
        {
            'name': 'onetwopunch',
            'description': "Use unicornscan to quickly scan all open ports, and then pass the open ports to nmap for detailed scans.",
            'aliases': ["onetwopunch", "onetwopunch"],
        },
        {
            'name': 'onionscan',
            'description': "Scan Onion Services for Security Issues.",
            'aliases': ["onionscan", "onionscan"],
        },
        {
            'name': 'openvas',
            'description': "Meta package for installing all OpenVAS components.",
            'aliases': ["openvas", "openvas scanner", "greenbone"],
        },
        {
            'name': 'pagodo',
            'description': "Google dork script to collect potentially vulnerable web pages and applications on the Internet.",
            'aliases': ["pagodo", "pagodo"],
        },
        {
            'name': 'paketto',
            'description': "Advanced TCP/IP Toolkit.",
            'aliases': ["paketto", "paketto"],
        },
        {
            'name': 'panhunt',
            'description': "Searches for credit card numbers (PANs) in directories.",
            'aliases': ["panhunt", "panhunt"],
        },
        {
            'name': 'paranoic',
            'description': "A simple vulnerability scanner written in Perl.",
            'aliases': ["paranoic", "paranoic"],
        },
        {
            'name': 'passhunt',
            'description': "Search drives for documents containing passwords.",
            'aliases': ["passhunt", "passhunt"],
        },
        {
            'name': 'pbscan',
            'description': "Faster and more efficient stateless SYN scanner and banner grabber due to userland TCP/IP stack usage.",
            'aliases': ["pbscan", "pbscan"],
        },
        {
            'name': 'pcredz',
            'description': "A tool that extracts credit card numbers and more from a pcap file or from a live interface.",
            'aliases': ["pcredz", "pcre dz"],
        },
        {
            'name': 'peass',
            'description': "Privilege Escalation Awesome Scripts SUITE (with colors).",
            'aliases': ["peass", "peass"],
        },
        {
            'name': 'pentestly',
            'description': "Python and Powershell internal penetration testing framework.",
            'aliases': ["pentestly", "pentestly"],
        },
        {
            'name': 'plcscan',
            'description': "This is a tool written in Python that will scan for PLC devices over s7comm or modbus protocols.",
            'aliases': ["plcscan", "plcscan"],
        },
        {
            'name': 'pnscan',
            'description': "A parallel network scanner that can be used to survey TCP network services.",
            'aliases': ["pnscan", "pnscan"],
        },
        {
            'name': 'poison',
            'description': "A fast, asynchronous syn and udp scanner.",
            'aliases': ["poison", "poison"],
        },
        {
            'name': 'ppscan',
            'description': "Yet another port scanner with HTTP and FTP tunneling support.",
            'aliases': ["ppscan", "ppscan"],
        },
        {
            'name': 'prads',
            'description': "A \"Passive Real-time Asset Detection System\".",
            'aliases': ["prads", "prads"],
        },
        {
            'name': 'praeda',
            'description': "An automated data/information harvesting tool designed to gather critical information from various embedded devices.",
            'aliases': ["praeda", "praeda"],
        },
        {
            'name': 'proxycheck',
            'description': "This is a simple proxy tool that checks for the HTTP CONNECT method and grabs verbose output from a webserver.",
            'aliases': ["proxycheck", "proxycheck"],
        },
        {
            'name': 'proxyscan',
            'description': "A security penetration testing tool to scan for hosts and ports through a Web proxy server.",
            'aliases': ["proxyscan", "proxyscan"],
        },
        {
            'name': 'pwndora',
            'description': "Massive IPv4 scanner, find and analyze internet-connected devices in minutes, create your own IoT search engine at home.",
            'aliases': ["pwndora", "pwndora"],
        },
        {
            'name': 'pyssltest',
            'description': "A python multithreaded script to make use of Qualys ssllabs api to test SSL flaws.",
            'aliases': ["pyssltest", "pyssltest"],
        },
        {
            'name': 'pytbull',
            'description': "Next generation of pytbull, IDS/IPS testing framework.",
            'aliases': ["pytbull", "pytbull"],
        },
        {
            'name': 'pythem',
            'description': "Python2 penetration testing framework.",
            'aliases': ["pythem", "pythem"],
        },
        {
            'name': 'python2-ldapdomaindump',
            'description': "Active Directory information dumper via LDAP.",
            'aliases': ["python2-ldapdomaindump", "python2 ldapdomaindump"],
        },
        {
            'name': 'ranger-scanner',
            'description': "A tool to support security professionals to access and interact with remote Microsoft Windows based systems.",
            'aliases': ["ranger-scanner", "ranger scanner"],
        },
        {
            'name': 'rawr',
            'description': "Rapid Assessment of Web Resources. A web enumerator.",
            'aliases': ["rawr", "rawr"],
        },
        {
            'name': 'rbac-lookup',
            'description': "A CLI that allows you to easily find Kubernetes roles and cluster roles bound to any user.",
            'aliases': ["rbac-lookup", "rbac lookup"],
        },
        {
            'name': 'rdp-cipher-checker',
            'description': "Enumerate the encryption protocols supported by the server and the cipher strengths supported using native RDP encryption.",
            'aliases': ["rdp-cipher-checker", "rdp cipher checker"],
        },
        {
            'name': 'rdp-sec-check',
            'description': "Script to enumerate security settings of an RDP Service.",
            'aliases': ["rdp-sec-check", "rdp sec check"],
        },
        {
            'name': 'relay-scanner',
            'description': "An SMTP relay scanner.",
            'aliases': ["relay-scanner", "relay scanner"],
        },
        {
            'name': 'remote-method-guesser',
            'description': "Java RMI vulnerability scanner.",
            'aliases': ["remote-method-guesser", "remote method guesser"],
        },
        {
            'name': 'responder',
            'description': "A LLMNR and NBT-NS poisoner, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2 (multirelay version).",
            'aliases': ["responder", "llmnr responder"],
        },
        {
            'name': 'retire',
            'description': "Scanner detecting the use of JavaScript libraries with known vulnerabilities.",
            'aliases': ["retire", "retire"],
        },
        {
            'name': 'routerhunter',
            'description': "Tool used to find vulnerable routers and devices on the Internet and perform tests.",
            'aliases': ["routerhunter", "routerhunter"],
        },
        {
            'name': 'rtlizer',
            'description': "Simple spectrum analyzer.",
            'aliases': ["rtlizer", "rtlizer"],
        },
        {
            'name': 'rtlsdr-scanner',
            'description': "A cross platform Python frequency scanning GUI for the OsmoSDR rtl-sdr library.",
            'aliases': ["rtlsdr-scanner", "rtlsdr scanner"],
        },
        {
            'name': 's3scanner',
            'description': "A tool to find open S3 buckets in AWS or other cloud providers.",
            'aliases': ["s3scanner", "s3scanner"],
        },
        {
            'name': 'sambascan',
            'description': "Allows you to search an entire network or a number of hosts for SMB shares. It will also list the contents of all public shares that it finds.",
            'aliases': ["sambascan", "sambascan"],
        },
        {
            'name': 'sandcastle',
            'description': "A Python script for AWS S3 bucket enumeration.",
            'aliases': ["sandcastle", "sandcastle"],
        },
        {
            'name': 'sandmap',
            'description': "Simple CLI with the ability to run pure Nmap engine, 31 modules with 459 scan profiles.",
            'aliases': ["sandmap", "sandmap"],
        },
        {
            'name': 'sandy',
            'description': "An open-source Samsung phone encryption assessment framework",
            'aliases': ["sandy", "sandy"],
        },
        {
            'name': 'sb0x',
            'description': "A simple and Lightweight framework for Penetration testing.",
            'aliases': ["sb0x", "sb0x"],
        },
        {
            'name': 'scamper',
            'description': "A tool that actively probes the Internet in order to analyze topology and performance.",
            'aliases': ["scamper", "scamper"],
        },
        {
            'name': 'scanless',
            'description': "Utility for using websites that can perform port scans on your behalf.",
            'aliases': ["scanless", "scanless"],
        },
        {
            'name': 'scanssh',
            'description': "Fast SSH server and open proxy scanner.",
            'aliases': ["scanssh", "scanssh"],
        },
        {
            'name': 'scout2',
            'description': "Security auditing tool for AWS environments.",
            'aliases': ["scout2", "scout2"],
        },
        {
            'name': 'scoutsuite',
            'description': "Multi-Cloud Security Auditing Tool.",
            'aliases': ["scoutsuite", "scoutsuite"],
        },
        {
            'name': 'scrape-dns',
            'description': "Searches for interesting cached DNS entries.",
            'aliases': ["scrape-dns", "scrape dns"],
        },
        {
            'name': 'sdnpwn',
            'description': "An SDN penetration testing toolkit.",
            'aliases': ["sdnpwn", "sdnpwn"],
        },
        {
            'name': 'seat',
            'description': "Next generation information digging application geared toward the needs of security professionals. It uses information stored in search engine databases, cache repositories, and other public resources to scan web sites for potential vulnerabilities.",
            'aliases': ["seat", "seat"],
        },
        {
            'name': 'shareenum',
            'description': "Tool to enumerate shares from Windows hosts.",
            'aliases': ["shareenum", "shareenum"],
        },
        {
            'name': 'sharesniffer',
            'description': "Network share sniffer and auto-mounter for crawling remote file systems.",
            'aliases': ["sharesniffer", "sharesniffer"],
        },
        {
            'name': 'shortscan',
            'description': "An IIS short filename enumeration tool.",
            'aliases': ["shortscan", "shortscan"],
        },
        {
            'name': 'simple-lan-scan',
            'description': "A simple python script that leverages scapy for discovering live hosts on a network.",
            'aliases': ["simple-lan-scan", "simple lan scan"],
        },
        {
            'name': 'simple-lan-scan3',
            'description': "A simple python3 script that leverages scapy for discovering live hosts on a network.",
            'aliases': ["simple-lan-scan3", "simple lan scan3"],
        },
        {
            'name': 'sipshock',
            'description': "A scanner for SIP proxies vulnerable to Shellshock.",
            'aliases': ["sipshock", "sipshock"],
        },
        {
            'name': 'slurp-scanner',
            'description': "Evaluate the security of S3 buckets.",
            'aliases': ["slurp-scanner", "slurp scanner"],
        },
        {
            'name': 'smap-scanner',
            'description': "Passive port scanner built with shodan free API.",
            'aliases': ["smap-scanner", "smap scanner"],
        },
        {
            'name': 'smbexec',
            'description': "A rapid psexec style attack with samba tools.",
            'aliases': ["smbexec", "smbexec"],
        },
        {
            'name': 'smbmap',
            'description': "A handy SMB enumeration tool.",
            'aliases': ["smbmap", "smb map"],
        },
        {
            'name': 'smbspider',
            'description': "A lightweight python utility for searching SMB/CIFS/Samba file shares.",
            'aliases': ["smbspider", "smbspider"],
        },
        {
            'name': 'smbsr',
            'description': "Lookup for interesting stuff in SMB shares.",
            'aliases': ["smbsr", "smbsr"],
        },
        {
            'name': 'smod',
            'description': "A modular framework with every kind of diagnostic and offensive feature you could need in order to pentest modbus protocol.",
            'aliases': ["smod", "smod"],
        },
        {
            'name': 'smtp-test',
            'description': "Automated testing of SMTP servers for penetration testing.",
            'aliases': ["smtp-test", "smtp test"],
        },
        {
            'name': 'smtp-vrfy',
            'description': "An SMTP Protocol Hacker.",
            'aliases': ["smtp-vrfy", "smtp vrfy"],
        },
        {
            'name': 'smtptx',
            'description': "A very simple tool used for sending simple email and do some basic email testing from a pentester perspective.",
            'aliases': ["smtptx", "smtptx"],
        },
        {
            'name': 'snmpenum',
            'description': "An snmp enumerator.",
            'aliases': ["snmpenum", "snmpenum"],
        },
        {
            'name': 'snmpscan',
            'description': "A free, multi-processes SNMP scanner.",
            'aliases': ["snmpscan", "snmpscan"],
        },
        {
            'name': 'snoopbrute',
            'description': "Multithreaded DNS recursive host brute-force tool.",
            'aliases': ["snoopbrute", "snoopbrute"],
        },
        {
            'name': 'sparta',
            'description': "Python GUI application which simplifies network infrastructure penetration testing by aiding the penetration tester in the scanning and enumeration phase.",
            'aliases': ["sparta", "sparta"],
        },
        {
            'name': 'sqlivulscan',
            'description': "This will give you the SQLi Vulnerable Website Just by Adding the Dork.",
            'aliases': ["sqlivulscan", "sqlivulscan"],
        },
        {
            'name': 'ssdp-scanner',
            'description': "SSDP amplification scanner written in Python. Makes use of Scapy.",
            'aliases': ["ssdp-scanner", "ssdp scanner"],
        },
        {
            'name': 'ssh-user-enum',
            'description': "SSH User Enumeration Script in Python Using The Timing Attack.",
            'aliases': ["ssh-user-enum", "ssh user enum"],
        },
        {
            'name': 'sslcaudit',
            'description': "Utility to perform security audits of SSL/TLS clients.",
            'aliases': ["sslcaudit", "sslcaudit"],
        },
        {
            'name': 'ssllabs-scan',
            'description': "Command-line client for the SSL Labs APIs",
            'aliases': ["ssllabs-scan", "ssllabs scan"],
        },
        {
            'name': 'sslmap',
            'description': "A lightweight TLS/SSL cipher suite scanner.",
            'aliases': ["sslmap", "sslmap"],
        },
        {
            'name': 'sslscan2',
            'description': "Tests SSL/TLS enabled services to discover supported cipher suites.",
            'aliases': ["sslscan2", "sslscan2"],
        },
        {
            'name': 'stacs',
            'description': "Static Token And Credential Scanner.",
            'aliases': ["stacs", "stacs"],
        },
        {
            'name': 'sticky-keys-hunter',
            'description': "Script to test an RDP host for sticky keys and utilman backdoor.",
            'aliases': ["sticky-keys-hunter", "sticky keys hunter"],
        },
        {
            'name': 'stig-viewer',
            'description': "XCCDF formatted SRGs and STIGs files viewer for SCAP validation tools.",
            'aliases': ["stig-viewer", "stig viewer"],
        },
        {
            'name': 'strutscan',
            'description': "Apache Struts2 vulnerability scanner written in Perl.",
            'aliases': ["strutscan", "strutscan"],
        },
        {
            'name': 'subbrute',
            'description': "A DNS meta-query spider that enumerates DNS records, and subdomains.",
            'aliases': ["subbrute", "subbrute"],
        },
        {
            'name': 'subjack',
            'description': "Subdomain Takeover tool written in Go.",
            'aliases': ["subjack", "sub jack", "subdomain takeover"],
        },
        {
            'name': 'subover',
            'description': "A Powerful Subdomain Takeover Tool.",
            'aliases': ["subover", "sub over", "subdomain takeover"],
        },
        {
            'name': 'subzy',
            'description': "Subdomain takeover vulnerability checker.",
            'aliases': ["subzy", "subzy"],
        },
        {
            'name': 'swarm',
            'description': "A distributed penetration testing tool.",
            'aliases': ["swarm", "swarm"],
        },
        {
            'name': 'synscan',
            'description': "fast asynchronous half-open TCP portscanner",
            'aliases': ["synscan", "synscan"],
        },
        {
            'name': 'tachyon-scanner',
            'description': "Fast Multi-Threaded Web Discovery Tool.",
            'aliases': ["tachyon-scanner", "tachyon scanner"],
        },
        {
            'name': 'tactical-exploitation',
            'description': "Modern tactical exploitation toolkit.",
            'aliases': ["tactical-exploitation", "tactical exploitation"],
        },
        {
            'name': 'taipan',
            'description': "Web application security scanner.",
            'aliases': ["taipan", "taipan"],
        },
        {
            'name': 'takeover',
            'description': "Sub-Domain TakeOver Vulnerability Scanner.",
            'aliases': ["takeover", "subdomain takeover"],
        },
        {
            'name': 'titus',
            'description': "High-performance secrets scanner based on NoseyParker.",
            'aliases': ["titus", "titus"],
        },
        {
            'name': 'tlsx',
            'description': "TLS grabber focused on TLS based data collection.",
            'aliases': ["tlsx", "tls x"],
        },
        {
            'name': 'topera',
            'description': "An IPv6 security analysis toolkit, with the particularity that their attacks can\'t be detected by Snort.",
            'aliases': ["topera", "topera"],
        },
        {
            'name': 'traxss',
            'description': "Automated XSS Vulnerability Scanner.",
            'aliases': ["traxss", "traxss"],
        },
        {
            'name': 'udp-hunter',
            'description': "Network assessment tool for various UDP Services covering both IPv4 and IPv6 protocols.",
            'aliases': ["udp-hunter", "udp hunter"],
        },
        {
            'name': 'udsim',
            'description': "A graphical simulator that can emulate different modules in a vehicle and respond to UDS request.",
            'aliases': ["udsim", "udsim"],
        },
        {
            'name': 'umap',
            'description': "The USB host security assessment tool.",
            'aliases': ["umap", "umap"],
        },
        {
            'name': 'unicornscan',
            'description': "Asynchronous, stateless TCP/UDP scanner for scalable, high-speed network reconnaissance. Includes Alicorn web UI for result visualization.",
            'aliases': ["unicornscan", "unicornscan"],
        },
        {
            'name': 'upnpscan',
            'description': "Scans the LAN or a given address range for UPnP capable devices.",
            'aliases': ["upnpscan", "upnpscan"],
        },
        {
            'name': 'uptux',
            'description': "Linux privilege escalation checks (systemd, dbus, socket fun, etc).",
            'aliases': ["uptux", "uptux"],
        },
        {
            'name': 'uw-loveimap',
            'description': "Multi threaded imap bounce scanner.",
            'aliases': ["uw-loveimap", "uw loveimap"],
        },
        {
            'name': 'uw-udpscan',
            'description': "Multi threaded udp scanner.",
            'aliases': ["uw-udpscan", "uw udpscan"],
        },
        {
            'name': 'uw-zone',
            'description': "Multi threaded, randomized IP zoner.",
            'aliases': ["uw-zone", "uw zone"],
        },
        {
            'name': 'v3n0m',
            'description': "Offensive Security Tool for Vulnerability Scanning & Pentesting",
            'aliases': ["v3n0m", "v3n0m"],
        },
        {
            'name': 'vault-scanner',
            'description': "Swiss army knife for hackers.",
            'aliases': ["vault-scanner", "vault scanner"],
        },
        {
            'name': 'vcsmap',
            'description': "A plugin-based tool to scan public version control systems for sensitive information.",
            'aliases': ["vcsmap", "vcsmap"],
        },
        {
            'name': 'vhostscan',
            'description': "A virtual host scanner that can be used with pivot tools, detect catch-all scenarios, aliases and dynamic default pages.",
            'aliases': ["vhostscan", "vhostscan"],
        },
        {
            'name': 'videosnarf',
            'description': "A new security assessment tool for pcap analysis",
            'aliases': ["videosnarf", "videosnarf"],
        },
        {
            'name': 'visql',
            'description': "Scan SQL vulnerability on target site and sites of on server.",
            'aliases': ["visql", "visql"],
        },
        {
            'name': 'vscan',
            'description': "HTTPS / Vulnerability scanner.",
            'aliases': ["vscan", "vscan"],
        },
        {
            'name': 'vulmap',
            'description': "Vulmap Online Local Vulnerability Scanners Project",
            'aliases': ["vulmap", "vulmap"],
        },
        {
            'name': 'vuls',
            'description': "Vulnerability scanner for Linux/FreeBSD, agentless, written in Go.",
            'aliases': ["vuls", "vuls"],
        },
        {
            'name': 'wafw00f',
            'description': "Identify and fingerprint Web Application Firewall (WAF) products protecting a website.",
            'aliases': ["wafw00f", "waf woof", "wafw00f.py"],
        },
        {
            'name': 'webenum',
            'description': "Tool to enumerate http responses using dynamically generated queries and more.",
            'aliases': ["webenum", "webenum"],
        },
        {
            'name': 'webhunter',
            'description': "Tool for scanning web applications and networks and easily completing the process of collecting knowledge.",
            'aliases': ["webhunter", "webhunter"],
        },
        {
            'name': 'webpwn3r',
            'description': "A python based Web Applications Security Scanner.",
            'aliases': ["webpwn3r", "webpwn3r"],
        },
        {
            'name': 'webrute',
            'description': "Web server directory brute forcer.",
            'aliases': ["webrute", "webrute"],
        },
        {
            'name': 'whitewidow',
            'description': "SQL Vulnerability Scanner.",
            'aliases': ["whitewidow", "whitewidow"],
        },
        {
            'name': 'wolpertinger',
            'description': "A distributed portscanner.",
            'aliases': ["wolpertinger", "wolpertinger"],
        },
        {
            'name': 'wordpresscan',
            'description': "WPScan rewritten in Python + some WPSeku ideas.",
            'aliases': ["wordpresscan", "wordpresscan"],
        },
        {
            'name': 'xcname',
            'description': "A tool for enumerating expired domains in CNAME records.",
            'aliases': ["xcname", "xcname"],
        },
        {
            'name': 'xpire-crossdomain-scanner',
            'description': "Scans crossdomain.xml policies for expired domain names.",
            'aliases': ["xpire-crossdomain-scanner", "xpire crossdomain scanner"],
        },
        {
            'name': 'xsstracer',
            'description': "Python script that checks remote web servers for Clickjacking, Cross-Frame Scripting, Cross-Site Tracing and Host Header Injection.",
            'aliases': ["xsstracer", "xsstracer"],
        },
        {
            'name': 'yasat',
            'description': "Yet Another Stupid Audit Tool.",
            'aliases': ["yasat", "yasat"],
        },
    ],

    # Reconnaissance (257 tools)
    'blackarch-recon': [
        {
            'name': 'activedirectoryenum',
            'description': "Enumerate AD through LDAP.",
            'aliases': ["activedirectoryenum", "activedirectoryenum"],
        },
        {
            'name': 'ad-ldap-enum',
            'description': "An LDAP based Active Directory user and group enumeration tool.",
            'aliases': ["ad-ldap-enum", "ad ldap enum"],
        },
        {
            'name': 'ad-miner',
            'description': "Active Directory audit tool that extract data from Bloodhound to uncover security weaknesses and generate an HTML report",
            'aliases': ["ad-miner", "ad miner"],
        },
        {
            'name': 'adexplorersnapshot',
            'description': "AD Explorer snapshot parser.",
            'aliases': ["adexplorersnapshot", "adexplorersnapshot"],
        },
        {
            'name': 'adidnsdump',
            'description': "Active Directory Integrated DNS dumping by any authenticated user.",
            'aliases': ["adidnsdump", "adidnsdump"],
        },
        {
            'name': 'aiodnsbrute',
            'description': "Python 3 DNS asynchronous brute force utility.",
            'aliases': ["aiodnsbrute", "aiodnsbrute"],
        },
        {
            'name': 'altdns',
            'description': "Generates permutations, alterations and mutations of subdomains and then resolves them.",
            'aliases': ["altdns", "altdns"],
        },
        {
            'name': 'aquatone',
            'description': "A Tool for Domain Flyovers.",
            'aliases': ["aquatone", "aquatone"],
        },
        {
            'name': 'asn',
            'description': "ASN, RPKI validity, BGP stats, IPv4v6, Prefix, URL, ASPath, Organization, IP reputation, IP geolocation, IP fingerprinting, Network recon, lookup API server, Web traceroute server.",
            'aliases': ["asn", "asn"],
        },
        {
            'name': 'attacksurfacemapper',
            'description': "Tool that aims to automate the reconnaissance process.",
            'aliases': ["attacksurfacemapper", "attacksurfacemapper"],
        },
        {
            'name': 'autosint',
            'description': "Tool to automate common osint tasks.",
            'aliases': ["autosint", "autosint"],
        },
        {
            'name': 'aws-inventory',
            'description': "Discover resources created in an AWS account.",
            'aliases': ["aws-inventory", "aws inventory"],
        },
        {
            'name': 'aztarna',
            'description': "A footprinting tool for ROS and SROS systems.",
            'aliases': ["aztarna", "aztarna"],
        },
        {
            'name': 'badkarma',
            'description': "Advanced network reconnaissance toolkit.",
            'aliases': ["badkarma", "badkarma"],
        },
        {
            'name': 'basedomainname',
            'description': "Tool that can extract TLD (Top Level Domain), domain extensions (Second Level Domain + TLD), domain name, and hostname from fully qualified domain names.",
            'aliases': ["basedomainname", "basedomainname"],
        },
        {
            'name': 'bbot',
            'description': "Multipurpose scanner built to automate your Recon, Bug Bounties, and ASM.",
            'aliases': ["bbot", "bbot"],
        },
        {
            'name': 'bfac',
            'description': "An automated tool that checks for backup artifacts that may disclose the web-application\'s source code.",
            'aliases': ["bfac", "bfac"],
        },
        {
            'name': 'billcipher',
            'description': "Information Gathering tool for a Website or IP address.",
            'aliases': ["billcipher", "billcipher"],
        },
        {
            'name': 'bing-ip2hosts',
            'description': "Enumerates all hostnames which Bing has indexed for a specific IP address.",
            'aliases': ["bing-ip2hosts", "bing ip2hosts"],
        },
        {
            'name': 'bloodhound',
            'description': "Six Degrees of Domain Admin",
            'aliases': ["bloodhound", "bloodhound gui"],
        },
        {
            'name': 'bloodhound-ce-python',
            'description': "Python data collector for Bloodhound community edition (v5)",
            'aliases': ["bloodhound-ce-python", "bloodhound ce python"],
        },
        {
            'name': 'bloodhound-python',
            'description': "Python data collector for Bloodhound legcacy (v4)",
            'aliases': ["bloodhound-python", "bloodhound python"],
        },
        {
            'name': 'bridgekeeper',
            'description': "Scrape employee names from search engine LinkedIn profiles. Convert employee names to a specified username format.",
            'aliases': ["bridgekeeper", "bridgekeeper"],
        },
        {
            'name': 'catnthecanary',
            'description': "An application to query the canary.pw data set for leaked data.",
            'aliases': ["catnthecanary", "catnthecanary"],
        },
        {
            'name': 'ccrawldns',
            'description': "Retrieves from the CommonCrawl data set unique subdomains for a given domain name.",
            'aliases': ["ccrawldns", "ccrawldns"],
        },
        {
            'name': 'certgraph',
            'description': "Crawl the graph of certificate Alternate Names.",
            'aliases': ["certgraph", "certgraph"],
        },
        {
            'name': 'chaos-client',
            'description': "Go client to communicate with Chaos dataset API.",
            'aliases': ["chaos-client", "chaos client"],
        },
        {
            'name': 'chronoleak',
            'description': "ICMP Timestamp Remote Time Leaker.",
            'aliases': ["chronoleak", "chronoleak"],
        },
        {
            'name': 'citadel',
            'description': "A library of OSINT tools.",
            'aliases': ["citadel", "citadel"],
        },
        {
            'name': 'cloud-buster',
            'description': "A tool that checks Cloudflare enabled sites for origin IP leaks.",
            'aliases': ["cloud-buster", "cloud buster"],
        },
        {
            'name': 'cloud_enum',
            'description': "Multi-cloud OSINT tool. Enumerate public resources in AWS, Azure, and Google Cloud.",
            'aliases': ["cloud_enum", "cloud enum"],
        },
        {
            'name': 'cloudfail',
            'description': "Utilize misconfigured DNS and old database records to find hidden IP\'s behind the CloudFlare network.",
            'aliases': ["cloudfail", "cloudfail"],
        },
        {
            'name': 'cloudlist',
            'description': "A tool for listing Assets from multiple Cloud Providers.",
            'aliases': ["cloudlist", "cloudlist"],
        },
        {
            'name': 'cloudmare',
            'description': "A simple tool to find origin servers of websites protected by CloudFlare with a misconfiguration DNS.",
            'aliases': ["cloudmare", "cloudmare"],
        },
        {
            'name': 'cloudunflare',
            'description': "Reconnaissance Real IP address for Cloudflare Bypass.",
            'aliases': ["cloudunflare", "cloudunflare"],
        },
        {
            'name': 'cr3dov3r',
            'description': "Search for public leaks for email addresses + check creds against 16 websites.",
            'aliases': ["cr3dov3r", "cr3dov3r"],
        },
        {
            'name': 'cutycapt',
            'description': "A Qt and WebEngine-based command-line utility that captures a web page\'s rendered output.",
            'aliases': ["cutycapt", "cutycapt"],
        },
        {
            'name': 'datasploit',
            'description': "Performs automated OSINT and more.",
            'aliases': ["datasploit", "datasploit"],
        },
        {
            'name': 'dga-detection',
            'description': "DGA Domain Detection using Bigram Frequency Analysis.",
            'aliases': ["dga-detection", "dga detection"],
        },
        {
            'name': 'dns-parallel-prober',
            'description': "PoC for an adaptive parallelised DNS prober.",
            'aliases': ["dns-parallel-prober", "dns parallel prober"],
        },
        {
            'name': 'dnsbrute',
            'description': "Multi-theaded DNS bruteforcing, average speed 80 lookups/second with 40 threads.",
            'aliases': ["dnsbrute", "dnsbrute"],
        },
        {
            'name': 'dnscobra',
            'description': "DNS subdomain bruteforcing tool with Tor support through torsocks.",
            'aliases': ["dnscobra", "dnscobra"],
        },
        {
            'name': 'dnsenum',
            'description': "Script that enumerates DNS information from a domain, attempts zone transfers, performs a brute force dictionary style attack, and then performs reverse look-ups on the results.",
            'aliases': ["dnsenum", "dns enum"],
        },
        {
            'name': 'dnsgrep',
            'description': "A utility for quickly searching presorted DNS names.",
            'aliases': ["dnsgrep", "dnsgrep"],
        },
        {
            'name': 'dnsprobe',
            'description': "Allows you to perform multiple dns queries of your choice with a list of user supplied resolvers.",
            'aliases': ["dnsprobe", "dnsprobe"],
        },
        {
            'name': 'dnsrecon',
            'description': "Python script for enumeration of hosts, subdomains and emails from a given domain using google.",
            'aliases': ["dnsrecon", "dns recon"],
        },
        {
            'name': 'dnssearch',
            'description': "A subdomain enumeration tool.",
            'aliases': ["dnssearch", "dnssearch"],
        },
        {
            'name': 'dnsspider',
            'description': "A fast multithreaded bruteforcer of subdomains that leverages a wordlist and/or character permutation.",
            'aliases': ["dnsspider", "dnsspider"],
        },
        {
            'name': 'dnstracer',
            'description': "Determines where a given DNS server gets its information from, and follows the chain of DNS servers",
            'aliases': ["dnstracer", "dnstracer"],
        },
        {
            'name': 'dnswalk',
            'description': "A DNS debugger and zone-transfer utility.",
            'aliases': ["dnswalk", "dnswalk"],
        },
        {
            'name': 'dnsx',
            'description': "Fast and multi-purpose DNS toolkit allow to run multiple DNS queries of your choice with a list of user-supplied resolvers.",
            'aliases': ["dnsx", "dns x"],
        },
        {
            'name': 'domain-analyzer',
            'description': "Finds all the security information for a given domain name.",
            'aliases': ["domain-analyzer", "domain analyzer"],
        },
        {
            'name': 'domain-stats',
            'description': "A web API to deliver domain information from whois and alexa.",
            'aliases': ["domain-stats", "domain stats"],
        },
        {
            'name': 'domained',
            'description': "Multi Tool Subdomain Enumeration.",
            'aliases': ["domained", "domained"],
        },
        {
            'name': 'domainhunter',
            'description': "Checks expired domains for categorization/reputation and Archive.org history to determine good candidates for phishing and C2 domain names.",
            'aliases': ["domainhunter", "domainhunter"],
        },
        {
            'name': 'dradis-ce',
            'description': "An open source framework to enable effective information sharing.",
            'aliases': ["dradis-ce", "dradis ce"],
        },
        {
            'name': 'elevate',
            'description': "Horizontal domain discovery tool you can use to discover other domains owned by a given company.",
            'aliases': ["elevate", "elevate"],
        },
        {
            'name': 'enum4linux',
            'description': "A tool for enumerating information from Windows and Samba systems.",
            'aliases': ["enum4linux", "enum4linux-ng"],
        },
        {
            'name': 'enum4linux-ng',
            'description': "A next generation version of enum4linux.",
            'aliases': ["enum4linux-ng", "enum4linux ng"],
        },
        {
            'name': 'enumerate-iam',
            'description': "Enumerate the permissions associated with an AWS credential set.",
            'aliases': ["enumerate-iam", "enumerate iam"],
        },
        {
            'name': 'enumerid',
            'description': "Enumerate RIDs using pure Python.",
            'aliases': ["enumerid", "enumerid"],
        },
        {
            'name': 'exitmap',
            'description': "A fast and modular scanner for Tor exit relays.",
            'aliases': ["exitmap", "exitmap"],
        },
        {
            'name': 'facebot',
            'description': "A facebook profile and reconnaissance system.",
            'aliases': ["facebot", "facebot"],
        },
        {
            'name': 'fav-up',
            'description': "IP lookup by favicon using Shodan.",
            'aliases': ["fav-up", "fav up"],
        },
        {
            'name': 'favfreak',
            'description': "Weaponizing favicon.ico for BugBounties , OSINT and what not.",
            'aliases': ["favfreak", "favfreak"],
        },
        {
            'name': 'fbid',
            'description': "Show info about the author by facebook photo url.",
            'aliases': ["fbid", "fbid"],
        },
        {
            'name': 'fierce',
            'description': "A DNS reconnaissance tool for locating non-contiguous IP space.",
            'aliases': ["fierce", "fierce dns"],
        },
        {
            'name': 'finalrecon',
            'description': "OSINT Tool for All-In-One Web Reconnaissance.",
            'aliases': ["finalrecon", "finalrecon"],
        },
        {
            'name': 'flashlight',
            'description': "Automated Information Gathering Tool for Penetration Testers.",
            'aliases': ["flashlight", "flashlight"],
        },
        {
            'name': 'forager',
            'description': "Multithreaded threat Intelligence gathering utilizing.",
            'aliases': ["forager", "forager"],
        },
        {
            'name': 'gasmask',
            'description': "All in one Information gathering tool - OSINT.",
            'aliases': ["gasmask", "gasmask"],
        },
        {
            'name': 'gatecrasher',
            'description': "Network auditing and analysis tool developed in Python.",
            'aliases': ["gatecrasher", "gatecrasher"],
        },
        {
            'name': 'geoedge',
            'description': "This little tools is designed to get geolocalization information of a host, it get the information from two sources (maxmind and geoiptool).",
            'aliases': ["geoedge", "geoedge"],
        },
        {
            'name': 'gh-dork',
            'description': "Github dorking tool.",
            'aliases': ["gh-dork", "gh dork"],
        },
        {
            'name': 'ghunt',
            'description': "An offensive OSINT Google framework.",
            'aliases': ["ghunt", "ghunt"],
        },
        {
            'name': 'git-hound',
            'description': "Pinpoints exposed API keys on GitHub. A batch-catching, pattern-matching, patch-attacking secret snatcher.",
            'aliases': ["git-hound", "git hound"],
        },
        {
            'name': 'git-wild-hunt',
            'description': "A tool to hunt for credentials in github wild AKA git*hunt.",
            'aliases': ["git-wild-hunt", "git wild hunt"],
        },
        {
            'name': 'gitdorker',
            'description': "Python program to scrape secrets from GitHub through usage of a large repository of dorks.",
            'aliases': ["gitdorker", "gitdorker"],
        },
        {
            'name': 'gitem',
            'description': "A Github organization reconnaissance tool.",
            'aliases': ["gitem", "gitem"],
        },
        {
            'name': 'gitgraber',
            'description': "Monitor GitHub to search and find sensitive data in real time for different online services.",
            'aliases': ["gitgraber", "gitgraber"],
        },
        {
            'name': 'githack',
            'description': "A `.git` folder disclosure exploit.",
            'aliases': ["githack", "githack"],
        },
        {
            'name': 'github-dorks',
            'description': "Collection of github dorks and helper tool to automate the process of checking dorks.",
            'aliases': ["github-dorks", "github dorks"],
        },
        {
            'name': 'github-subdomains',
            'description': "Find subdomains on GitHub.",
            'aliases': ["github-subdomains", "github subdomains"],
        },
        {
            'name': 'gitmails',
            'description': "An information gathering tool to collect git commit emails in version control host services.",
            'aliases': ["gitmails", "gitmails"],
        },
        {
            'name': 'gitminer',
            'description': "Tool for advanced mining for content on Github.",
            'aliases': ["gitminer", "gitminer"],
        },
        {
            'name': 'gitrecon',
            'description': "OSINT tool to get information from a Github and Gitlab profile and find user\'s email addresses leaked on commits.",
            'aliases': ["gitrecon", "gitrecon"],
        },
        {
            'name': 'go-windapsearch',
            'description': "Utility to enumerate users, groups and computers from a Windows domain through LDAP queries.",
            'aliases': ["go-windapsearch", "go windapsearch"],
        },
        {
            'name': 'goddi',
            'description': "Dumps Active Directory domain information.",
            'aliases': ["goddi", "goddi"],
        },
        {
            'name': 'goodork',
            'description': "A python script designed to allow you to leverage the power of google dorking straight from the comfort of your command line.",
            'aliases': ["goodork", "goodork"],
        },
        {
            'name': 'goog-mail',
            'description': "Enumerate domain emails from google.",
            'aliases': ["goog-mail", "goog mail"],
        },
        {
            'name': 'googlesub',
            'description': "A python script to find domains by using google dorks.",
            'aliases': ["googlesub", "googlesub"],
        },
        {
            'name': 'goohak',
            'description': "Automatically Launch Google Hacking Queries Against A Target Domain.",
            'aliases': ["goohak", "goohak"],
        },
        {
            'name': 'goop',
            'description': "Perform google searches without being blocked by the CAPTCHA or hitting any rate limits.",
            'aliases': ["goop", "goop"],
        },
        {
            'name': 'gosint',
            'description': "OSINT framework in Go.",
            'aliases': ["gosint", "gosint"],
        },
        {
            'name': 'grabing',
            'description': "Counts all the hostnames for an IP adress",
            'aliases': ["grabing", "grabing"],
        },
        {
            'name': 'graphinder',
            'description': "GraphQL endpoints finder using subdomain enumeration, scripts analysis and bruteforce.",
            'aliases': ["graphinder", "graphinder"],
        },
        {
            'name': 'gwtenum',
            'description': "Enumeration of GWT-RCP method calls.",
            'aliases': ["gwtenum", "gwtenum"],
        },
        {
            'name': 'h8mail',
            'description': "Email OSINT and password breach hunting.",
            'aliases': ["h8mail", "h8mail"],
        },
        {
            'name': 'hakrevdns',
            'description': "Small, fast tool for performing reverse DNS lookups en masse.",
            'aliases': ["hakrevdns", "hakrevdns"],
        },
        {
            'name': 'halcyon',
            'description': "A repository crawler that runs checksums for static files found within a given git repository.",
            'aliases': ["halcyon", "halcyon"],
        },
        {
            'name': 'hasere',
            'description': "Discover the vhosts using google and bing.",
            'aliases': ["hasere", "hasere"],
        },
        {
            'name': 'hatcloud',
            'description': "Bypass CloudFlare with Ruby.",
            'aliases': ["hatcloud", "hatcloud"],
        },
        {
            'name': 'hoper',
            'description': "Trace URL\'s jumps across the rel links to obtain the last URL.",
            'aliases': ["hoper", "hoper"],
        },
        {
            'name': 'hosthunter',
            'description': "A recon tool for discovering hostnames using OSINT techniques.",
            'aliases': ["hosthunter", "hosthunter"],
        },
        {
            'name': 'howmanypeoplearearound',
            'description': "Count the number of people around you by monitoring wifi signals.",
            'aliases': ["howmanypeoplearearound", "howmanypeoplearearound"],
        },
        {
            'name': 'id-entify',
            'description': "Search for information related to a domain: Emails - IP addresses - Domains - Information on WEB technology - Type of Firewall - NS and MX records.",
            'aliases': ["id-entify", "id entify"],
        },
        {
            'name': 'idswakeup',
            'description': "A collection of tools that allows to test network intrusion detection systems.",
            'aliases': ["idswakeup", "idswakeup"],
        },
        {
            'name': 'infoga',
            'description': "Tool for gathering e-mail accounts information from different public sources (search engines, pgp key servers).",
            'aliases': ["infoga", "infoga"],
        },
        {
            'name': 'inquisitor',
            'description': "OSINT Gathering Tool for Companies and Organizations.",
            'aliases': ["inquisitor", "inquisitor"],
        },
        {
            'name': 'intelplot',
            'description': "OSINT Tool to Mark Points on Offline Map.",
            'aliases': ["intelplot", "intelplot"],
        },
        {
            'name': 'intrace',
            'description': "Traceroute-like application piggybacking on existing TCP connections.",
            'aliases': ["intrace", "intrace"],
        },
        {
            'name': 'ip-tracer',
            'description': "Track and retrieve any ip address information.",
            'aliases': ["ip-tracer", "ip tracer"],
        },
        {
            'name': 'ip2clue',
            'description': "A small memory/CPU footprint daemon to lookup country (and other info) based on IP (v4 and v6).",
            'aliases': ["ip2clue", "ip2clue"],
        },
        {
            'name': 'iptodomain',
            'description': "This tool extract domains from IP address based in the information saved in virustotal.",
            'aliases': ["iptodomain", "iptodomain"],
        },
        {
            'name': 'ipv666',
            'description': "Golang IPv6 address enumeration.",
            'aliases': ["ipv666", "ipv666"],
        },
        {
            'name': 'ircsnapshot',
            'description': "Tool to gather information from IRC servers.",
            'aliases': ["ircsnapshot", "ircsnapshot"],
        },
        {
            'name': 'isr-form',
            'description': "Simple html parsing tool that extracts all form related information and generates reports of the data. Allows for quick analyzing of data.",
            'aliases': ["isr-form", "isr form"],
        },
        {
            'name': 'ivre',
            'description': "Network recon framework based on Nmap, Masscan, Zeek (Bro), Argus, Netflow,...",
            'aliases': ["ivre", "ivre"],
        },
        {
            'name': 'ivre-docs',
            'description': "Network recon framework based on Nmap, Masscan, Zeek (Bro), Argus, Netflow,... (documentation)",
            'aliases': ["ivre-docs", "ivre docs"],
        },
        {
            'name': 'ivre-web',
            'description': "Network recon framework based on Nmap, Masscan, Zeek (Bro), Argus, Netflow,... (web application)",
            'aliases': ["ivre-web", "ivre web"],
        },
        {
            'name': 'jackdaw',
            'description': "Collect all information in your domain, show you graphs on how domain objects interact with each-other and how to exploit these interactions.",
            'aliases': ["jackdaw", "jackdaw"],
        },
        {
            'name': 'jsearch',
            'description': "Simple script that grep infos from javascript files.",
            'aliases': ["jsearch", "jsearch"],
        },
        {
            'name': 'kacak',
            'description': "Tools for penetration testers that can enumerate which users logged on windows system.",
            'aliases': ["kacak", "kacak"],
        },
        {
            'name': 'kamerka',
            'description': "Build interactive map of cameras from Shodan.",
            'aliases': ["kamerka", "kamerka"],
        },
        {
            'name': 'keye',
            'description': "Recon tool detecting changes of websites based on content-length differences.",
            'aliases': ["keye", "keye"],
        },
        {
            'name': 'lanmap2',
            'description': "Passive network mapping tool.",
            'aliases': ["lanmap2", "lanmap2"],
        },
        {
            'name': 'lbd',
            'description': "Load Balancing detector,",
            'aliases': ["lbd", "load balancing detector"],
        },
        {
            'name': 'ldapenum',
            'description': "Enumerate domain controllers using LDAP.",
            'aliases': ["ldapenum", "ldapenum"],
        },
        {
            'name': 'ldeep',
            'description': "In-depth ldap enumeration utility.",
            'aliases': ["ldeep", "ldeep"],
        },
        {
            'name': 'legion',
            'description': "Automatic Enumeration Tool based in Open Source tools.",
            'aliases': ["legion", "legion"],
        },
        {
            'name': 'lft',
            'description': "A layer four traceroute implementing numerous other features.",
            'aliases': ["lft", "lft"],
        },
        {
            'name': 'lhf',
            'description': "A modular recon tool for pentesting.",
            'aliases': ["lhf", "lhf"],
        },
        {
            'name': 'linux-exploit-suggester',
            'description': "A Perl script that tries to suggest exploits based OS version number.",
            'aliases': ["linux-exploit-suggester", "linux exploit suggester"],
        },
        {
            'name': 'linux-exploit-suggester.sh',
            'description': "Linux privilege escalation auditing tool.",
            'aliases': ["linux-exploit-suggester.sh", "linux exploit suggester.sh"],
        },
        {
            'name': 'littlebrother',
            'description': "OSINT tool to get informations on French, Belgian and Swizerland people.",
            'aliases': ["littlebrother", "littlebrother"],
        },
        {
            'name': 'loot',
            'description': "Sensitive information extraction tool.",
            'aliases': ["loot", "loot"],
        },
        {
            'name': 'machinae',
            'description': "A tool for collecting intelligence from public sites/feeds about various security-related pieces of data.",
            'aliases': ["machinae", "machinae"],
        },
        {
            'name': 'mail-crawl',
            'description': "Tool to harvest emails from website.",
            'aliases': ["mail-crawl", "mail crawl"],
        },
        {
            'name': 'massbleed',
            'description': "SSL Vulnerability Scanner.",
            'aliases': ["massbleed", "massbleed"],
        },
        {
            'name': 'mdns-recon',
            'description': "An mDNS recon tool written in Python.",
            'aliases': ["mdns-recon", "mdns recon"],
        },
        {
            'name': 'metabigor',
            'description': "Intelligence Tool but without API key.",
            'aliases': ["metabigor", "metabigor"],
        },
        {
            'name': 'metafinder',
            'description': "Search for documents in a domain through Search Engines (Google, Bing and Baidu). The objective is to extract metadata.",
            'aliases': ["metafinder", "metafinder"],
        },
        {
            'name': 'metagoofil',
            'description': "An information gathering tool designed for extracting metadata of public documents.",
            'aliases': ["metagoofil", "metagoofil"],
        },
        {
            'name': 'mildew',
            'description': "Dotmil subdomain discovery tool that scrapes domains from official DoD website directories and certificate transparency logs.",
            'aliases': ["mildew", "mildew"],
        },
        {
            'name': 'missidentify',
            'description': "A program to find Win32 applications.",
            'aliases': ["missidentify", "missidentify"],
        },
        {
            'name': 'monocle',
            'description': "A local network host discovery tool. In passive mode, it will listen for ARP request and reply packets. In active mode, it will send ARP requests to the specific IP range. The results are a list of IP and MAC addresses present on the local network.",
            'aliases': ["monocle", "monocle"],
        },
        {
            'name': 'nasnum',
            'description': "Script to enumerate network attached storages.",
            'aliases': ["nasnum", "nasnum"],
        },
        {
            'name': 'necromant',
            'description': "Python Script that search unused Virtual Hosts in Web Servers.",
            'aliases': ["necromant", "necromant"],
        },
        {
            'name': 'neglected',
            'description': "Facebook CDN Photo Resolver.",
            'aliases': ["neglected", "neglected"],
        },
        {
            'name': 'netdiscover',
            'description': "An active/passive address reconnaissance tool, mainly developed for those wireless networks without dhcp server, when you are wardriving. It can be also used on hub/switched networks.",
            'aliases': ["netdiscover", "net discover"],
        },
        {
            'name': 'netkit-bsd-finger',
            'description': "BSD-finger ported to Linux.",
            'aliases': ["netkit-bsd-finger", "netkit bsd finger"],
        },
        {
            'name': 'netkit-rusers',
            'description': "Logged in users; Displays who is logged in to machines on local network.",
            'aliases': ["netkit-rusers", "netkit rusers"],
        },
        {
            'name': 'netkit-rwho',
            'description': "Remote who client and server (with Debian patches).",
            'aliases': ["netkit-rwho", "netkit rwho"],
        },
        {
            'name': 'netmask',
            'description': "Helps determine network masks",
            'aliases': ["netmask", "netmask"],
        },
        {
            'name': 'netscout',
            'description': "OSINT tool that finds domains, subdomains, directories, endpoints and files.",
            'aliases': ["netscout", "netscout"],
        },
        {
            'name': 'nohidy',
            'description': "The system admins best friend, multi platform auditing tool.",
            'aliases': ["nohidy", "nohidy"],
        },
        {
            'name': 'nsec3map',
            'description': "A tool to enumerate the resource records of a DNS zone using its DNSSEC NSEC or NSEC3 chain.",
            'aliases': ["nsec3map", "nsec3map"],
        },
        {
            'name': 'nsec3walker',
            'description': "Enumerate domain names using DNSSEC.",
            'aliases': ["nsec3walker", "nsec3walker"],
        },
        {
            'name': 'ntp-ip-enum',
            'description': "Script to pull addresses from a NTP server using the monlist command. Can also output Maltego resultset.",
            'aliases': ["ntp-ip-enum", "ntp ip enum"],
        },
        {
            'name': 'nullinux',
            'description': "Tool that can be used to enumerate OS information, domain information, shares, directories, and users through SMB null sessions.",
            'aliases': ["nullinux", "nullinux"],
        },
        {
            'name': 'omnibus',
            'description': "OSINT tool for intelligence collection, research and artifact management.",
            'aliases': ["omnibus", "omnibus"],
        },
        {
            'name': 'onioff',
            'description': "An onion url inspector for inspecting deep web links.",
            'aliases': ["onioff", "onioff"],
        },
        {
            'name': 'osint-spy',
            'description': "Performs OSINT scan on email/domain/ip_address/organization.",
            'aliases': ["osint-spy", "osint spy"],
        },
        {
            'name': 'osinterator',
            'description': "Open Source Toolkit for Open Source Intelligence Gathering.",
            'aliases': ["osinterator", "osinterator"],
        },
        {
            'name': 'osintgram',
            'description': "OSINT tool offering an interactive shell to perform analysis on Instagram account of any users by its nickname.",
            'aliases': ["osintgram", "osintgram"],
        },
        {
            'name': 'parsero',
            'description': "A robots.txt audit tool.",
            'aliases': ["parsero", "parsero"],
        },
        {
            'name': 'pastemonitor',
            'description': "Scrape Pastebin API to collect daily pastes, setup a wordlist and be alerted by email when you have a match..",
            'aliases': ["pastemonitor", "pastemonitor"],
        },
        {
            'name': 'pdfgrab',
            'description': "Tool for searching pdfs withthin google and extracting pdf metadata.",
            'aliases': ["pdfgrab", "pdfgrab"],
        },
        {
            'name': 'pius-pi',
            'description': "Organizational asset discovery tool with 20+ plugins covering certificate transparency, passive DNS, and all 5 Regional Internet Registries.",
            'aliases': ["pius-pi", "pius pi"],
        },
        {
            'name': 'pmapper',
            'description': "A tool for quickly evaluating IAM permissions in AWS.",
            'aliases': ["pmapper", "pmapper"],
        },
        {
            'name': 'postenum',
            'description': "Clean, nice and easy tool for basic/advanced privilege escalation techniques.",
            'aliases': ["postenum", "postenum"],
        },
        {
            'name': 'protosint',
            'description': "Python script that helps you investigate Protonmail accounts and ProtonVPN IP addresses.",
            'aliases': ["protosint", "protosint"],
        },
        {
            'name': 'punter',
            'description': "Hunt domain names using DNSDumpster, WHOIS, Reverse WHOIS, Shodan, Crimeflare.",
            'aliases': ["punter", "punter"],
        },
        {
            'name': 'puredns',
            'description': "Fast domain resolver and subdomain bruteforcing with accurate wildcard filtering.",
            'aliases': ["puredns", "pure dns"],
        },
        {
            'name': 'pwned',
            'description': "A command-line tool for querying the \'Have I been pwned?\' service.",
            'aliases': ["pwned", "pwned"],
        },
        {
            'name': 'pwned-search',
            'description': "Pwned Password API lookup.",
            'aliases': ["pwned-search", "pwned search"],
        },
        {
            'name': 'pwnedornot',
            'description': "Tool to find passwords for compromised email addresses.",
            'aliases': ["pwnedornot", "pwnedornot"],
        },
        {
            'name': 'pymeta',
            'description': "Auto Scanning to SSL Vulnerability.",
            'aliases': ["pymeta", "pymeta"],
        },
        {
            'name': 'python-api-dnsdumpster',
            'description': "Unofficial Python API for http://dnsdumpster.com/.",
            'aliases': ["python-api-dnsdumpster", "python api dnsdumpster"],
        },
        {
            'name': 'python-ivre',
            'description': "Network recon framework based on Nmap, Masscan, Zeek (Bro), Argus, Netflow,... (library)",
            'aliases': ["python-ivre", "python ivre"],
        },
        {
            'name': 'python2-api-dnsdumpster',
            'description': "Unofficial Python API for http://dnsdumpster.com/.",
            'aliases': ["python2-api-dnsdumpster", "python2 api dnsdumpster"],
        },
        {
            'name': 'python2-ivre',
            'description': "Network recon framework based on Nmap, Masscan, Zeek (Bro), Argus, Netflow,... (library)",
            'aliases': ["python2-ivre", "python2 ivre"],
        },
        {
            'name': 'python2-shodan',
            'description': "Python library and command-line utility for Shodan (https://developer.shodan.io).",
            'aliases': ["python2-shodan", "python2 shodan"],
        },
        {
            'name': 'quickrecon',
            'description': "A python script for simple information gathering. It attempts to find subdomain names, perform zone transfers and gathers emails from Google and Bing.",
            'aliases': ["quickrecon", "quickrecon"],
        },
        {
            'name': 'raccoon',
            'description': "A high performance offensive security tool for reconnaissance and vulnerability scanning.",
            'aliases': ["raccoon", "raccoon"],
        },
        {
            'name': 'rdwatool',
            'description': "A python script to extract information from a Microsoft Remote Desktop Web Access (RDWA) application.",
            'aliases': ["rdwatool", "rdwatool"],
        },
        {
            'name': 'recon-ng',
            'description': "A full-featured Web Reconnaissance framework written in Python.",
            'aliases': ["recon-ng", "reconng", "recon ng"],
        },
        {
            'name': 'reconnoitre',
            'description': "A security tool for multithreaded information gathering and service enumeration.",
            'aliases': ["reconnoitre", "reconnoitre"],
        },
        {
            'name': 'reconscan',
            'description': "Network reconnaissance and vulnerability assessment tools.",
            'aliases': ["reconscan", "reconscan"],
        },
        {
            'name': 'recsech',
            'description': "Tool for doing Footprinting and Reconnaissance on the target web.",
            'aliases': ["recsech", "recsech"],
        },
        {
            'name': 'red-hawk',
            'description': "All in one tool for Information Gathering, Vulnerability Scanning and Crawling.",
            'aliases': ["red-hawk", "red hawk"],
        },
        {
            'name': 'reverseip',
            'description': "Ruby based reverse IP-lookup tool.",
            'aliases': ["reverseip", "reverseip"],
        },
        {
            'name': 'revipd',
            'description': "A simple reverse IP domain scanner.",
            'aliases': ["revipd", "revipd"],
        },
        {
            'name': 'ridrelay',
            'description': "Enumerate usernames on a domain where you have no creds by using SMB Relay with low priv.",
            'aliases': ["ridrelay", "ridrelay"],
        },
        {
            'name': 'ripdc',
            'description': "A script which maps domains related to an given ip address or domainname.",
            'aliases': ["ripdc", "ripdc"],
        },
        {
            'name': 'rita',
            'description': "Real Intelligence Threat Analytics.",
            'aliases': ["rita", "rita"],
        },
        {
            'name': 'rusthound-ce',
            'description': "Active Directory data collector for BloodHound community edition (v5).",
            'aliases': ["rusthound-ce", "rusthound ce"],
        },
        {
            'name': 's3enum',
            'description': "Amazon S3 bucket enumeration.",
            'aliases': ["s3enum", "s3enum"],
        },
        {
            'name': 'scavenger',
            'description': "Crawler (Bot) searching for credential leaks on different paste sites.",
            'aliases': ["scavenger", "scavenger"],
        },
        {
            'name': 'screamer',
            'description': "Fast Subnet Discovery.",
            'aliases': ["screamer", "screamer"],
        },
        {
            'name': 'sctpscan',
            'description': "A network scanner for discovery and security.",
            'aliases': ["sctpscan", "sctpscan"],
        },
        {
            'name': 'scylla',
            'description': "Find Advanced Information on a Username, Website, Phone Number, etc.",
            'aliases': ["scylla", "scylla"],
        },
        {
            'name': 'seekr',
            'description': "A multi-purpose OSINT toolkit with a neat web-interface.",
            'aliases': ["seekr", "seekr"],
        },
        {
            'name': 'server-status-pwn',
            'description': "A script that monitors and extracts requested URLs and clients connected to the service by exploiting publicly accessible Apache server-status instances.",
            'aliases': ["server-status-pwn", "server status pwn"],
        },
        {
            'name': 'shard',
            'description': "A command line tool to detect shared passwords.",
            'aliases': ["shard", "shard"],
        },
        {
            'name': 'shhgit',
            'description': "Find committed secrets and sensitive files across GitHub, Gists, GitLab and BitBucket or your local repositories in real time.",
            'aliases': ["shhgit", "shhgit"],
        },
        {
            'name': 'shodanhat',
            'description': "Search for hosts info with shodan.",
            'aliases': ["shodanhat", "shodanhat"],
        },
        {
            'name': 'shosubgo',
            'description': "Small tool to Grab subdomains using Shodan API.",
            'aliases': ["shosubgo", "shosubgo"],
        },
        {
            'name': 'simplyemail',
            'description': "Email recon made fast and easy, with a framework to build on CyberSyndicates.",
            'aliases': ["simplyemail", "simplyemail"],
        },
        {
            'name': 'sipi',
            'description': "Simple IP Information Tools for Reputation Data Analysis.",
            'aliases': ["sipi", "sipi"],
        },
        {
            'name': 'smbcrunch',
            'description': "3 tools that work together to simplify reconnaissance of Windows File Shares.",
            'aliases': ["smbcrunch", "smbcrunch"],
        },
        {
            'name': 'smtp-user-enum',
            'description': "Username guessing tool primarily for use against the default Solaris SMTP service. Can use either EXPN, VRFY or RCPT TO.",
            'aliases': ["smtp-user-enum", "smtp user enum"],
        },
        {
            'name': 'snscrape',
            'description': "A social networking service scraper in Python.",
            'aliases': ["snscrape", "snscrape"],
        },
        {
            'name': 'socialscan',
            'description': "Check email address and username availability on online platforms.",
            'aliases': ["socialscan", "socialscan"],
        },
        {
            'name': 'spfmap',
            'description': "A program to map out SPF and DKIM records for a large number of domains.",
            'aliases': ["spfmap", "spfmap"],
        },
        {
            'name': 'spiderfoot',
            'description': "The Open Source Footprinting Tool.",
            'aliases': ["spiderfoot", "spiderfoot"],
        },
        {
            'name': 'spoofcheck',
            'description': "Simple script that checks a domain for email protections.",
            'aliases': ["spoofcheck", "spoofcheck"],
        },
        {
            'name': 'spyse',
            'description': "Python API wrapper and command-line client for the tools hosted on spyse.com.",
            'aliases': ["spyse", "spyse"],
        },
        {
            'name': 'sr',
            'description': "Perform subdomain enumeration, endpoint recognition, and more.",
            'aliases': ["sr", "sr"],
        },
        {
            'name': 'ssl-hostname-resolver',
            'description': "CN (Common Name) grabber on X.509 Certificates over HTTPS.",
            'aliases': ["ssl-hostname-resolver", "ssl hostname resolver"],
        },
        {
            'name': 'stardox',
            'description': "Github stargazers information gathering tool.",
            'aliases': ["stardox", "stardox"],
        },
        {
            'name': 'subdomainer',
            'description': "A tool designed for obtaining subdomain names from public sources.",
            'aliases': ["subdomainer", "subdomainer"],
        },
        {
            'name': 'subfinder',
            'description': "Modular subdomain discovery tool that can discover massive amounts of valid subdomains for any target.",
            'aliases': ["subfinder", "sub finder"],
        },
        {
            'name': 'sublert',
            'description': "A security and reconnaissance tool which leverages certificate transparency to automatically monitor new subdomains deployed by specific organizations and issued TLS/SSL certificate.",
            'aliases': ["sublert", "sublert"],
        },
        {
            'name': 'sublist3r',
            'description': "A Fast subdomains enumeration tool for penetration testers.",
            'aliases': ["sublist3r", "sub list 3r", "sublister"],
        },
        {
            'name': 'subscraper',
            'description': "Tool that performs subdomain enumeration through various techniques.",
            'aliases': ["subscraper", "subscraper"],
        },
        {
            'name': 'svn-extractor',
            'description': "A simple script to extract all web resources by means of .SVN folder exposed over network.",
            'aliases': ["svn-extractor", "svn extractor"],
        },
        {
            'name': 'swamp',
            'description': "An OSINT tool for discovering associated sites through Google Analytics Tracking IDs.",
            'aliases': ["swamp", "swamp"],
        },
        {
            'name': 'syborg',
            'description': "Recursive DNS Subdomain Enumerator with dead-end avoidance system.",
            'aliases': ["syborg", "syborg"],
        },
        {
            'name': 'teamsuserenum',
            'description': "User enumeration with Microsoft Teams API",
            'aliases': ["teamsuserenum", "teamsuserenum"],
        },
        {
            'name': 'thedorkbox',
            'description': "Comprehensive collection of Google Dorks & OSINT techniques to find Confidential Data.",
            'aliases': ["thedorkbox", "thedorkbox"],
        },
        {
            'name': 'theharvester',
            'description': "E-mails, subdomains and names Harvester - OSINT",
            'aliases': ["theharvester", "harvester", "the harvester"],
        },
        {
            'name': 'tilt',
            'description': "An easy and simple tool implemented in Python for ip reconnaissance, with reverse ip lookup.",
            'aliases': ["tilt", "tilt"],
        },
        {
            'name': 'tinfoleak',
            'description': "Get detailed information about a Twitter user activity.",
            'aliases': ["tinfoleak", "tinfoleak"],
        },
        {
            'name': 'tinfoleak2',
            'description': "The most complete open-source tool for Twitter intelligence analysis.",
            'aliases': ["tinfoleak2", "tinfoleak2"],
        },
        {
            'name': 'treasure',
            'description': "Hunt for sensitive information through githubs code search.",
            'aliases': ["treasure", "treasure"],
        },
        {
            'name': 'trusttrees',
            'description': "A Tool for DNS Delegation Trust Graphing.",
            'aliases': ["trusttrees", "trusttrees"],
        },
        {
            'name': 'twofi',
            'description': "Twitter Words of Interest.",
            'aliases': ["twofi", "twofi"],
        },
        {
            'name': 'ubiquiti-probing',
            'description': "A Ubiquiti device discovery tool.",
            'aliases': ["ubiquiti-probing", "ubiquiti probing"],
        },
        {
            'name': 'udork',
            'description': "Bash script that uses advanced Google search techniques to obtain sensitive information in files or directories, find IoT devices, detect versions of web applications.",
            'aliases': ["udork", "udork"],
        },
        {
            'name': 'uhoh365',
            'description': "Script to enumerate Office 365 users without performing login attempts",
            'aliases': ["uhoh365", "uhoh365"],
        },
        {
            'name': 'uncover',
            'description': "Discover exposed hosts on the internet using multiple search engines.",
            'aliases': ["uncover", "uncover"],
        },
        {
            'name': 'userrecon',
            'description': "Find usernames across over 75 social networks.",
            'aliases': ["userrecon", "userrecon"],
        },
        {
            'name': 'vbrute',
            'description': "Virtual hosts brute forcer.",
            'aliases': ["vbrute", "vbrute"],
        },
        {
            'name': 'vpnpivot',
            'description': "Explore the network using this tool.",
            'aliases': ["vpnpivot", "vpnpivot"],
        },
        {
            'name': 'waldo',
            'description': "A lightweight and multithreaded directory and subdomain bruteforcer implemented in Python.",
            'aliases': ["waldo", "waldo"],
        },
        {
            'name': 'waybackurls',
            'description': "Fetch all the URLs that the Wayback Machine knows about for a domain.",
            'aliases': ["waybackurls", "waybackurls"],
        },
        {
            'name': 'waymore',
            'description': "Find way more from the Wayback Machine, Common Crawl, Alien Vault OTX, URLScan & VirusTotal.",
            'aliases': ["waymore", "waymore"],
        },
        {
            'name': 'websearch',
            'description': "Search vhost names given a host range. Powered by Bing..",
            'aliases': ["websearch", "websearch"],
        },
        {
            'name': 'weebdns',
            'description': "DNS Enumeration with Asynchronicity.",
            'aliases': ["weebdns", "weebdns"],
        },
        {
            'name': 'whatweb',
            'description': "Next generation web scanner that identifies what websites are running.",
            'aliases': ["whatweb", "what web"],
        },
        {
            'name': 'whoxyrm',
            'description': "A reverse whois tool based on Whoxy API.",
            'aliases': ["whoxyrm", "whoxyrm"],
        },
        {
            'name': 'windapsearch',
            'description': "Script to enumerate users, groups and computers from a Windows domain through LDAP queries.",
            'aliases': ["windapsearch", "windapsearch"],
        },
        {
            'name': 'windows-exploit-suggester',
            'description': "This tool compares a targets patch levels against the Microsoft vulnerability database in order to detect potential missing patches on the target.",
            'aliases': ["windows-exploit-suggester", "windows exploit suggester"],
        },
        {
            'name': 'xray',
            'description': "A tool for recon, mapping and OSINT gathering from public networks.",
            'aliases': ["xray", "xray"],
        },
        {
            'name': 'zeus-scanner',
            'description': "Advanced dork searching utility.",
            'aliases': ["zeus-scanner", "zeus scanner"],
        },
        {
            'name': 'zgrab',
            'description': "Grab banners (optionally over TLS).",
            'aliases': ["zgrab", "zgrab"],
        },
    ],

    # Exploitation (181 tools)
    'blackarch-exploitation': [
        {
            'name': 'aclpwn',
            'description': "Active Directory ACL exploitation with BloodHound.",
            'aliases': ["aclpwn", "aclpwn"],
        },
        {
            'name': 'adaptix-c2',
            'description': "Extensible post-exploitation and adversarial emulation framework.",
            'aliases': ["adaptix-c2", "adaptix c2"],
        },
        {
            'name': 'adenum',
            'description': "A pentesting tool that allows to find misconfiguration through the the protocol LDAP and exploit some of those weaknesses with kerberos.",
            'aliases': ["adenum", "adenum"],
        },
        {
            'name': 'aggroargs',
            'description': "Bruteforce commandline buffer overflows, linux, aggressive arguments.",
            'aliases': ["aggroargs", "aggroargs"],
        },
        {
            'name': 'angrop',
            'description': "A rop gadget finder and chain builder.",
            'aliases': ["angrop", "angrop"],
        },
        {
            'name': 'armitage',
            'description': "A graphical cyber attack management tool for Metasploit.",
            'aliases': ["armitage", "armitage"],
        },
        {
            'name': 'armor',
            'description': "A simple Bash script designed to create encrypted macOS payloads capable of evading antivirus scanners.",
            'aliases': ["armor", "armor"],
        },
        {
            'name': 'armscgen',
            'description': "ARM Shellcode Generator (Mostly Thumb Mode).",
            'aliases': ["armscgen", "armscgen"],
        },
        {
            'name': 'arpoison',
            'description': "The UNIX arp cache update utility",
            'aliases': ["arpoison", "arpoison"],
        },
        {
            'name': 'autosploit',
            'description': "Automate the exploitation of remote hosts.",
            'aliases': ["autosploit", "autosploit"],
        },
        {
            'name': 'backoori',
            'description': "Tool aided persistence via Windows URI schemes abuse.",
            'aliases': ["backoori", "backoori"],
        },
        {
            'name': 'bad-pdf',
            'description': "Steal NTLM Hashes with Bad-PDF.",
            'aliases': ["bad-pdf", "bad pdf"],
        },
        {
            'name': 'barq',
            'description': "An AWS Cloud Post Exploitation framework.",
            'aliases': ["barq", "barq"],
        },
        {
            'name': 'bed',
            'description': "Collection of scripts to test for buffer overflows, format string vulnerabilities.",
            'aliases': ["bed", "bed"],
        },
        {
            'name': 'beef',
            'description': "The Browser Exploitation Framework that focuses on the web browser.",
            'aliases': ["beef", "beef framework", "beef-xss"],
        },
        {
            'name': 'beroot',
            'description': "A post exploitation tool to check common misconfigurations to find a way to escalate our privilege.",
            'aliases': ["beroot", "beroot"],
        },
        {
            'name': 'bfbtester',
            'description': "Perform checks of single and multiple argument command line overflows and environment variable overflows.",
            'aliases': ["bfbtester", "bfbtester"],
        },
        {
            'name': 'binex',
            'description': "Format String exploit building tool.",
            'aliases': ["binex", "binex"],
        },
        {
            'name': 'bitdump',
            'description': "A tool to extract database data from a blind SQL injection vulnerability.",
            'aliases': ["bitdump", "bitdump"],
        },
        {
            'name': 'blind-sql-bitshifting',
            'description': "A blind SQL injection module that uses bitshfting to calculate characters.",
            'aliases': ["blind-sql-bitshifting", "blind sql bitshifting"],
        },
        {
            'name': 'bloodyad',
            'description': "An Active Directory Privilege Escalation Framework.",
            'aliases': ["bloodyad", "bloodyad"],
        },
        {
            'name': 'bluffy',
            'description': "Convert shellcode into different formats.",
            'aliases': ["bluffy", "bluffy"],
        },
        {
            'name': 'botb',
            'description': "A container analysis and exploitation tool for pentesters and engineers.",
            'aliases': ["botb", "botb"],
        },
        {
            'name': 'bowcaster',
            'description': "A framework intended to aid those developing exploits.",
            'aliases': ["bowcaster", "bowcaster"],
        },
        {
            'name': 'brosec',
            'description': "An interactive reference tool to help security professionals utilize useful payloads and commands.",
            'aliases': ["brosec", "brosec"],
        },
        {
            'name': 'camover',
            'description': "A camera exploitation tool that allows to disclosure network camera admin password.",
            'aliases': ["camover", "camover"],
        },
        {
            'name': 'certsync',
            'description': "Dump NTDS remotely without DRSUAPI: using golden certificate and UnPAC the hash.",
            'aliases': ["certsync", "certsync"],
        },
        {
            'name': 'chw00t',
            'description': "Unices chroot breaking tool.",
            'aliases': ["chw00t", "chw00t"],
        },
        {
            'name': 'cisco-global-exploiter',
            'description': "Target multiple vulnerabilities in the Cisco Internetwork Operating System (IOS) and Catalyst products.",
            'aliases': ["cisco-global-exploiter", "cisco global exploiter"],
        },
        {
            'name': 'cisco-torch',
            'description': "Cisco Torch mass scanning, fingerprinting, and exploitation tool.",
            'aliases': ["cisco-torch", "cisco torch"],
        },
        {
            'name': 'coercer',
            'description': "Coerce a Windows server to authenticate on an arbitrary machine through 15 methods.",
            'aliases': ["coercer", "coercer tool"],
        },
        {
            'name': 'cve-search',
            'description': "A tool to perform local searches for known vulnerabilities.",
            'aliases': ["cve-search", "cve search"],
        },
        {
            'name': 'cvemap',
            'description': "CLI tool designed to provide a structured and easily navigable interface to various vulnerability databases.",
            'aliases': ["cvemap", "cvemap"],
        },
        {
            'name': 'darkd0rk3r',
            'description': "Python script that performs dork searching and searches for local file inclusion and SQL injection errors.",
            'aliases': ["darkd0rk3r", "darkd0rk3r"],
        },
        {
            'name': 'darkmysqli',
            'description': "Multi-Purpose MySQL Injection Tool",
            'aliases': ["darkmysqli", "darkmysqli"],
        },
        {
            'name': 'darkspiritz',
            'description': "A penetration testing framework for Linux, MacOS, and Windows systems.",
            'aliases': ["darkspiritz", "darkspiritz"],
        },
        {
            'name': 'deepce',
            'description': "Docker Enumeration, Escalation of Privileges and Container Escapes.",
            'aliases': ["deepce", "deepce"],
        },
        {
            'name': 'delorean',
            'description': "NTP Main-in-the-Middle tool.",
            'aliases': ["delorean", "delorean"],
        },
        {
            'name': 'dkmc',
            'description': "Dont kill my cat - Malicious payload evasion tool.",
            'aliases': ["dkmc", "dkmc"],
        },
        {
            'name': 'dotdotpwn',
            'description': "The Transversal Directory Fuzzer.",
            'aliases': ["dotdotpwn", "dotdotpwn"],
        },
        {
            'name': 'dr-checker',
            'description': "A Soundy Vulnerability Detection Tool for Linux Kernel Drivers.",
            'aliases': ["dr-checker", "dr checker"],
        },
        {
            'name': 'drinkme',
            'description': "A shellcode testing harness.",
            'aliases': ["drinkme", "drinkme"],
        },
        {
            'name': 'ducktoolkit',
            'description': "Encoding Tools for Rubber Ducky.",
            'aliases': ["ducktoolkit", "ducktoolkit"],
        },
        {
            'name': 'encodeshellcode',
            'description': "This is an encoding tool for 32-bit x86 shellcode that assists a researcher when dealing with character filter or byte restrictions in a buffer overflow vulnerability or some kind of IDS/IPS/AV blocking your code.",
            'aliases': ["encodeshellcode", "encodeshellcode"],
        },
        {
            'name': 'enteletaor',
            'description': "Message Queue & Broker Injection tool that implements attacks to Redis, RabbitMQ and ZeroMQ.",
            'aliases': ["enteletaor", "enteletaor"],
        },
        {
            'name': 'entropy',
            'description': "A set of tools to exploit Netwave and GoAhead IP Webcams.",
            'aliases': ["entropy", "entropy"],
        },
        {
            'name': 'erl-matter',
            'description': "Tool to exploit epmd related services such as rabbitmq, ejabberd and couchdb by bruteforcing the cookie and gaining RCE afterwards.",
            'aliases': ["erl-matter", "erl matter"],
        },
        {
            'name': 'evil-winrm',
            'description': "The ultimate WinRM shell for hacking/pentesting.",
            'aliases': ["evil-winrm", "evil winrm", "evilwinrm"],
        },
        {
            'name': 'evilclippy',
            'description': "A cross-platform assistant for creating malicious MS Office documents.",
            'aliases': ["evilclippy", "evilclippy"],
        },
        {
            'name': 'exploit-db',
            'description': "The Exploit Database (EDB) – an ultimate archive of exploits and vulnerable software - A collection of hacks",
            'aliases': ["exploit-db", "exploit db"],
        },
        {
            'name': 'exploitpack',
            'description': "Exploit Pack - The next generation exploit framework.",
            'aliases': ["exploitpack", "exploitpack"],
        },
        {
            'name': 'eyepwn',
            'description': "Exploit for Eye-Fi Helper directory traversal vulnerability",
            'aliases': ["eyepwn", "eyepwn"],
        },
        {
            'name': 'ffm',
            'description': "A hacking harness that you can use during the post-exploitation phase of a red-teaming engagement.",
            'aliases': ["ffm", "ffm"],
        },
        {
            'name': 'firstexecution',
            'description': "A Collection of different ways to execute code outside of the expected entry points.",
            'aliases': ["firstexecution", "firstexecution"],
        },
        {
            'name': 'flashsploit',
            'description': "Exploitation Framework for ATtiny85 Based HID Attacks.",
            'aliases': ["flashsploit", "flashsploit"],
        },
        {
            'name': 'formatstringexploiter',
            'description': "Helper script for working with format string bugs.",
            'aliases': ["formatstringexploiter", "formatstringexploiter"],
        },
        {
            'name': 'fs-exploit',
            'description': "Format string exploit generation.",
            'aliases': ["fs-exploit", "fs exploit"],
        },
        {
            'name': 'fuzzbunch',
            'description': "NSA Exploit framework",
            'aliases': ["fuzzbunch", "fuzzbunch"],
        },
        {
            'name': 'gadgettojscript',
            'description': ".NET serialized gadgets that can trigger .NET assembly from JS/VBS/VBA based scripts.",
            'aliases': ["gadgettojscript", "gadgettojscript"],
        },
        {
            'name': 'getsploit',
            'description': "Command line utility for searching and downloading exploits.",
            'aliases': ["getsploit", "getsploit"],
        },
        {
            'name': 'ghostdelivery',
            'description': "Python script to generate obfuscated .vbs script that delivers payload (payload dropper) with persistence and windows antivirus disabling functions.",
            'aliases': ["ghostdelivery", "ghostdelivery"],
        },
        {
            'name': 'hackredis',
            'description': "A simple tool to scan and exploit redis servers.",
            'aliases': ["hackredis", "hackredis"],
        },
        {
            'name': 'hamster',
            'description': "Tool for HTTP session sidejacking.",
            'aliases': ["hamster", "hamster"],
        },
        {
            'name': 'hcraft',
            'description': "HTTP Vuln Request Crafter.",
            'aliases': ["hcraft", "hcraft"],
        },
        {
            'name': 'heartleech',
            'description': "Scans for systems vulnerable to the heartbleed bug, and then download them.",
            'aliases': ["heartleech", "heartleech"],
        },
        {
            'name': 'hqlmap',
            'description': "A tool to exploit HQL Injections.",
            'aliases': ["hqlmap", "hqlmap"],
        },
        {
            'name': 'htexploit',
            'description': "A Python script that exploits a weakness in the way that .htaccess files can be configured to protect a web directory with an authentication process.",
            'aliases': ["htexploit", "htexploit"],
        },
        {
            'name': 'htshells',
            'description': "Self contained web shells and other attacks via .htaccess files.",
            'aliases': ["htshells", "htshells"],
        },
        {
            'name': 'impacket-ba',
            'description': "Collection of classes for working with network protocols.",
            'aliases': ["impacket-ba", "impacket ba"],
        },
        {
            'name': 'inception',
            'description': "A FireWire physical memory manipulation and hacking tool exploiting IEEE 1394 SBP DMA.",
            'aliases': ["inception", "inception"],
        },
        {
            'name': 'insanity',
            'description': "Generate Payloads and Control Remote Machines .",
            'aliases': ["insanity", "insanity"],
        },
        {
            'name': 'irpas',
            'description': "Internetwork Routing Protocol Attack Suite.",
            'aliases': ["irpas", "irpas"],
        },
        {
            'name': 'isf',
            'description': "An exploitation framework based on Python.",
            'aliases': ["isf", "isf"],
        },
        {
            'name': 'jdwp-knife',
            'description': "Advanced JDWP exploitation and data extraction tool with interactive shell.",
            'aliases': ["jdwp-knife", "jdwp knife"],
        },
        {
            'name': 'jndi-injection-exploit',
            'description': "A tool which generates JNDI links can start several servers to exploit JNDI Injection vulnerability, like Jackson, Fastjson, etc.",
            'aliases': ["jndi-injection-exploit", "jndi injection exploit"],
        },
        {
            'name': 'katana-framework',
            'description': "A framework that seekss to unite general auditing tools, which are general pentesting tools (Network,Web,Desktop and others).",
            'aliases': ["katana-framework", "katana framework"],
        },
        {
            'name': 'kerberoast',
            'description': "Kerberoast attack -pure python-.",
            'aliases': ["kerberoast", "kerberoast"],
        },
        {
            'name': 'kernelpop',
            'description': "Kernel privilege escalation enumeration and exploitation framework.",
            'aliases': ["kernelpop", "kernelpop"],
        },
        {
            'name': 'killcast',
            'description': "Manipulate Chromecast Devices in your Network.",
            'aliases': ["killcast", "killcast"],
        },
        {
            'name': 'killerbee',
            'description': "Framework and tools for exploiting ZigBee and IEEE 802.15.4 networks.",
            'aliases': ["killerbee", "killerbee"],
        },
        {
            'name': 'klar',
            'description': "Integration of Clair and Docker Registry.",
            'aliases': ["klar", "klar"],
        },
        {
            'name': 'l0l',
            'description': "The Exploit Development Kit.",
            'aliases': ["l0l", "l0l"],
        },
        {
            'name': 'leroy-jenkins',
            'description': "A python tool that will allow remote execution of commands on a Jenkins server and its nodes.",
            'aliases': ["leroy-jenkins", "leroy jenkins"],
        },
        {
            'name': 'lfi-autopwn',
            'description': "A Perl script to try to gain code execution on a remote server via LFI.",
            'aliases': ["lfi-autopwn", "lfi autopwn"],
        },
        {
            'name': 'limelighter',
            'description': "A tool for generating fake code signing certificates or signing real ones.",
            'aliases': ["limelighter", "limelighter"],
        },
        {
            'name': 'lisa.py',
            'description': "An Exploit Dev Swiss Army Knife.",
            'aliases': ["lisa.py", "lisa.py"],
        },
        {
            'name': 'm3-gen',
            'description': "Generates Malicious Macro and Execute Powershell or Shellcode via MSBuild Application Whitelisting Bypass, this tool intended for adversary simulation and red teaming purpose.",
            'aliases': ["m3-gen", "m3 gen"],
        },
        {
            'name': 'marshalsec',
            'description': "Java Unmarshaller Security - Turning your data into code execution.",
            'aliases': ["marshalsec", "marshalsec"],
        },
        {
            'name': 'minimysqlator',
            'description': "A multi-platform application used to audit web sites in order to discover and exploit SQL injection vulnerabilities.",
            'aliases': ["minimysqlator", "minimysqlator"],
        },
        {
            'name': 'miranda-upnp',
            'description': "A Python-based Universal Plug-N-Play client application designed to discover, query and interact with UPNP devices.",
            'aliases': ["miranda-upnp", "miranda upnp"],
        },
        {
            'name': 'mitmf',
            'description': "A Framework for Man-In-The-Middle attacks written in Python.",
            'aliases': ["mitmf", "mitmf"],
        },
        {
            'name': 'moonwalk',
            'description': "Cover your tracks during Linux Exploitation by leaving zero traces on system logs and filesystem timestamps.",
            'aliases': ["moonwalk", "moonwalk"],
        },
        {
            'name': 'mosquito',
            'description': "XSS exploitation tool - access victims through HTTP proxy.",
            'aliases': ["mosquito", "mosquito"],
        },
        {
            'name': 'myjwt',
            'description': "This cli is for pentesters, CTF players, or dev. You can modify your jwt, sign, inject, etc.",
            'aliases': ["myjwt", "myjwt"],
        },
        {
            'name': 'n1qlmap',
            'description': "An N1QL exploitation tool.",
            'aliases': ["n1qlmap", "n1qlmap"],
        },
        {
            'name': 'nosqli-user-pass-enum',
            'description': "Script to enumerate usernames and passwords from vulnerable web applications running MongoDB.",
            'aliases': ["nosqli-user-pass-enum", "nosqli user pass enum"],
        },
        {
            'name': 'ntlm-theft',
            'description': "A tool for generating multiple types of NTLMv2 hash theft files.",
            'aliases': ["ntlm-theft", "ntlm theft"],
        },
        {
            'name': 'office-dde-payloads',
            'description': "Collection of scripts and templates to generate Office documents embedded with the DDE, macro-less command execution technique.",
            'aliases': ["office-dde-payloads", "office dde payloads"],
        },
        {
            'name': 'opensvp',
            'description': "A security tool implementing \"attacks\" to be able to the resistance of firewall to protocol level attack.",
            'aliases': ["opensvp", "opensvp"],
        },
        {
            'name': 'osueta',
            'description': "A simple Python script to exploit the OpenSSH User Enumeration Timing Attack.",
            'aliases': ["osueta", "osueta"],
        },
        {
            'name': 'otori',
            'description': "Toolbox intended to allow useful exploitation of XML external entity (\"XXE\") vulnerabilities.",
            'aliases': ["otori", "otori"],
        },
        {
            'name': 'owasp-zsc',
            'description': "Shellcode/Obfuscate Code Generator.",
            'aliases': ["owasp-zsc", "owasp zsc"],
        },
        {
            'name': 'pacu',
            'description': "The AWS exploitation framework, designed for testing the security of Amazon Web Services environments.",
            'aliases': ["pacu", "pacu"],
        },
        {
            'name': 'pathzuzu',
            'description': "Checks for PATH substitution vulnerabilities and logs the commands executed by the vulnerable executables.",
            'aliases': ["pathzuzu", "pathzuzu"],
        },
        {
            'name': 'pblind',
            'description': "Little utility to help exploiting blind sql injection vulnerabilities.",
            'aliases': ["pblind", "pblind"],
        },
        {
            'name': 'phantom-evasion',
            'description': "Antivirus evasion tool written in python.",
            'aliases': ["phantom-evasion", "phantom evasion"],
        },
        {
            'name': 'pirana',
            'description': "Exploitation framework that tests the security of a email content filter.",
            'aliases': ["pirana", "pirana"],
        },
        {
            'name': 'pkinittools',
            'description': "Tools for Kerberos PKINIT and relaying to AD CS.",
            'aliases': ["pkinittools", "pkinittools"],
        },
        {
            'name': 'pmcma',
            'description': "Automated exploitation of invalid memory writes (being them the consequences of an overflow in a writable section, of a missing format string, integer overflow, variable misuse, or any other type of memory corruption).",
            'aliases': ["pmcma", "pmcma"],
        },
        {
            'name': 'pocsuite',
            'description': "An open-sourced remote vulnerability testing framework developed by the Knownsec Security Team.",
            'aliases': ["pocsuite", "pocsuite"],
        },
        {
            'name': 'pompem',
            'description': "A python exploit tool finder.",
            'aliases': ["pompem", "pompem"],
        },
        {
            'name': 'powersploit',
            'description': "A PowerShell Post-Exploitation Framework.",
            'aliases': ["powersploit", "power sploit"],
        },
        {
            'name': 'preeny',
            'description': "Some helpful preload libraries for pwning stuff.",
            'aliases': ["preeny", "preeny"],
        },
        {
            'name': 'pret',
            'description': "Printer Exploitation Toolkit - The tool that made dumpster diving obsolete.",
            'aliases': ["pret", "pret"],
        },
        {
            'name': 'ps1encode',
            'description': "A tool to generate and encode a PowerShell based Metasploit payloads.",
            'aliases': ["ps1encode", "ps1encode"],
        },
        {
            'name': 'ptf',
            'description': "The Penetration Testers Framework: Way for modular support for up-to-date tools.",
            'aliases': ["ptf", "ptf"],
        },
        {
            'name': 'punk',
            'description': "A post-exploitation tool meant to help network pivoting from a compromised unix box.",
            'aliases': ["punk", "punk"],
        },
        {
            'name': 'pwncat-caleb',
            'description': "A post-exploitation platform.",
            'aliases': ["pwncat-caleb", "pwncat caleb"],
        },
        {
            'name': 'pykek',
            'description': "Kerberos Exploitation Kit.",
            'aliases': ["pykek", "pykek"],
        },
        {
            'name': 'python-ssh-mitm',
            'description': "SSH mitm server for security audits supporting public key authentication, session hijacking and file manipulation.",
            'aliases': ["python-ssh-mitm", "python ssh mitm"],
        },
        {
            'name': 'python2-ropgadget',
            'description': "Pythonic argument parser, that will make you smile.",
            'aliases': ["python2-ropgadget", "python2 ropgadget"],
        },
        {
            'name': 'rebind',
            'description': "DNS Rebinding Tool.",
            'aliases': ["rebind", "rebind"],
        },
        {
            'name': 'rex',
            'description': "Shellphish\'s automated exploitation engine, originally created for the Cyber Grand Challenge.",
            'aliases': ["rex", "rex"],
        },
        {
            'name': 'rext',
            'description': "Router EXploitation Toolkit - small toolkit for easy creation and usage of various python scripts that work with embedded devices.",
            'aliases': ["rext", "rext"],
        },
        {
            'name': 'richsploit',
            'description': "Exploitation toolkit for RichFaces.",
            'aliases': ["richsploit", "richsploit"],
        },
        {
            'name': 'rmiscout',
            'description': "Enumerate Java RMI functions and exploit RMI parameter unmarshalling vulnerabilities.",
            'aliases': ["rmiscout", "rmiscout"],
        },
        {
            'name': 'rombuster',
            'description': "A router exploitation tool that allows to disclosure network router admin password.",
            'aliases': ["rombuster", "rombuster"],
        },
        {
            'name': 'ropeme',
            'description': "A set of python scripts to generate ROP gadgets and payload.",
            'aliases': ["ropeme", "ropeme"],
        },
        {
            'name': 'roputils',
            'description': "A Return-oriented Programming toolkit.",
            'aliases': ["roputils", "roputils"],
        },
        {
            'name': 'rp',
            'description': "A full-cpp written tool that aims to find ROP sequences in PE/Elf/Mach-O x86/x64 binaries.",
            'aliases': ["rp", "rp"],
        },
        {
            'name': 'rspet',
            'description': "A Python based reverse shell equipped with functionalities that assist in a post exploitation scenario.",
            'aliases': ["rspet", "rspet"],
        },
        {
            'name': 'sc-make',
            'description': "Tool for automating shellcode creation.",
            'aliases': ["sc-make", "sc make"],
        },
        {
            'name': 'scansploit',
            'description': "Exploit using barcodes, QRcodes, earn13, datamatrix.",
            'aliases': ["scansploit", "scansploit"],
        },
        {
            'name': 'sensepost-xrdp',
            'description': "A rudimentary remote desktop tool for the X11 protocol exploiting unauthenticated x11 sessions.",
            'aliases': ["sensepost-xrdp", "sensepost xrdp"],
        },
        {
            'name': 'serialbrute',
            'description': "Java serialization brute force attack tool.",
            'aliases': ["serialbrute", "serialbrute"],
        },
        {
            'name': 'shellcode-compiler',
            'description': "Compiles C/C++ style code into a small, position-independent and NULL-free shellcode for Windows & Linux.",
            'aliases': ["shellcode-compiler", "shellcode compiler"],
        },
        {
            'name': 'shellcode-factory',
            'description': "Tool to create and test shellcodes from custom assembly sources.",
            'aliases': ["shellcode-factory", "shellcode factory"],
        },
        {
            'name': 'shellcodecs',
            'description': "A collection of shellcode, loaders, sources, and generators provided with documentation designed to ease the exploitation and shellcode programming process.",
            'aliases': ["shellcodecs", "shellcodecs"],
        },
        {
            'name': 'shellen',
            'description': "Interactive shellcoding environment to easily craft shellcodes.",
            'aliases': ["shellen", "shellen"],
        },
        {
            'name': 'shellme',
            'description': "Because sometimes you just need shellcode and opcodes quickly. This essentially just wraps some nasm/objdump calls into a neat script.",
            'aliases': ["shellme", "shellme"],
        },
        {
            'name': 'shellsploit-framework',
            'description': "New Generation Exploit Development Kit.",
            'aliases': ["shellsploit-framework", "shellsploit framework"],
        },
        {
            'name': 'shellter',
            'description': "A dynamic shellcode injection tool, and the first truly dynamic PE infector ever created.",
            'aliases': ["shellter", "shellter"],
        },
        {
            'name': 'shocker',
            'description': "A tool to find and exploit servers vulnerable to Shellshock.",
            'aliases': ["shocker", "shocker"],
        },
        {
            'name': 'sickle',
            'description': "A shellcode development tool, created to speed up the various steps needed to create functioning shellcode.",
            'aliases': ["sickle", "sickle"],
        },
        {
            'name': 'sigploit',
            'description': "Telecom Signaling Exploitation Framework - SS7, GTP, Diameter & SIP.",
            'aliases': ["sigploit", "sigploit"],
        },
        {
            'name': 'sigthief',
            'description': "Stealing Signatures and Making One Invalid Signature at a Time.",
            'aliases': ["sigthief", "sigthief"],
        },
        {
            'name': 'sireprat',
            'description': "Remote Command Execution as SYSTEM on Windows IoT Core.",
            'aliases': ["sireprat", "sireprat"],
        },
        {
            'name': 'sjet',
            'description': "Siberas JMX exploitation toolkit.",
            'aliases': ["sjet", "sjet"],
        },
        {
            'name': 'smap',
            'description': "Shellcode mapper - Handy tool for shellcode analysis.",
            'aliases': ["smap", "smap"],
        },
        {
            'name': 'smtptester',
            'description': "Small python3 tool to check common vulnerabilities in SMTP servers.",
            'aliases': ["smtptester", "smtptester"],
        },
        {
            'name': 'snarf-mitm',
            'description': "SMB Man in the Middle Attack Engine / relay suite.",
            'aliases': ["snarf-mitm", "snarf mitm"],
        },
        {
            'name': 'spraykatz',
            'description': "Credentials gathering tool automating remote procdump and parse of lsass process.",
            'aliases': ["spraykatz", "spray katz"],
        },
        {
            'name': 'sqlninja',
            'description': "A tool targeted to exploit SQL Injection vulnerabilities on a web application that uses Microsoft SQL Server as its back-end.",
            'aliases': ["sqlninja", "sqlninja"],
        },
        {
            'name': 'sqlsus',
            'description': "An open source MySQL injection and takeover tool.",
            'aliases': ["sqlsus", "sqlsus"],
        },
        {
            'name': 'ssh-mitm',
            'description': "SSH man-in-the-middle tool.",
            'aliases': ["ssh-mitm", "ssh mitm"],
        },
        {
            'name': 'sstimap',
            'description': "Automatic SSTI detection tool with interactive interface.",
            'aliases': ["sstimap", "sstimap"],
        },
        {
            'name': 'stackflow',
            'description': "Universal stack-based buffer overfow exploitation tool.",
            'aliases': ["stackflow", "stackflow"],
        },
        {
            'name': 'staekka',
            'description': "This plugin extends Metasploit for some missing features and modules allowing interaction with other/custom exploits/ways of getting shell access.",
            'aliases': ["staekka", "staekka"],
        },
        {
            'name': 'subterfuge',
            'description': "Automated Man-in-the-Middle Attack Framework.",
            'aliases': ["subterfuge", "subterfuge"],
        },
        {
            'name': 'suid3num',
            'description': "Python script which utilizes python\'s built-in modules to enumerate SUID binaries.",
            'aliases': ["suid3num", "suid3num"],
        },
        {
            'name': 'tcpjunk',
            'description': "A general tcp protocols testing and hacking utility.",
            'aliases': ["tcpjunk", "tcpjunk"],
        },
        {
            'name': 'tomcatwardeployer',
            'description': "Apache Tomcat auto WAR deployment & pwning penetration testing tool.",
            'aliases': ["tomcatwardeployer", "tomcatwardeployer"],
        },
        {
            'name': 'unibrute',
            'description': "Multithreaded SQL union bruteforcer.",
            'aliases': ["unibrute", "unibrute"],
        },
        {
            'name': 'venom',
            'description': "A Multi-hop Proxy for Penetration Testers.",
            'aliases': ["venom", "venom"],
        },
        {
            'name': 'viproy-voipkit',
            'description': "VoIP Pen-Test Kit for Metasploit Framework.",
            'aliases': ["viproy-voipkit", "viproy voipkit"],
        },
        {
            'name': 'vmap',
            'description': "A Vulnerability-Exploit desktop finder.",
            'aliases': ["vmap", "vmap"],
        },
        {
            'name': 'volana',
            'description': "Shell command obfuscation to avoid detection systems.",
            'aliases': ["volana", "volana"],
        },
        {
            'name': 'webexploitationtool',
            'description': "A cross platform web exploitation toolkit.",
            'aliases': ["webexploitationtool", "webexploitationtool"],
        },
        {
            'name': 'websploit',
            'description': "An Open Source Project For, Social Engineering Works, Scan, Crawler & Analysis Web, Automatic Exploiter, Support Network Attacks",
            'aliases': ["websploit", "websploit"],
        },
        {
            'name': 'wesng',
            'description': "Windows Exploit Suggester - Next Generation.",
            'aliases': ["wesng", "wesng"],
        },
        {
            'name': 'wildpwn',
            'description': "Unix wildcard attacks.",
            'aliases': ["wildpwn", "wildpwn"],
        },
        {
            'name': 'wsuspect-proxy',
            'description': "A tool for MITM\'ing insecure WSUS connections.",
            'aliases': ["wsuspect-proxy", "wsuspect proxy"],
        },
        {
            'name': 'xcat',
            'description': "A command line tool to automate the exploitation of blind XPath injection vulnerabilities.",
            'aliases': ["xcat", "xcat"],
        },
        {
            'name': 'xpl-search',
            'description': "Search exploits in multiple exploit databases!.",
            'aliases': ["xpl-search", "xpl search"],
        },
        {
            'name': 'xrop',
            'description': "Tool to generate ROP gadgets for ARM, AARCH64, x86, MIPS, PPC, RISCV, SH4 and SPARC.",
            'aliases': ["xrop", "xrop"],
        },
        {
            'name': 'xxeinjector',
            'description': "Tool for automatic exploitation of XXE vulnerability using direct and different out of band methods.",
            'aliases': ["xxeinjector", "xxeinjector"],
        },
        {
            'name': 'xxexploiter',
            'description': "It generates the XML payloads, and automatically starts a server to serve the needed DTD\'s or to do data exfiltration.",
            'aliases': ["xxexploiter", "xxexploiter"],
        },
        {
            'name': 'yinjector',
            'description': "A MySQL injection penetration tool. It has multiple features, proxy support, and multiple exploitation methods.",
            'aliases': ["yinjector", "yinjector"],
        },
        {
            'name': 'zarp',
            'description': "A network attack tool centered around the exploitation of local networks.",
            'aliases': ["zarp", "zarp"],
        },
        {
            'name': 'zeratool',
            'description': "Automatic Exploit Generation (AEG) and remote flag capture for exploitable CTF problems.",
            'aliases': ["zeratool", "zeratool"],
        },
        {
            'name': 'zirikatu',
            'description': "Fud Payload generator script.",
            'aliases': ["zirikatu", "zirikatu"],
        },
    ],

    # Cracker (161 tools)
    'blackarch-cracker': [
        {
            'name': 'acccheck',
            'description': "A password dictionary attack tool that targets windows authentication via the SMB protocol.",
            'aliases': ["acccheck", "acccheck"],
        },
        {
            'name': 'adfspray',
            'description': "Python3 tool to perform password spraying against Microsoft Online service using various methods.",
            'aliases': ["adfspray", "adfspray"],
        },
        {
            'name': 'aesfix',
            'description': "A tool to find AES key in RAM.",
            'aliases': ["aesfix", "aesfix"],
        },
        {
            'name': 'aeskeyfind',
            'description': "A tool to find AES key in RAM.",
            'aliases': ["aeskeyfind", "aeskeyfind"],
        },
        {
            'name': 'against',
            'description': "A very fast ssh attacking script which includes a multithreaded port scanning module (tcp connect) for discovering possible targets and a multithreaded brute-forcing module which attacks parallel all discovered hosts or given ip addresses from a list.",
            'aliases': ["against", "against"],
        },
        {
            'name': 'ares',
            'description': "Automated decoding of encrypted text without knowing the key or ciphers used.",
            'aliases': ["ares", "ares"],
        },
        {
            'name': 'asleap',
            'description': "Actively recover LEAP/PPTP passwords.",
            'aliases': ["asleap", "as leap"],
        },
        {
            'name': 'beleth',
            'description': "A Multi-threaded Dictionary based SSH cracker.",
            'aliases': ["beleth", "beleth"],
        },
        {
            'name': 'bgp-md5crack',
            'description': "RFC2385 password cracker",
            'aliases': ["bgp-md5crack", "bgp md5crack"],
        },
        {
            'name': 'bios_memimage',
            'description': "A tool to dump RAM contents to disk (aka cold boot attack).",
            'aliases': ["bios_memimage", "bios memimage"],
        },
        {
            'name': 'bkcrack',
            'description': "Crack legacy zip encryption with Biham and Kocher known plaintext attack.",
            'aliases': ["bkcrack", "bkcrack"],
        },
        {
            'name': 'bkhive',
            'description': "Program for dumping the syskey bootkey from a Windows NT/2K/XP system hive.",
            'aliases': ["bkhive", "bkhive"],
        },
        {
            'name': 'blackhash',
            'description': "Creates a filter from system hashes.",
            'aliases': ["blackhash", "blackhash"],
        },
        {
            'name': 'bob-the-butcher',
            'description': "A distributed password cracker package.",
            'aliases': ["bob-the-butcher", "bob the butcher"],
        },
        {
            'name': 'brute-force',
            'description': "Brute-Force attack tool for Gmail Hotmail Twitter Facebook Netflix.",
            'aliases': ["brute-force", "brute force"],
        },
        {
            'name': 'bruteforce-luks',
            'description': "Try to find the password of a LUKS encrypted volume.",
            'aliases': ["bruteforce-luks", "bruteforce luks"],
        },
        {
            'name': 'bruteforce-salted-openssl',
            'description': "Try to find the password of a file that was encrypted with the \'openssl\' command.",
            'aliases': ["bruteforce-salted-openssl", "bruteforce salted openssl"],
        },
        {
            'name': 'bruteforce-wallet',
            'description': "Try to find the password of an encrypted Peercoin (or Bitcoin,Litecoin, etc...) wallet file.",
            'aliases': ["bruteforce-wallet", "bruteforce wallet"],
        },
        {
            'name': 'brutessh',
            'description': "A simple sshd password bruteforcer using a wordlist, it\'s very fast for internal networks. It\'s multithreads.",
            'aliases': ["brutessh", "brutessh"],
        },
        {
            'name': 'chapcrack',
            'description': "A tool for parsing and decrypting MS-CHAPv2 network handshakes.",
            'aliases': ["chapcrack", "chapcrack"],
        },
        {
            'name': 'cintruder',
            'description': "An automatic pentesting tool to bypass captchas.",
            'aliases': ["cintruder", "cintruder"],
        },
        {
            'name': 'cisco-auditing-tool',
            'description': "Perl script which scans cisco routers for common vulnerabilities. Checks for default passwords, easily guessable community names, and the IOS history bug. Includes support for plugins and scanning multiple hosts.",
            'aliases': ["cisco-audit", "cisco auditing tool"],
        },
        {
            'name': 'cisco-ocs',
            'description': "Cisco Router Default Password Scanner.",
            'aliases': ["cisco-ocs", "cisco ocs"],
        },
        {
            'name': 'cisco-scanner',
            'description': "Multithreaded Cisco HTTP vulnerability scanner. Tested on Linux, OpenBSD and Solaris.",
            'aliases': ["cisco-scanner", "cisco scanner"],
        },
        {
            'name': 'cisco5crack',
            'description': "Crypt and decrypt the cisco enable 5 passwords.",
            'aliases': ["cisco5crack", "cisco5crack"],
        },
        {
            'name': 'cisco7crack',
            'description': "Crypt and decrypt the cisco enable 7 passwords.",
            'aliases': ["cisco7crack", "cisco7crack"],
        },
        {
            'name': 'cmospwd',
            'description': "Decrypts password stored in CMOS used to access BIOS setup.",
            'aliases': ["cmospwd", "cmospwd"],
        },
        {
            'name': 'compp',
            'description': "Company Passwords Profiler helps making a bruteforce wordlist for a targeted company.",
            'aliases': ["compp", "compp"],
        },
        {
            'name': 'crackhor',
            'description': "A Password cracking utility.",
            'aliases': ["crackhor", "crackhor"],
        },
        {
            'name': 'crackle',
            'description': "Crack and decrypt BLE encryption.",
            'aliases': ["crackle", "crackle"],
        },
        {
            'name': 'crackpkcs12',
            'description': "A multithreaded program to crack PKCS#12 files (p12 and pfx extensions).",
            'aliases': ["crackpkcs12", "crackpkcs12"],
        },
        {
            'name': 'crackq',
            'description': "Hashcrack.org GPU-accelerated password cracker.",
            'aliases': ["crackq", "crackq"],
        },
        {
            'name': 'crackserver',
            'description': "An XMLRPC server for password cracking.",
            'aliases': ["crackserver", "crackserver"],
        },
        {
            'name': 'creddump',
            'description': "A python tool to extract various credentials and secrets from Windows registry hives.",
            'aliases': ["creddump", "creddump"],
        },
        {
            'name': 'credmaster',
            'description': "Refactored & improved CredKing password spraying tool, uses FireProx APIs to rotate IP addresses, stay anonymous, and beat throttling.",
            'aliases': ["credmaster", "credmaster"],
        },
        {
            'name': 'crowbar',
            'description': "Brute forcing tool that can be used during penetration tests.",
            'aliases': ["crowbar", "crowbar bruteforce"],
        },
        {
            'name': 'cryptohazemultiforcer',
            'description': "High performance multihash brute forcer with CUDA support.",
            'aliases': ["cryptohazemultiforcer", "cryptohazemultiforcer"],
        },
        {
            'name': 'cudahashcat',
            'description': "Worlds fastest WPA cracker with dictionary mutation engine.",
            'aliases': ["cudahashcat", "cudahashcat"],
        },
        {
            'name': 'cupp',
            'description': "Common User Password Profiler",
            'aliases': ["cupp", "cupp"],
        },
        {
            'name': 'dbpwaudit',
            'description': "A Java tool that allows you to perform online audits of password quality for several database engines.",
            'aliases': ["dbpwaudit", "dbpwaudit"],
        },
        {
            'name': 'depant',
            'description': "Check network for services with default passwords.",
            'aliases': ["depant", "depant"],
        },
        {
            'name': 'device-pharmer',
            'description': "Opens 1K+ IPs or Shodan search results and attempts to login.",
            'aliases': ["device-pharmer", "device pharmer"],
        },
        {
            'name': 'doozer',
            'description': "A Password cracking utility.",
            'aliases': ["doozer", "doozer"],
        },
        {
            'name': 'dpeparser',
            'description': "Default password enumeration project",
            'aliases': ["dpeparser", "dpeparser"],
        },
        {
            'name': 'eapmd5pass',
            'description': "An implementation of an offline dictionary attack against the EAP-MD5 protocol.",
            'aliases': ["eapmd5pass", "eap md5 pass"],
        },
        {
            'name': 'enabler',
            'description': "Attempts to find the enable password on a cisco system via brute force.",
            'aliases': ["enabler", "enabler"],
        },
        {
            'name': 'evilize',
            'description': "Tool to create MD5 colliding binaries.",
            'aliases': ["evilize", "evilize"],
        },
        {
            'name': 'evilmaid',
            'description': "TrueCrypt loader backdoor to sniff volume password.",
            'aliases': ["evilmaid", "evilmaid"],
        },
        {
            'name': 'f-scrack',
            'description': "A single file bruteforcer supports multi-protocol.",
            'aliases': ["f-scrack", "f scrack"],
        },
        {
            'name': 'facebrute',
            'description': "This script tries to guess passwords for a given facebook account using a list of passwords (dictionary).",
            'aliases': ["facebrute", "facebrute"],
        },
        {
            'name': 'fang',
            'description': "A multi service threaded MD5 cracker.",
            'aliases': ["fang", "fang"],
        },
        {
            'name': 'flask-unsign',
            'description': "Command line tool to fetch, decode, brute-force and craft session cookies of a Flask application by guessing secret keys.",
            'aliases': ["flask-unsign", "flask unsign"],
        },
        {
            'name': 'ftp-scanner',
            'description': "Multithreaded ftp scanner/brute forcer. Tested on Linux, OpenBSD and Solaris.",
            'aliases': ["ftp-scanner", "ftp scanner"],
        },
        {
            'name': 'gomapenum',
            'description': "User enumeration and password bruteforce on Azure, ADFS, OWA, O365, Teams and gather emails on Linkedin.",
            'aliases': ["gomapenum", "gomapenum"],
        },
        {
            'name': 'gpocrack',
            'description': "Active Directory Group Policy Preferences cpassword cracker/decrypter.",
            'aliases': ["gpocrack", "gpocrack"],
        },
        {
            'name': 'hasher',
            'description': "A tool that allows you to quickly hash plaintext strings, or compare hashed values with a plaintext locally.",
            'aliases': ["hasher", "hasher"],
        },
        {
            'name': 'hashtag',
            'description': "A python script written to parse and identify password hashes.",
            'aliases': ["hashtag", "hashtag"],
        },
        {
            'name': 'hostbox-ssh',
            'description': "A ssh password/account scanner.",
            'aliases': ["hostbox-ssh", "hostbox ssh"],
        },
        {
            'name': 'htpwdscan',
            'description': "A python HTTP weak pass scanner.",
            'aliases': ["htpwdscan", "htpwdscan"],
        },
        {
            'name': 'ibrute',
            'description': "An AppleID password bruteforce tool. It uses Find My Iphone service API, where bruteforce protection was not implemented.",
            'aliases': ["ibrute", "ibrute"],
        },
        {
            'name': 'icloudbrutter',
            'description': "Tool for AppleID Bruteforce.",
            'aliases': ["icloudbrutter", "icloudbrutter"],
        },
        {
            'name': 'iheartxor',
            'description': "A tool for bruteforcing encoded strings within a boundary defined by a regular expression. It will bruteforce the key value range of 0x1 through 0x255.",
            'aliases': ["iheartxor", "iheartxor"],
        },
        {
            'name': 'iisbruteforcer',
            'description': "HTTP authentication cracker. It\'s a tool that launchs an online dictionary attack to test for weak or simple passwords against protected areas on an IIS Web server.",
            'aliases': ["iisbruteforcer", "iisbruteforcer"],
        },
        {
            'name': 'ikecrack',
            'description': "An IKE/IPSec crack tool designed to perform Pre-Shared-Key analysis of RFC compliant aggressive mode authentication",
            'aliases': ["ikecrack", "ikecrack"],
        },
        {
            'name': 'ikeforce',
            'description': "A command line IPSEC VPN brute forcing tool for Linux that allows group name/ID enumeration and XAUTH brute forcing capabilities.",
            'aliases': ["ikeforce", "ikeforce"],
        },
        {
            'name': 'inguma',
            'description': "A free penetration testing and vulnerability discovery toolkit entirely written in python. Framework includes modules to discover hosts, gather information about, fuzz targets, brute force usernames and passwords, exploits, and a disassembler.",
            'aliases': ["inguma", "inguma"],
        },
        {
            'name': 'instashell',
            'description': "Multi-threaded Instagram Brute Forcer without password limit.",
            'aliases': ["instashell", "instashell"],
        },
        {
            'name': 'ipmipwn',
            'description': "IPMI cipher 0 attack tool.",
            'aliases': ["ipmipwn", "ipmipwn"],
        },
        {
            'name': 'jbrute',
            'description': "Open Source Security tool to audit hashed passwords.",
            'aliases': ["jbrute", "jbrute"],
        },
        {
            'name': 'jeangrey',
            'description': "A tool to perform differential fault analysis attacks (DFA).",
            'aliases': ["jeangrey", "jeangrey"],
        },
        {
            'name': 'johnny',
            'description': "GUI for John the Ripper.",
            'aliases': ["johnny", "john gui"],
        },
        {
            'name': 'jwt-cracker',
            'description': "JWT brute force cracker written in C.",
            'aliases': ["jwt-cracker", "jwt cracker"],
        },
        {
            'name': 'jwt-tool',
            'description': "Toolkit for validating, forging and cracking JWTs (JSON Web Tokens).",
            'aliases': ["jwt-tool", "jwt tool"],
        },
        {
            'name': 'jwtcat',
            'description': "Script performs offline brute-force attacks against JSON Web Token (JWT)",
            'aliases': ["jwtcat", "jwtcat"],
        },
        {
            'name': 'keimpx',
            'description': "Tool to verify the usefulness of credentials across a network over SMB.",
            'aliases': ["keimpx", "keimpx tool"],
        },
        {
            'name': 'kerbrute',
            'description': "A tool to perform Kerberos pre-auth bruteforcing.",
            'aliases': ["kerbrute", "kerb brute"],
        },
        {
            'name': 'khc',
            'description': "A small tool designed to recover hashed known_hosts fiels back to their plain-text equivalents.",
            'aliases': ["khc", "khc"],
        },
        {
            'name': 'ldap-brute',
            'description': "A semi fast tool to bruteforce values of LDAP injections over HTTP.",
            'aliases': ["ldap-brute", "ldap brute"],
        },
        {
            'name': 'levye',
            'description': "A brute force tool which is support sshkey, vnckey, rdp, openvpn.",
            'aliases': ["levye", "levye"],
        },
        {
            'name': 'lodowep',
            'description': "Lodowep is a tool for analyzing password strength of accounts on a Lotus Domino webserver system.",
            'aliases': ["lodowep", "lodowep"],
        },
        {
            'name': 'mdcrack',
            'description': "MD4/MD5/NTLM1 hash cracker",
            'aliases': ["mdcrack", "mdcrack"],
        },
        {
            'name': 'mkbrutus',
            'description': "Password bruteforcer for MikroTik devices or boxes running RouterOS.",
            'aliases': ["mkbrutus", "mkbrutus"],
        },
        {
            'name': 'morxbook',
            'description': "A password cracking tool written in perl to perform a dictionary-based attack on a specific Facebook user through HTTPS.",
            'aliases': ["morxbook", "morxbook"],
        },
        {
            'name': 'morxbrute',
            'description': "A customizable HTTP dictionary-based password cracking tool written in Perl.",
            'aliases': ["morxbrute", "morxbrute"],
        },
        {
            'name': 'morxbtcrack',
            'description': "Single Bitcoin private key cracking tool released.",
            'aliases': ["morxbtcrack", "morxbtcrack"],
        },
        {
            'name': 'morxcoinpwn',
            'description': "Mass Bitcoin private keys brute forcing/Take over tool released.",
            'aliases': ["morxcoinpwn", "morxcoinpwn"],
        },
        {
            'name': 'morxcrack',
            'description': "A cracking tool written in Perl to perform a dictionary-based attack on various hashing algorithm and CMS salted-passwords.",
            'aliases': ["morxcrack", "morxcrack"],
        },
        {
            'name': 'mybff',
            'description': "A Brute Force Framework.",
            'aliases': ["mybff", "mybff"],
        },
        {
            'name': 'o365enum',
            'description': "Username enumeration and password enuming tool aimed at Microsoft O365.",
            'aliases': ["o365enum", "o365enum"],
        },
        {
            'name': 'o365spray',
            'description': "Username enumeration and password spraying tool aimed at Microsoft O365.",
            'aliases': ["o365spray", "o365spray"],
        },
        {
            'name': 'obevilion',
            'description': "Another archive cracker created in python, cracking [zip/7z/rar].",
            'aliases': ["obevilion", "obevilion"],
        },
        {
            'name': 'oclhashcat',
            'description': "Worlds fastest WPA cracker with dictionary mutation engine.",
            'aliases': ["oclhashcat", "oclhashcat"],
        },
        {
            'name': 'omen',
            'description': "Ordered Markov ENumerator - Password Guesser.",
            'aliases': ["omen", "omen"],
        },
        {
            'name': 'onesixtyone',
            'description': "An SNMP scanner that sends multiple SNMP requests to multiple IP addresses",
            'aliases': ["onesixtyone", "one sixty one"],
        },
        {
            'name': 'ophcrack',
            'description': "Windows password cracker based on rainbow tables.",
            'aliases': ["ophcrack", "ophcrack"],
        },
        {
            'name': 'outlook-webapp-brute',
            'description': "Microsoft Outlook WebAPP Brute.",
            'aliases': ["outlook-webapp-brute", "outlook webapp brute"],
        },
        {
            'name': 'owabf',
            'description': "Outlook Web Access bruteforcer tool.",
            'aliases': ["owabf", "owabf"],
        },
        {
            'name': 'pack',
            'description': "Password Analysis and Cracking Kit",
            'aliases': ["pack", "pack"],
        },
        {
            'name': 'passe-partout',
            'description': "Tool to extract RSA and DSA private keys from any process linked with OpenSSL. The target memory is scanned to lookup specific OpenSSL patterns.",
            'aliases': ["passe-partout", "passe partout"],
        },
        {
            'name': 'passgan',
            'description': "A Deep Learning Approach for Password Guessing.",
            'aliases': ["passgan", "passgan"],
        },
        {
            'name': 'patator',
            'description': "A multi-purpose bruteforcer.",
            'aliases': ["patator", "patator bruteforce"],
        },
        {
            'name': 'pdgmail',
            'description': "A password dictionary attack tool that targets windows authentication via the SMB protocol.",
            'aliases': ["pdgmail", "pdgmail"],
        },
        {
            'name': 'pemcrack',
            'description': "Cracks SSL PEM files that hold encrypted private keys. Brute forces or dictionary cracks.",
            'aliases': ["pemcrack", "pemcrack"],
        },
        {
            'name': 'pemcracker',
            'description': "Tool to crack encrypted PEM files.",
            'aliases': ["pemcracker", "pemcracker"],
        },
        {
            'name': 'phoss',
            'description': "Sniffer designed to find HTTP, FTP, LDAP, Telnet, IMAP4, VNC and POP3 logins.",
            'aliases': ["phoss", "phoss"],
        },
        {
            'name': 'php-mt-seed',
            'description': "PHP mt_rand() seed cracker.",
            'aliases': ["php-mt-seed", "php mt seed"],
        },
        {
            'name': 'php-rfi-payload-decoder',
            'description': "Decode and analyze RFI payloads developed in PHP.",
            'aliases': ["php-rfi-payload-decoder", "php rfi payload decoder"],
        },
        {
            'name': 'phrasendrescher',
            'description': "A modular and multi processing pass phrase cracking tool.",
            'aliases': ["phrasendrescher", "phrasendrescher"],
        },
        {
            'name': 'pipal',
            'description': "A password analyser.",
            'aliases': ["pipal", "pipal"],
        },
        {
            'name': 'pipeline',
            'description': "Designed to aid in targeted brute force password cracking attacks.",
            'aliases': ["pipeline", "pipeline"],
        },
        {
            'name': 'pkcrack',
            'description': "A PkZip encryption cracker.",
            'aliases': ["pkcrack", "pkcrack"],
        },
        {
            'name': 'pwcrack',
            'description': "Password hash automatic cracking framework.",
            'aliases': ["pwcrack", "pwcrack"],
        },
        {
            'name': 'pybozocrack',
            'description': "A silly & effective MD5 cracker in Python.",
            'aliases': ["pybozocrack", "pybozocrack"],
        },
        {
            'name': 'pyrit',
            'description': "The famous WPA precomputed cracker.",
            'aliases': ["pyrit", "pyrit wpa"],
        },
        {
            'name': 'rainbowcrack',
            'description': "Password cracker based on the faster time-memory trade-off. With MySQL and Cisco PIX Algorithm patches.",
            'aliases': ["rainbowcrack", "rainbowcrack"],
        },
        {
            'name': 'rcracki-mt',
            'description': "A tool to perform rainbow table attacks on password hashes. It is intended for indexed/perfected rainbow tables, mainly generated by the distributed project www.freerainbowtables.com.",
            'aliases': ["rcracki-mt", "rcracki mt"],
        },
        {
            'name': 'rdesktop-brute',
            'description': "It connects to windows terminal servers - Bruteforce patch included.",
            'aliases': ["rdesktop-brute", "rdesktop brute"],
        },
        {
            'name': 'rdpassspray',
            'description': "Python3 tool to perform password spraying using RDP.",
            'aliases': ["rdpassspray", "rdpassspray"],
        },
        {
            'name': 'rfcrack',
            'description': "A Software Defined Radio Attack Tool.",
            'aliases': ["rfcrack", "rfcrack"],
        },
        {
            'name': 'ridenum',
            'description': "A null session RID cycle attack for brute forcing domain controllers.",
            'aliases': ["ridenum", "ridenum"],
        },
        {
            'name': 'rlogin-scanner',
            'description': "Multithreaded rlogin scanner. Tested on Linux, OpenBSD and Solaris.",
            'aliases': ["rlogin-scanner", "rlogin scanner"],
        },
        {
            'name': 'rootbrute',
            'description': "Local root account bruteforcer.",
            'aliases': ["rootbrute", "rootbrute"],
        },
        {
            'name': 'rpdscan',
            'description': "Remmina Password Decoder and scanner.",
            'aliases': ["rpdscan", "rpdscan"],
        },
        {
            'name': 'rsakeyfind',
            'description': "A tool to find RSA key in RAM.",
            'aliases': ["rsakeyfind", "rsakeyfind"],
        },
        {
            'name': 'samdump2',
            'description': "Dump password hashes from a Windows NT/2k/XP installation",
            'aliases': ["samdump2", "samdump2"],
        },
        {
            'name': 'samydeluxe',
            'description': "Automatic samdump creation script.",
            'aliases': ["samydeluxe", "samydeluxe"],
        },
        {
            'name': 'shreder',
            'description': "A powerful multi-threaded SSH protocol password bruteforce tool.",
            'aliases': ["shreder", "shreder"],
        },
        {
            'name': 'sidguesser',
            'description': "Guesses sids/instances against an Oracle database according to a predefined dictionary file.",
            'aliases': ["sidguesser", "sidguesser"],
        },
        {
            'name': 'sipcrack',
            'description': "A SIP protocol login cracker.",
            'aliases': ["sipcrack", "sip crack"],
        },
        {
            'name': 'skul',
            'description': "A PoC to bruteforce the Cryptsetup implementation of Linux Unified Key Setup (LUKS).",
            'aliases': ["skul", "skul"],
        },
        {
            'name': 'smbbf',
            'description': "SMB password bruteforcer.",
            'aliases': ["smbbf", "smbbf"],
        },
        {
            'name': 'snmp-brute',
            'description': "SNMP brute force, enumeration, CISCO config downloader and password cracking script.",
            'aliases': ["snmp-brute", "snmp brute"],
        },
        {
            'name': 'speedpwn',
            'description': "An active WPA/2 Bruteforcer, original created to prove weak standard key generation in different ISP labeled routers without a client is connected.",
            'aliases': ["speedpwn", "speedpwn"],
        },
        {
            'name': 'spray365',
            'description': "Makes spraying Microsoft accounts (Office 365 / Azure AD) easy through its customizable two-step password spraying approach.",
            'aliases': ["spray365", "spray365"],
        },
        {
            'name': 'spraycharles',
            'description': "Low and slow password spraying tool, designed to spray on an interval over a long period of time.",
            'aliases': ["spraycharles", "spraycharles"],
        },
        {
            'name': 'sqlpat',
            'description': "This tool should be used to audit the strength of Microsoft SQL Server passwords offline.",
            'aliases': ["sqlpat", "sqlpat"],
        },
        {
            'name': 'ssh-privkey-crack',
            'description': "A SSH private key cracker.",
            'aliases': ["ssh-privkey-crack", "ssh privkey crack"],
        },
        {
            'name': 'sshatter',
            'description': "Password bruteforcer for SSH.",
            'aliases': ["sshatter", "sshatter"],
        },
        {
            'name': 'sshprank',
            'description': "A fast SSH mass-scanner, login cracker, banner grabber and password auth checker tool using the python-masscan and shodan module.",
            'aliases': ["sshprank", "sshprank"],
        },
        {
            'name': 'sshscan',
            'description': "A horizontal SSH scanner that scans large swaths of IPv4 space for a single SSH user and pass.",
            'aliases': ["sshscan", "sshscan"],
        },
        {
            'name': 'sshtrix',
            'description': "A very fast multithreaded SSH login cracker.",
            'aliases': ["sshtrix", "sshtrix"],
        },
        {
            'name': 'sslnuke',
            'description': "Transparent proxy that decrypts SSL traffic and prints out IRC messages.",
            'aliases': ["sslnuke", "sslnuke"],
        },
        {
            'name': 'sucrack',
            'description': "A multi-threaded Linux/UNIX tool for brute-force cracking local user accounts via su.",
            'aliases': ["sucrack", "sucrack"],
        },
        {
            'name': 'talon',
            'description': "A password guessing tool that targets the Kerberos and LDAP services within the Windows Active Directory environment.",
            'aliases': ["talon", "talon"],
        },
        {
            'name': 'tftp-bruteforce',
            'description': "A fast TFTP filename bruteforcer written in perl.",
            'aliases': ["tftp-bruteforce", "tftp bruteforce"],
        },
        {
            'name': 'thc-keyfinder',
            'description': "Finds crypto keys, encrypted data and compressed data in files by analyzing the entropy of parts of the file.",
            'aliases': ["thc-keyfinder", "thc keyfinder"],
        },
        {
            'name': 'thc-pptp-bruter',
            'description': "A brute force program that works against pptp vpn endpoints (tcp port 1723).",
            'aliases': ["thc-pptp-bruter", "thc pptp bruter"],
        },
        {
            'name': 'thc-smartbrute',
            'description': "This tool finds undocumented and secret commands implemented in a smartcard.",
            'aliases': ["thc-smartbrute", "thc smartbrute"],
        },
        {
            'name': 'timeverter',
            'description': "Bruteforce time-based tokens and to convert several time domains.",
            'aliases': ["timeverter", "timeverter"],
        },
        {
            'name': 'trevorspray',
            'description': "A modular password sprayer with threading, clever proxying, loot modules, and more!",
            'aliases': ["trevorspray", "trevorspray"],
        },
        {
            'name': 'truecrack',
            'description': "Password cracking for truecrypt(c) volumes.",
            'aliases': ["truecrack", "truecrack"],
        },
        {
            'name': 'tweetshell',
            'description': "Multi-thread Twitter BruteForcer in Shell Script.",
            'aliases': ["tweetshell", "tweetshell"],
        },
        {
            'name': 'ufo-wardriving',
            'description': "Allows you to test the security of wireless networks by detecting their passwords based on the router model.",
            'aliases': ["ufo-wardriving", "ufo wardriving"],
        },
        {
            'name': 'vnc-bypauth',
            'description': "Multi-threaded bypass authentication scanner for VNC smaller than v4.1.1 servers.",
            'aliases': ["vnc-bypauth", "vnc bypauth"],
        },
        {
            'name': 'vncrack',
            'description': "What it looks like: crack VNC.",
            'aliases': ["vncrack", "vncrack"],
        },
        {
            'name': 'wmat',
            'description': "Automatic tool for testing webmail accounts.",
            'aliases': ["wmat", "wmat"],
        },
        {
            'name': 'wordbrutepress',
            'description': "Python script that performs brute forcing against WordPress installs using a wordlist.",
            'aliases': ["wordbrutepress", "wordbrutepress"],
        },
        {
            'name': 'wpbf',
            'description': "Multithreaded WordPress brute forcer.",
            'aliases': ["wpbf", "wpbf"],
        },
        {
            'name': 'wpbrute-rpc',
            'description': "Tool for amplified bruteforce attacks on wordpress based website via xmlrcp API.",
            'aliases': ["wpbrute-rpc", "wpbrute rpc"],
        },
        {
            'name': 'wyd',
            'description': "Gets keywords from personal files. IT security/forensic tool.",
            'aliases': ["wyd", "wyd"],
        },
        {
            'name': 'zulu',
            'description': "A light weight 802.11 wireless frame generation tool to enable fast and easy debugging and probing of 802.11 networks.",
            'aliases': ["zulu", "zulu"],
        },
    ],

    # Windows (158 tools)
    'blackarch-windows': [
        {
            'name': '3proxy-win32',
            'description': "Tiny free proxy server.",
            'aliases': ["3proxy-win32", "3proxy win32"],
        },
        {
            'name': 'adape-script',
            'description': "Active Directory Assessment and Privilege Escalation Script.",
            'aliases': ["adape-script", "adape script"],
        },
        {
            'name': 'adpeas',
            'description': "winPEAS, but for Active Directory.",
            'aliases': ["adpeas", "adpeas"],
        },
        {
            'name': 'agafi',
            'description': "A gadget finder and a ROP-Chainer tool for x86 platforms.",
            'aliases': ["agafi", "agafi"],
        },
        {
            'name': 'analyzepesig',
            'description': "Analyze digital signature of PE file.",
            'aliases': ["analyzepesig", "analyzepesig"],
        },
        {
            'name': 'antiransom',
            'description': "A tool capable of detect and stop attacks of Ransomware using honeypots.",
            'aliases': ["antiransom", "antiransom"],
        },
        {
            'name': 'atstaketools',
            'description': "This is an archive of various @Stake tools that help perform vulnerability scanning and analysis, information gathering, password auditing, and forensics.",
            'aliases': ["atstaketools", "atstaketools"],
        },
        {
            'name': 'backorifice',
            'description': "A remote administration system which allows a user to control a computer across a tcpip connection using a simple console or GUI application.",
            'aliases': ["backorifice", "backorifice"],
        },
        {
            'name': 'browselist',
            'description': "Retrieves the browse list ; the output list contains computer names, and the roles they play in the network.",
            'aliases': ["browselist", "browselist"],
        },
        {
            'name': 'brute12',
            'description': "A tool designed for auditing the cryptography container security in PKCS12 format.",
            'aliases': ["brute12", "brute12"],
        },
        {
            'name': 'brutus',
            'description': "One of the fastest, most flexible remote password crackers you can get your hands on.",
            'aliases': ["brutus", "brutus"],
        },
        {
            'name': 'cachedump',
            'description': "A tool that demonstrates how to recover cache entry information: username and hashed password (called MSCASH).",
            'aliases': ["cachedump", "cachedump"],
        },
        {
            'name': 'certi',
            'description': "Active Directory Certificate Services (ADCS) abuser. impacket copy of Certify.",
            'aliases': ["certi", "certi"],
        },
        {
            'name': 'certipy',
            'description': "Active Directory Certificate Services enumeration and abuse.",
            'aliases': ["certipy", "certipy ad"],
        },
        {
            'name': 'chrome-decode',
            'description': "Chrome web browser decoder tool that demonstrates recovering passwords.",
            'aliases': ["chrome-decode", "chrome decode"],
        },
        {
            'name': 'chromensics',
            'description': "A Google chrome forensics tool.",
            'aliases': ["chromensics", "chromensics"],
        },
        {
            'name': 'conpass',
            'description': "Password spraying in AD environment avoing account locking.",
            'aliases': ["conpass", "conpass"],
        },
        {
            'name': 'crackmapexec-pingcastle',
            'description': "NetExec & CrackMapExec module that execute PingCastle on a remote machine.",
            'aliases': ["crackmapexec-pingcastle", "crackmapexec pingcastle"],
        },
        {
            'name': 'dark-dork-searcher',
            'description': "Dark-Dork Searcher.",
            'aliases': ["dark-dork-searcher", "dark dork searcher"],
        },
        {
            'name': 'darkarmour',
            'description': "Store and execute an encrypted windows binary from inside memory, without a single bit touching disk.",
            'aliases': ["darkarmour", "darkarmour"],
        },
        {
            'name': 'de4dot',
            'description': ".NET deobfuscator and unpacker.",
            'aliases': ["de4dot", "de4dot"],
        },
        {
            'name': 'de4dotex',
            'description': ".NET deobfuscator and unpacker.",
            'aliases': ["de4dotex", "de4dotex"],
        },
        {
            'name': 'directorytraversalscan',
            'description': "Detect directory traversal vulnerabilities in HTTP servers and web applications.",
            'aliases': ["directorytraversalscan", "directorytraversalscan"],
        },
        {
            'name': 'dnspy',
            'description': ".NET debugger and assembly editor.",
            'aliases': ["dnspy", "dnspy"],
        },
        {
            'name': 'donpapi',
            'description': "Dumping revelant information on compromised targets without AV detection with DPAPI.",
            'aliases': ["donpapi", "don papi"],
        },
        {
            'name': 'dotpeek',
            'description': "Free .NET Decompiler and Assembly Browser.",
            'aliases': ["dotpeek", "dotpeek"],
        },
        {
            'name': 'dumpacl',
            'description': "Dumps NTs ACLs and audit settings.",
            'aliases': ["dumpacl", "dumpacl"],
        },
        {
            'name': 'dumpusers',
            'description': "Dumps account names and information even though RestrictAnonymous has been set to 1.",
            'aliases': ["dumpusers", "dumpusers"],
        },
        {
            'name': 'eraser',
            'description': "Windows tool which allows you to completely remove sensitive data from your hard drive by overwriting it several times with carefully selected patterns.",
            'aliases': ["eraser", "eraser"],
        },
        {
            'name': 'etherchange',
            'description': "Can change the Ethernet address of the network adapters in Windows.",
            'aliases': ["etherchange", "etherchange"],
        },
        {
            'name': 'etherflood',
            'description': "Floods a switched network with Ethernet frames with random hardware addresses.",
            'aliases': ["etherflood", "etherflood"],
        },
        {
            'name': 'evil-winrm-py',
            'description': "WinRM shell for Windows and Active Directory pentesting.",
            'aliases': ["evil-winrm-py", "evil winrm py"],
        },
        {
            'name': 'extractbitlockerkeys',
            'description': "Script to automatically extract the bitlocker recovery keys from a domain.",
            'aliases': ["extractbitlockerkeys", "extractbitlockerkeys"],
        },
        {
            'name': 'filefuzz',
            'description': "A binary file fuzzer for Windows with several options.",
            'aliases': ["filefuzz", "filefuzz"],
        },
        {
            'name': 'finduncommonshares',
            'description': "Python script allowing to quickly find uncommon shares in vast Windows Domains.",
            'aliases': ["finduncommonshares", "finduncommonshares"],
        },
        {
            'name': 'fport',
            'description': "Identify unknown open ports and their associated applications.",
            'aliases': ["fport", "fport"],
        },
        {
            'name': 'fred',
            'description': "Cross-platform M$ registry hive editor.",
            'aliases': ["fred", "fred"],
        },
        {
            'name': 'fuzztalk',
            'description': "An XML driven fuzz testing framework that emphasizes easy extensibility and reusability.",
            'aliases': ["fuzztalk", "fuzztalk"],
        },
        {
            'name': 'gene',
            'description': "Signature Engine for Windows Event Logs.",
            'aliases': ["gene", "gene"],
        },
        {
            'name': 'ghostpack',
            'description': "Compiled Binaries for Ghostpack (.NET v4.8.1).",
            'aliases': ["ghostpack", "ghostpack"],
        },
        {
            'name': 'gplist',
            'description': "Lists information about the applied Group Policies.",
            'aliases': ["gplist", "gplist"],
        },
        {
            'name': 'gpowned',
            'description': "GPOs manipulation tool.",
            'aliases': ["gpowned", "gpowned"],
        },
        {
            'name': 'grabitall',
            'description': "Performs traffic redirection by sending spoofed ARP replies.",
            'aliases': ["grabitall", "grabitall"],
        },
        {
            'name': 'gsd',
            'description': "Gives you the Discretionary Access Control List of any Windows NT service you specify as a command line option.",
            'aliases': ["gsd", "gsd"],
        },
        {
            'name': 'gtalk-decode',
            'description': "Google Talk decoder tool that demonstrates recovering passwords from accounts.",
            'aliases': ["gtalk-decode", "gtalk decode"],
        },
        {
            'name': 'handle',
            'description': "An small application designed to analyze your system searching for global objects related to running process and display information for every found object, like tokens, semaphores, ports, files,..",
            'aliases': ["handle", "handle"],
        },
        {
            'name': 'hekatomb',
            'description': "Extract and decrypt all credentials from all domain computers using DPAPI.",
            'aliases': ["hekatomb", "hekatomb"],
        },
        {
            'name': 'hexodus',
            'description': "Python framework project designed to enumerate and help in Active Directory attacks through Windows protocols like SMB, LDAP, WinRM and other.",
            'aliases': ["hexodus", "hexodus"],
        },
        {
            'name': 'hollows-hunter',
            'description': "Scans all running processes. Recognizes and dumps a variety of potentially malicious implants (replaced/injected PEs, shellcodes, hooks, in-memory patches).",
            'aliases': ["hollows-hunter", "hollows hunter"],
        },
        {
            'name': 'hookanalyser',
            'description': "A hook tool which can be potentially helpful in reversing applications and analyzing malware. It can hook to an API in a process and search for a pattern in memory or dump the buffer.",
            'aliases': ["hookanalyser", "hookanalyser"],
        },
        {
            'name': 'httpbog',
            'description': "A slow HTTP denial-of-service tool that works similarly to other attacks, but rather than leveraging request headers or POST data Bog consumes sockets by slowly reading responses.",
            'aliases': ["httpbog", "httpbog"],
        },
        {
            'name': 'httprecon',
            'description': "Tool for web server fingerprinting, also known as http fingerprinting.",
            'aliases': ["httprecon", "httprecon"],
        },
        {
            'name': 'httprint-win32',
            'description': "A web server fingerprinting tool (Windows binaries).",
            'aliases': ["httprint-win32", "httprint win32"],
        },
        {
            'name': 'hyperion-crypter',
            'description': "A runtime encrypter for 32-bit and 64-bit portable executables.",
            'aliases': ["hyperion-crypter", "hyperion crypter"],
        },
        {
            'name': 'ikeprobe',
            'description': "Determine vulnerabilities in the PSK implementation of the VPN server.",
            'aliases': ["ikeprobe", "ikeprobe"],
        },
        {
            'name': 'intercepter-ng',
            'description': "A next generation sniffer including a lot of features: capturing passwords/hashes, sniffing chat messages, performing man-in-the-middle attacks, etc.",
            'aliases': ["intercepter-ng", "intercepter ng"],
        },
        {
            'name': 'inzider',
            'description': "This is a tool that lists processes in your Windows system and the ports each one listen on.",
            'aliases': ["inzider", "inzider"],
        },
        {
            'name': 'juicy-potato',
            'description': "A sugared version of RottenPotatoNG, with a bit of juice.",
            'aliases': ["juicy-potato", "juicy potato"],
        },
        {
            'name': 'justdecompile',
            'description': "The decompilation engine of JustDecompile.",
            'aliases': ["justdecompile", "justdecompile"],
        },
        {
            'name': 'kekeo',
            'description': "A little toolbox to play with Microsoft Kerberos in C.",
            'aliases': ["kekeo", "kekeo tool"],
        },
        {
            'name': 'kerbcrack',
            'description': "Kerberos sniffer and cracker for Windows.",
            'aliases': ["kerbcrack", "kerbcrack"],
        },
        {
            'name': 'klogger',
            'description': "A keystroke logger for the NT-series of Windows.",
            'aliases': ["klogger", "klogger"],
        },
        {
            'name': 'ldapmonitor',
            'description': "Monitor creation, deletion and changes to LDAP objects live during your pentest or system administration!",
            'aliases': ["ldapmonitor", "ldapmonitor"],
        },
        {
            'name': 'lethalhta',
            'description': "Lateral Movement technique using DCOM and HTA.",
            'aliases': ["lethalhta", "lethalhta"],
        },
        {
            'name': 'lolbas',
            'description': "Living Off The Land Binaries And Scripts - (LOLBins and LOLScripts).",
            'aliases': ["lolbas", "lolbas"],
        },
        {
            'name': 'malwareanalyser',
            'description': "A freeware tool to perform static and dynamic analysis on malware.",
            'aliases': ["malwareanalyser", "malwareanalyser"],
        },
        {
            'name': 'mbenum',
            'description': "Queries the master browser for whatever information it has registered.",
            'aliases': ["mbenum", "mbenum"],
        },
        {
            'name': 'memimager',
            'description': "Performs a memory dump using NtSystemDebugControl.",
            'aliases': ["memimager", "memimager"],
        },
        {
            'name': 'mimikatz',
            'description': "A little tool to play with Windows security.",
            'aliases': ["mimikatz", "mimi katz"],
        },
        {
            'name': 'mingsweeper',
            'description': "A network reconnaissance tool designed to facilitate large address space,high speed node discovery and identification.",
            'aliases': ["mingsweeper", "mingsweeper"],
        },
        {
            'name': 'modifycerttemplate',
            'description': "Aid operators in modifying ADCS certificate templates so that a created vulnerable state can be leveraged for privilege escalation.",
            'aliases': ["modifycerttemplate", "modifycerttemplate"],
        },
        {
            'name': 'mrkaplan',
            'description': "Help red teamers to stay hidden by clearing evidence of execution.",
            'aliases': ["mrkaplan", "mrkaplan"],
        },
        {
            'name': 'mssqlrelay',
            'description': "Microsoft SQL Relay is an offensive tool for auditing and abusing Microsoft SQL (MSSQL) services.",
            'aliases': ["mssqlrelay", "mssqlrelay"],
        },
        {
            'name': 'msvpwn',
            'description': "Bypass Windows\' authentication via binary patching.",
            'aliases': ["msvpwn", "msvpwn"],
        },
        {
            'name': 'nbname',
            'description': "Decodes and displays all NetBIOS name packets it receives on UDP port 137 and more!",
            'aliases': ["nbname", "nbname"],
        },
        {
            'name': 'nbtenum',
            'description': "A utility for Windows that can be used to enumerate NetBIOS information from one host or a range of hosts.",
            'aliases': ["nbtenum", "nbtenum"],
        },
        {
            'name': 'netbus',
            'description': "NetBus remote administration tool",
            'aliases': ["netbus", "netbus"],
        },
        {
            'name': 'netexec-pingcastle',
            'description': "NetExec & CrackMapExec module that execute PingCastle on a remote machine.",
            'aliases': ["netexec-pingcastle", "netexec pingcastle"],
        },
        {
            'name': 'netripper',
            'description': "Smart traffic sniffing for penetration testers.",
            'aliases': ["netripper", "netripper"],
        },
        {
            'name': 'netstumbler',
            'description': "Well-known wireless AP scanner and sniffer.",
            'aliases': ["netstumbler", "netstumbler"],
        },
        {
            'name': 'nimrm',
            'description': "Native WinRM shell client with NTLM, Kerberos, file transfers, in-memory operations, and multi-session support.",
            'aliases': ["nimrm", "nimrm"],
        },
        {
            'name': 'nirsoft',
            'description': "Unique collection of small and useful freeware utilities.",
            'aliases': ["nirsoft", "nirsoft"],
        },
        {
            'name': 'nishang',
            'description': "Using PowerShell for Penetration Testing.",
            'aliases': ["nishang", "nishang"],
        },
        {
            'name': 'ntds-decode',
            'description': "This application dumps LM and NTLM hashes from active accounts stored in an Active Directory database.",
            'aliases': ["ntds-decode", "ntds decode"],
        },
        {
            'name': 'orakelcrackert',
            'description': "This tool can crack passwords which are encrypted using Oracle\'s latest SHA1 based password protection algorithm.",
            'aliases': ["orakelcrackert", "orakelcrackert"],
        },
        {
            'name': 'osslsigncode',
            'description': "A small tool that implements part of the functionality of the Microsoft tool signtool.exe.",
            'aliases': ["osslsigncode", "osslsigncode"],
        },
        {
            'name': 'pafish',
            'description': "A demonstration tool that employs several techniques to detect sandboxes and analysis environments in the same way as malware families do.",
            'aliases': ["pafish", "pafish"],
        },
        {
            'name': 'pe-bear',
            'description': "A freeware reversing tool for PE files.",
            'aliases': ["pe-bear", "pe bear"],
        },
        {
            'name': 'pe-sieve',
            'description': "Scans a given process. Recognizes and dumps a variety of potentially malicious implants (replaced/injected PEs, shellcodes, hooks, in-memory patches).",
            'aliases': ["pe-sieve", "pe sieve"],
        },
        {
            'name': 'periscope',
            'description': "A PE file inspection tool.",
            'aliases': ["periscope", "periscope"],
        },
        {
            'name': 'petools',
            'description': "Portable executable (PE) manipulation toolkit.",
            'aliases': ["petools", "petools"],
        },
        {
            'name': 'pextractor',
            'description': "A forensics tool that can extract all files from an executable file created by a joiner or similar.",
            'aliases': ["pextractor", "pextractor"],
        },
        {
            'name': 'php-vulnerability-hunter',
            'description': "An whitebox fuzz testing tool capable of detected several classes of vulnerabilities in PHP web applications.",
            'aliases': ["php-vulnerability-hunter", "php vulnerability hunter"],
        },
        {
            'name': 'pingcastle',
            'description': "Active Directory scanning tool.",
            'aliases': ["pingcastle", "pingcastle"],
        },
        {
            'name': 'pmap',
            'description': "Passively discover, scan, and fingerprint link-local peers by the background noise they generate (i.e. their broadcast and multicast traffic).",
            'aliases': ["pmap", "pmap"],
        },
        {
            'name': 'pmdump',
            'description': "A tool that lets you dump the memory contents of a process to a file without stopping the process.",
            'aliases': ["pmdump", "pmdump"],
        },
        {
            'name': 'powercloud',
            'description': "Deliver powershell payloads via DNS TXT via CloudFlare using PowerShell.",
            'aliases': ["powercloud", "powercloud"],
        },
        {
            'name': 'powerlessshell',
            'description': "Run PowerShell command without invoking powershell.exe.",
            'aliases': ["powerlessshell", "powerlessshell"],
        },
        {
            'name': 'powerops',
            'description': "PowerShell Runspace Portable Post Exploitation Tool aimed at making Penetration Testing with PowerShell \"easier\".",
            'aliases': ["powerops", "powerops"],
        },
        {
            'name': 'powershdll',
            'description': "Run PowerShell with rundll32. Bypass software restrictions.",
            'aliases': ["powershdll", "powershdll"],
        },
        {
            'name': 'ppee',
            'description': "A Professional PE file Explorer for reversers, malware researchers and those who want to statically inspect PE files in more details.",
            'aliases': ["ppee", "ppee"],
        },
        {
            'name': 'pre2k',
            'description': "Query for existence of pre-windows 2000 computer objects which can be leveraged to gain a foothold in a target domain.",
            'aliases': ["pre2k", "pre2k"],
        },
        {
            'name': 'promiscdetect',
            'description': "Checks if your network adapter(s) is running in promiscuous mode, which may be a sign that you have a sniffer running on your computer.",
            'aliases': ["promiscdetect", "promiscdetect"],
        },
        {
            'name': 'pstoreview',
            'description': "Lists the contents of the Protected Storage.",
            'aliases': ["pstoreview", "pstoreview"],
        },
        {
            'name': 'pwdump',
            'description': "Extracts the binary SAM and SYSTEM file from the filesystem and then the hashes.",
            'aliases': ["pwdump", "pwdump"],
        },
        {
            'name': 'pyadrecon',
            'description': "Gathers information about the Active Directory and generates a report which can provide a holistic picture of the current state of the target AD environment.",
            'aliases': ["pyadrecon", "pyadrecon"],
        },
        {
            'name': 'pygpoabuse',
            'description': "RCE via GPO scheduled tasks.",
            'aliases': ["pygpoabuse", "pygpoabuse"],
        },
        {
            'name': 'python2-minidump',
            'description': "Python library to parse and read Microsoft minidump file format.",
            'aliases': ["python2-minidump", "python2 minidump"],
        },
        {
            'name': 'python2-minikerberos',
            'description': "Kerberos manipulation library in pure Python.",
            'aliases': ["python2-minikerberos", "python2 minikerberos"],
        },
        {
            'name': 'radiography',
            'description': "A forensic tool which grabs as much information as possible from a Windows system.",
            'aliases': ["radiography", "radiography"],
        },
        {
            'name': 'rasenum',
            'description': "A small program which lists the information for all of the entries in any phonebook file (.pbk).",
            'aliases': ["rasenum", "rasenum"],
        },
        {
            'name': 'regreport',
            'description': "Windows registry forensic analysis tool.",
            'aliases': ["regreport", "regreport"],
        },
        {
            'name': 'regview',
            'description': "Open raw Windows NT 5 Registry files (Windows 2000 or higher).",
            'aliases': ["regview", "regview"],
        },
        {
            'name': 'resourcehacker',
            'description': "Resource compiler and decompiler for Windows® applications.",
            'aliases': ["resourcehacker", "resourcehacker"],
        },
        {
            'name': 'roadlib',
            'description': "Azure AD and O365 exploration framework.",
            'aliases': ["roadlib", "roadlib"],
        },
        {
            'name': 'roadoidc',
            'description': "Azure AD and O365 exploration framework.",
            'aliases': ["roadoidc", "roadoidc"],
        },
        {
            'name': 'roadrecon',
            'description': "Azure AD and O365 exploration framework.",
            'aliases': ["roadrecon", "roadrecon"],
        },
        {
            'name': 'roadtx',
            'description': "Azure AD and O365 exploration framework.",
            'aliases': ["roadtx", "roadtx"],
        },
        {
            'name': 'rpak',
            'description': "A collection of tools that can be useful for doing attacks on routing protocols.",
            'aliases': ["rpak", "rpak"],
        },
        {
            'name': 'rpcsniffer',
            'description': "Sniffs WINDOWS RPC messages in a given RPC server process.",
            'aliases': ["rpcsniffer", "rpcsniffer"],
        },
        {
            'name': 'rpctools',
            'description': "Contains three separate tools for obtaining information from a system that is running RPC services",
            'aliases': ["rpctools", "rpctools"],
        },
        {
            'name': 'sccmhunter',
            'description': "Identifying, profiling, and attacking SCCM related assets in an Active Directory domain.",
            'aliases': ["sccmhunter", "sccmhunter"],
        },
        {
            'name': 'setowner',
            'description': "Allows you to set file ownership to any account, as long as you have the \"Restore files and directories\" user right.",
            'aliases': ["setowner", "setowner"],
        },
        {
            'name': 'shad0w',
            'description': "A modular C2 framework designed to successfully operate on mature environments.",
            'aliases': ["shad0w", "shad0w"],
        },
        {
            'name': 'shed',
            'description': ".NET runtime inspector.",
            'aliases': ["shed", "shed"],
        },
        {
            'name': 'sigspotter',
            'description': "A tool that search in your HD to find which publishers has been signed binaries in your PC.",
            'aliases': ["sigspotter", "sigspotter"],
        },
        {
            'name': 'sipscan',
            'description': "A sip scanner.",
            'aliases': ["sipscan", "sipscan"],
        },
        {
            'name': 'skype-dump',
            'description': "This is a tool that demonstrates dumping MD5 password hashes from the configuration file in Skype.",
            'aliases': ["skype-dump", "skype dump"],
        },
        {
            'name': 'smbrelay',
            'description': "SMB / HTTP to SMB replay attack toolkit.",
            'aliases': ["smbrelay", "smbrelay"],
        },
        {
            'name': 'snitch',
            'description': "Turn back the asterisks in password fields to plaintext passwords.",
            'aliases': ["snitch", "snitch"],
        },
        {
            'name': 'snowman',
            'description': "A native code to C/C++ decompiler, see the examples of generated code.",
            'aliases': ["snowman", "snowman"],
        },
        {
            'name': 'snscan',
            'description': "A Windows based SNMP detection utility that can quickly and accurately identify SNMP enabled devices on a network.",
            'aliases': ["snscan", "snscan"],
        },
        {
            'name': 'spade',
            'description': "A general-purpose Internet utility package, with some extra features to help in tracing the source of spam and other forms of Internet harassment.",
            'aliases': ["spade", "spade"],
        },
        {
            'name': 'sqldict',
            'description': "A dictionary attack tool for SQL Server.",
            'aliases': ["sqldict", "sqldict"],
        },
        {
            'name': 'sqlping',
            'description': "SQL Server scanning tool that also checks for weak passwords using wordlists.",
            'aliases': ["sqlping", "sqlping"],
        },
        {
            'name': 'sqlpowerinjector',
            'description': "Application created in .Net 1.1 that helps the penetration tester to find and exploit SQL injections on a web page.",
            'aliases': ["sqlpowerinjector", "sqlpowerinjector"],
        },
        {
            'name': 'streamfinder',
            'description': "Searches for Alternate Data Streams (ADS).",
            'aliases': ["streamfinder", "streamfinder"],
        },
        {
            'name': 'sub7',
            'description': "A remote administration tool. No further comments ;-)",
            'aliases': ["sub7", "sub7"],
        },
        {
            'name': 'superscan',
            'description': "Powerful TCP port scanner, pinger, resolver.",
            'aliases': ["superscan", "superscan"],
        },
        {
            'name': 'sysinternals-suite',
            'description': "Sysinternals tools suite.",
            'aliases': ["sysinternals-suite", "sysinternals suite"],
        },
        {
            'name': 'targetedkerberoast',
            'description': "Kerberoast with ACL abuse capabilities.",
            'aliases': ["targetedkerberoast", "targetedkerberoast"],
        },
        {
            'name': 'uacme',
            'description': "Defeating Windows User Account Control.",
            'aliases': ["uacme", "uacme"],
        },
        {
            'name': 'unsecure',
            'description': "Bruteforces network login masks.",
            'aliases': ["unsecure", "unsecure"],
        },
        {
            'name': 'upnp-pentest-toolkit',
            'description': "UPnP Pentest Toolkit for Windows.",
            'aliases': ["upnp-pentest-toolkit", "upnp pentest toolkit"],
        },
        {
            'name': 'wce',
            'description': "A security tool to list logon sessions and add, change, list and delete associated credentials (ex.: LM/NT hashes, plaintext passwords and Kerberos tickets).",
            'aliases': ["wce", "wce"],
        },
        {
            'name': 'wifichannelmonitor',
            'description': "A utility for Windows that captures wifi traffic on the channel you choose, using Microsoft Network Monitor capture driver.",
            'aliases': ["wifichannelmonitor", "wifichannelmonitor"],
        },
        {
            'name': 'windivert',
            'description': "A user-mode packet capture-and-divert package for Windows.",
            'aliases': ["windivert", "windivert"],
        },
        {
            'name': 'windows-binaries',
            'description': "A colleciton of pentesting Windows binaries.",
            'aliases': ["windows-binaries", "windows binaries"],
        },
        {
            'name': 'windows-privesc-check',
            'description': "Standalone Executable to Check for Simple Privilege Escalation Vectors on Windows Systems.",
            'aliases': ["windows-privesc-check", "windows privesc check"],
        },
        {
            'name': 'windowsspyblocker',
            'description': "Block spying and tracking on Windows.",
            'aliases': ["windowsspyblocker", "windowsspyblocker"],
        },
        {
            'name': 'winfo',
            'description': "Uses null sessions to remotely try to retrieve lists of and information about user accounts, workstation/interdomain/server trust accounts, shares (also hidden), sessions, logged in users, and password/lockout policy, from Windows NT/2000/XP.",
            'aliases': ["winfo", "winfo"],
        },
        {
            'name': 'winhex',
            'description': "Hex Editor and Disk Editor.",
            'aliases': ["winhex", "winhex"],
        },
        {
            'name': 'winpwn',
            'description': "Automation for internal Windows Penetrationtest / AD-Security.",
            'aliases': ["winpwn", "winpwn"],
        },
        {
            'name': 'winrelay',
            'description': "A TCP/UDP forwarder/redirector that works with both IPv4 and IPv6.",
            'aliases': ["winrelay", "winrelay"],
        },
        {
            'name': 'wpsweep',
            'description': "A simple ping sweeper, that is, it pings a range of IP addresses and lists the ones that reply.",
            'aliases': ["wpsweep", "wpsweep"],
        },
        {
            'name': 'wups',
            'description': "An UDP port scanner for Windows.",
            'aliases': ["wups", "wups"],
        },
        {
            'name': 'x-scan',
            'description': "A general network vulnerabilities scanner for scanning network vulnerabilities for specific IP address scope or stand-alone computer by multi-threading method, plug-ins are supportable.",
            'aliases': ["x-scan", "x scan"],
        },
        {
            'name': 'x64dbg',
            'description': "An open-source x64/x32 debugger for windows.",
            'aliases': ["x64dbg", "x64 debugger", "x32dbg"],
        },
    ],

    # Networking (146 tools)
    'blackarch-networking': [
        {
            'name': 'adassault',
            'description': "An Active Directory environments pentest tool complementary to existing ones like NetExec.",
            'aliases': ["adassault", "adassault"],
        },
        {
            'name': 'aiengine',
            'description': "A packet inspection engine with capabilities of learning without any human intervention.",
            'aliases': ["aiengine", "aiengine"],
        },
        {
            'name': 'apacket',
            'description': "Sniffer syn and backscatter packets.",
            'aliases': ["apacket", "apacket"],
        },
        {
            'name': 'argus',
            'description': "Network monitoring tool with flow control.",
            'aliases': ["argus", "argus"],
        },
        {
            'name': 'argus-clients',
            'description': "Network monitoring client for Argus.",
            'aliases': ["argus-clients", "argus clients"],
        },
        {
            'name': 'arpalert',
            'description': "Monitor ARP changes in ethernet networks.",
            'aliases': ["arpalert", "arpalert"],
        },
        {
            'name': 'arping-th',
            'description': "ARP Ping from Thomas Habets (aka Debian arping).",
            'aliases': ["arping-th", "arping th"],
        },
        {
            'name': 'arptools',
            'description': "A simple tool about ARP broadcast, ARP attack, and data transmission.",
            'aliases': ["arptools", "arptools"],
        },
        {
            'name': 'arpwner',
            'description': "GUI-based python tool for arp poisoning and dns poisoning attacks.",
            'aliases': ["arpwner", "arpwner"],
        },
        {
            'name': 'asnmap',
            'description': "Map organization network ranges using ASN information.",
            'aliases': ["asnmap", "asnmap"],
        },
        {
            'name': 'autovpn',
            'description': "Easily connect to a VPN in a country of your choice.",
            'aliases': ["autovpn", "autovpn"],
        },
        {
            'name': 'buttinsky',
            'description': "Provide an open source framework for automated botnet monitoring.",
            'aliases': ["buttinsky", "buttinsky"],
        },
        {
            'name': 'bypass-firewall-dns-history',
            'description': "Firewall bypass script based on DNS history records.",
            'aliases': ["bypass-firewall-dns-history", "bypass firewall dns history"],
        },
        {
            'name': 'chameleon',
            'description': "A tool for evading Proxy categorisation.",
            'aliases': ["chameleon", "chameleon"],
        },
        {
            'name': 'chaosreader',
            'description': "A freeware tool to trace tcp, udp etc. sessions and fetch application data from snoop or tcpdump logs.",
            'aliases': ["chaosreader", "chaos reader"],
        },
        {
            'name': 'chopshop',
            'description': "Protocol Analysis/Decoder Framework.",
            'aliases': ["chopshop", "chopshop"],
        },
        {
            'name': 'cidr2range',
            'description': "Script for listing the IP addresses contained in a CIDR netblock.",
            'aliases': ["cidr2range", "cidr2range"],
        },
        {
            'name': 'creak',
            'description': "Poison, reset, spoof, redirect MITM script.",
            'aliases': ["creak", "creak"],
        },
        {
            'name': 'cyberscan',
            'description': "A Network Pentesting Tool.",
            'aliases': ["cyberscan", "cyberscan"],
        },
        {
            'name': 'dcdetector',
            'description': "Spot all domain controllers in a Microsoft Active Directory environment. Find computer name, FQDN, and IP address(es) of all DCs.",
            'aliases': ["dcdetector", "dcdetector"],
        },
        {
            'name': 'depdep',
            'description': "A merciless sentinel which will seek sensitive files containing critical info leaking through your network.",
            'aliases': ["depdep", "depdep"],
        },
        {
            'name': 'det',
            'description': "(extensible) Data Exfiltration Toolkit.",
            'aliases': ["det", "det"],
        },
        {
            'name': 'dhcpoptinj',
            'description': "DHCP option injector.",
            'aliases': ["dhcpoptinj", "dhcpoptinj"],
        },
        {
            'name': 'dinouml',
            'description': "A network simulation tool, based on UML (User Mode Linux) that can simulate big Linux networks on a single PC",
            'aliases': ["dinouml", "dinouml"],
        },
        {
            'name': 'dnsdiag',
            'description': "DNS Diagnostics and Performance Measurement Tools.",
            'aliases': ["dnsdiag", "dnsdiag"],
        },
        {
            'name': 'dnsfilexfer',
            'description': "File transfer via DNS.",
            'aliases': ["dnsfilexfer", "dnsfilexfer"],
        },
        {
            'name': 'dnsobserver',
            'description': "A handy DNS service written in Go to aid in the detection of several types of blind vulnerabilities.",
            'aliases': ["dnsobserver", "dnsobserver"],
        },
        {
            'name': 'dnsteal',
            'description': "DNS Exfiltration tool for stealthily sending files over DNS requests..",
            'aliases': ["dnsteal", "dnsteal"],
        },
        {
            'name': 'dnsvalidator',
            'description': "Maintains a list of IPv4 DNS servers by verifying them against baseline servers, and ensuring accurate responses.",
            'aliases': ["dnsvalidator", "dnsvalidator"],
        },
        {
            'name': 'dripcap',
            'description': "Caffeinated Packet Analyzer.",
            'aliases': ["dripcap", "dripcap"],
        },
        {
            'name': 'dtp-spoof',
            'description': "Python script/security tool to test Dynamic Trunking Protocol configuration on a switch.",
            'aliases': ["dtp-spoof", "dtp spoof"],
        },
        {
            'name': 'dublin-traceroute',
            'description': "NAT-aware multipath tracerouting tool.",
            'aliases': ["dublin-traceroute", "dublin traceroute"],
        },
        {
            'name': 'dump1090',
            'description': "A simple Mode S decoder for RTLSDR devices.",
            'aliases': ["dump1090", "dump1090"],
        },
        {
            'name': 'evillimiter',
            'description': "Tool that limits bandwidth of devices on the same network without access.",
            'aliases': ["evillimiter", "evillimiter"],
        },
        {
            'name': 'exabgp',
            'description': "The BGP swiss army knife of networking.",
            'aliases': ["exabgp", "exabgp"],
        },
        {
            'name': 'filibuster',
            'description': "A Egress filter mapping application with additional functionality.",
            'aliases': ["filibuster", "filibuster"],
        },
        {
            'name': 'firecat',
            'description': "A penetration testing tool that allows you to punch reverse TCP tunnels out of a compromised network.",
            'aliases': ["firecat", "firecat"],
        },
        {
            'name': 'flowinspect',
            'description': "A network traffic inspection tool.",
            'aliases': ["flowinspect", "flowinspect"],
        },
        {
            'name': 'girsh',
            'description': "Automatically spawn a reverse shell fully interactive for Linux or Windows victim.",
            'aliases': ["girsh", "girsh"],
        },
        {
            'name': 'gspoof',
            'description': "A simple GTK/command line TCP/IP packet generator.",
            'aliases': ["gspoof", "gspoof"],
        },
        {
            'name': 'gwcheck',
            'description': "A simple program that checks if a host in an ethernet network is a gateway to Internet.",
            'aliases': ["gwcheck", "gwcheck"],
        },
        {
            'name': 'haka',
            'description': "A collection of tool that allows capturing TCP/IP packets and filtering them based on Lua policy files.",
            'aliases': ["haka", "haka"],
        },
        {
            'name': 'hharp',
            'description': "This tool can perform man-in-the-middle and switch flooding attacks. It has 4 major functions, 3 of which attempt to man-in-the-middle one or more computers on a network with a passive method or flood type method.",
            'aliases': ["hharp", "hharp"],
        },
        {
            'name': 'http-traceroute',
            'description': "This is a python script that uses the Max-Forwards header in HTTP and SIP to perform a traceroute-like scanning functionality.",
            'aliases': ["http-traceroute", "http traceroute"],
        },
        {
            'name': 'hyde',
            'description': "Just another tool in C to do DDoS (with spoofing).",
            'aliases': ["hyde", "hyde"],
        },
        {
            'name': 'hyenae',
            'description': "Flexible platform independent packet generator.",
            'aliases': ["hyenae", "hyenae"],
        },
        {
            'name': 'hyperfox',
            'description': "A security tool for proxying and recording HTTP and HTTPs traffic.",
            'aliases': ["hyperfox", "hyperfox"],
        },
        {
            'name': 'infection-monkey',
            'description': "Automated security testing tool for networks.",
            'aliases': ["infection-monkey", "infection monkey"],
        },
        {
            'name': 'interlace',
            'description': "Easily turn single threaded command line applications into a fast, multi-threaded application with CIDR and glob support.",
            'aliases': ["interlace", "interlace"],
        },
        {
            'name': 'ipaudit',
            'description': "Monitors network activity on a network.",
            'aliases': ["ipaudit", "ipaudit"],
        },
        {
            'name': 'ipdecap',
            'description': "Can decapsulate traffic encapsulated within GRE, IPIP, 6in4, ESP (ipsec) protocols, and can also remove IEEE 802.1Q (virtual lan) header.",
            'aliases': ["ipdecap", "ipdecap"],
        },
        {
            'name': 'ipv4bypass',
            'description': "Using IPv6 to Bypass Security.",
            'aliases': ["ipv4bypass", "ipv4bypass"],
        },
        {
            'name': 'jnetmap',
            'description': "A network monitor of sorts.",
            'aliases': ["jnetmap", "jnetmap"],
        },
        {
            'name': 'kickthemout',
            'description': "Kick devices off your network by performing an ARP Spoof attack.",
            'aliases': ["kickthemout", "kickthemout"],
        },
        {
            'name': 'krbjack',
            'description': "DNS dynamic update abuse in ADIDNS and MitM attack using Kerberos AP-REQ hijacking.",
            'aliases': ["krbjack", "krbjack"],
        },
        {
            'name': 'latd',
            'description': "A LAT terminal daemon for Linux and BSD.",
            'aliases': ["latd", "latd"],
        },
        {
            'name': 'ldapconsole',
            'description': "Script allows you to perform custom LDAP requests to a Windows domain.",
            'aliases': ["ldapconsole", "ldapconsole"],
        },
        {
            'name': 'libparistraceroute',
            'description': "A library written in C dedicated to active network measurements with examples, such as paris-ping and paris-traceroute.",
            'aliases': ["libparistraceroute", "libparistraceroute"],
        },
        {
            'name': 'libtins',
            'description': "High-level, multiplatform C++ network packet sniffing and crafting library.",
            'aliases': ["libtins", "libtins"],
        },
        {
            'name': 'ligolo-mp',
            'description': "Multiplayer pivoting solution.",
            'aliases': ["ligolo-mp", "ligolo mp"],
        },
        {
            'name': 'loic',
            'description': "An open source network stress tool for Windows.",
            'aliases': ["loic", "loic"],
        },
        {
            'name': 'maclookup',
            'description': "Lookup MAC addresses in the IEEE MA-L/OUI public listing.",
            'aliases': ["maclookup", "maclookup"],
        },
        {
            'name': 'maketh',
            'description': "A packet generator that supports forging ARP, IP, TCP, UDP, ICMP and the ethernet header as well.",
            'aliases': ["maketh", "maketh"],
        },
        {
            'name': 'malcom',
            'description': "Analyze a system\'s network communication using graphical representations of network traffic.",
            'aliases': ["malcom", "malcom"],
        },
        {
            'name': 'massdns',
            'description': "A high-performance DNS stub resolver in C.",
            'aliases': ["massdns", "massdns"],
        },
        {
            'name': 'middler',
            'description': "A Man in the Middle tool to demonstrate protocol middling attacks.",
            'aliases': ["middler", "middler"],
        },
        {
            'name': 'mitm',
            'description': "A simple yet effective python3 script to perform DNS spoofing via ARP poisoning.",
            'aliases': ["mitm", "mitm"],
        },
        {
            'name': 'moloch',
            'description': "An open source large scale IPv4 full PCAP capturing, indexing and database system.",
            'aliases': ["moloch", "moloch"],
        },
        {
            'name': 'mptcp',
            'description': "A tool for manipulation of raw packets that allows a large number of options.",
            'aliases': ["mptcp", "mptcp"],
        },
        {
            'name': 'mptcp-abuse',
            'description': "A collection of tools and resources to explore MPTCP on your network. Initially released at Black Hat USA 2014.",
            'aliases': ["mptcp-abuse", "mptcp abuse"],
        },
        {
            'name': 'mylg',
            'description': "Network Diagnostic Tool.",
            'aliases': ["mylg", "mylg"],
        },
        {
            'name': 'nacker',
            'description': "A tool to circumvent 802.1x Network Access Control on a wired LAN.",
            'aliases': ["nacker", "nacker"],
        },
        {
            'name': 'nbtool',
            'description': "Some tools for NetBIOS and DNS investigation, attacks, and communication.",
            'aliases': ["nbtool", "nbtool"],
        },
        {
            'name': 'ncpfs',
            'description': "Allows you to mount volumes of NetWare servers under Linux.",
            'aliases': ["ncpfs", "ncpfs"],
        },
        {
            'name': 'nemesis',
            'description': "A command-line network packet crafting and injection utility.",
            'aliases': ["nemesis", "nemesis"],
        },
        {
            'name': 'netactview',
            'description': "A graphical network connections viewer similar in functionality to netstat.",
            'aliases': ["netactview", "netactview"],
        },
        {
            'name': 'netcon',
            'description': "A network connection establishment and management script.",
            'aliases': ["netcon", "netcon"],
        },
        {
            'name': 'netmap',
            'description': "Can be used to make a graphical representation of the surrounding network.",
            'aliases': ["netmap", "netmap"],
        },
        {
            'name': 'netreconn',
            'description': "A collection of network scan/recon tools that are relatively small compared to their larger cousins.",
            'aliases': ["netreconn", "netreconn"],
        },
        {
            'name': 'netsed',
            'description': "Small and handful utility design to alter the contents of packets forwarded thru network in real time.",
            'aliases': ["netsed", "netsed"],
        },
        {
            'name': 'networkmap',
            'description': "Post-exploitation network mapper.",
            'aliases': ["networkmap", "networkmap"],
        },
        {
            'name': 'nextnet',
            'description': "Pivot point discovery tool.",
            'aliases': ["nextnet", "nextnet"],
        },
        {
            'name': 'nfdump',
            'description': "A set of tools to collect and process netflow data.",
            'aliases': ["nfdump", "nfdump"],
        },
        {
            'name': 'nield',
            'description': "A tool to receive notifications from kernel through netlink socket, and generate logs related to interfaces, neighbor cache(ARP,NDP), IP address(IPv4,IPv6), routing, FIB rules, traffic control.",
            'aliases': ["nield", "nield"],
        },
        {
            'name': 'nipper',
            'description': "Network Infrastructure Parser",
            'aliases': ["nipper", "nipper"],
        },
        {
            'name': 'nsdtool',
            'description': "A netgear switch discovery tool. It contains some extra features like bruteoforce and setting a new password.",
            'aliases': ["nsdtool", "nsdtool"],
        },
        {
            'name': 'nsoq',
            'description': "A Network Security Tool for packet manipulation that allows a large number of options.",
            'aliases': ["nsoq", "nsoq"],
        },
        {
            'name': 'packet-o-matic',
            'description': "A real time packet processor. Reads the packet from an input module, match the packet using rules and connection tracking information and then send it to a target module.",
            'aliases': ["packet-o-matic", "packet o matic"],
        },
        {
            'name': 'packetq',
            'description': "A tool that provides a basic SQL-frontend to PCAP-files.",
            'aliases': ["packetq", "packetq"],
        },
        {
            'name': 'packetsender',
            'description': "An open source utility to allow sending and receiving TCP and UDP packets.",
            'aliases': ["packetsender", "packetsender"],
        },
        {
            'name': 'packit',
            'description': "A network auditing tool with the ability to customize, inject, monitor, and manipulate IP traffic.",
            'aliases': ["packit", "packit"],
        },
        {
            'name': 'pcapfex',
            'description': "Packet CAPture Forensic Evidence eXtractor.",
            'aliases': ["pcapfex", "pcapfex"],
        },
        {
            'name': 'pcapfix',
            'description': "Tries to repair your broken pcap and pcapng files.",
            'aliases': ["pcapfix", "pcapfix"],
        },
        {
            'name': 'phantap',
            'description': "An \'invisible\' network tap aimed at red teams.",
            'aliases': ["phantap", "phantap"],
        },
        {
            'name': 'pivotsuite',
            'description': "A portable, platform independent and powerful network pivoting toolkit.",
            'aliases': ["pivotsuite", "pivotsuite"],
        },
        {
            'name': 'pkt2flow',
            'description': "A simple utility to classify packets into flows.",
            'aliases': ["pkt2flow", "pkt2flow"],
        },
        {
            'name': 'pmacct',
            'description': "Small set of multi-purpose passive network monitoring tools [NetFlow IPFIX sFlow libpcap BGP BMP IGP Streaming Telemetry].",
            'aliases': ["pmacct", "pmacct"],
        },
        {
            'name': 'prometheus-firewall',
            'description': "A Firewall analyzer written in ruby",
            'aliases': ["prometheus-firewall", "prometheus firewall"],
        },
        {
            'name': 'pwnat',
            'description': "A tool that allows any number of clients behind NATs to communicate with a server behind a separate NAT with *no* port forwarding and *no* DMZ setup on any routers in order to directly communicate with each other.",
            'aliases': ["pwnat", "pwnat"],
        },
        {
            'name': 'pyersinia',
            'description': "Network attack tool like yersinia but written in Python.",
            'aliases': ["pyersinia", "pyersinia"],
        },
        {
            'name': 'pyexfil',
            'description': "A couple of beta stage tools for data exfiltration.",
            'aliases': ["pyexfil", "pyexfil"],
        },
        {
            'name': 'pyminifakedns',
            'description': "Minimal DNS server written in Python; it always replies with a 127.0.0.1 A-record.",
            'aliases': ["pyminifakedns", "pyminifakedns"],
        },
        {
            'name': 'python-cymruwhois',
            'description': "Python client for the whois.cymru.com service",
            'aliases': ["python-cymruwhois", "python cymruwhois"],
        },
        {
            'name': 'python2-cymruwhois',
            'description': "Python client for the whois.cymru.com service",
            'aliases': ["python2-cymruwhois", "python2 cymruwhois"],
        },
        {
            'name': 'rinetd',
            'description': "Internet redirection server.",
            'aliases': ["rinetd", "rinetd"],
        },
        {
            'name': 'rtpbreak',
            'description': "Detects, reconstructs and analyzes any RTP session.",
            'aliases': ["rtpbreak", "rtpbreak"],
        },
        {
            'name': 'rustcat',
            'description': "A modern port listener and reverse shell.",
            'aliases': ["rustcat", "rustcat"],
        },
        {
            'name': 'samplicator',
            'description': "Send copies of (UDP) datagrams to multiple receivers, with optional sampling and spoofing.",
            'aliases': ["samplicator", "samplicator"],
        },
        {
            'name': 'sdn-toolkit',
            'description': "Discover, Identify, and Manipulate SDN-Based Networks",
            'aliases': ["sdn-toolkit", "sdn toolkit"],
        },
        {
            'name': 'sessionlist',
            'description': "Sniffer that intents to sniff HTTP packets and attempts to reconstruct interesting authentication data from websites that do not employ proper secure cookie auth.",
            'aliases': ["sessionlist", "sessionlist"],
        },
        {
            'name': 'seth',
            'description': "Perform a MitM attack and extract clear text credentials from RDP connections.",
            'aliases': ["seth", "seth"],
        },
        {
            'name': 'silk',
            'description': "A collection of traffic analysis tools developed by the CERT NetSA to facilitate security analysis of large networks.",
            'aliases': ["silk", "silk"],
        },
        {
            'name': 'skydive',
            'description': "An open source real-time network topology and protocols analyzer.",
            'aliases': ["skydive", "skydive"],
        },
        {
            'name': 'smbclient-ng',
            'description': "Interact with SMB shares.",
            'aliases': ["smbclient-ng", "smbclient ng"],
        },
        {
            'name': 'sniffer',
            'description': "Packet Trace Parser for TCP, SMTP Emails, and HTTP Cookies.",
            'aliases': ["sniffer", "sniffer"],
        },
        {
            'name': 'sniffles',
            'description': "A Packet Capture Generator for IDS and Regular Expression Evaluation.",
            'aliases': ["sniffles", "sniffles"],
        },
        {
            'name': 'snmpattack',
            'description': "SNMP scanner and attacking tool.",
            'aliases': ["snmpattack", "snmpattack"],
        },
        {
            'name': 'snmpcheck',
            'description': "A free open source utility to get information via SNMP protocols.",
            'aliases': ["snmpcheck", "snmpcheck"],
        },
        {
            'name': 'sockstat',
            'description': "A tool to let you view information about open connections. It is similar to the tool of the same name that is included in FreeBSD, trying to faithfully reproduce as much functionality as is possible.",
            'aliases': ["sockstat", "sockstat"],
        },
        {
            'name': 'sprayhound',
            'description': "Password spraying tool and Bloodhound integration.",
            'aliases': ["sprayhound", "sprayhound"],
        },
        {
            'name': 'sps',
            'description': "A Linux packet crafting tool. Supports IPv4, IPv6 including extension headers, and tunneling IPv6 over IPv4.",
            'aliases': ["sps", "sps"],
        },
        {
            'name': 'stunner',
            'description': "Test and exploit STUN, TURN and TURN over TCP servers.",
            'aliases': ["stunner", "stunner"],
        },
        {
            'name': 'tcpcopy',
            'description': "A TCP stream replay tool to support real testing of Internet server applications.",
            'aliases': ["tcpcopy", "tcpcopy"],
        },
        {
            'name': 'tcpdstat',
            'description': "Get protocol statistics from tcpdump pcap files.",
            'aliases': ["tcpdstat", "tcpdstat"],
        },
        {
            'name': 'tcpextract',
            'description': "Extracts files from captured TCP sessions. Support live streams and pcap files.",
            'aliases': ["tcpextract", "tcpextract"],
        },
        {
            'name': 'tcptrace',
            'description': "A TCP dump file analysis tool.",
            'aliases': ["tcptrace", "tcptrace"],
        },
        {
            'name': 'tcptraceroute',
            'description': "A traceroute implementation using TCP packets.",
            'aliases': ["tcptraceroute", "tcptraceroute"],
        },
        {
            'name': 'tcpwatch',
            'description': "A utility written in Python that lets you monitor forwarded TCP connections or HTTP proxy connections.",
            'aliases': ["tcpwatch", "tcpwatch"],
        },
        {
            'name': 'tgcd',
            'description': "TCP/IP Gender Changer Daemon utility.",
            'aliases': ["tgcd", "tgcd"],
        },
        {
            'name': 'torpy',
            'description': "Pure python Tor client implementation.",
            'aliases': ["torpy", "torpy"],
        },
        {
            'name': 'tunna',
            'description': "a set of tools which will wrap and tunnel any TCP communication over HTTP. It can be used to bypass network restrictions in fully firewalled environments.",
            'aliases': ["tunna", "tunna"],
        },
        {
            'name': 'turner',
            'description': "Tunnels HTTP over a permissive/open TURN server; supports HTTP and SOCKS5 proxy.",
            'aliases': ["turner", "turner"],
        },
        {
            'name': 'udpastcp',
            'description': "This program hides UDP traffic as TCP traffic in order to bypass certain firewalls.",
            'aliases': ["udpastcp", "udpastcp"],
        },
        {
            'name': 'udptunnel',
            'description': "Tunnels TCP over UDP packets.",
            'aliases': ["udptunnel", "udptunnel"],
        },
        {
            'name': 'umit',
            'description': "A powerful nmap frontend.",
            'aliases': ["umit", "umit"],
        },
        {
            'name': 'uw-offish',
            'description': "Clear-text protocol simulator.",
            'aliases': ["uw-offish", "uw offish"],
        },
        {
            'name': 'websockify',
            'description': "WebSocket to TCP proxy/bridge.",
            'aliases': ["websockify", "websockify"],
        },
        {
            'name': 'wondershaper',
            'description': "Limit the bandwidth of one or more network adapters.",
            'aliases': ["wondershaper", "wondershaper"],
        },
        {
            'name': 'xerosploit',
            'description': "Efficient and advanced man in the middle framework.",
            'aliases': ["xerosploit", "xerosploit"],
        },
        {
            'name': 'xxeserv',
            'description': "A mini webserver with FTP support for XXE payloads.",
            'aliases': ["xxeserv", "xxeserv"],
        },
        {
            'name': 'yaf',
            'description': "Yet Another Flowmeter.",
            'aliases': ["yaf", "yaf"],
        },
        {
            'name': 'yersinia',
            'description': "A network tool designed to take advantage of some weakness in different network protocols.",
            'aliases': ["yersinia", "yersinia network"],
        },
        {
            'name': 'zackattack',
            'description': "A new tool set to do NTLM Authentication relaying unlike any other tool currently out there.",
            'aliases': ["zackattack", "zackattack"],
        },
        {
            'name': 'zdns',
            'description': "Fast CLI DNS Lookup Tool.",
            'aliases': ["zdns", "zdns"],
        },
        {
            'name': 'zeek',
            'description': "A powerful network analysis framework that is much different from the typical IDS you may know.",
            'aliases': ["zeek", "zeek"],
        },
        {
            'name': 'zeek-aux',
            'description': "Handy auxiliary programs related to the use of the Zeek Network Security Monitor.",
            'aliases': ["zeek-aux", "zeek aux"],
        },
    ],

    # Miscellaneous (145 tools)
    'blackarch-misc': [
        {
            'name': 'alterx',
            'description': "Fast and customizable subdomain wordlist generator using DSL.",
            'aliases': ["alterx", "alterx"],
        },
        {
            'name': 'archivebox',
            'description': "The open source self-hosted web archive. Takes browser history/bookmarks/Pocket/Pinboard/etc., saves HTML, JS, PDFs, media, and more.",
            'aliases': ["archivebox", "archivebox"],
        },
        {
            'name': 'aspisec',
            'description': "Removes the traces left by offensive security tools.",
            'aliases': ["aspisec", "aspisec"],
        },
        {
            'name': 'aurebeshjs',
            'description': "Translate JavaScript to Other Alphabets.",
            'aliases': ["aurebeshjs", "aurebeshjs"],
        },
        {
            'name': 'avml',
            'description': "A portable volatile memory acquisition tool for Linux.",
            'aliases': ["avml", "avml"],
        },
        {
            'name': 'azurehound',
            'description': "Azure data exporter for BloodHound.",
            'aliases': ["azurehound", "azurehound"],
        },
        {
            'name': 'base64dump',
            'description': "Extract and decode base64 strings from files.",
            'aliases': ["base64dump", "base64dump"],
        },
        {
            'name': 'bettercap-ui',
            'description': "Official Bettercap\'s Web UI.",
            'aliases': ["bettercap-ui", "bettercap ui"],
        },
        {
            'name': 'bless',
            'description': "High-quality, full-featured hex editor.",
            'aliases': ["bless", "bless"],
        },
        {
            'name': 'bloodhound-cli',
            'description': "Command-line interface for BloodHound v5.",
            'aliases': ["bloodhound-cli", "bloodhound cli"],
        },
        {
            'name': 'bqm',
            'description': "Download BloudHound query lists, deduplicate entries and merge them in one file.",
            'aliases': ["bqm", "bqm"],
        },
        {
            'name': 'catana',
            'description': "Filter your wordlist according to the specified password policy.",
            'aliases': ["catana", "catana"],
        },
        {
            'name': 'centry',
            'description': "Cold boot & DMA protection",
            'aliases': ["centry", "centry"],
        },
        {
            'name': 'checkiban',
            'description': "Checks the validity of an International Bank Account Number (IBAN).",
            'aliases': ["checkiban", "checkiban"],
        },
        {
            'name': 'cisco-router-config',
            'description': "Tools to copy and merge Cisco Routers Configuration.",
            'aliases': ["cisco-router-config", "cisco router config"],
        },
        {
            'name': 'cloakify',
            'description': "Data Exfiltration In Plain Sight; Evade DLP/MLS Devices; Social Engineering of Analysts; Evade AV Detection.",
            'aliases': ["cloakify", "cloakify"],
        },
        {
            'name': 'cracken',
            'description': "A ast password wordlist generator, Smartlist creation and password hybrid-mask analysis tool written in pure safe Rust.",
            'aliases': ["cracken", "cracken"],
        },
        {
            'name': 'credmap',
            'description': "The Credential mapper - Tool that was created to bring awareness to the dangers of credential reuse.",
            'aliases': ["credmap", "credmap"],
        },
        {
            'name': 'ctf-party',
            'description': "A CLI tool & library to enhance and speed up script/exploit writing for CTF players.",
            'aliases': ["ctf-party", "ctf party"],
        },
        {
            'name': 'cve-api',
            'description': "Unofficial api for cve.mitre.org.",
            'aliases': ["cve-api", "cve api"],
        },
        {
            'name': 'dbd',
            'description': "A Netcat-clone, designed to be portable and offer strong encryption. It runs on Unix-like operating systems and on Microsoft Win32.",
            'aliases': ["dbd", "dbd"],
        },
        {
            'name': 'densityscout',
            'description': "Calculates density for files of any file-system-path to finally output an accordingly descending ordered list.",
            'aliases': ["densityscout", "densityscout"],
        },
        {
            'name': 'depix',
            'description': "A tool for recovering passwords from pixelized screenshots.",
            'aliases': ["depix", "depix"],
        },
        {
            'name': 'der-ascii',
            'description': "A reversible DER and BER pretty-printer.",
            'aliases': ["der-ascii", "der ascii"],
        },
        {
            'name': 'dhcdrop',
            'description': "Remove illegal dhcp servers with IP-pool underflow.",
            'aliases': ["dhcdrop", "dhcdrop"],
        },
        {
            'name': 'dnsgen',
            'description': "Generate combination of domain names from the provided input.",
            'aliases': ["dnsgen", "dnsgen"],
        },
        {
            'name': 'domlink',
            'description': "A tool to link a domain with registered organisation names and emails, to other domains.",
            'aliases': ["domlink", "domlink"],
        },
        {
            'name': 'dsd',
            'description': "Digital Speech Decoder.",
            'aliases': ["dsd", "dsd"],
        },
        {
            'name': 'dsd-fme',
            'description': "Digital Speech Decoder - Florida Man Edition.",
            'aliases': ["dsd-fme", "dsd fme"],
        },
        {
            'name': 'dumpsmbshare',
            'description': "A script to dump files and folders remotely from a Windows SMB share.",
            'aliases': ["dumpsmbshare", "dumpsmbshare"],
        },
        {
            'name': 'duplicut',
            'description': "Remove duplicates from massive wordlist, without sorting it (for dictionnary-based password cracking).",
            'aliases': ["duplicut", "duplicut"],
        },
        {
            'name': 'elettra',
            'description': "A plausible deniable cryptography tool that supports a dynamic number of files and requires a password for each file.",
            'aliases': ["elettra", "elettra"],
        },
        {
            'name': 'elettra-gui',
            'description': "Gui for the elettra crypto application.",
            'aliases': ["elettra-gui", "elettra gui"],
        },
        {
            'name': 'ent',
            'description': "Pseudorandom number sequence test.",
            'aliases': ["ent", "ent"],
        },
        {
            'name': 'evilgrade',
            'description': "Modular framework that takes advantage of poor upgrade implementations by injecting fake updates.",
            'aliases': ["evilgrade", "evilgrade"],
        },
        {
            'name': 'exrex',
            'description': "Irregular methods on regular expressions.",
            'aliases': ["exrex", "exrex"],
        },
        {
            'name': 'extracthosts',
            'description': "Extracts hosts (IP/Hostnames) from files.",
            'aliases': ["extracthosts", "extracthosts"],
        },
        {
            'name': 'eyeballer',
            'description': "Convolutional neural network for analyzing pentest screenshots.",
            'aliases': ["eyeballer", "eyeballer"],
        },
        {
            'name': 'fakemail',
            'description': "Fake mail server that captures e-mails as files for acceptance testing.",
            'aliases': ["fakemail", "fakemail"],
        },
        {
            'name': 'ffuf-scripts',
            'description': "Scripts and snippets for ffuf payloads.",
            'aliases': ["ffuf-scripts", "ffuf scripts"],
        },
        {
            'name': 'find3',
            'description': "High-precision indoor positioning framework.",
            'aliases': ["find3", "find3"],
        },
        {
            'name': 'firefox-security-toolkit',
            'description': "A tool that transforms Firefox browsers into a penetration testing suite.",
            'aliases': ["firefox-security-toolkit", "firefox security toolkit"],
        },
        {
            'name': 'flare',
            'description': "Flare processes an SWF and extracts all scripts from it.",
            'aliases': ["flare", "flare"],
        },
        {
            'name': 'genlist',
            'description': "Generates lists of IP addresses.",
            'aliases': ["genlist", "genlist"],
        },
        {
            'name': 'geoipgen',
            'description': "A country to IP addresses generator.",
            'aliases': ["geoipgen", "geoipgen"],
        },
        {
            'name': 'gf',
            'description': "A wrapper around grep, to help you grep for things.",
            'aliases': ["gf", "gf"],
        },
        {
            'name': 'gibberish-detector',
            'description': "Train a model and detect gibberish strings with it.",
            'aliases': ["gibberish-detector", "gibberish detector"],
        },
        {
            'name': 'githubcloner',
            'description': "A script that clones Github repositories of users and organizations automatically.",
            'aliases': ["githubcloner", "githubcloner"],
        },
        {
            'name': 'gmsadumper',
            'description': "A tool that Reads any gMSA password blobs the user can access and parses the values.",
            'aliases': ["gmsadumper", "gmsadumper"],
        },
        {
            'name': 'goshs',
            'description': "A single-binary file server for pentesters and sysadmins with HTTP/S, WebDAV, SFTP, SMB, LDAP, NTLM hash capture, DNS/SMTP callbacks and more.",
            'aliases': ["goshs", "goshs"],
        },
        {
            'name': 'graffiti',
            'description': "A tool to generate obfuscated one liners to aid in penetration testing.",
            'aliases': ["graffiti", "graffiti"],
        },
        {
            'name': 'gtfo',
            'description': "Search gtfobins and lolbas files from your terminal.",
            'aliases': ["gtfo", "gtfo"],
        },
        {
            'name': 'gtfoblookup',
            'description': "Offline command line lookup utility for GTFOBins and LOLBAS.",
            'aliases': ["gtfoblookup", "gtfoblookup"],
        },
        {
            'name': 'h2spec',
            'description': "A conformance testing tool for HTTP/2 implementation.",
            'aliases': ["h2spec", "h2spec"],
        },
        {
            'name': 'halcyon-ide',
            'description': "First IDE for Nmap Script (NSE) Development.",
            'aliases': ["halcyon-ide", "halcyon ide"],
        },
        {
            'name': 'http-put',
            'description': "Simple http put perl script.",
            'aliases': ["http-put", "http put"],
        },
        {
            'name': 'httpscreenshot',
            'description': "A tool for grabbing screenshots and HTML of large numbers of websites.",
            'aliases': ["httpscreenshot", "httpscreenshot"],
        },
        {
            'name': 'hurl-encoder',
            'description': "Hexadecimal & URL (en/de)coder.",
            'aliases': ["hurl-encoder", "hurl encoder"],
        },
        {
            'name': 'hxd',
            'description': "Freeware Hex Editor and Disk Editor.",
            'aliases': ["hxd", "hxd"],
        },
        {
            'name': 'imagegrep',
            'description': "Grep word in pdf or image based on OCR.",
            'aliases': ["imagegrep", "imagegrep"],
        },
        {
            'name': 'imhex',
            'description': "A Hex Editor for Reverse Engineers, Programmers and people that value their eye sight when working at 3 AM.",
            'aliases': ["imhex", "imhex"],
        },
        {
            'name': 'intelmq',
            'description': "A tool for collecting and processing security feeds using a message queuing protocol.",
            'aliases': ["intelmq", "intelmq"],
        },
        {
            'name': 'intensio-obfuscator',
            'description': "Obfuscate a python code 2 and 3.",
            'aliases': ["intensio-obfuscator", "intensio obfuscator"],
        },
        {
            'name': 'inundator',
            'description': "An ids evasion tool, used to anonymously inundate intrusion detection logs with false positives in order to obfuscate a real attack.",
            'aliases': ["inundator", "inundator"],
        },
        {
            'name': 'ipcountry',
            'description': "Fetches IPv4 ranges of given country in host and cidr format.",
            'aliases': ["ipcountry", "ipcountry"],
        },
        {
            'name': 'ipobfuscator',
            'description': "A simple tool to convert the IP to a DWORD IP.",
            'aliases': ["ipobfuscator", "ipobfuscator"],
        },
        {
            'name': 'jsfuck',
            'description': "Write any JavaScript with 6 Characters: []()!+.",
            'aliases': ["jsfuck", "jsfuck"],
        },
        {
            'name': 'laudanum',
            'description': "A collection of injectable files, designed to be used in a pentest when SQL injection flaws are found and are in multiple languages for different environments.",
            'aliases': ["laudanum", "laudanum"],
        },
        {
            'name': 'leo',
            'description': "Literate programmer\'s editor, outliner, and project manager.",
            'aliases': ["leo", "leo"],
        },
        {
            'name': 'magictree',
            'description': "A penetration tester productivity tool designed to allow easy and straightforward data consolidation, querying, external command execution and report generation",
            'aliases': ["magictree", "magictree"],
        },
        {
            'name': 'mapcidr',
            'description': "Utility program to perform multiple operations for a given subnet/CIDR ranges.",
            'aliases': ["mapcidr", "mapcidr"],
        },
        {
            'name': 'metaforge',
            'description': "Auto Scanning to SSL Vulnerability.",
            'aliases': ["metaforge", "metaforge"],
        },
        {
            'name': 'mibble',
            'description': "An open-source SNMP MIB parser (or SMI parser) written in Java. It can be used to read SNMP MIB files as well as simple ASN.1 files.",
            'aliases': ["mibble", "mibble"],
        },
        {
            'name': 'minimodem',
            'description': "A command-line program which decodes (or generates) audio modem tones at any specified baud rate, using various framing protocols.",
            'aliases': ["minimodem", "minimodem"],
        },
        {
            'name': 'mkyara',
            'description': "Tool to generate YARA rules based on binary code.",
            'aliases': ["mkyara", "mkyara"],
        },
        {
            'name': 'mrtparse',
            'description': "A module to read and analyze the MRT format data.",
            'aliases': ["mrtparse", "mrtparse"],
        },
        {
            'name': 'msfdb',
            'description': "Manage the metasploit framework database.",
            'aliases': ["msfdb", "msfdb"],
        },
        {
            'name': 'narthex',
            'description': "Modular personalized dictionary generator.",
            'aliases': ["narthex", "narthex"],
        },
        {
            'name': 'nmap-parse-output',
            'description': "Converts/manipulates/extracts data from a nmap scan output.",
            'aliases': ["nmap-parse", "nmap parse output"],
        },
        {
            'name': 'nsearch',
            'description': "Minimal script to help find script into the nse database.",
            'aliases': ["nsearch", "nsearch"],
        },
        {
            'name': 'one-lin3r',
            'description': "Gives you one-liners that aids in penetration testing and more.",
            'aliases': ["one-lin3r", "one lin3r"],
        },
        {
            'name': 'openrisk',
            'description': "Generates a risk score based on the results of a Nuclei scan using OpenAI\'s GPT model.",
            'aliases': ["openrisk", "openrisk"],
        },
        {
            'name': 'osert',
            'description': "Markdown Templates for Offensive Security exam reports.",
            'aliases': ["osert", "osert"],
        },
        {
            'name': 'pass-station',
            'description': "CLI & library to search for default credentials among thousands of Products / Vendors.",
            'aliases': ["pass-station", "pass station"],
        },
        {
            'name': 'passdetective',
            'description': "Scans shell command history to detect mistakenly written passwords, API keys, and secrets.",
            'aliases': ["passdetective", "passdetective"],
        },
        {
            'name': 'payloadsallthethings',
            'description': "A list of useful payloads and bypass for Web Application Security and Pentest/CTF.",
            'aliases': ["payloads", "payloads all the things"],
        },
        {
            'name': 'pdfwalker',
            'description': "Frontend to explore the internals of a PDF document with Origami",
            'aliases': ["pdfwalker", "pdfwalker"],
        },
        {
            'name': 'pencode',
            'description': "Complex payload encoder.",
            'aliases': ["pencode", "pencode"],
        },
        {
            'name': 'plumber.py',
            'description': "A python implementation of a grep friendly ftrace wrapper.",
            'aliases': ["plumber.py", "plumber.py"],
        },
        {
            'name': 'plutil',
            'description': "Converts .plist files between binary and UTF (editable) text formats.",
            'aliases': ["plutil", "plutil"],
        },
        {
            'name': 'princeprocessor',
            'description': "Standalone password candidate generator using the PRINCE algorithm.",
            'aliases': ["princeprocessor", "princeprocessor"],
        },
        {
            'name': 'pspy',
            'description': "Monitor linux processes without root permissions.",
            'aliases': ["pspy", "pspy"],
        },
        {
            'name': 'pulledpork',
            'description': "Snort rule management.",
            'aliases': ["pulledpork", "pulledpork"],
        },
        {
            'name': 'pwdlogy',
            'description': "A target specific wordlist generating tool for social engineers and security researchers.",
            'aliases': ["pwdlogy", "pwdlogy"],
        },
        {
            'name': 'pwfuzz-rs',
            'description': "Rust-based password mutator for brute force attacks.",
            'aliases': ["pwfuzz-rs", "pwfuzz rs"],
        },
        {
            'name': 'pwnedpasswords',
            'description': "Generate and verify pwnedpasswords check digits.",
            'aliases': ["pwnedpasswords", "pwnedpasswords"],
        },
        {
            'name': 'pydictor',
            'description': "A useful hacker dictionary builder for a brute-force attack.",
            'aliases': ["pydictor", "pydictor"],
        },
        {
            'name': 'pyinstaller',
            'description': "Bundles a Python application and all its dependencies into a single package.",
            'aliases': ["pyinstaller", "pyinstaller"],
        },
        {
            'name': 'pyinstaller-hooks-contrib',
            'description': "PyInstaller community hooks.",
            'aliases': ["pyinstaller-hooks-contrib", "pyinstaller hooks contrib"],
        },
        {
            'name': 'python-google-streetview',
            'description': "A command line tool and module for Google Street View Image API.",
            'aliases': ["python-google-streetview", "python google streetview"],
        },
        {
            'name': 'python2-darts.util.lru',
            'description': "Simple dictionary with LRU behaviour.",
            'aliases': ["python2-darts.util.lru", "python2 darts.util.lru"],
        },
        {
            'name': 'python2-exrex',
            'description': "Irregular methods on regular expressions.",
            'aliases': ["python2-exrex", "python2 exrex"],
        },
        {
            'name': 'python2-google-streetview',
            'description': "A command line tool and module for Google Street View Image API.",
            'aliases': ["python2-google-streetview", "python2 google streetview"],
        },
        {
            'name': 'python2-utidylib',
            'description': "Python bindings for Tidy HTML parser/cleaner.",
            'aliases': ["python2-utidylib", "python2 utidylib"],
        },
        {
            'name': 'qrgen',
            'description': "Simple script for generating Malformed QRCodes.",
            'aliases': ["qrgen", "qrgen"],
        },
        {
            'name': 'qsreplace',
            'description': "Accept URLs on stdin, replace all query string values with a user-supplied value, only output each combination of query string parameters once per host and path.",
            'aliases': ["qsreplace", "query string replace"],
        },
        {
            'name': 'rawsec-cli',
            'description': "Rawsec Inventory search CLI to find security tools and resources.",
            'aliases': ["rawsec-cli", "rawsec cli"],
        },
        {
            'name': 'rbkb',
            'description': "A miscellaneous collection of command-line tools related to pen-testing and reversing.",
            'aliases': ["rbkb", "rbkb"],
        },
        {
            'name': 'redeye',
            'description': "Visual analytic tool supporting Red & Blue Team operations.",
            'aliases': ["redeye", "redeye"],
        },
        {
            'name': 'redpoint',
            'description': "Digital Bond\'s ICS Enumeration Tools.",
            'aliases': ["redpoint", "redpoint"],
        },
        {
            'name': 'reptor',
            'description': "CLI tool to automate pentest reporting with SysReptor.",
            'aliases': ["reptor", "reptor"],
        },
        {
            'name': 'rogue-mysql-server',
            'description': "A rogue MySQL server written in Python.",
            'aliases': ["rogue-mysql-server", "rogue mysql server"],
        },
        {
            'name': 'rtfm',
            'description': "A database of common, interesting or useful commands, in one handy referable form.",
            'aliases': ["rtfm", "rtfm"],
        },
        {
            'name': 'rulesfinder',
            'description': "Machine-learn password mangling rules.",
            'aliases': ["rulesfinder", "rulesfinder"],
        },
        {
            'name': 'sasm',
            'description': "A simple crossplatform IDE for NASM, MASM, GAS and FASM assembly languages.",
            'aliases': ["sasm", "sasm"],
        },
        {
            'name': 'schnappi-dhcp',
            'description': "Can fuck network with no DHCP.",
            'aliases': ["schnappi-dhcp", "schnappi dhcp"],
        },
        {
            'name': 'sh00t',
            'description': "A Testing Environment for Manual Security Testers.",
            'aliases': ["sh00t", "sh00t"],
        },
        {
            'name': 'shadowfinder',
            'description': "Find possible locations of shadows around the world.",
            'aliases': ["shadowfinder", "shadowfinder"],
        },
        {
            'name': 'shelling',
            'description': "An offensive approach to the anatomy of improperly written OS command injection sanitisers.",
            'aliases': ["shelling", "shelling"],
        },
        {
            'name': 'sleuthql',
            'description': "Python3 Burp History parsing tool to discover potential SQL injection points. To be used in tandem with SQLmap.",
            'aliases': ["sleuthql", "sleuthql"],
        },
        {
            'name': 'stompy',
            'description': "An advanced utility to test the quality of WWW session identifiers and other tokens that are meant to be unpredictable.",
            'aliases': ["stompy", "stompy"],
        },
        {
            'name': 'suricata-verify',
            'description': "Suricata Verification Tests - Testing Suricata Output.",
            'aliases': ["suricata-verify", "suricata verify"],
        },
        {
            'name': 'tcpxtract',
            'description': "A tool for extracting files from network traffic.",
            'aliases': ["tcpxtract", "tcpxtract"],
        },
        {
            'name': 'tempomail',
            'description': "Tool to create a temporary email address in 1 Second and receive emails.",
            'aliases': ["tempomail", "tempomail"],
        },
        {
            'name': 'tnscmd',
            'description': "A lame tool to prod the oracle tnslsnr process (1521/tcp).",
            'aliases': ["tnscmd", "tnscmd"],
        },
        {
            'name': 'token-reverser',
            'description': "Word list generator to crack security tokens.",
            'aliases': ["token-reverser", "token reverser"],
        },
        {
            'name': 'tpcat',
            'description': "Tool based upon pcapdiff by the EFF.",
            'aliases': ["tpcat", "tpcat"],
        },
        {
            'name': 'uatester',
            'description': "User Agent String Tester",
            'aliases': ["uatester", "uatester"],
        },
        {
            'name': 'uberfile',
            'description': "CLI tool for the generation of downloader oneliners for UNIX-like or Windows systems.",
            'aliases': ["uberfile", "uberfile"],
        },
        {
            'name': 'unfurl',
            'description': "Pull out bits of URLs provided on stdin.",
            'aliases': ["unfurl", "unfurl url"],
        },
        {
            'name': 'unisec',
            'description': "Unicode Security Toolkit.",
            'aliases': ["unisec", "unisec"],
        },
        {
            'name': 'urlview',
            'description': "A curses URL parser for text files.",
            'aliases': ["urlview", "urlview"],
        },
        {
            'name': 'usernamer',
            'description': "Pentest Tool to generate usernames/logins based on supplied names.",
            'aliases': ["usernamer", "usernamer"],
        },
        {
            'name': 'verinice',
            'description': "Tool for managing information security.",
            'aliases': ["verinice", "verinice"],
        },
        {
            'name': 'vfeed',
            'description': "Open Source Cross Linked and Aggregated Local Vulnerability Database main repository.",
            'aliases': ["vfeed", "vfeed"],
        },
        {
            'name': 'visualize-logs',
            'description': "A Python library and command line tools to provide interactive log visualization.",
            'aliases': ["visualize-logs", "visualize logs"],
        },
        {
            'name': 'web2ldap',
            'description': "Full-featured LDAP client running as web application.",
            'aliases': ["web2ldap", "web2ldap"],
        },
        {
            'name': 'whapa',
            'description': "WhatsApp Parser Tool.",
            'aliases': ["whapa", "whapa"],
        },
        {
            'name': 'whatportis',
            'description': "A command to search port names and numbers.",
            'aliases': ["whatportis", "whatportis"],
        },
        {
            'name': 'winexe',
            'description': "Remotely execute commands on Windows NT/2000/XP/2003 systems.",
            'aliases': ["winexe", "winexe"],
        },
        {
            'name': 'winregfs',
            'description': "Windows Registry FUSE filesystem.",
            'aliases': ["winregfs", "winregfs"],
        },
        {
            'name': 'wol-e',
            'description': "A suite of tools for the Wake on LAN feature of network attached computers.",
            'aliases': ["wol-e", "wol e"],
        },
        {
            'name': 'wordlistctl',
            'description': "Fetch, install and search wordlist archives from websites.",
            'aliases': ["wordlistctl", "wordlistctl"],
        },
        {
            'name': 'wordlister',
            'description': "A simple wordlist generator and mangler written in python.",
            'aliases': ["wordlister", "wordlister"],
        },
        {
            'name': 'yay',
            'description': "Yet another yogurt. Pacman wrapper and AUR helper written in go.",
            'aliases': ["yay", "yay"],
        },
    ],

    # Forensic (126 tools)
    'blackarch-forensic': [
        {
            'name': 'afflib',
            'description': "An extensible open format for the storage of disk images and related forensic information.",
            'aliases': ["afflib", "afflib"],
        },
        {
            'name': 'aimage',
            'description': "A tool to create aff-images.",
            'aliases': ["aimage", "aimage"],
        },
        {
            'name': 'air',
            'description': "A GUI front-end to dd/dc3dd designed for easily creating forensic images.",
            'aliases': ["air", "air"],
        },
        {
            'name': 'analyzemft',
            'description': "Parse the MFT file from an NTFS filesystem.",
            'aliases': ["analyzemft", "analyzemft"],
        },
        {
            'name': 'autopsy',
            'description': "The forensic browser. A GUI for the Sleuth Kit.",
            'aliases': ["autopsy", "autopsy forensic"],
        },
        {
            'name': 'bmap-tools',
            'description': "Tool for copying largely sparse files using information from a block map file.",
            'aliases': ["bmap-tools", "bmap tools"],
        },
        {
            'name': 'bmc-tools',
            'description': "RDP Bitmap Cache parser.",
            'aliases': ["bmc-tools", "bmc tools"],
        },
        {
            'name': 'bulk-extractor',
            'description': "Bulk Email and URL extraction tool.",
            'aliases': ["bulk-extractor", "bulk extractor"],
        },
        {
            'name': 'canari',
            'description': "Maltego rapid transform development and execution framework.",
            'aliases': ["canari", "canari"],
        },
        {
            'name': 'captipper',
            'description': "Malicious HTTP traffic explorer tool.",
            'aliases': ["captipper", "captipper"],
        },
        {
            'name': 'casefile',
            'description': "The little brother to Maltego without transforms, but combines graph and link analysis to examine links between manually added data to mind map your information",
            'aliases': ["casefile", "casefile"],
        },
        {
            'name': 'chaosmap',
            'description': "An information gathering tool and dns / whois / web server scanner",
            'aliases': ["chaosmap", "chaosmap"],
        },
        {
            'name': 'chromefreak',
            'description': "A Cross-Platform Forensic Framework for Google Chrome",
            'aliases': ["chromefreak", "chromefreak"],
        },
        {
            'name': 'dc3dd',
            'description': "A patched version of dd that includes a number of features useful for computer forensics.",
            'aliases': ["dc3dd", "dc3dd"],
        },
        {
            'name': 'dcfldd',
            'description': "DCFL (DoD Computer Forensics Lab) dd replacement with hashing.",
            'aliases': ["dcfldd", "dcfldd"],
        },
        {
            'name': 'dfir-ntfs',
            'description': "An NTFS parser for digital forensics & incident response.",
            'aliases': ["dfir-ntfs", "dfir ntfs"],
        },
        {
            'name': 'dftimewolf',
            'description': "Framework for orchestrating forensic collection, processing and data export.",
            'aliases': ["dftimewolf", "dftimewolf"],
        },
        {
            'name': 'disitool',
            'description': "Tool to work with Windows executables digital signatures.",
            'aliases': ["disitool", "disitool"],
        },
        {
            'name': 'dmde',
            'description': "Disk Editor and Data Recovery Software.",
            'aliases': ["dmde", "dmde"],
        },
        {
            'name': 'dmg2img',
            'description': "A CLI tool to uncompress Apple\'s compressed DMG files to the HFS+ IMG format.",
            'aliases': ["dmg2img", "dmg2img"],
        },
        {
            'name': 'dshell',
            'description': "A network forensic analysis framework.",
            'aliases': ["dshell", "dshell"],
        },
        {
            'name': 'dumpzilla',
            'description': "A forensic tool for firefox.",
            'aliases': ["dumpzilla", "dumpzilla"],
        },
        {
            'name': 'eindeutig',
            'description': "Examine the contents of Outlook Express DBX email repository files.",
            'aliases': ["eindeutig", "eindeutig"],
        },
        {
            'name': 'emldump',
            'description': "Analyze MIME files.",
            'aliases': ["emldump", "emldump"],
        },
        {
            'name': 'evtkit',
            'description': "Fix acquired .evt - Windows Event Log files (Forensics).",
            'aliases': ["evtkit", "evtkit"],
        },
        {
            'name': 'exiflooter',
            'description': "Find geolocation on all image urls and directories also integrates with OpenStreetMap.",
            'aliases': ["exiflooter", "exiflooter"],
        },
        {
            'name': 'ext4magic',
            'description': "File carver used when recovering from disasters or in digital forensics activities.",
            'aliases': ["ext4magic", "ext4magic"],
        },
        {
            'name': 'extractusnjrnl',
            'description': "Tool to extract the $UsnJrnl from an NTFS volume.",
            'aliases': ["extractusnjrnl", "extractusnjrnl"],
        },
        {
            'name': 'firefox-decrypt',
            'description': "Extract passwords from Mozilla Firefox, Waterfox, Thunderbird, SeaMonkey profiles.",
            'aliases': ["firefox-decrypt", "firefox decrypt"],
        },
        {
            'name': 'fridump',
            'description': "A universal memory dumper using Frida.",
            'aliases': ["fridump", "fridump"],
        },
        {
            'name': 'galleta',
            'description': "Examine the contents of the IE\'s cookie files for forensic purposes.",
            'aliases': ["galleta", "galleta"],
        },
        {
            'name': 'grokevt',
            'description': "A collection of scripts built for reading Windows® NT/2K/XP/2K eventlog files.",
            'aliases': ["grokevt", "grokevt"],
        },
        {
            'name': 'gspy',
            'description': "Forensic goroutine-to-syscall inspector for live Go processes.",
            'aliases': ["gspy", "gspy"],
        },
        {
            'name': 'guymager',
            'description': "A forensic imager for media acquisition.",
            'aliases': ["guymager", "guymager"],
        },
        {
            'name': 'imagemounter',
            'description': "Command line utility and Python package to ease the (un)mounting of forensic disk images.",
            'aliases': ["imagemounter", "imagemounter"],
        },
        {
            'name': 'indx2csv',
            'description': "An advanced parser for INDX records.",
            'aliases': ["indx2csv", "indx2csv"],
        },
        {
            'name': 'indxcarver',
            'description': "Carve INDX records from a chunk of data.",
            'aliases': ["indxcarver", "indxcarver"],
        },
        {
            'name': 'indxparse',
            'description': "A Tool suite for inspecting NTFS artifacts.",
            'aliases': ["indxparse", "indxparse"],
        },
        {
            'name': 'interrogate',
            'description': "A proof-of-concept tool for identification of cryptographic keys in binary material (regardless of target operating system), first and foremost for memory dump analysis and forensic usage.",
            'aliases': ["interrogate", "interrogate"],
        },
        {
            'name': 'iosforensic',
            'description': "iOS forensic tool.",
            'aliases': ["iosforensic", "iosforensic"],
        },
        {
            'name': 'ipba2',
            'description': "IOS Backup Analyzer.",
            'aliases': ["ipba2", "ipba2"],
        },
        {
            'name': 'iphoneanalyzer',
            'description': "Allows you to forensically examine or recover date from in iOS device.",
            'aliases': ["iphoneanalyzer", "iphoneanalyzer"],
        },
        {
            'name': 'jefferson',
            'description': "JFFS2 filesystem extraction tool.",
            'aliases': ["jefferson", "jefferson"],
        },
        {
            'name': 'lazagne',
            'description': "An open source application used to retrieve lots of passwords stored on a local computer.",
            'aliases': ["lazagne", "lazagne"],
        },
        {
            'name': 'ldsview',
            'description': "Offline search tool for LDAP directory dumps in LDIF format.",
            'aliases': ["ldsview", "ldsview"],
        },
        {
            'name': 'lfle',
            'description': "Recover event log entries from an image by heurisitically looking for record structures.",
            'aliases': ["lfle", "lfle"],
        },
        {
            'name': 'libfvde',
            'description': "Library and tools to access FileVault Drive Encryption (FVDE) encrypted volumes.",
            'aliases': ["libfvde", "libfvde"],
        },
        {
            'name': 'limeaide',
            'description': "Remotely dump RAM of a Linux client and create a volatility profile for later analysis on your local host.",
            'aliases': ["limeaide", "limeaide"],
        },
        {
            'name': 'log-file-parser',
            'description': "Parser for $LogFile on NTFS.",
            'aliases': ["log-file-parser", "log file parser"],
        },
        {
            'name': 'loki-scanner',
            'description': "Simple IOC and Incident Response Scanner.",
            'aliases': ["loki-scanner", "loki scanner"],
        },
        {
            'name': 'mac-robber',
            'description': "A digital investigation tool that collects data from allocated files in a mounted file system.",
            'aliases': ["mac-robber", "mac robber"],
        },
        {
            'name': 'magicrescue',
            'description': "Find and recover deleted files on block devices.",
            'aliases': ["magicrescue", "magicrescue"],
        },
        {
            'name': 'make-pdf',
            'description': "This tool will embed javascript inside a PDF document.",
            'aliases': ["make-pdf", "make pdf"],
        },
        {
            'name': 'malheur',
            'description': "A tool for the automatic analyze of malware behavior.",
            'aliases': ["malheur", "malheur"],
        },
        {
            'name': 'maltego',
            'description': "An open source intelligence and forensics application, enabling to easily gather information about DNS, domains, IP addresses, websites, persons, etc.",
            'aliases': ["maltego", "maltego ce"],
        },
        {
            'name': 'malwaredetect',
            'description': "Submits a file\'s SHA1 sum to VirusTotal to determine whether it is a known piece of malware",
            'aliases': ["malwaredetect", "malwaredetect"],
        },
        {
            'name': 'mboxgrep',
            'description': "A small, non-interactive utility that scans mail folders for messages matching regular expressions. It does matching against basic and extended POSIX regular expressions, and reads and writes a variety of mailbox formats.",
            'aliases': ["mboxgrep", "mboxgrep"],
        },
        {
            'name': 'mdbtools',
            'description': "Utilities for viewing data and exporting schema from Microsoft Access Database files.",
            'aliases': ["mdbtools", "mdbtools"],
        },
        {
            'name': 'memdump',
            'description': "Dumps system memory to stdout, skipping over holes in memory maps.",
            'aliases': ["memdump", "memdump"],
        },
        {
            'name': 'memfetch',
            'description': "Dumps any userspace process memory without affecting its execution.",
            'aliases': ["memfetch", "memfetch"],
        },
        {
            'name': 'mft2csv',
            'description': "Extract $MFT record info and log it to a csv file.",
            'aliases': ["mft2csv", "mft2csv"],
        },
        {
            'name': 'mftcarver',
            'description': "Carve $MFT records from a chunk of data (for instance a memory dump).",
            'aliases': ["mftcarver", "mftcarver"],
        },
        {
            'name': 'mftrcrd',
            'description': "Command line $MFT record decoder.",
            'aliases': ["mftrcrd", "mftrcrd"],
        },
        {
            'name': 'mftref2name',
            'description': "Resolve file index number to name or vice versa on NTFS.",
            'aliases': ["mftref2name", "mftref2name"],
        },
        {
            'name': 'mimipenguin',
            'description': "A tool to dump the login password from the current linux user.",
            'aliases': ["mimipenguin", "mimipenguin"],
        },
        {
            'name': 'mobiusft',
            'description': "An open-source forensic framework written in Python/GTK that manages cases and case items, providing an abstract interface for developing extensions.",
            'aliases': ["mobiusft", "mobiusft"],
        },
        {
            'name': 'mp3nema',
            'description': "A tool aimed at analyzing and capturing data that is hidden between frames in an MP3 file or stream, otherwise noted as \"out of band\" data.",
            'aliases': ["mp3nema", "mp3nema"],
        },
        {
            'name': 'mxtract',
            'description': "Memory Extractor & Analyzer.",
            'aliases': ["mxtract", "mxtract"],
        },
        {
            'name': 'myrescue',
            'description': "A hard disk recovery tool that reads undamaged regions first.",
            'aliases': ["myrescue", "myrescue"],
        },
        {
            'name': 'naft',
            'description': "Network Appliance Forensic Toolkit.",
            'aliases': ["naft", "naft"],
        },
        {
            'name': 'netspionage',
            'description': "Network Forensics CLI utility that performs Network Scanning, OSINT, and Attack Detection.",
            'aliases': ["netspionage", "netspionage"],
        },
        {
            'name': 'networkminer',
            'description': "A Network Forensic Analysis Tool for advanced Network Traffic Analysis, sniffer and packet analyzer.",
            'aliases': ["networkminer", "networkminer"],
        },
        {
            'name': 'nfex',
            'description': "A tool for extracting files from the network in real-time or post-capture from an offline tcpdump pcap savefile.",
            'aliases': ["nfex", "nfex"],
        },
        {
            'name': 'ntdsxtract',
            'description': "Active Directory forensic framework.",
            'aliases': ["ntdsxtract", "ntdsxtract"],
        },
        {
            'name': 'ntfs-file-extractor',
            'description': "Extract files off NTFS.",
            'aliases': ["ntfs-file-extractor", "ntfs file extractor"],
        },
        {
            'name': 'ntfs-log-tracker',
            'description': "This tool can parse $LogFile, $UsnJrnl of NTFS.",
            'aliases': ["ntfs-log-tracker", "ntfs log tracker"],
        },
        {
            'name': 'parse-evtx',
            'description': "A tool to parse the Windows XML Event Log (EVTX) format.",
            'aliases': ["parse-evtx", "parse evtx"],
        },
        {
            'name': 'pasco',
            'description': "Examines the contents of Internet Explorer\'s cache files for forensic purposes.",
            'aliases': ["pasco", "pasco"],
        },
        {
            'name': 'pcapxray',
            'description': "A Network Forensics Tool - To visualize a Packet Capture offline as a Network Diagram including device identification, highlight important communication and file extraction.",
            'aliases': ["pcapxray", "pcapxray"],
        },
        {
            'name': 'pdblaster',
            'description': "Extract PDB file paths from large sample sets of executable files.",
            'aliases': ["pdblaster", "pdblaster"],
        },
        {
            'name': 'pdf-parser',
            'description': "Parses a PDF document to identify the fundamental elements used in the analyzed file.",
            'aliases': ["pdf-parser", "pdf parser"],
        },
        {
            'name': 'pdfbook-analyzer',
            'description': "Utility for facebook memory forensics.",
            'aliases': ["pdfbook-analyzer", "pdfbook analyzer"],
        },
        {
            'name': 'pdfid',
            'description': "Scan a file to look for certain PDF keywords.",
            'aliases': ["pdfid", "pdfid"],
        },
        {
            'name': 'pdfresurrect',
            'description': "A tool aimed at analyzing PDF documents.",
            'aliases': ["pdfresurrect", "pdfresurrect"],
        },
        {
            'name': 'peepdf',
            'description': "A Python tool to explore PDF files in order to find out if the file can be harmful or not.",
            'aliases': ["peepdf", "peepdf"],
        },
        {
            'name': 'pev',
            'description': "Command line based tool for PE32/PE32+ file analysis.",
            'aliases': ["pev", "pev"],
        },
        {
            'name': 'powermft',
            'description': "Powerful commandline $MFT record editor.",
            'aliases': ["powermft", "powermft"],
        },
        {
            'name': 'python-flow.record',
            'description': "Recordization library.",
            'aliases': ["python-flow.record", "python flow.record"],
        },
        {
            'name': 'python2-peepdf',
            'description': "A Python tool to explore PDF files in order to find out if the file can be harmful or not.",
            'aliases': ["python2-peepdf", "python2 peepdf"],
        },
        {
            'name': 'rcrdcarver',
            'description': "Carve RCRD records ($LogFile) from a chunk of data..",
            'aliases': ["rcrdcarver", "rcrdcarver"],
        },
        {
            'name': 'recentfilecache-parser',
            'description': "Python parser for the RecentFileCache.bcf on Windows.",
            'aliases': ["recentfilecache-parser", "recentfilecache parser"],
        },
        {
            'name': 'recoverdm',
            'description': "Recover damaged CD DVD and disks with bad sectors.",
            'aliases': ["recoverdm", "recoverdm"],
        },
        {
            'name': 'recoverjpeg',
            'description': "Recover jpegs from damaged devices.",
            'aliases': ["recoverjpeg", "recoverjpeg"],
        },
        {
            'name': 'recuperabit',
            'description': "A tool for forensic file system reconstruction.",
            'aliases': ["recuperabit", "recuperabit"],
        },
        {
            'name': 'regipy',
            'description': "Library for parsing offline registry hives.",
            'aliases': ["regipy", "regipy"],
        },
        {
            'name': 'reglookup',
            'description': "Command line utility for reading and querying Windows NT registries.",
            'aliases': ["reglookup", "reglookup"],
        },
        {
            'name': 'regripper',
            'description': "Open source forensic software used as a Windows Registry data extraction command line or GUI tool.",
            'aliases': ["regripper", "regripper"],
        },
        {
            'name': 'regrippy',
            'description': "Framework for reading and extracting useful forensics data from Windows registry hives.",
            'aliases': ["regrippy", "regrippy"],
        },
        {
            'name': 'rekall',
            'description': "Memory Forensic Framework.",
            'aliases': ["rekall", "rekall"],
        },
        {
            'name': 'replayproxy',
            'description': "Forensic tool to replay web-based attacks (and also general HTTP traffic) that were captured in a pcap file.",
            'aliases': ["replayproxy", "replayproxy"],
        },
        {
            'name': 'rifiuti2',
            'description': "A rewrite of rifiuti, a great tool from Foundstone folks for analyzing Windows Recycle Bin INFO2 file.",
            'aliases': ["rifiuti2", "rifiuti2"],
        },
        {
            'name': 'safecopy',
            'description': "A disk data recovery tool to extract data from damaged media.",
            'aliases': ["safecopy", "safecopy"],
        },
        {
            'name': 'scalpel',
            'description': "A frugal, high performance file carver.",
            'aliases': ["scalpel", "scalpel tool"],
        },
        {
            'name': 'scrounge-ntfs',
            'description': "Data recovery program for NTFS file systems",
            'aliases': ["scrounge-ntfs", "scrounge ntfs"],
        },
        {
            'name': 'secure2csv',
            'description': "Decode security descriptors in $Secure on NTFS.",
            'aliases': ["secure2csv", "secure2csv"],
        },
        {
            'name': 'shadowexplorer',
            'description': "Browse the Shadow Copies created by the Windows Vista / 7 / 8 / 10 Volume Shadow Copy Service.",
            'aliases': ["shadowexplorer", "shadowexplorer"],
        },
        {
            'name': 'skypefreak',
            'description': "A Cross Platform Forensic Framework for Skype.",
            'aliases': ["skypefreak", "skypefreak"],
        },
        {
            'name': 'swap-digger',
            'description': "A tool used to automate Linux swap analysis during post-exploitation or forensics.",
            'aliases': ["swap-digger", "swap digger"],
        },
        {
            'name': 'tchunt-ng',
            'description': "Reveal encrypted files stored on a filesystem.",
            'aliases': ["tchunt-ng", "tchunt ng"],
        },
        {
            'name': 'tekdefense-automater',
            'description': "IP URL and MD5 OSINT Analysis",
            'aliases': ["tekdefense-automater", "tekdefense automater"],
        },
        {
            'name': 'thumbcacheviewer',
            'description': "Extract Windows thumbcache database files.",
            'aliases': ["thumbcacheviewer", "thumbcacheviewer"],
        },
        {
            'name': 'trid',
            'description': "An utility designed to identify file types from their binary signatures.",
            'aliases': ["trid", "trid"],
        },
        {
            'name': 'truehunter',
            'description': "Detect TrueCrypt containers using a fast and memory efficient approach.",
            'aliases': ["truehunter", "truehunter"],
        },
        {
            'name': 'unblob',
            'description': "Extract files from any kind of container formats.",
            'aliases': ["unblob", "unblob"],
        },
        {
            'name': 'undbx',
            'description': "Extract e-mail messages from Outlook Express DBX files.",
            'aliases': ["undbx", "undbx"],
        },
        {
            'name': 'usbrip',
            'description': "USB device artifacts tracker.",
            'aliases': ["usbrip", "usbrip"],
        },
        {
            'name': 'usnjrnl2csv',
            'description': "Parser for $UsnJrnl on NTFS.",
            'aliases': ["usnjrnl2csv", "usnjrnl2csv"],
        },
        {
            'name': 'usnparser',
            'description': "A Python script to parse the NTFS USN journal.",
            'aliases': ["usnparser", "usnparser"],
        },
        {
            'name': 'vinetto',
            'description': "A forensics tool to examine Thumbs.db files.",
            'aliases': ["vinetto", "vinetto"],
        },
        {
            'name': 'vipermonkey',
            'description': "A VBA parser and emulation engine to analyze malicious macros.",
            'aliases': ["vipermonkey", "vipermonkey"],
        },
        {
            'name': 'volafox',
            'description': "Mac OS X Memory Analysis Toolkit.",
            'aliases': ["volafox", "volafox"],
        },
        {
            'name': 'volatility-extra',
            'description': "Volatility plugins developed and maintained by the community.",
            'aliases': ["volatility-extra", "volatility extra"],
        },
        {
            'name': 'windows-prefetch-parser',
            'description': "Parse Windows Prefetch files.",
            'aliases': ["windows-prefetch-parser", "windows prefetch parser"],
        },
        {
            'name': 'wmi-forensics',
            'description': "Scripts used to find evidence in WMI repositories.",
            'aliases': ["wmi-forensics", "wmi forensics"],
        },
        {
            'name': 'xplico',
            'description': "Internet Traffic Decoder. Network Forensic Analysis Tool (NFAT).",
            'aliases': ["xplico", "xplico"],
        },
        {
            'name': 'zipdump',
            'description': "ZIP dump utility.",
            'aliases': ["zipdump", "zipdump"],
        },
    ],

    # Automation (108 tools)
    'blackarch-automation': [
        {
            'name': 'apt2',
            'description': "Automated penetration toolkit.",
            'aliases': ["apt2", "apt2"],
        },
        {
            'name': 'automato',
            'description': "Should help with automating some of the user-focused enumeration tasks during an internal penetration test.",
            'aliases': ["automato", "automato"],
        },
        {
            'name': 'autonessus',
            'description': "This script communicates with the Nessus API in an attempt to help with automating scans.",
            'aliases': ["autonessus", "autonessus"],
        },
        {
            'name': 'autonse',
            'description': "Massive NSE (Nmap Scripting Engine) AutoSploit and AutoScanner.",
            'aliases': ["autonse", "autonse"],
        },
        {
            'name': 'autopwn',
            'description': "Specify targets and run sets of tools against them.",
            'aliases': ["autopwn", "autopwn"],
        },
        {
            'name': 'autorecon',
            'description': "A multi-threaded network reconnaissance tool which performs automated enumeration of services.",
            'aliases': ["autorecon", "autorecon"],
        },
        {
            'name': 'awsbucketdump',
            'description': "A tool to quickly enumerate AWS S3 buckets to look for loot.",
            'aliases': ["awsbucketdump", "awsbucketdump"],
        },
        {
            'name': 'bashfuscator',
            'description': "Fully configurable and extendable Bash obfuscation framework.",
            'aliases': ["bashfuscator", "bashfuscator"],
        },
        {
            'name': 'blueranger',
            'description': "A simple Bash script which uses Link Quality to locate Bluetooth device radios.",
            'aliases': ["blueranger", "blue ranger"],
        },
        {
            'name': 'bopscrk',
            'description': "Tool to generate smart wordlists, eg. based on lyrics.",
            'aliases': ["bopscrk", "bopscrk"],
        },
        {
            'name': 'brutespray',
            'description': "Brute-Forcing from Nmap output - Automatically attempts default creds on found services.",
            'aliases': ["brutespray", "brutespray"],
        },
        {
            'name': 'brutex',
            'description': "Automatically brute force all services running on a target.",
            'aliases': ["brutex", "brutex"],
        },
        {
            'name': 'byepass',
            'description': "Automates password cracking tasks using optimized dictionaries and mangling rules.",
            'aliases': ["byepass", "byepass"],
        },
        {
            'name': 'cewl',
            'description': "A custom word list generator.",
            'aliases': ["cewl", "cewl"],
        },
        {
            'name': 'cheat-sh',
            'description': "The only cheat sheet you need.",
            'aliases': ["cheat-sh", "cheat sh"],
        },
        {
            'name': 'cisco-snmp-enumeration',
            'description': "Automated Cisco SNMP Enumeration, Brute Force, Configuration Download and Password Cracking.",
            'aliases': ["cisco-snmp-enumeration", "cisco snmp enumeration"],
        },
        {
            'name': 'clusterd',
            'description': "Automates the fingerprinting, reconnaissance, and exploitation phases of an application server attack.",
            'aliases': ["clusterd", "clusterd"],
        },
        {
            'name': 'codeql',
            'description': "The CLI tool for GitHub CodeQL",
            'aliases': ["codeql", "codeql"],
        },
        {
            'name': 'commonspeak',
            'description': "Leverages publicly available datasets from Google BigQuery to generate wordlists.",
            'aliases': ["commonspeak", "commonspeak"],
        },
        {
            'name': 'cook',
            'description': "Easily create word\'s permutation and combination to generate complex wordlists and passwords.",
            'aliases': ["cook", "cook"],
        },
        {
            'name': 'crunch',
            'description': "A wordlist generator for all combinations/permutations of a given character set.",
            'aliases': ["crunch", "crunch"],
        },
        {
            'name': 'deathstar',
            'description': "Automate getting Domain Admin using Empire.",
            'aliases': ["deathstar", "deathstar"],
        },
        {
            'name': 'dorkscout',
            'description': "Golang tool to automate google dork scan against the entire internet or specific targets.",
            'aliases': ["dorkscout", "dorkscout"],
        },
        {
            'name': 'dracnmap',
            'description': "Tool to exploit the network and gathering information with nmap help.",
            'aliases': ["dracnmap", "dracnmap"],
        },
        {
            'name': 'dumb0',
            'description': "A simple tool to dump users in popular forums and CMS.",
            'aliases': ["dumb0", "dumb0"],
        },
        {
            'name': 'easy-creds',
            'description': "A bash script that leverages ettercap and other tools to obtain credentials.",
            'aliases': ["easy-creds", "easy creds"],
        },
        {
            'name': 'easyda',
            'description': "Easy Windows Domain Access Script.",
            'aliases': ["easyda", "easyda"],
        },
        {
            'name': 'emp3r0r',
            'description': "Linux post-exploitation framework made by linux user.",
            'aliases': ["emp3r0r", "emp3r0r"],
        },
        {
            'name': 'empire',
            'description': "A PowerShell and Python post-exploitation agent.",
            'aliases': ["empire", "powershell empire"],
        },
        {
            'name': 'findsploit',
            'description': "Find exploits in local and online databases instantly.",
            'aliases': ["findsploit", "findsploit"],
        },
        {
            'name': 'fstealer',
            'description': "Automates file system mirroring through remote file disclosure vulnerabilities on Linux machines.",
            'aliases': ["fstealer", "fstealer"],
        },
        {
            'name': 'glue',
            'description': "A framework for running a series of tools.",
            'aliases': ["glue", "glue"],
        },
        {
            'name': 'go-exploitdb',
            'description': "Tool for searching Exploits from Exploit Databases, etc.",
            'aliases': ["go-exploitdb", "go exploitdb"],
        },
        {
            'name': 'google-explorer',
            'description': "Google mass exploit robot - Make a google search, and parse the results for a especific exploit you define.",
            'aliases': ["google-explorer", "google explorer"],
        },
        {
            'name': 'gooscan',
            'description': "A tool that automates queries against Google search appliances, but with a twist.",
            'aliases': ["gooscan", "gooscan"],
        },
        {
            'name': 'hackersh',
            'description': "A shell for with Pythonect-like syntax, including wrappers for commonly used security tools.",
            'aliases': ["hackersh", "hackersh"],
        },
        {
            'name': 'harpoon',
            'description': "CLI tool for open source and threat intelligence.",
            'aliases': ["harpoon", "harpoon"],
        },
        {
            'name': 'hate-crack',
            'description': "A tool for automating cracking methodologies through Hashcat.",
            'aliases': ["hate-crack", "hate crack"],
        },
        {
            'name': 'havoc-c2',
            'description': "Modern and malleable post-exploitation command and control framework.",
            'aliases': ["havoc-c2", "havoc c2"],
        },
        {
            'name': 'intersect',
            'description': "Post-exploitation framework.",
            'aliases': ["intersect", "intersect"],
        },
        {
            'name': 'invoke-cradlecrafter',
            'description': "PowerShell Remote Download Cradle Generator & Obfuscator.",
            'aliases': ["invoke-cradlecrafter", "invoke cradlecrafter"],
        },
        {
            'name': 'invoke-dosfuscation',
            'description': "Cmd.exe Command Obfuscation Generator & Detection Test Harness.",
            'aliases': ["invoke-dosfuscation", "invoke dosfuscation"],
        },
        {
            'name': 'invoke-obfuscation',
            'description': "PowerShell Obfuscator.",
            'aliases': ["invoke-obfuscation", "invoke obfuscation"],
        },
        {
            'name': 'koadic',
            'description': "A Windows post-exploitation rootkit similar to other penetration testing tools such as Meterpreter and Powershell Empire.",
            'aliases': ["koadic", "koadic c2"],
        },
        {
            'name': 'ldapscripts',
            'description': "Simple shell scripts to handle POSIX entries in an LDAP directory.",
            'aliases': ["ldapscripts", "ldapscripts"],
        },
        {
            'name': 'linikatz',
            'description': "Tool to attack AD on UNIX.",
            'aliases': ["linikatz", "linikatz"],
        },
        {
            'name': 'linset',
            'description': "Evil Twin Attack Bash script - An automated WPA/WPA2 hacker.",
            'aliases': ["linset", "linset"],
        },
        {
            'name': 'lyricpass',
            'description': "Tool to generate wordlists based on lyrics.",
            'aliases': ["lyricpass", "lyricpass"],
        },
        {
            'name': 'maskprocessor',
            'description': "A High-Performance word generator with a per-position configurable charset.",
            'aliases': ["maskprocessor", "maskprocessor"],
        },
        {
            'name': 'masscan-automation',
            'description': "Masscan integrated with Shodan API.",
            'aliases': ["masscan-automation", "masscan automation"],
        },
        {
            'name': 'massexpconsole',
            'description': "A collection of tools and exploits with a cli ui for mass exploitation.",
            'aliases': ["massexpconsole", "massexpconsole"],
        },
        {
            'name': 'mentalist',
            'description': "Graphical tool for custom wordlist generation.",
            'aliases': ["mentalist", "mentalist"],
        },
        {
            'name': 'merlin-server',
            'description': "Merlin is a cross-platform post-exploitation HTTP/2 Command & Control server and agent written in golang.",
            'aliases': ["merlin-server", "merlin server"],
        },
        {
            'name': 'metasploit-autopwn',
            'description': "db_autopwn plugin of metasploit.",
            'aliases': ["metasploit-autopwn", "metasploit autopwn"],
        },
        {
            'name': 'mitmap-old',
            'description': "Shell Script for launching a Fake AP with karma functionality and launches ettercap for packet capture and traffic manipulation.",
            'aliases': ["mitmap-old", "mitmap old"],
        },
        {
            'name': 'msf-mpc',
            'description': "Msfvenom payload creator.",
            'aliases': ["msf-mpc", "msf mpc"],
        },
        {
            'name': 'msfenum',
            'description': "A Metasploit auto auxiliary script.",
            'aliases': ["msfenum", "msfenum"],
        },
        {
            'name': 'mutator',
            'description': "This project aims to be a wordlist mutator with hormones, which means that some mutations will be applied to the result of the ones that have been already done, resulting in something like: corporation -> C0rp0r4t10n_2012",
            'aliases': ["mutator", "mutator"],
        },
        {
            'name': 'nettacker',
            'description': "Automated Penetration Testing Framework.",
            'aliases': ["nettacker", "nettacker"],
        },
        {
            'name': 'nfspy',
            'description': "A Python library for automating the falsification of NFS credentials when mounting an NFS share.",
            'aliases': ["nfspy", "nfspy"],
        },
        {
            'name': 'nfsshell',
            'description': "Userland NFS command tool.",
            'aliases': ["nfsshell", "nfsshell"],
        },
        {
            'name': 'nosqlattack',
            'description': "Python tool to automate exploit MongoDB server IP on Internet anddisclose the database data by MongoDB default configuration weaknesses and injection attacks.",
            'aliases': ["nosqlattack", "nosqlattack"],
        },
        {
            'name': 'nullscan',
            'description': "A modular framework designed to chain and automate security tests.",
            'aliases': ["nullscan", "nullscan"],
        },
        {
            'name': 'octopwnweb',
            'description': "Internal pentest framework running in your browser via WebAssembly, powerd by Pyodide",
            'aliases': ["octopwnweb", "octopwnweb"],
        },
        {
            'name': 'openscap',
            'description': "Open Source Security Compliance Solution.",
            'aliases': ["openscap", "openscap"],
        },
        {
            'name': 'panoptic',
            'description': "A tool that automates the process of search and retrieval of content for common log and config files through LFI vulnerability.",
            'aliases': ["panoptic", "panoptic"],
        },
        {
            'name': 'pastejacker',
            'description': "Hacking systems with the automation of PasteJacking attacks.",
            'aliases': ["pastejacker", "pastejacker"],
        },
        {
            'name': 'pasv-agrsv',
            'description': "Passive recon / OSINT automation script.",
            'aliases': ["pasv-agrsv", "pasv agrsv"],
        },
        {
            'name': 'penbox',
            'description': "A Penetration Testing Framework - The Tool With All The Tools.",
            'aliases': ["penbox", "penbox"],
        },
        {
            'name': 'pentestgpt',
            'description': "A penetration testing tool empowered by ChatGPT. It is designed to automate the penetration testing process.",
            'aliases': ["pentestgpt", "pentestgpt"],
        },
        {
            'name': 'pentmenu',
            'description': "A bash script for recon and DOS attacks.",
            'aliases': ["pentmenu", "pentmenu"],
        },
        {
            'name': 'pin',
            'description': "A dynamic binary instrumentation tool.",
            'aliases': ["pin", "pin"],
        },
        {
            'name': 'portia',
            'description': "Automate a number of techniques commonly performed on internal network penetration tests after a low privileged account has been compromised.",
            'aliases': ["portia", "portia"],
        },
        {
            'name': 'pupy',
            'description': "Opensource, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool mainly written in python.",
            'aliases': ["pupy", "pupy"],
        },
        {
            'name': 'pureblood',
            'description': "A Penetration Testing Framework created for Hackers / Pentester / Bug Hunter.",
            'aliases': ["pureblood", "pureblood"],
        },
        {
            'name': 'pyfuscation',
            'description': "Obfuscate powershell scripts by replacing Function names, Variables and Parameters.",
            'aliases': ["pyfuscation", "pyfuscation"],
        },
        {
            'name': 'recomposer',
            'description': "Randomly changes Win32/64 PE Files for \'safer\' uploading to malware and sandbox sites.",
            'aliases': ["recomposer", "recomposer"],
        },
        {
            'name': 'rhodiola',
            'description': "Personalized wordlist generator with NLP, by analyzing tweets (A.K.A crunch2049).",
            'aliases': ["rhodiola", "rhodiola"],
        },
        {
            'name': 'rsmangler',
            'description': "rsmangler takes a wordlist and mangle it",
            'aliases': ["rsmangler", "rsmangler"],
        },
        {
            'name': 'sakis3g',
            'description': "An all-in-one script for connecting with 3G.",
            'aliases': ["sakis3g", "sakis3g"],
        },
        {
            'name': 'scap-security-guide',
            'description': "Security compliance content in SCAP, Bash, Ansible, and other formats.",
            'aliases': ["scap-security-guide", "scap security guide"],
        },
        {
            'name': 'scap-workbench',
            'description': "SCAP Scanner And Tailoring Graphical User Interface.",
            'aliases': ["scap-workbench", "scap workbench"],
        },
        {
            'name': 'search1337',
            'description': "1337Day Online Exploit Scanner.",
            'aliases': ["search1337", "search1337"],
        },
        {
            'name': 'shellerator',
            'description': "Simple command-line tool aimed to help pentesters quickly generate one-liner reverse/bind shells in multiple languages.",
            'aliases': ["shellerator", "shellerator"],
        },
        {
            'name': 'shellpop',
            'description': "Generate easy and sophisticated reverse or bind shell commands.",
            'aliases': ["shellpop", "shellpop"],
        },
        {
            'name': 'shellz',
            'description': "A script for generating common revshells fast and easy.",
            'aliases': ["shellz", "shellz"],
        },
        {
            'name': 'simple-ducky',
            'description': "A payload generator.",
            'aliases': ["simple-ducky", "simple ducky"],
        },
        {
            'name': 'sipvicious',
            'description': "Tools for auditing SIP devices.",
            'aliases': ["sipvicious", "sipvicious"],
        },
        {
            'name': 'sn00p',
            'description': "A modular tool written in bourne shell and designed to chain and automate security tools and tests.",
            'aliases': ["sn00p", "sn00p"],
        },
        {
            'name': 'sn1per',
            'description': "Automated Pentest Recon Scanner.",
            'aliases': ["sn1per", "sn1per"],
        },
        {
            'name': 'sploitctl',
            'description': "Fetch, install and search exploit archives from exploit sites like exploit-db and packetstorm.",
            'aliases': ["sploitctl", "sploitctl"],
        },
        {
            'name': 'spookflare',
            'description': "Loader, dropper generator with multiple features for bypassing client-side and network-side countermeasures.",
            'aliases': ["spookflare", "spookflare"],
        },
        {
            'name': 'statsprocessor',
            'description': "A high-performance word-generator based on per-position Markov-attack.",
            'aliases': ["statsprocessor", "statsprocessor"],
        },
        {
            'name': 'thefatrat',
            'description': "TheFatRat a massive exploiting tool: easy tool to generate backdoor and easy tool to post exploitation attack.",
            'aliases': ["thefatrat", "thefatrat"],
        },
        {
            'name': 'tiger',
            'description': "A security scanner, that checks computer for known problems. Can also use tripwire, aide and chkrootkit.",
            'aliases': ["tiger", "tiger"],
        },
        {
            'name': 'tlssled',
            'description': "A Linux shell script whose purpose is to evaluate the security of a target SSL/TLS (HTTPS) web server implementation.",
            'aliases': ["tlssled", "tlssled"],
        },
        {
            'name': 'torctl',
            'description': "Script to redirect all traffic through tor network including dns queries for anonymizing entire system.",
            'aliases': ["torctl", "torctl"],
        },
        {
            'name': 'ttpassgen',
            'description': "Highly flexible and scriptable password dictionary generator based on Python.",
            'aliases': ["ttpassgen", "ttpassgen"],
        },
        {
            'name': 'unix-privesc-check',
            'description': "Tries to find misconfigurations that could allow local unprivilged users to escalate privileges to other users or to access local apps (e.g. databases).",
            'aliases': ["unix-privesc-check", "unix privesc check"],
        },
        {
            'name': 'username-anarchy',
            'description': "Tools for generating usernames when penetration testing.",
            'aliases': ["username-anarchy", "username anarchy"],
        },
        {
            'name': 'valhalla-api',
            'description': "Valhalla API Client.",
            'aliases': ["valhalla-api", "valhalla api"],
        },
        {
            'name': 'veil',
            'description': "A tool designed to generate metasploit payloads that bypass common anti-virus solutions.",
            'aliases': ["veil", "veil evasion", "veil framework"],
        },
        {
            'name': 'vlan-hopping',
            'description': "Easy 802.1Q VLAN Hopping",
            'aliases': ["vlan-hopping", "vlan hopping"],
        },
        {
            'name': 'voiphopper',
            'description': "A security validation tool that tests to see if a PC can mimic the behavior of an IP Phone. It rapidly automates a VLAN Hop into the Voice VLAN.",
            'aliases': ["voiphopper", "voip hopper"],
        },
        {
            'name': 'wifi-autopwner',
            'description': "Script to automate searching and auditing Wi-Fi networks with weak security.",
            'aliases': ["wifi-autopwner", "wifi autopwner"],
        },
        {
            'name': 'wikigen',
            'description': "A script to generate wordlists out of wikipedia pages.",
            'aliases': ["wikigen", "wikigen"],
        },
        {
            'name': 'wmd',
            'description': "Python framework for IT security tools.",
            'aliases': ["wmd", "wmd"],
        },
        {
            'name': 'wnmap',
            'description': "A shell script written with the purpose to automate and chain scans via nmap.",
            'aliases': ["wnmap", "wnmap"],
        },
    ],

    # Fuzzer (84 tools)
    'blackarch-fuzzer': [
        {
            'name': 'ajpfuzzer',
            'description': "A command-line fuzzer for the Apache JServ Protocol (ajp13).",
            'aliases': ["ajpfuzzer", "ajpfuzzer"],
        },
        {
            'name': 'backfuzz',
            'description': "A network protocol fuzzing toolkit.",
            'aliases': ["backfuzz", "backfuzz"],
        },
        {
            'name': 'bfuzz',
            'description': "Input based fuzzer tool for browsers.",
            'aliases': ["bfuzz", "bfuzz"],
        },
        {
            'name': 'brainstorm',
            'description': "A smarter web fuzzing tool that combines local LLM models and ffuf to optimize directory and file discovery.",
            'aliases': ["brainstorm", "brainstorm"],
        },
        {
            'name': 'browser-fuzzer',
            'description': "Browser Fuzzer 3",
            'aliases': ["browser-fuzzer", "browser fuzzer"],
        },
        {
            'name': 'bunny',
            'description': "A closed loop, high-performance, general purpose protocol-blind fuzzer for C programs.",
            'aliases': ["bunny", "bunny"],
        },
        {
            'name': 'choronzon',
            'description': "An evolutionary knowledge-based fuzzer.",
            'aliases': ["choronzon", "choronzon"],
        },
        {
            'name': 'cirt-fuzzer',
            'description': "A simple TCP/UDP protocol fuzzer.",
            'aliases': ["cirt-fuzzer", "cirt fuzzer"],
        },
        {
            'name': 'conscan',
            'description': "A blackbox vulnerability scanner for the Concre5 CMS.",
            'aliases': ["conscan", "conscan"],
        },
        {
            'name': 'cookie-cadger',
            'description': "An auditing tool for Wi-Fi or wired Ethernet connections.",
            'aliases': ["cookie-cadger", "cookie cadger"],
        },
        {
            'name': 'crlf-injector',
            'description': "A python script for testing CRLF injecting issues.",
            'aliases': ["crlf-injector", "crlf injector"],
        },
        {
            'name': 'dharma',
            'description': "Generation-based, context-free grammar fuzzer.",
            'aliases': ["dharma", "dharma"],
        },
        {
            'name': 'dizzy',
            'description': "A Python based fuzzing framework with many features.",
            'aliases': ["dizzy", "dizzy"],
        },
        {
            'name': 'domato',
            'description': "DOM fuzzer.",
            'aliases': ["domato", "domato"],
        },
        {
            'name': 'doona',
            'description': "A fork of the Bruteforce Exploit Detector Tool (BED).",
            'aliases': ["doona", "doona"],
        },
        {
            'name': 'easyfuzzer',
            'description': "A flexible fuzzer, not only for web, has a CSV output for efficient output analysis (platform independent).",
            'aliases': ["easyfuzzer", "easyfuzzer"],
        },
        {
            'name': 'firewalk',
            'description': "An active reconnaissance network security tool.",
            'aliases': ["firewalk", "firewalk"],
        },
        {
            'name': 'flyr',
            'description': "Block-based software vulnerability fuzzing framework.",
            'aliases': ["flyr", "flyr"],
        },
        {
            'name': 'frisbeelite',
            'description': "A GUI-based USB device fuzzer.",
            'aliases': ["frisbeelite", "frisbeelite"],
        },
        {
            'name': 'ftester',
            'description': "A tool designed for testing firewall filtering policies and Intrusion Detection System (IDS) capabilities.",
            'aliases': ["ftester", "ftester"],
        },
        {
            'name': 'ftp-fuzz',
            'description': "The master of all master fuzzing scripts specifically targeted towards FTP server software.",
            'aliases': ["ftp-fuzz", "ftp fuzz"],
        },
        {
            'name': 'fuddly',
            'description': "Fuzzing and Data Manipulation Framework (for GNU/Linux).",
            'aliases': ["fuddly", "fuddly"],
        },
        {
            'name': 'fusil',
            'description': "A Python library used to write fuzzing programs.",
            'aliases': ["fusil", "fusil"],
        },
        {
            'name': 'fuzzball2',
            'description': "A fuzzer for TCP and IP protocol options. It sends a bunch of more or less bogus packets to the target.",
            'aliases': ["fuzzball2", "fuzzball2"],
        },
        {
            'name': 'fuzzdb',
            'description': "Attack and Discovery Pattern Dictionary for Application Fault Injection Testing.",
            'aliases': ["fuzzdb", "fuzzdb"],
        },
        {
            'name': 'fuzzdiff',
            'description': "A simple tool designed to help out with crash analysis during fuzz testing. It selectively \'un-fuzzes\' portions of a fuzzed file that is known to cause a crash, re-launches the targeted application, and sees if it still crashes.",
            'aliases': ["fuzzdiff", "fuzzdiff"],
        },
        {
            'name': 'fuzzowski',
            'description': "A Network Protocol Fuzzer made by NCCGroup based on Sulley and BooFuzz.",
            'aliases': ["fuzzowski", "fuzzowski"],
        },
        {
            'name': 'goofuzz',
            'description': "A Bash script that uses advanced Google search techniques to obtain sensitive information in files or directories without making requests to the web server.",
            'aliases': ["goofuzz", "goofuzz"],
        },
        {
            'name': 'grammarinator',
            'description': "A random test generator / fuzzer that creates test cases according to an input ANTLR v4 grammar.",
            'aliases': ["grammarinator", "grammarinator"],
        },
        {
            'name': 'grr',
            'description': "High-throughput fuzzer and emulator of DECREE binaries.",
            'aliases': ["grr", "grr"],
        },
        {
            'name': 'hexorbase',
            'description': "A database application designed for administering and auditing multiple database servers simultaneously from a centralized location. It is capable of performing SQL queries and bruteforce attacks against common database servers (MySQL, SQLite, Microsoft SQL Server, Oracle, PostgreSQL).",
            'aliases': ["hexorbase", "hexorbase"],
        },
        {
            'name': 'hodor',
            'description': "A general-use fuzzer that can be configured to use known-good input and delimiters in order to fuzz specific locations.",
            'aliases': ["hodor", "hodor"],
        },
        {
            'name': 'honggfuzz',
            'description': "A general-purpose fuzzer with simple, command-line interface.",
            'aliases': ["honggfuzz", "honggfuzz"],
        },
        {
            'name': 'http-fuzz',
            'description': "A simple http fuzzer.",
            'aliases': ["http-fuzz", "http fuzz"],
        },
        {
            'name': 'ifuzz',
            'description': "A binary file fuzzer with several options.",
            'aliases': ["ifuzz", "ifuzz"],
        },
        {
            'name': 'ikeprober',
            'description': "Tool crafting IKE initiator packets and allowing many options to be manually set. Useful to find overflows, error conditions and identifiyng vendors",
            'aliases': ["ikeprober", "ikeprober"],
        },
        {
            'name': 'jbrofuzz',
            'description': "Web application protocol fuzzer that emerged from the needs of penetration testing.",
            'aliases': ["jbrofuzz", "jbrofuzz"],
        },
        {
            'name': 'kitty-framework',
            'description': "Fuzzing framework written in python.",
            'aliases': ["kitty-framework", "kitty framework"],
        },
        {
            'name': 'malybuzz',
            'description': "A Python tool focused in discovering programming faults in network software.",
            'aliases': ["malybuzz", "malybuzz"],
        },
        {
            'name': 'manul',
            'description': "A coverage-guided parallel fuzzer for open-source and blackbox binaries on Windows, Linux and MacOS.",
            'aliases': ["manul", "manul"],
        },
        {
            'name': 'melkor',
            'description': "An ELF fuzzer that mutates the existing data in an ELF sample given to create orcs (malformed ELFs), however, it does not change values randomly (dumb fuzzing), instead, it fuzzes certain metadata with semi-valid values through the use of fuzzing rules (knowledge base).",
            'aliases': ["melkor", "melkor"],
        },
        {
            'name': 'notspikefile',
            'description': "A Linux based file format fuzzing tool",
            'aliases': ["notspikefile", "notspikefile"],
        },
        {
            'name': 'oat',
            'description': "A toolkit that could be used to audit security within Oracle database servers.",
            'aliases': ["oat", "oat"],
        },
        {
            'name': 'ohrwurm',
            'description': "A small and simple RTP fuzzer.",
            'aliases': ["ohrwurm", "ohrwurm"],
        },
        {
            'name': 'oscanner',
            'description': "An Oracle assessment framework developed in Java.",
            'aliases': ["oscanner", "oracle scanner"],
        },
        {
            'name': 'peach',
            'description': "A SmartFuzzer that is capable of performing both generation and mutation based fuzzing.",
            'aliases': ["peach", "peach"],
        },
        {
            'name': 'peach-fuzz',
            'description': "Simple vulnerability scanning framework.",
            'aliases': ["peach-fuzz", "peach fuzz"],
        },
        {
            'name': 'pentbox',
            'description': "A security suite that packs security and stability testing oriented tools for networks and systems.",
            'aliases': ["pentbox", "pentbox"],
        },
        {
            'name': 'portmanteau',
            'description': "An experimental unix driver IOCTL security tool that is useful for fuzzing and discovering device driver attack surface.",
            'aliases': ["portmanteau", "portmanteau"],
        },
        {
            'name': 'powerfuzzer',
            'description': "Powerfuzzer is a highly automated web fuzzer based on many other Open Source fuzzers available (incl. cfuzzer, fuzzled, fuzzer.pl, jbrofuzz, webscarab, wapiti, Socket Fuzzer). It can detect XSS, Injections (SQL, LDAP, commands, code, XPATH) and others.",
            'aliases': ["powerfuzzer", "powerfuzzer"],
        },
        {
            'name': 'profuzz',
            'description': "Simple PROFINET fuzzer based on Scapy.",
            'aliases': ["profuzz", "profuzz"],
        },
        {
            'name': 'pulsar',
            'description': "Protocol Learning and Stateful Fuzzing.",
            'aliases': ["pulsar", "pulsar"],
        },
        {
            'name': 'pyjfuzz',
            'description': "Python JSON Fuzzer.",
            'aliases': ["pyjfuzz", "pyjfuzz"],
        },
        {
            'name': 'ratproxy',
            'description': "A passive web application security assessment tool",
            'aliases': ["ratproxy", "ratproxy"],
        },
        {
            'name': 's3-fuzzer',
            'description': "A concurrent, command-line AWS S3 Fuzzer.",
            'aliases': ["s3-fuzzer", "s3 fuzzer"],
        },
        {
            'name': 'samesame',
            'description': "Command line tool to generate crafty homograph strings.",
            'aliases': ["samesame", "samesame"],
        },
        {
            'name': 'sandsifter',
            'description': "The x86 processor fuzzer.",
            'aliases': ["sandsifter", "sandsifter"],
        },
        {
            'name': 'sfuzz',
            'description': "A simple fuzzer.",
            'aliases': ["sfuzz", "sfuzz"],
        },
        {
            'name': 'sharpfuzz',
            'description': "AFL-based fuzz testing for .NET.",
            'aliases': ["sharpfuzz", "sharpfuzz"],
        },
        {
            'name': 'sloth-fuzzer',
            'description': "A smart file fuzzer.",
            'aliases': ["sloth-fuzzer", "sloth fuzzer"],
        },
        {
            'name': 'smtp-fuzz',
            'description': "Simple smtp fuzzer.",
            'aliases': ["smtp-fuzz", "smtp fuzz"],
        },
        {
            'name': 'snmp-fuzzer',
            'description': "SNMP fuzzer uses Protos test cases with an entirely new engine written in Perl.",
            'aliases': ["snmp-fuzzer", "snmp fuzzer"],
        },
        {
            'name': 'socketfuzz',
            'description': "Simple socket fuzzer.",
            'aliases': ["socketfuzz", "socketfuzz"],
        },
        {
            'name': 'spiderpig-pdffuzzer',
            'description': "A javascript pdf fuzzer.",
            'aliases': ["spiderpig-pdffuzzer", "spiderpig pdffuzzer"],
        },
        {
            'name': 'spike-fuzzer',
            'description': "IMMUNITYsec\'s fuzzer creation kit in C.",
            'aliases': ["spike-fuzzer", "spike fuzzer"],
        },
        {
            'name': 'sploitego',
            'description': "Maltego Penetration Testing Transforms.",
            'aliases': ["sploitego", "sploitego"],
        },
        {
            'name': 'sqlbrute',
            'description': "Brute forces data out of databases using blind SQL injection.",
            'aliases': ["sqlbrute", "sqlbrute"],
        },
        {
            'name': 'sshfuzz',
            'description': "A SSH Fuzzing utility written in Perl that uses Net::SSH2.",
            'aliases': ["sshfuzz", "sshfuzz"],
        },
        {
            'name': 'sulley',
            'description': "A pure-python fully automated and unattended fuzzing framework.",
            'aliases': ["sulley", "sulley"],
        },
        {
            'name': 'taof',
            'description': "A GUI cross-platform Python generic network protocol fuzzer.",
            'aliases': ["taof", "taof"],
        },
        {
            'name': 'tcpcontrol-fuzzer',
            'description': "2^6 TCP control bit fuzzer (no ECN or CWR).",
            'aliases': ["tcpcontrol-fuzzer", "tcpcontrol fuzzer"],
        },
        {
            'name': 'termineter',
            'description': "Smart meter testing framework.",
            'aliases': ["termineter", "smart meter"],
        },
        {
            'name': 'tftp-fuzz',
            'description': "Master TFTP fuzzing script as part of the ftools series of fuzzers.",
            'aliases': ["tftp-fuzz", "tftp fuzz"],
        },
        {
            'name': 'thefuzz',
            'description': "CLI fuzzing tool.",
            'aliases': ["thefuzz", "thefuzz"],
        },
        {
            'name': 'trinity',
            'description': "A Linux System call fuzzer.",
            'aliases': ["trinity", "trinity"],
        },
        {
            'name': 'uff',
            'description': "Unleashed ffuf. A fork of ffuf with more functions & a modified HTTP stack.",
            'aliases': ["uff", "uff"],
        },
        {
            'name': 'unifuzzer',
            'description': "A fuzzing tool for closed-source binaries based on Unicorn and LibFuzzer.",
            'aliases': ["unifuzzer", "unifuzzer"],
        },
        {
            'name': 'uniofuzz',
            'description': "The universal fuzzing tool for browsers, web services, files, programs and network services/ports",
            'aliases': ["uniofuzz", "uniofuzz"],
        },
        {
            'name': 'uniscan',
            'description': "A simple Remote File Include, Local File Include and Remote Command Execution vulnerability scanner.",
            'aliases': ["uniscan", "uniscan"],
        },
        {
            'name': 'w3af',
            'description': "Web Application Attack and Audit Framework.",
            'aliases': ["w3af", "w3af"],
        },
        {
            'name': 'webscarab',
            'description': "Framework for analysing applications that communicate using the HTTP and HTTPS protocols",
            'aliases': ["webscarab", "webscarab"],
        },
        {
            'name': 'webshag',
            'description': "A multi-threaded, multi-platform web server audit tool.",
            'aliases': ["webshag", "webshag"],
        },
        {
            'name': 'wfuzz',
            'description': "Utility to bruteforce web applications to find their not linked resources.",
            'aliases': ["wfuzz", "w fuzz"],
        },
        {
            'name': 'wsfuzzer',
            'description': "A Python tool written to automate SOAP pentesting of web services.",
            'aliases': ["wsfuzzer", "wsfuzzer"],
        },
    ],

    # Cryptography (80 tools)
    'blackarch-crypto': [
        {
            'name': 'aespipe',
            'description': "Reads data from stdin and outputs encrypted or decrypted results to stdout.",
            'aliases': ["aespipe", "aespipe"],
        },
        {
            'name': 'auto-xor-decryptor',
            'description': "Automatic XOR decryptor tool.",
            'aliases': ["auto-xor-decryptor", "auto xor decryptor"],
        },
        {
            'name': 'bletchley',
            'description': "A collection of practical application cryptanalysis tools.",
            'aliases': ["bletchley", "bletchley"],
        },
        {
            'name': 'c7decrypt',
            'description': "Cisco password type encryptor and decryptor.",
            'aliases': ["c7decrypt", "c7decrypt"],
        },
        {
            'name': 'ciphertest',
            'description': "A better SSL cipher checker using gnutls.",
            'aliases': ["ciphertest", "ciphertest"],
        },
        {
            'name': 'ciphr',
            'description': "A CLI tool for encoding, decoding, encryption, decryption, and hashing streams of data.",
            'aliases': ["ciphr", "ciphr"],
        },
        {
            'name': 'codetective',
            'description': "A tool to determine the crypto/encoding algorithm used according to traces of its representation.",
            'aliases': ["codetective", "codetective"],
        },
        {
            'name': 'cribdrag',
            'description': "An interactive crib dragging tool for cryptanalysis on ciphertext generated with reused or predictable stream cipher keys.",
            'aliases': ["cribdrag", "cribdrag"],
        },
        {
            'name': 'crypthook',
            'description': "TCP/UDP symmetric encryption tunnel wrapper.",
            'aliases': ["crypthook", "crypthook"],
        },
        {
            'name': 'cryptonark',
            'description': "SSL security checker.",
            'aliases': ["cryptonark", "cryptonark"],
        },
        {
            'name': 'dagon',
            'description': "Advanced Hash Manipulation.",
            'aliases': ["dagon", "dagon"],
        },
        {
            'name': 'daredevil',
            'description': "A tool to perform (higher-order) correlation power analysis attacks (CPA).",
            'aliases': ["daredevil", "daredevil"],
        },
        {
            'name': 'decodify',
            'description': "Tool that can detect and decode encoded strings, recursively.",
            'aliases': ["decodify", "decodify"],
        },
        {
            'name': 'deen',
            'description': "Generic data encoding/decoding application built with PyQt5.",
            'aliases': ["deen", "deen"],
        },
        {
            'name': 'demiguise',
            'description': "HTA encryption tool for RedTeams.",
            'aliases': ["demiguise", "demiguise"],
        },
        {
            'name': 'dislocker',
            'description': "Read BitLocker encrypted volumes under Linux.",
            'aliases': ["dislocker", "dislocker"],
        },
        {
            'name': 'factordb-pycli',
            'description': "CLI for factordb and Python API Client.",
            'aliases': ["factordb-pycli", "factordb pycli"],
        },
        {
            'name': 'featherduster',
            'description': "An automated, modular cryptanalysis tool.",
            'aliases': ["featherduster", "featherduster"],
        },
        {
            'name': 'findmyhash',
            'description': "Crack different types of hashes using free online services.",
            'aliases': ["findmyhash", "findmyhash"],
        },
        {
            'name': 'foresight',
            'description': "A tool for predicting the output of random number generators.",
            'aliases': ["foresight", "foresight"],
        },
        {
            'name': 'gcrypt',
            'description': "Simple, secure and performance file encryption tool written in C",
            'aliases': ["gcrypt", "gcrypt"],
        },
        {
            'name': 'gdir.pl',
            'description': "Perl wrapper on gcrypt for directory encryption/decryption.",
            'aliases': ["gdir.pl", "gdir.pl"],
        },
        {
            'name': 'gpp-decrypt',
            'description': "Parse the Group Policy Preferences XML file which extracts the username and decrypts the cpassword attribute.",
            'aliases': ["gpp-decrypt", "gpp decrypt", "grouppolicy decrypt"],
        },
        {
            'name': 'haiti',
            'description': "Hash type identifier (CLI & lib).",
            'aliases': ["haiti", "haiti"],
        },
        {
            'name': 'hash-buster',
            'description': "A python script which scraps online hash crackers to find cleartext of a hash.",
            'aliases': ["hash-buster", "hash buster"],
        },
        {
            'name': 'hash-extender',
            'description': "A hash length extension attack tool.",
            'aliases': ["hash-extender", "hash extender"],
        },
        {
            'name': 'hash-identifier',
            'description': "Software to identify the different types of hashes used to encrypt data and especially passwords.",
            'aliases': ["hash-identifier", "hash identifier"],
        },
        {
            'name': 'hashcheck',
            'description': "Search for leaked passwords while maintaining a high level of privacy using the k-anonymity method.",
            'aliases': ["hashcheck", "hashcheck"],
        },
        {
            'name': 'hashdb',
            'description': "A block hash toolkit.",
            'aliases': ["hashdb", "hashdb"],
        },
        {
            'name': 'hashdeep',
            'description': "Cross-platform tools to message digests for any number of files.",
            'aliases': ["hashdeep", "hashdeep"],
        },
        {
            'name': 'hashfind',
            'description': "A tool to search files for matching password hash types and other interesting data.",
            'aliases': ["hashfind", "hashfind"],
        },
        {
            'name': 'hashid',
            'description': "Software to identify the different types of hashes used to encrypt data.",
            'aliases': ["hashid", "hashid"],
        },
        {
            'name': 'hashpeek',
            'description': "A fast Go-based CLI tool to identify, extract, and classify hash types from structured data/files with JSON/CSV output and Hashcat/John formatting details (a hash identifier).",
            'aliases': ["hashpeek", "hashpeek"],
        },
        {
            'name': 'hashpump',
            'description': "A tool to exploit the hash length extension attack in various hashing algorithms.",
            'aliases': ["hashpump", "hashpump"],
        },
        {
            'name': 'hashrat',
            'description': "Hashing tool supporting MD5, SHA1, SHA256, SHA512, Whirlpool, JH and their HMAC.",
            'aliases': ["hashrat", "hashrat"],
        },
        {
            'name': 'hdcp-genkey',
            'description': "Generate HDCP source and sink keys from the leaked master key.",
            'aliases': ["hdcp-genkey", "hdcp genkey"],
        },
        {
            'name': 'hlextend',
            'description': "Pure Python hash length extension module.",
            'aliases': ["hlextend", "hlextend"],
        },
        {
            'name': 'ja3',
            'description': "Standard for creating SSL client fingerprints in an easy to produce and shareable way.",
            'aliases': ["ja3", "ja3"],
        },
        {
            'name': 'jwt-key-recovery',
            'description': "Recovers the public key used to sign JWT tokens.",
            'aliases': ["jwt-key-recovery", "jwt key recovery"],
        },
        {
            'name': 'kh2hc',
            'description': "Convert OpenSSH known_hosts file hashed with HashKnownHosts to hashes crackable by Hashcat.",
            'aliases': ["kh2hc", "kh2hc"],
        },
        {
            'name': 'kraken',
            'description': "A project to encrypt A5/1 GSM signaling using a Time/Memory Tradeoff Attack.",
            'aliases': ["kraken", "kraken"],
        },
        {
            'name': 'libbde',
            'description': "A library to access the BitLocker Drive Encryption (BDE) format.",
            'aliases': ["libbde", "libbde"],
        },
        {
            'name': 'luksipc',
            'description': "A tool to convert unencrypted block devices to encrypted LUKS devices in-place.",
            'aliases': ["luksipc", "luksipc"],
        },
        {
            'name': 'morxkeyfmt',
            'description': "Read a private key from stdin and output formatted data values.",
            'aliases': ["morxkeyfmt", "morxkeyfmt"],
        },
        {
            'name': 'nomorexor',
            'description': "Tool to help guess a files 256 byte XOR key by using frequency analysis.",
            'aliases': ["nomorexor", "nomorexor"],
        },
        {
            'name': 'ntlmv1-multi',
            'description': "NTLMv1 Multitool.",
            'aliases': ["ntlmv1-multi", "ntlmv1 multi"],
        },
        {
            'name': 'omnihash',
            'description': "Hash files, strings, input streams and network resources in various common algorithms simultaneously.",
            'aliases': ["omnihash", "omnihash"],
        },
        {
            'name': 'openstego',
            'description': "A tool implemented in Java for generic steganography, with support for password-based encryption of the data.",
            'aliases': ["openstego", "openstego"],
        },
        {
            'name': 'outguess',
            'description': "A universal steganographic tool.",
            'aliases': ["outguess", "outguess"],
        },
        {
            'name': 'pacumen',
            'description': "Packet Acumen - Analyse encrypted network traffic and more (side-channel attacks).",
            'aliases': ["pacumen", "pacumen"],
        },
        {
            'name': 'padbuster',
            'description': "Automated script for performing Padding Oracle attacks.",
            'aliases': ["padbuster", "padbuster"],
        },
        {
            'name': 'padoracle',
            'description': "Padding Oracle Attack with Node.js.",
            'aliases': ["padoracle", "padoracle"],
        },
        {
            'name': 'padre',
            'description': "Padding Oracle attack tool.",
            'aliases': ["padre", "padre"],
        },
        {
            'name': 'pax-oracle',
            'description': "CLI tool for PKCS7 padding oracle attacks.",
            'aliases': ["pax-oracle", "pax oracle"],
        },
        {
            'name': 'pip3line',
            'description': "The Swiss army knife of byte manipulation.",
            'aliases': ["pip3line", "pip3line"],
        },
        {
            'name': 'poracle',
            'description': "A tool for demonstrating padding oracle attacks.",
            'aliases': ["poracle", "poracle"],
        },
        {
            'name': 'posttester',
            'description': "A jar file that will send POST requests to servers in order to test for the hash collision vulnerability discussed at the Chaos Communication Congress in Berlin.",
            'aliases': ["posttester", "posttester"],
        },
        {
            'name': 'pwd-hash',
            'description': "A password hashing tool that use the crypt function to generate the hash of a string given on standard input.",
            'aliases': ["pwd-hash", "pwd hash"],
        },
        {
            'name': 'pwdlyser',
            'description': "Python-based CLI Password Analyser (Reporting Tool).",
            'aliases': ["pwdlyser", "pwdlyser"],
        },
        {
            'name': 'rsactftool',
            'description': "RSA tool for ctf - retrieve private key from weak public key and/or uncipher data.",
            'aliases': ["rsactftool", "rsactftool"],
        },
        {
            'name': 'rsatool',
            'description': "Tool that can be used to calculate RSA and RSA-CRT parameters.",
            'aliases': ["rsatool", "rsatool"],
        },
        {
            'name': 'rshack',
            'description': "Python tool which allows to carry out some attacks on RSA, and offer a few tools to manipulate RSA keys.",
            'aliases': ["rshack", "rshack"],
        },
        {
            'name': 'rupture',
            'description': "A framework for BREACH and other compression-based crypto attacks.",
            'aliases': ["rupture", "rupture"],
        },
        {
            'name': 'rustpad',
            'description': "Multi-threaded Padding Oracle attacks against any service.",
            'aliases': ["rustpad", "rustpad"],
        },
        {
            'name': 'sbd',
            'description': "Netcat-clone, portable, offers strong encryption - features AES-CBC + HMAC-SHA1 encryption, program execution (-e), choosing source port, continuous reconnection with delay + more",
            'aliases': ["sbd", "sbd"],
        },
        {
            'name': 'sha1collisiondetection',
            'description': "Library and command line tool to detect SHA collision in a file",
            'aliases': ["sha1collisiondetection", "sha1collisiondetection"],
        },
        {
            'name': 'snow',
            'description': "Steganography program for concealing messages in text files.",
            'aliases': ["snow", "snow"],
        },
        {
            'name': 'sslyze',
            'description': "Python tool for analyzing the configuration of SSL servers and for identifying misconfigurations.",
            'aliases': ["sslyze", "ssl yze"],
        },
        {
            'name': 'tls-attacker',
            'description': "A Java-based framework for analyzing TLS libraries.",
            'aliases': ["tls-attacker", "tls attacker"],
        },
        {
            'name': 'tls-map',
            'description': "CLI & library for TLS cipher suites manipulation.",
            'aliases': ["tls-map", "tls map"],
        },
        {
            'name': 'tlsenum',
            'description': "A command line tool to enumerate TLS cipher-suites supported by a server.",
            'aliases': ["tlsenum", "tlsenum"],
        },
        {
            'name': 'tlsfuzzer',
            'description': "SSL and TLS protocol test suite and fuzzer.",
            'aliases': ["tlsfuzzer", "tlsfuzzer"],
        },
        {
            'name': 'tlshelpers',
            'description': "A collection of shell scripts that help handling X.509 certificate and TLS issues.",
            'aliases': ["tlshelpers", "tlshelpers"],
        },
        {
            'name': 'tlspretense',
            'description': "SSL/TLS client testing framework.",
            'aliases': ["tlspretense", "tlspretense"],
        },
        {
            'name': 'untwister',
            'description': "Seed recovery tool for PRNGs.",
            'aliases': ["untwister", "untwister"],
        },
        {
            'name': 'x-rsa',
            'description': "Contains a many of attack types in RSA such as Hasted, Common Modulus, Chinese Remainder Theorem.",
            'aliases': ["x-rsa", "x rsa"],
        },
        {
            'name': 'xorbruteforcer',
            'description': "Script that implements a XOR bruteforcing of a given file, although a specific key can be used too.",
            'aliases': ["xorbruteforcer", "xorbruteforcer"],
        },
        {
            'name': 'xorsearch',
            'description': "Program to search for a given string in an XOR, ROL or ROT encoded binary file.",
            'aliases': ["xorsearch", "xorsearch"],
        },
        {
            'name': 'zipexec',
            'description': "A unique technique to execute binaries from a password protected zip.",
            'aliases': ["zipexec", "zipexec"],
        },
        {
            'name': 'zulucrypt',
            'description': "Front end to cryptsetup and tcplay and it allows easy management of encrypted block devices.",
            'aliases': ["zulucrypt", "zulucrypt"],
        },
    ],

    # Wireless (68 tools)
    'blackarch-wireless': [
        {
            'name': 'airflood',
            'description': "A modification of aireplay that allows for a DoS of the AP. This program fills the table of clients of the AP with random MACs doing impossible new connections. [Tool in Spanish]",
            'aliases': ["airflood", "airflood"],
        },
        {
            'name': 'airgeddon',
            'description': "Multi-use bash script for Linux systems to audit wireless networks.",
            'aliases': ["airgeddon", "airgeddon"],
        },
        {
            'name': 'airopy',
            'description': "Get (wireless) clients and access points.",
            'aliases': ["airopy", "airopy"],
        },
        {
            'name': 'airoscript',
            'description': "A script to simplify the use of aircrack-ng tools.",
            'aliases': ["airoscript", "airoscript"],
        },
        {
            'name': 'airpwn',
            'description': "A tool for generic packet injection on an 802.11 network.",
            'aliases': ["airpwn", "airpwn"],
        },
        {
            'name': 'aphopper',
            'description': "A program that automatically hops between access points of different wireless networks.",
            'aliases': ["aphopper", "aphopper"],
        },
        {
            'name': 'apnbf',
            'description': "A small python script designed for enumerating valid APNs (Access Point Name) on a GTP-C speaking device.",
            'aliases': ["apnbf", "apnbf"],
        },
        {
            'name': 'atear',
            'description': "Wireless Hacking, WiFi Security, Vulnerability Analyzer, Pentestration.",
            'aliases': ["atear", "atear"],
        },
        {
            'name': 'auto-eap',
            'description': "Automated Brute-Force Login Attacks Against EAP Networks.",
            'aliases': ["auto-eap", "auto eap"],
        },
        {
            'name': 'batman-adv',
            'description': "Batman kernel module, (included upstream since .38)",
            'aliases': ["batman-adv", "batman adv"],
        },
        {
            'name': 'batman-alfred',
            'description': "Almighty Lightweight Fact Remote Exchange Daemon.",
            'aliases': ["batman-alfred", "batman alfred"],
        },
        {
            'name': 'beholder',
            'description': "A wireless intrusion detection tool that looks for anomalies in a wifi environment.",
            'aliases': ["beholder", "beholder"],
        },
        {
            'name': 'berate_ap',
            'description': "Script for orchestrating mana rogue WiFi Access Points.",
            'aliases': ["berate_ap", "berate ap"],
        },
        {
            'name': 'boopsuite',
            'description': "A Suite of Tools written in Python for wireless auditing and security testing.",
            'aliases': ["boopsuite", "boopsuite"],
        },
        {
            'name': 'create_ap',
            'description': "A shell script to create a NATed/Bridged Software Access Point.",
            'aliases': ["create_ap", "create ap"],
        },
        {
            'name': 'eapeak',
            'description': "Analysis Suite For EAP Enabled Wireless Networks.",
            'aliases': ["eapeak", "eapeak"],
        },
        {
            'name': 'eaphammer',
            'description': "Targeted evil twin attacks against WPA2-Enterprise networks. Indirect wireless pivots using hostile portal attacks.",
            'aliases': ["eaphammer", "eaphammer"],
        },
        {
            'name': 'fern-wifi-cracker',
            'description': "WEP, WPA wifi cracker for wireless penetration testing.",
            'aliases': ["fern-wifi-cracker", "fern wifi cracker"],
        },
        {
            'name': 'freewifi',
            'description': "How to get free wifi.",
            'aliases': ["freewifi", "freewifi"],
        },
        {
            'name': 'fuzzap',
            'description': "A python script for obfuscating wireless networks.",
            'aliases': ["fuzzap", "fuzzap"],
        },
        {
            'name': 'g72x++',
            'description': "Decoder for the g72x++ codec.",
            'aliases': ["g72x++", "g72x++"],
        },
        {
            'name': 'gerix-wifi-cracker',
            'description': "A graphical user interface for aircrack-ng and pyrit.",
            'aliases': ["gerix-wifi-cracker", "gerix wifi cracker"],
        },
        {
            'name': 'giskismet',
            'description': "A program to visually represent the Kismet data in a flexible manner.",
            'aliases': ["giskismet", "giskismet"],
        },
        {
            'name': 'hashcatch',
            'description': "Capture handshakes of nearby WiFi networks automatically.",
            'aliases': ["hashcatch", "hashcatch"],
        },
        {
            'name': 'hoover',
            'description': "Wireless Probe Requests Sniffer.",
            'aliases': ["hoover", "hoover"],
        },
        {
            'name': 'hostapd-mana',
            'description': "Modified hostapd for Wi-Fi attacks to create a rogue access point.",
            'aliases': ["hostapd-mana", "hostapd mana"],
        },
        {
            'name': 'hostapd-wpe',
            'description': "Modified hostapd to facilitate AP impersonation attacks.",
            'aliases': ["hostapd-wpe", "hostapd wpe"],
        },
        {
            'name': 'hotspotter',
            'description': "Passively monitor the network for probe request frames to identify the preferred networks of Windows XP clients, and compare it to a supplied list of common hotspot network names.",
            'aliases': ["hotspotter", "hotspotter"],
        },
        {
            'name': 'hwk',
            'description': "Collection of packet crafting and wireless network flooding tools",
            'aliases': ["hwk", "hwk"],
        },
        {
            'name': 'jcrack',
            'description': "A utility to create dictionary files that will crack the default passwords of select wireless gateways",
            'aliases': ["jcrack", "jcrack"],
        },
        {
            'name': 'kismet-earth',
            'description': "Various scripts to convert kismet logs to kml file to be used in Google Earth.",
            'aliases': ["kismet-earth", "kismet earth"],
        },
        {
            'name': 'kismet2earth',
            'description': "A set of utilities that convert from Kismet logs to Google Earth .kml format.",
            'aliases': ["kismet2earth", "kismet2earth"],
        },
        {
            'name': 'kismon',
            'description': "GUI client for kismet (wireless scanner/sniffer/monitor).",
            'aliases': ["kismon", "kismon"],
        },
        {
            'name': 'mana',
            'description': "A toolkit for rogue access point (evilAP) attacks first presented at Defcon 22.",
            'aliases': ["mana", "mana"],
        },
        {
            'name': 'mdk3',
            'description': "WLAN penetration tool.",
            'aliases': ["mdk3", "mdk3"],
        },
        {
            'name': 'mfcuk',
            'description': "MIFARE Classic Universal toolKit.",
            'aliases': ["mfcuk", "mfcuk tool"],
        },
        {
            'name': 'mitmap',
            'description': "A python program to create a fake AP and sniff data.",
            'aliases': ["mitmap", "mitmap"],
        },
        {
            'name': 'mousejack',
            'description': "Wireless mouse/keyboard attack with replay/transmit poc.",
            'aliases': ["mousejack", "mousejack"],
        },
        {
            'name': 'mtscan',
            'description': "Mikrotik RouterOS wireless scanner.",
            'aliases': ["mtscan", "mtscan"],
        },
        {
            'name': 'netattack',
            'description': "Python script to scan and attack wireless networks.",
            'aliases': ["netattack", "netattack"],
        },
        {
            'name': 'nzyme',
            'description': "WiFi defense system.",
            'aliases': ["nzyme", "nzyme"],
        },
        {
            'name': 'pidense',
            'description': "Monitor illegal wireless network activities. (Fake Access Points)",
            'aliases': ["pidense", "pidense"],
        },
        {
            'name': 'python-trackerjacker',
            'description': "Finds and tracks wifi devices through raw 802.11 monitoring.",
            'aliases': ["python-trackerjacker", "python trackerjacker"],
        },
        {
            'name': 'rfidiot',
            'description': "An open source python library for exploring RFID devices.",
            'aliases': ["rfidiot", "rfidiot"],
        },
        {
            'name': 'rfidtool',
            'description': "An open source tool to read / write rfid tags.",
            'aliases': ["rfidtool", "rfidtool"],
        },
        {
            'name': 'roguehostapd',
            'description': "Hostapd fork including Wi-Fi attacks and providing Python bindings with ctypes.",
            'aliases': ["roguehostapd", "roguehostapd"],
        },
        {
            'name': 'rtl8814au-dkms-git',
            'description': "RTL8814AU and RTL8813AU chipset driver with firmware v5.8.5.1.",
            'aliases': ["rtl8814au-dkms-git", "rtl8814au dkms git"],
        },
        {
            'name': 'sniff-probe-req',
            'description': "Wi-Fi Probe Requests Sniffer.",
            'aliases': ["sniff-probe-req", "sniff probe req"],
        },
        {
            'name': 'spectools',
            'description': "Spectrum-Tools is a set of utilities for using the Wi-Spy USB spectrum analyzer hardware.",
            'aliases': ["spectools", "spectools"],
        },
        {
            'name': 'timegen',
            'description': "This program generates a *.wav file to \"send\" an own time signal to DCF77 compatible devices.",
            'aliases': ["timegen", "timegen"],
        },
        {
            'name': 'ubitack',
            'description': "Tool, which automates some of the tasks you might need on a (wireless) penetration test or while you are on the go.",
            'aliases': ["ubitack", "ubitack"],
        },
        {
            'name': 'waidps',
            'description': "Wireless Auditing, Intrusion Detection & Prevention System.",
            'aliases': ["waidps", "waidps"],
        },
        {
            'name': 'wepbuster',
            'description': "script for automating aircrack-ng",
            'aliases': ["wepbuster", "wepbuster"],
        },
        {
            'name': 'wifi-pumpkin',
            'description': "Framework for Rogue Wi-Fi Access Point Attack.",
            'aliases': ["wifi-pumpkin", "wifi pumpkin"],
        },
        {
            'name': 'wifibroot',
            'description': "A WiFi Pentest Cracking tool for WPA/WPA2 (Handshake, PMKID, Cracking, EAPOL, Deauthentication).",
            'aliases': ["wifibroot", "wifibroot"],
        },
        {
            'name': 'wificurse',
            'description': "WiFi jamming tool.",
            'aliases': ["wificurse", "wificurse"],
        },
        {
            'name': 'wifijammer',
            'description': "A python script to continuously jam all wifi clients within range.",
            'aliases': ["wifijammer", "wifijammer"],
        },
        {
            'name': 'wifiphisher',
            'description': "Fast automated phishing attacks against WPA networks.",
            'aliases': ["wifiphisher", "wifiphisher"],
        },
        {
            'name': 'wifiscanmap',
            'description': "Another wifi mapping tool.",
            'aliases': ["wifiscanmap", "wifiscanmap"],
        },
        {
            'name': 'wifitap',
            'description': "WiFi injection tool through tun/tap device.",
            'aliases': ["wifitap", "wifitap"],
        },
        {
            'name': 'wireless-ids',
            'description': "Ability to detect suspicious activity such as (WEP/WPA/WPS) attack by sniffing the air for wireless packets.",
            'aliases': ["wireless-ids", "wireless ids"],
        },
        {
            'name': 'wirouter-keyrec',
            'description': "A platform independent software to recover the default WPA passphrases of the supported router models",
            'aliases': ["wirouter-keyrec", "wirouter keyrec"],
        },
        {
            'name': 'wlan2eth',
            'description': "Re-writes 802.11 captures into standard Ethernet frames.",
            'aliases': ["wlan2eth", "wlan2eth"],
        },
        {
            'name': 'wpa-bruteforcer',
            'description': "Attacking WPA/WPA encrypted access point without client.",
            'aliases': ["wpa-bruteforcer", "wpa bruteforcer"],
        },
        {
            'name': 'wpa2-halfhandshake-crack',
            'description': "A POC to show it is possible to capture enough of a handshake with a user from a fake AP to crack a WPA2 network without knowing the passphrase of the actual AP.",
            'aliases': ["wpa2-halfhandshake-crack", "wpa2 halfhandshake crack"],
        },
        {
            'name': 'wpsik',
            'description': "WPS scan and pwn tool.",
            'aliases': ["wpsik", "wpsik"],
        },
        {
            'name': 'zizzania',
            'description': "Automated DeAuth attack.",
            'aliases': ["zizzania", "zizzania"],
        },
        {
            'name': 'zykeys',
            'description': "Demonstrates how default wireless settings are derived on some models of ZyXEL routers.",
            'aliases': ["zykeys", "zykeys"],
        },
    ],

    # Binary (63 tools)
    'blackarch-binary': [
        {
            'name': 'amber',
            'description': "Reflective PE packer.",
            'aliases': ["amber", "amber"],
        },
        {
            'name': 'amoco',
            'description': "Yet another tool for analysing binaries.",
            'aliases': ["amoco", "amoco"],
        },
        {
            'name': 'androguard',
            'description': "Reverse engineering, Malware and goodware analysis of Android applications and more.",
            'aliases': ["androguard", "androguard"],
        },
        {
            'name': 'angr',
            'description': "The next-generation binary analysis platform from UC Santa Barbaras Seclab.",
            'aliases': ["angr", "angr"],
        },
        {
            'name': 'angr-management',
            'description': "The official angr GUI.",
            'aliases': ["angr-management", "angr management"],
        },
        {
            'name': 'angr-py2',
            'description': "The next-generation binary analysis platform from UC Santa Barbaras Seclab.",
            'aliases': ["angr-py2", "angr py2"],
        },
        {
            'name': 'avet',
            'description': "AntiVirus Evasion Tool.",
            'aliases': ["avet", "avet"],
        },
        {
            'name': 'barf',
            'description': "A multiplatform open source Binary Analysis and Reverse engineering Framework.",
            'aliases': ["barf", "barf"],
        },
        {
            'name': 'bgrep',
            'description': "Binary grep.",
            'aliases': ["bgrep", "bgrep"],
        },
        {
            'name': 'bindead',
            'description': "A static analysis tool for binaries",
            'aliases': ["bindead", "bindead"],
        },
        {
            'name': 'bindiff',
            'description': "A comparison tool for binary files, that assists vulnerability researchers and engineers to quickly find differences and similarities in disassembled code.",
            'aliases': ["bindiff", "bindiff"],
        },
        {
            'name': 'binflow',
            'description': "POSIX function tracing. Much better and faster than ftrace.",
            'aliases': ["binflow", "binflow"],
        },
        {
            'name': 'binwally',
            'description': "Binary and Directory tree comparison tool using the Fuzzy Hashing concept (ssdeep).",
            'aliases': ["binwally", "binwally"],
        },
        {
            'name': 'bsdiff',
            'description': "Tools for building and applying patches to binary files.",
            'aliases': ["bsdiff", "bsdiff"],
        },
        {
            'name': 'bvi',
            'description': "A display-oriented editor for binary files operate like \"vi\" editor.",
            'aliases': ["bvi", "bvi"],
        },
        {
            'name': 'bytecode-viewer',
            'description': "A Java 8/Android APK Reverse Engineering Suite.",
            'aliases': ["bytecode-viewer", "bytecode viewer"],
        },
        {
            'name': 'cminer',
            'description': "A tool for enumerating the code caves in PE files.",
            'aliases': ["cminer", "cminer"],
        },
        {
            'name': 'cpp2il',
            'description': "A tool to reverse unity\'s IL2PP toolchain",
            'aliases': ["cpp2il", "cpp2il"],
        },
        {
            'name': 'detect-it-easy',
            'description': "A program for determining types of files.",
            'aliases': ["detect-it-easy", "detect it easy"],
        },
        {
            'name': 'dissector',
            'description': "This code dissects the internal data structures in ELF files. It supports x86 and x86_64 archs and runs under Linux.",
            'aliases': ["dissector", "dissector"],
        },
        {
            'name': 'dutas',
            'description': "Analysis PE file or Shellcode.",
            'aliases': ["dutas", "dutas"],
        },
        {
            'name': 'dwarf',
            'description': "Full featured multi arch/os debugger built on top of PyQt5 and frida.",
            'aliases': ["dwarf", "dwarf"],
        },
        {
            'name': 'dynamorio',
            'description': "A dynamic binary instrumentation framework.",
            'aliases': ["dynamorio", "dynamorio"],
        },
        {
            'name': 'ecfs',
            'description': "Extended core file snapshot format.",
            'aliases': ["ecfs", "ecfs"],
        },
        {
            'name': 'elfparser',
            'description': "Cross Platform ELF analysis.",
            'aliases': ["elfparser", "elfparser"],
        },
        {
            'name': 'eresi',
            'description': "The ERESI Reverse Engineering Software Interface.",
            'aliases': ["eresi", "eresi"],
        },
        {
            'name': 'exescan',
            'description': "A tool to detect anomalies in PE (Portable Executable) files.",
            'aliases': ["exescan", "exescan"],
        },
        {
            'name': 'expimp-lookup',
            'description': "Looks for all export and import names that contain a specified string in all Portable Executable in a directory tree.",
            'aliases': ["expimp-lookup", "expimp lookup"],
        },
        {
            'name': 'expose',
            'description': "A Dynamic Symbolic Execution (DSE) engine for JavaScript",
            'aliases': ["expose", "expose"],
        },
        {
            'name': 'haystack',
            'description': "A Python framework for finding C structures from process memory - heap analysis - Memory structures forensics.",
            'aliases': ["haystack", "haystack"],
        },
        {
            'name': 'hercules-payload',
            'description': "A special payload generator that can bypass all antivirus software.",
            'aliases': ["hercules-payload", "hercules payload"],
        },
        {
            'name': 'hex2bin',
            'description': "Converts Motorola and Intel hex files to binary.",
            'aliases': ["hex2bin", "hex2bin"],
        },
        {
            'name': 'imagejs',
            'description': "Small tool to package javascript into a valid image file.",
            'aliases': ["imagejs", "imagejs"],
        },
        {
            'name': 'jpegdump',
            'description': "Tool to analyzse JPEG images Reads binary files and parses the JPEG markers inside them.",
            'aliases': ["jpegdump", "jpegdump"],
        },
        {
            'name': 'klee',
            'description': "A symbolic virtual machine built on top of the LLVM compiler infrastructure.",
            'aliases': ["klee", "klee"],
        },
        {
            'name': 'leena',
            'description': "Symbolic execution engine for JavaScript",
            'aliases': ["leena", "leena"],
        },
        {
            'name': 'loadlibrary',
            'description': "Porting Windows Dynamic Link Libraries to Linux.",
            'aliases': ["loadlibrary", "loadlibrary"],
        },
        {
            'name': 'manticore',
            'description': "Symbolic execution tool.",
            'aliases': ["manticore", "manticore"],
        },
        {
            'name': 'metame',
            'description': "A simple metamorphic code engine for arbitrary executables.",
            'aliases': ["metame", "metame"],
        },
        {
            'name': 'objdump2shellcode',
            'description': "A tool I have found incredibly useful whenever creating custom shellcode.",
            'aliases': ["objdump2shellcode", "objdump2shellcode"],
        },
        {
            'name': 'oledump',
            'description': "Analyze OLE files (Compound File Binary Format). These files contain streams of data. This tool allows you to analyze these streams.",
            'aliases': ["oledump", "oledump"],
        },
        {
            'name': 'packerid',
            'description': "Script which uses a PEiD database to identify which packer (if any) is being used by a binary.",
            'aliases': ["packerid", "packerid"],
        },
        {
            'name': 'patchkit',
            'description': "Powerful binary patching from Python.",
            'aliases': ["patchkit", "patchkit"],
        },
        {
            'name': 'pixd',
            'description': "Colourful visualization tool for binary files.",
            'aliases': ["pixd", "pixd"],
        },
        {
            'name': 'powerstager',
            'description': "A payload stager using PowerShell.",
            'aliases': ["powerstager", "powerstager"],
        },
        {
            'name': 'procdump',
            'description': "Generate coredumps based off performance triggers.",
            'aliases': ["procdump", "procdump"],
        },
        {
            'name': 'proctal',
            'description': "Provides a command line interface and a C library to manipulate the address space of a running program on Linux.",
            'aliases': ["proctal", "proctal"],
        },
        {
            'name': 'python-oletools',
            'description': "Tools to analyze Microsoft OLE2 files.",
            'aliases': ["python-oletools", "python oletools"],
        },
        {
            'name': 'python-peid',
            'description': "Python implementation of the Packed Executable iDentifier (PEiD).",
            'aliases': ["python-peid", "python peid"],
        },
        {
            'name': 'python2-oletools',
            'description': "Tools to analyze Microsoft OLE2 files.",
            'aliases': ["python2-oletools", "python2 oletools"],
        },
        {
            'name': 'qbdi',
            'description': "A Dynamic Binary Instrumentation framework based on LLVM.",
            'aliases': ["qbdi", "qbdi"],
        },
        {
            'name': 'quickscope',
            'description': "Statically analyze windows, linux, osx, executables and also APK files.",
            'aliases': ["quickscope", "quickscope"],
        },
        {
            'name': 'rbasefind',
            'description': "A firmware base address search tool.",
            'aliases': ["rbasefind", "rbasefind"],
        },
        {
            'name': 'redress',
            'description': "A tool for analyzing stripped Go binaries.",
            'aliases': ["redress", "redress"],
        },
        {
            'name': 'saruman',
            'description': "ELF anti-forensics exec, for injecting full dynamic executables into process image (With thread injection).",
            'aliases': ["saruman", "saruman"],
        },
        {
            'name': 'sgn',
            'description': "Shikata ga nai encoder ported into go with several improvements.",
            'aliases': ["sgn", "sgn"],
        },
        {
            'name': 'soot',
            'description': "A Java Bytecode Analysis and Transformation Framework.",
            'aliases': ["soot", "soot"],
        },
        {
            'name': 'stringsifter',
            'description': "Machine learning tool that automatically ranks strings based on their relevance for malware analysis.",
            'aliases': ["stringsifter", "stringsifter"],
        },
        {
            'name': 'triton',
            'description': "A Dynamic Binary Analysis (DBA) framework.",
            'aliases': ["triton", "triton"],
        },
        {
            'name': 'veles',
            'description': "New open source tool for binary data analysis.",
            'aliases': ["veles", "veles"],
        },
        {
            'name': 'wcc',
            'description': "The Witchcraft Compiler Collection.",
            'aliases': ["wcc", "wcc"],
        },
        {
            'name': 'wxhexeditor',
            'description': "A free hex editor / disk editor for Linux, Windows and MacOSX.",
            'aliases': ["wxhexeditor", "wxhexeditor"],
        },
        {
            'name': 'zelos',
            'description': "A comprehensive binary emulation and instrumentation platform.",
            'aliases': ["zelos", "zelos"],
        },
    ],

    # Social Engineering (60 tools)
    'blackarch-social': [
        {
            'name': 'anontwi',
            'description': "A free software python client designed to navigate anonymously on social networks. It supports Identi.ca and Twitter.com.",
            'aliases': ["anontwi", "anontwi"],
        },
        {
            'name': 'blackeye',
            'description': "Ultimate phishing tool with ngrok and serveo.",
            'aliases': ["blackeye", "blackeye"],
        },
        {
            'name': 'buster',
            'description': "Find emails of a person and return info associated with them.",
            'aliases': ["buster", "buster"],
        },
        {
            'name': 'cardpwn',
            'description': "OSINT Tool to find Breached Credit Cards Information.",
            'aliases': ["cardpwn", "cardpwn"],
        },
        {
            'name': 'catphish',
            'description': "For phishing and corporate espionage.",
            'aliases': ["catphish", "catphish"],
        },
        {
            'name': 'chameleonmini',
            'description': "Official repository of ChameleonMini, a freely programmable, portable tool for NFC security analysis that can emulate and clone contactless cards, read RFID tags and sniff/log RF data.",
            'aliases': ["chameleonmini", "chameleonmini"],
        },
        {
            'name': 'credsniper',
            'description': "Phishing framework written with the Python micro-framework Flask and Jinja2 templating which supports capturing 2FA tokens.",
            'aliases': ["credsniper", "credsniper"],
        },
        {
            'name': 'crosslinked',
            'description': "LinkedIn enumeration tool to extract valid employee names from an organization through search engine scraping.",
            'aliases': ["crosslinked", "crosslinked"],
        },
        {
            'name': 'email2phonenumber',
            'description': "A OSINT tool to obtain a target\'s phone number just by having his email address.",
            'aliases': ["email2phonenumber", "email2phonenumber"],
        },
        {
            'name': 'facebash',
            'description': "Facebook Brute Forcer in shellscript using TOR.",
            'aliases': ["facebash", "facebash"],
        },
        {
            'name': 'facebookosint',
            'description': "OSINT tool to replace facebook graph search.",
            'aliases': ["facebookosint", "facebookosint"],
        },
        {
            'name': 'facebrok',
            'description': "Social Engineering Tool Oriented to facebook.",
            'aliases': ["facebrok", "facebrok"],
        },
        {
            'name': 'fbi',
            'description': "An accurate facebook account information gathering.",
            'aliases': ["fbi", "fbi"],
        },
        {
            'name': 'fluxion',
            'description': "A security auditing and social-engineering research tool.",
            'aliases': ["fluxion", "fluxion"],
        },
        {
            'name': 'genisys',
            'description': "Powerful Telegram Members Scraping and Adding Toolkit.",
            'aliases': ["genisys", "genisys"],
        },
        {
            'name': 'gg-images',
            'description': "The application was created to allow anyone to easily download profile pictures from GG.",
            'aliases': ["gg-images", "gg images"],
        },
        {
            'name': 'gocabrito',
            'description': "Super organized and flexible script for sending phishing campaigns.",
            'aliases': ["gocabrito", "gocabrito"],
        },
        {
            'name': 'gophish',
            'description': "Open-Source Phishing Framework.",
            'aliases': ["gophish", "gophish"],
        },
        {
            'name': 'hemingway',
            'description': "A simple and easy to use spear phishing helper.",
            'aliases': ["hemingway", "hemingway"],
        },
        {
            'name': 'hiddeneye',
            'description': "Modern phishing tool with advanced functionality.",
            'aliases': ["hiddeneye", "hiddeneye"],
        },
        {
            'name': 'hiddeneye-legacy',
            'description': "Modern Phishing Tool With Advanced Functionality.",
            'aliases': ["hiddeneye-legacy", "hiddeneye legacy"],
        },
        {
            'name': 'holehe',
            'description': "A tool for Efficiently finding registered accounts from emails.",
            'aliases': ["holehe", "holehe"],
        },
        {
            'name': 'instagramosint',
            'description': "An Instagram Open Source Intelligence Tool.",
            'aliases': ["instagramosint", "instagramosint"],
        },
        {
            'name': 'linkedin2username',
            'description': "OSINT Tool: Generate username lists for companies on LinkedIn.",
            'aliases': ["linkedin2username", "linkedin2username"],
        },
        {
            'name': 'linkedint',
            'description': "LinkedIn Recon Tool.",
            'aliases': ["linkedint", "linkedint"],
        },
        {
            'name': 'maigret',
            'description': "OSINT username checker. Collect a dossier on a person by username from a huge number of sites.",
            'aliases': ["maigret", "maigret"],
        },
        {
            'name': 'muraena',
            'description': "Almost-transparent reverse proxy to automate phishing and post-phishing activities.",
            'aliases': ["muraena", "muraena"],
        },
        {
            'name': 'nexfil',
            'description': "OSINT tool for finding profiles by username.",
            'aliases': ["nexfil", "nexfil"],
        },
        {
            'name': 'osi.ig',
            'description': "Instagram OSINT Tool gets a range of information from an Instagram account.",
            'aliases': ["osi.ig", "osi.ig"],
        },
        {
            'name': 'pepe',
            'description': "Collect information about email addresses from Pastebin.",
            'aliases': ["pepe", "pepe"],
        },
        {
            'name': 'phemail',
            'description': "A python open source phishing email tool that automates the process of sending phishing emails as part of a social engineering test.",
            'aliases': ["phemail", "phemail"],
        },
        {
            'name': 'phishingkithunter',
            'description': "Find phishing kits which use your brand/organization\'s files and image\'.",
            'aliases': ["phishingkithunter", "phishingkithunter"],
        },
        {
            'name': 'phoneinfoga',
            'description': "Information gathering & OSINT framework for phone numbers.",
            'aliases': ["phoneinfoga", "phoneinfoga"],
        },
        {
            'name': 'phonia',
            'description': "Advanced toolkits to scan phone numbers using only free resources.",
            'aliases': ["phonia", "phonia"],
        },
        {
            'name': 'qrljacker',
            'description': "QRLJacker is a highly customizable exploitation framework to demonstrate \"QRLJacking Attack Vector\".",
            'aliases': ["qrljacker", "qrljacker"],
        },
        {
            'name': 'raven',
            'description': "A Linkedin information gathering tool that can be used by pentesters to gather information about an organization employees using Linkedin.",
            'aliases': ["raven", "raven"],
        },
        {
            'name': 'reelphish',
            'description': "A Real-Time Two-Factor Phishing Tool.",
            'aliases': ["reelphish", "reelphish"],
        },
        {
            'name': 'seeker',
            'description': "Accurately Locate People using Social Engineering.",
            'aliases': ["seeker", "seeker"],
        },
        {
            'name': 'sees',
            'description': "Increase the success rate of phishing attacks by sending emails to company users as if they are coming from the very same company\'s domain.",
            'aliases': ["sees", "sees"],
        },
        {
            'name': 'set',
            'description': "Social-engineer toolkit. Aimed at penetration testing around Social-Engineering.",
            'aliases': ["set", "set"],
        },
        {
            'name': 'sherlock',
            'description': "Find usernames across social networks.",
            'aliases': ["sherlock", "sherlock project"],
        },
        {
            'name': 'simpleemailspoofer',
            'description': "A simple Python CLI to spoof emails.",
            'aliases': ["simpleemailspoofer", "simpleemailspoofer"],
        },
        {
            'name': 'skiptracer',
            'description': "OSINT python2 webscraping framework. Skipping the needs of API keys.",
            'aliases': ["skiptracer", "skiptracer"],
        },
        {
            'name': 'slackpirate',
            'description': "Slack Enumeration and Extraction Tool - extract sensitive information from a Slack Workspace.",
            'aliases': ["slackpirate", "slackpirate"],
        },
        {
            'name': 'social-analyzer',
            'description': "Analyzing & finding a person\'s profile across social media websites.",
            'aliases': ["social-analyzer", "social analyzer"],
        },
        {
            'name': 'social-mapper',
            'description': "A social media enumeration and correlation tool.",
            'aliases': ["social-mapper", "social mapper"],
        },
        {
            'name': 'social-vuln-scanner',
            'description': "Gathers public information on companies to highlight social engineering risk.",
            'aliases': ["social-vuln-scanner", "social vuln scanner"],
        },
        {
            'name': 'socialfish',
            'description': "Ultimate phishing tool with Ngrok integrated.",
            'aliases': ["socialfish", "socialfish"],
        },
        {
            'name': 'socialpwned',
            'description': "OSINT tool that allows to get the emails, from a target, published in social networks.",
            'aliases': ["socialpwned", "socialpwned"],
        },
        {
            'name': 'spf',
            'description': "A python tool designed to allow for quick recon and deployment of simple social engineering phishing exercises.",
            'aliases': ["spf", "spf"],
        },
        {
            'name': 'token-hunter',
            'description': "OSINT Tool - Search the group and group members\' snippets, issues, and issue discussions for sensitive data that may be included in these assets.",
            'aliases': ["token-hunter", "token hunter"],
        },
        {
            'name': 'trape',
            'description': "People tracker on the Internet: OSINT analysis and research tool by Jose Pino.",
            'aliases': ["trape", "trape"],
        },
        {
            'name': 'tweets-analyzer',
            'description': "Tweets metadata scraper & activity analyzer.",
            'aliases': ["tweets-analyzer", "tweets analyzer"],
        },
        {
            'name': 'twint',
            'description': "An advanced Twitter scraping & OSINT tool written in Python that doesn\'t use Twitter\'s API, allowing you to scrape a user\'s followers, following, Tweets and more while evading most API limitations.",
            'aliases': ["twint", "twint"],
        },
        {
            'name': 'ultimate-facebook-scraper',
            'description': "A bot which scrapes almost everything about a Facebook user\'s profile.",
            'aliases': ["ultimate-facebook-scraper", "ultimate facebook scraper"],
        },
        {
            'name': 'user-scanner',
            'description': "OSINT tool that analyzes username and email presence across multiple platforms, intended for security research, investigations, legitimate analysis.",
            'aliases': ["user-scanner", "user scanner"],
        },
        {
            'name': 'userrecon-py',
            'description': "Recognition usernames in 187 social networks.",
            'aliases': ["userrecon-py", "userrecon py"],
        },
        {
            'name': 'weeman',
            'description': "HTTP Server for phishing in python.",
            'aliases': ["weeman", "weeman"],
        },
        {
            'name': 'whatbreach',
            'description': "OSINT tool to find breached emails and databases.",
            'aliases': ["whatbreach", "whatbreach"],
        },
        {
            'name': 'whatsmyname',
            'description': "Tool to perform user and username enumeration on various websites.",
            'aliases': ["whatsmyname", "whatsmyname"],
        },
    ],

    # Backdoor (52 tools)
    'blackarch-backdoor': [
        {
            'name': 'aesshell',
            'description': "A backconnect shell for Windows and Unix written in python and uses AES in CBC mode in conjunction with HMAC-SHA256 for secure transport.",
            'aliases': ["aesshell", "aesshell"],
        },
        {
            'name': 'azazel',
            'description': "A userland rootkit based off of the original LD_PRELOAD technique from Jynx rootkit.",
            'aliases': ["azazel", "azazel"],
        },
        {
            'name': 'backcookie',
            'description': "Small backdoor using cookie.",
            'aliases': ["backcookie", "backcookie"],
        },
        {
            'name': 'backdoor-factory',
            'description': "Patch win32/64 binaries with shellcode.",
            'aliases': ["backdoor-factory", "backdoor factory"],
        },
        {
            'name': 'backdoorme',
            'description': "A powerful utility capable of backdooring Unix machines with a slew of backdoors.",
            'aliases': ["backdoorme", "backdoorme"],
        },
        {
            'name': 'backdoorppt',
            'description': "Transform your payload.exe into one fake word doc (.ppt).",
            'aliases': ["backdoorppt", "backdoorppt"],
        },
        {
            'name': 'cymothoa',
            'description': "A stealth backdooring tool, that inject backdoor\'s shellcode into an existing process.",
            'aliases': ["cymothoa", "cymothoa"],
        },
        {
            'name': 'debinject',
            'description': "Inject malicious code into *.debs.",
            'aliases': ["debinject", "debinject"],
        },
        {
            'name': 'donut',
            'description': "Generates x86, x64 or AMD64+x86 P.I. shellcode loading .NET Assemblies from memory.",
            'aliases': ["donut", "donut"],
        },
        {
            'name': 'dr0p1t-framework',
            'description': "A framework that creates a dropper that bypass most AVs, some sandboxes and have some tricks.",
            'aliases': ["dr0p1t-framework", "dr0p1t framework"],
        },
        {
            'name': 'dragon-backdoor',
            'description': "A sniffing, non binding, reverse down/exec, portknocking service Based on cd00r.c.",
            'aliases': ["dragon-backdoor", "dragon backdoor"],
        },
        {
            'name': 'eggshell',
            'description': "iOS/macOS/Linux Remote Administration Tool.",
            'aliases': ["eggshell", "eggshell"],
        },
        {
            'name': 'enyelkm',
            'description': "Rootkit for Linux x86 kernels v2.6.",
            'aliases': ["enyelkm", "enyelkm"],
        },
        {
            'name': 'evilpdf',
            'description': "Embedding executable files in PDF Documents.",
            'aliases': ["evilpdf", "evilpdf"],
        },
        {
            'name': 'exe2image',
            'description': "A simple utility to convert EXE files to JPEG images and vice versa.",
            'aliases': ["exe2image", "exe2image"],
        },
        {
            'name': 'gobd',
            'description': "A Golang covert backdoor.",
            'aliases': ["gobd", "gobd"],
        },
        {
            'name': 'harness',
            'description': "Interactive remote PowerShell Payload.",
            'aliases': ["harness", "harness"],
        },
        {
            'name': 'hoaxshell',
            'description': "A Windows reverse shell payload generator and handler that abuses the http(s) protocol to establish a beacon-like reverse shell.",
            'aliases': ["hoaxshell", "hoaxshell"],
        },
        {
            'name': 'hotpatch',
            'description': "Hot patches executables on Linux using .so file injection.",
            'aliases': ["hotpatch", "hotpatch"],
        },
        {
            'name': 'icmpsh',
            'description': "Simple reverse ICMP shell.",
            'aliases': ["icmpsh", "icmpsh"],
        },
        {
            'name': 'jinjector',
            'description': "Joomla modules backdoor injector.",
            'aliases': ["jinjector", "jinjector"],
        },
        {
            'name': 'jynx2',
            'description': "An expansion of the original Jynx LD_PRELOAD rootkit.",
            'aliases': ["jynx2", "jynx2"],
        },
        {
            'name': 'k55',
            'description': "Linux x86_64 Process Injection Utility.",
            'aliases': ["k55", "k55"],
        },
        {
            'name': 'kimi',
            'description': "Script to generate malicious debian packages (debain trojans).",
            'aliases': ["kimi", "kimi"],
        },
        {
            'name': 'kwetza',
            'description': "Python script to inject existing Android applications with a Meterpreter payload.",
            'aliases': ["kwetza", "kwetza"],
        },
        {
            'name': 'ld-shatner',
            'description': "ld-linux code injector.",
            'aliases': ["ld-shatner", "ld shatner"],
        },
        {
            'name': 'linux-inject',
            'description': "Tool for injecting a shared object into a Linux process.",
            'aliases': ["linux-inject", "linux inject"],
        },
        {
            'name': 'meterssh',
            'description': "A way to take shellcode, inject it into memory then tunnel whatever port you want to over SSH to mask any type of communications as a normal SSH connection.",
            'aliases': ["meterssh", "meterssh"],
        },
        {
            'name': 'microsploit',
            'description': "Fast and easy create backdoor office exploitation using module metasploit packet, Microsoft Office, Open Office, Macro attack, Buffer Overflow.",
            'aliases': ["microsploit", "microsploit"],
        },
        {
            'name': 'ms-sys',
            'description': "A tool to write Win9x- master boot records (mbr) under linux - RTM!",
            'aliases': ["ms-sys", "ms sys"],
        },
        {
            'name': 'nxcrypt',
            'description': "Python backdoor framework.",
            'aliases': ["nxcrypt", "nxcrypt"],
        },
        {
            'name': 'phishery',
            'description': "An SSL Enabled Basic Auth Credential Harvester with a Word Document Template URL Injector.",
            'aliases': ["phishery", "phishery"],
        },
        {
            'name': 'platypus',
            'description': "A modern multiple reverse shell sessions manager written in go.",
            'aliases': ["platypus", "platypus"],
        },
        {
            'name': 'pwncat',
            'description': "Bind and reverse shell handler with FW/IDS/IPS evasion, self-inject and port-scanning.",
            'aliases': ["pwncat", "pwncat"],
        },
        {
            'name': 'pyrasite',
            'description': "Code injection and introspection of running Python processes.",
            'aliases': ["pyrasite", "pyrasite"],
        },
        {
            'name': 'revsh',
            'description': "A reverse shell with terminal support, data tunneling, and advanced pivoting capabilities.",
            'aliases': ["revsh", "revsh"],
        },
        {
            'name': 'rrs',
            'description': "A reverse (connecting) remote shell. Instead of listening for incoming connections it will connect out to a listener (rrs in listen mode). With tty support and more.",
            'aliases': ["rrs", "rrs"],
        },
        {
            'name': 'rubilyn',
            'description': "64bit Mac OS-X kernel rootkit that uses no hardcoded address to hook the BSD subsystem in all OS-X Lion & below. It uses a combination of syscall hooking and DKOM to hide activity on a host.",
            'aliases': ["rubilyn", "rubilyn"],
        },
        {
            'name': 'shellinabox',
            'description': "Implements a web server that can export arbitrary command line tools to a web based terminal emulator.",
            'aliases': ["shellinabox", "shellinabox"],
        },
        {
            'name': 'shootback',
            'description': "A reverse TCP tunnel let you access target behind NAT or firewall.",
            'aliases': ["shootback", "shootback"],
        },
        {
            'name': 'silenttrinity',
            'description': "An asynchronous, collaborative post-exploitation agent powered by Python and .NET\'s DLR.",
            'aliases': ["silenttrinity", "silenttrinity"],
        },
        {
            'name': 'sliver',
            'description': "Opensource C2 framework.",
            'aliases': ["sliver", "sliver"],
        },
        {
            'name': 'syringe',
            'description': "A General Purpose DLL & Code Injection Utility.",
            'aliases': ["syringe", "syringe"],
        },
        {
            'name': 'trixd00r',
            'description': "An advanced and invisible userland backdoor based on TCP/IP for UNIX systems.",
            'aliases': ["trixd00r", "trixd00r"],
        },
        {
            'name': 'tsh',
            'description': "An open-source UNIX backdoor that compiles on all variants, has full pty support, and uses strong crypto for communication.",
            'aliases': ["tsh", "tsh"],
        },
        {
            'name': 'tsh-sctp',
            'description': "An open-source UNIX backdoor.",
            'aliases': ["tsh-sctp", "tsh sctp"],
        },
        {
            'name': 'u3-pwn',
            'description': "A tool designed to automate injecting executables to Sandisk smart usb devices with default U3 software install.",
            'aliases': ["u3-pwn", "u3 pwn"],
        },
        {
            'name': 'unicorn-powershell',
            'description': "A simple tool for using a PowerShell downgrade attack and inject shellcode straight into memory.",
            'aliases': ["unicorn-powershell", "unicorn powershell"],
        },
        {
            'name': 'villain',
            'description': "C2 framework that can handle multiple TCP socket & HoaxShell-based reverse shells, enhance their functionality with additional features and share them among connected sibling servers.",
            'aliases': ["villain", "villain"],
        },
        {
            'name': 'vlany',
            'description': "Linux LD_PRELOAD rootkit (x86 and x86_64 architectures).",
            'aliases': ["vlany", "vlany"],
        },
        {
            'name': 'webacoo',
            'description': "Web Backdoor Cookie Script-Kit.",
            'aliases': ["webacoo", "webacoo"],
        },
        {
            'name': 'webspa',
            'description': "A web knocking tool, sending a single HTTP/S to run O/S commands.",
            'aliases': ["webspa", "webspa"],
        },
    ],

    # Mobile (47 tools)
    'blackarch-mobile': [
        {
            'name': 'androbugs',
            'description': "An efficient Android vulnerability scanner that helps developers or hackers find potential security vulnerabilities in Android applications.",
            'aliases': ["androbugs", "androbugs"],
        },
        {
            'name': 'androick',
            'description': "A python tool to help in forensics analysis on android.",
            'aliases': ["androick", "androick"],
        },
        {
            'name': 'android-backup-extractor',
            'description': "Android backup extractor",
            'aliases': ["android-backup-extractor", "android backup extractor"],
        },
        {
            'name': 'android-ndk',
            'description': "Android C/C++ developer kit",
            'aliases': ["android-ndk", "android ndk"],
        },
        {
            'name': 'android-sdk',
            'description': "Google Android SDK",
            'aliases': ["android-sdk", "android sdk"],
        },
        {
            'name': 'android-udev-rules',
            'description': "Android udev rules.",
            'aliases': ["android-udev-rules", "android udev rules"],
        },
        {
            'name': 'androidmeda',
            'description': "AI tool to deobfuscate and find any potential vulnerabilities in android apps.",
            'aliases': ["androidmeda", "androidmeda"],
        },
        {
            'name': 'androidpincrack',
            'description': "Bruteforce the Android Passcode given the hash and salt.",
            'aliases': ["androidpincrack", "androidpincrack"],
        },
        {
            'name': 'androidsniffer',
            'description': "A perl script that lets you search for 3rd party passwords, dump the call log, dump contacts, dump wireless configuration, and more.",
            'aliases': ["androidsniffer", "androidsniffer"],
        },
        {
            'name': 'androwarn',
            'description': "Yet another static code analyzer for malicious Android applications.",
            'aliases': ["androwarn", "androwarn"],
        },
        {
            'name': 'apkid',
            'description': "Android Application Identifier for Packers, Protectors, Obfuscators and Oddities.",
            'aliases': ["apkid", "apkid"],
        },
        {
            'name': 'apkleaks',
            'description': "Scanning APK file for URIs, endpoints & secrets.",
            'aliases': ["apkleaks", "apkleaks"],
        },
        {
            'name': 'apkstat',
            'description': "Automated Information Retrieval From APKs For Initial Analysis.",
            'aliases': ["apkstat", "apkstat"],
        },
        {
            'name': 'apkurlgrep',
            'description': "Extract endpoints from APK files.",
            'aliases': ["apkurlgrep", "apkurlgrep"],
        },
        {
            'name': 'appmon',
            'description': "A runtime security testing & profiling framework for native apps on macOS, iOS & android and it is built using Frida.",
            'aliases': ["appmon", "appmon"],
        },
        {
            'name': 'arcane',
            'description': "Backdoor iOS packages and create the necessary resources for APT repositories.",
            'aliases': ["arcane", "arcane"],
        },
        {
            'name': 'backdoor-apk',
            'description': "Shell script that simplifies the process of adding a backdoor to any Android APK file",
            'aliases': ["backdoor-apk", "backdoor apk"],
        },
        {
            'name': 'backhack',
            'description': "Tool to perform Android app analysis by backing up and extracting apps, allowing you to analyze and modify file system contents for apps.",
            'aliases': ["backhack", "backhack"],
        },
        {
            'name': 'bagbak',
            'description': "Yet another frida based App decryptor.",
            'aliases': ["bagbak", "bagbak"],
        },
        {
            'name': 'bandicoot',
            'description': "A toolbox to analyze mobile phone metadata.",
            'aliases': ["bandicoot", "bandicoot"],
        },
        {
            'name': 'cnamulator',
            'description': "A phone CNAM lookup utility using the OpenCNAM API.",
            'aliases': ["cnamulator", "cnamulator"],
        },
        {
            'name': 'dexpatcher',
            'description': "Modify Android DEX/APK files at source-level using Java.",
            'aliases': ["dexpatcher", "dexpatcher"],
        },
        {
            'name': 'drozer',
            'description': "A security testing framework for Android - Precompiled binary from official repository.",
            'aliases': ["drozer", "drozer"],
        },
        {
            'name': 'findmyiphone',
            'description': "Locates all devices associated with an iCloud account",
            'aliases': ["findmyiphone", "findmyiphone"],
        },
        {
            'name': 'firebaseenum',
            'description': "Tool to mass analyse potentially exposed Firebase databases on Android apps.",
            'aliases': ["firebaseenum", "firebaseenum"],
        },
        {
            'name': 'frida-ios-dump',
            'description': "Pull decrypted ipa from jailbreak device.",
            'aliases': ["frida-ios-dump", "frida ios dump"],
        },
        {
            'name': 'ghost',
            'description': "Android post-exploitation framework that exploits the Android Debug Bridge to remotely access an Android device.",
            'aliases': ["ghost", "ghost"],
        },
        {
            'name': 'idb',
            'description': "A tool to simplify some common tasks for iOS pentesting and research.",
            'aliases': ["idb", "idb"],
        },
        {
            'name': 'kalibrate-rtl',
            'description': "Fork of http://thre.at/kalibrate/ for use with rtl-sdr devices.",
            'aliases': ["kalibrate-rtl", "kalibrate rtl"],
        },
        {
            'name': 'lazydroid',
            'description': "Tool written as a bash script to facilitate some aspects of an Android Assessment",
            'aliases': ["lazydroid", "lazydroid"],
        },
        {
            'name': 'mara-framework',
            'description': "A Mobile Application Reverse engineering and Analysis Framework.",
            'aliases': ["mara-framework", "mara framework"],
        },
        {
            'name': 'mobsf',
            'description': "An intelligent, all-in-one open source mobile application (Android/iOS) automated pen-testing framework capable of performing static, dynamic analysis and web API testing.",
            'aliases': ["mobsf", "mobsf"],
        },
        {
            'name': 'needle',
            'description': "The iOS Security Testing Framework.",
            'aliases': ["needle", "needle"],
        },
        {
            'name': 'objection',
            'description': "Instrumented Mobile Pentest Framework.",
            'aliases': ["objection", "objection"],
        },
        {
            'name': 'phonesploit',
            'description': "Adb exploiting tools.",
            'aliases': ["phonesploit", "phonesploit"],
        },
        {
            'name': 'pyaxmlparser',
            'description': "A simple parser to parse Android XML file.",
            'aliases': ["pyaxmlparser", "pyaxmlparser"],
        },
        {
            'name': 'python-frida-tools',
            'description': "Frida CLI tools.",
            'aliases': ["python-frida-tools", "python frida tools"],
        },
        {
            'name': 'python2-frida-tools',
            'description': "Frida CLI tools.",
            'aliases': ["python2-frida-tools", "python2 frida tools"],
        },
        {
            'name': 'qark',
            'description': "Tool to look for several security related Android application vulnerabilities.",
            'aliases': ["qark", "qark"],
        },
        {
            'name': 'quark-engine',
            'description': "An Obfuscation-Neglect Android Malware Scoring System.",
            'aliases': ["quark-engine", "quark engine"],
        },
        {
            'name': 'sign',
            'description': "Automatically signs an apk with the Android test certificate.",
            'aliases': ["sign", "sign"],
        },
        {
            'name': 'simplify',
            'description': "Generic Android Deobfuscator.",
            'aliases': ["simplify", "simplify"],
        },
        {
            'name': 'smali-cfgs',
            'description': "Smali Control Flow Graph\'s.",
            'aliases': ["smali-cfgs", "smali cfgs"],
        },
        {
            'name': 'smalisca',
            'description': "Static Code Analysis for Smali files.",
            'aliases': ["smalisca", "smalisca"],
        },
        {
            'name': 'smartphone-pentest-framework',
            'description': "Repository for the Smartphone Pentest Framework (SPF).",
            'aliases': ["smartphone-pentest-framework", "smartphone pentest framework"],
        },
        {
            'name': 'stacoan',
            'description': "Crossplatform tool which aids developers, bugbounty hunters and ethical hackers performing static code analysis on mobile applications.",
            'aliases': ["stacoan", "stacoan"],
        },
        {
            'name': 'truegaze',
            'description': "Static analysis tool for Android/iOS apps focusing on security issues outside the source code.",
            'aliases': ["truegaze", "truegaze"],
        },
    ],

    # Defensive (44 tools)
    'blackarch-defensive': [
        {
            'name': 'arpon',
            'description': "A host-based solution to secure the ARP protocol and prevent MITM attacks via ARP spoofing or cache poisoning.",
            'aliases': ["arpon", "arpon"],
        },
        {
            'name': 'arpstraw',
            'description': "Arp spoof detection tool.",
            'aliases': ["arpstraw", "arpstraw"],
        },
        {
            'name': 'artillery',
            'description': "Blue team tool designed to protect Linux and Windows operating systems through multiple methods.",
            'aliases': ["artillery", "artillery"],
        },
        {
            'name': 'artlas',
            'description': "Apache Real Time Logs Analyzer System.",
            'aliases': ["artlas", "artlas"],
        },
        {
            'name': 'capa',
            'description': "The FLARE team\'s open-source tool to identify capabilities in executable files.",
            'aliases': ["capa", "capa"],
        },
        {
            'name': 'chainsaw',
            'description': "A powerful ‘first-response’ capability to quickly identify threats within Windows event logs.",
            'aliases': ["chainsaw", "chainsaw"],
        },
        {
            'name': 'chkrootkit',
            'description': "Checks for rootkits on a system.",
            'aliases': ["chkrootkit", "chkrootkit"],
        },
        {
            'name': 'detect-sniffer',
            'description': "Tool that detects sniffers in the network.",
            'aliases': ["detect-sniffer", "detect sniffer"],
        },
        {
            'name': 'fastnetmon',
            'description': "High performance DoS/DDoS load analyzer built on top of multiple packet capture engines.",
            'aliases': ["fastnetmon", "fastnetmon"],
        },
        {
            'name': 'fssb',
            'description': "A low-level filesystem sandbox for Linux using syscall intercepts.",
            'aliases': ["fssb", "fssb"],
        },
        {
            'name': 'honeycreds',
            'description': "Network credential injection to detect responder and other network poisoners.",
            'aliases': ["honeycreds", "honeycreds"],
        },
        {
            'name': 'ifchk',
            'description': "A network interface promiscuous mode detection tool.",
            'aliases': ["ifchk", "ifchk"],
        },
        {
            'name': 'inetsim',
            'description': "A software suite for simulating common internet services in a lab environment, e.g. for analyzing the network behaviour of unknown malware samples.",
            'aliases': ["inetsim", "inetsim"],
        },
        {
            'name': 'jeopardize',
            'description': "A low(zero) cost threat intelligence & response tool against phishing domains.",
            'aliases': ["jeopardize", "jeopardize"],
        },
        {
            'name': 'lorg',
            'description': "Apache Logfile Security Analyzer.",
            'aliases': ["lorg", "lorg"],
        },
        {
            'name': 'malice',
            'description': "VirusTotal Wanna Be - Now with 100% more Hipster.",
            'aliases': ["malice", "malice"],
        },
        {
            'name': 'malmon',
            'description': "Hosting exploit/backdoor detection daemon.",
            'aliases': ["malmon", "malmon"],
        },
        {
            'name': 'maltrail',
            'description': "Malicious traffic detection system.",
            'aliases': ["maltrail", "maltrail"],
        },
        {
            'name': 'mat',
            'description': "Metadata Anonymisation Toolkit composed of a GUI application, a CLI application and a library.",
            'aliases': ["mat", "mat"],
        },
        {
            'name': 'munin-hashchecker',
            'description': "Online hash checker for Virustotal and other services",
            'aliases': ["munin-hashchecker", "munin hashchecker"],
        },
        {
            'name': 'nipe',
            'description': "A script to make Tor Network your default gateway.",
            'aliases': ["nipe", "nipe"],
        },
        {
            'name': 'orjail',
            'description': "A more secure way to force programs to exclusively use tor network.",
            'aliases': ["orjail", "orjail"],
        },
        {
            'name': 'osfooler-ng',
            'description': "Prevents remote active/passive OS fingerprinting by tools like nmap or p0f.",
            'aliases': ["osfooler-ng", "osfooler ng"],
        },
        {
            'name': 'persistencesniper',
            'description': "Hunt persistences implanted in Windows machines.",
            'aliases': ["persistencesniper", "persistencesniper"],
        },
        {
            'name': 'portspoof',
            'description': "This program\'s primary goal is to enhance OS security through a set of new techniques.",
            'aliases': ["portspoof", "portspoof"],
        },
        {
            'name': 'procscope',
            'description': "Process-scoped runtime investigation tool using eBPF.",
            'aliases': ["procscope", "procscope"],
        },
        {
            'name': 'prowler',
            'description': "Tool for AWS security assessment, auditing and hardening.",
            'aliases': ["prowler", "prowler"],
        },
        {
            'name': 'quicksand-lite',
            'description': "Command line tool for scanning streams within office documents plus xor db attack.",
            'aliases': ["quicksand-lite", "quicksand lite"],
        },
        {
            'name': 'sentrypeer',
            'description': "Protect SIP Servers from bad actors.",
            'aliases': ["sentrypeer", "sentrypeer"],
        },
        {
            'name': 'sigma',
            'description': "Generic Signature Format for SIEM Systems",
            'aliases': ["sigma", "sigma"],
        },
        {
            'name': 'sniffjoke',
            'description': "Injects packets in the transmission flow that are able to seriously disturb passive analysis like sniffing, interception and low level information theft.",
            'aliases': ["sniffjoke", "sniffjoke"],
        },
        {
            'name': 'snort',
            'description': "A lightweight network intrusion detection system.",
            'aliases': ["snort", "snort"],
        },
        {
            'name': 'sooty',
            'description': "The SOC Analysts all-in-one CLI tool to automate and speed up workflow.",
            'aliases': ["sooty", "sooty"],
        },
        {
            'name': 'suricata',
            'description': "An Open Source Next Generation Intrusion Detection and Prevention Engine.",
            'aliases': ["suricata", "suricata"],
        },
        {
            'name': 'tabi',
            'description': "BGP Hijack Detection.",
            'aliases': ["tabi", "tabi"],
        },
        {
            'name': 'tfsec',
            'description': "Security scanner for your Terraform code.",
            'aliases': ["tfsec", "tfsec"],
        },
        {
            'name': 'threatspec',
            'description': "Project to integrate threat modelling into development process.",
            'aliases': ["threatspec", "threatspec"],
        },
        {
            'name': 'tor-autocircuit',
            'description': "Tor Autocircuit was developed to give users a finer control over Tor circuit creation. The tool exposes the functionality of TorCtl library which allows its users to control circuit length, speed, geolocation, and other parameters.",
            'aliases': ["tor-autocircuit", "tor autocircuit"],
        },
        {
            'name': 'tor-browser',
            'description': "Tor Browser Bundle: anonymous browsing using Firefox and Tor.",
            'aliases': ["tor-browser", "tor browser"],
        },
        {
            'name': 'tor-router',
            'description': "A tool that allow you to make TOR your default gateway and send all internet connections under TOR (as transparent proxy) for increase privacy/anonymity without extra unnecessary code.",
            'aliases': ["tor-router", "tor router"],
        },
        {
            'name': 'tyton',
            'description': "Kernel-Mode Rootkit Hunter.",
            'aliases': ["tyton", "tyton"],
        },
        {
            'name': 'usb-canary',
            'description': "A Linux or OSX tool that uses psutil to monitor devices while your computer is locked. In the case it detects someone plugging in or unplugging devices it can be configured to send you an SMS or alert you via Slack or Pushover.",
            'aliases': ["usb-canary", "usb canary"],
        },
        {
            'name': 'yeti',
            'description': "A platform meant to organize observables, indicators of compromise, TTPs, and knowledge on threats in a single, unified repository.",
            'aliases': ["yeti", "yeti"],
        },
        {
            'name': 'zeus',
            'description': "AWS Auditing & Hardening Tool.",
            'aliases': ["zeus", "zeus"],
        },
    ],

    # Sniffer (38 tools)
    'blackarch-sniffer': [
        {
            'name': 'above',
            'description': "Network Protocols Sniffer.",
            'aliases': ["above", "above"],
        },
        {
            'name': 'bittwist',
            'description': "A simple yet powerful libpcap-based Ethernet packet generator. It is designed to complement tcpdump, which by itself has done a great job at capturing network traffic.",
            'aliases': ["bittwist", "bittwist"],
        },
        {
            'name': 'capfuzz',
            'description': "Capture, fuzz and intercept web traffic.",
            'aliases': ["capfuzz", "capfuzz"],
        },
        {
            'name': 'cdpsnarf',
            'description': "Cisco discovery protocol sniffer.",
            'aliases': ["cdpsnarf", "cdpsnarf"],
        },
        {
            'name': 'cottontail',
            'description': "Capture all RabbitMQ messages being sent through a broker.",
            'aliases': ["cottontail", "cottontail"],
        },
        {
            'name': 'creds',
            'description': "Harvest FTP/POP/IMAP/HTTP/IRC credentials along with interesting data from each of the protocols.",
            'aliases': ["creds", "creds"],
        },
        {
            'name': 'dnswatch',
            'description': "DNS Traffic Sniffer and Analyzer.",
            'aliases': ["dnswatch", "dnswatch"],
        },
        {
            'name': 'eigrp-tools',
            'description': "This is a custom EIGRP packet generator and sniffer developed to test the security and overall operation quality of this brilliant Cisco routing protocol.",
            'aliases': ["eigrp-tools", "eigrp tools"],
        },
        {
            'name': 'espionage',
            'description': "A Network Packet and Traffic Interceptor For Linux. Sniff All Data Sent Through a Network.",
            'aliases': ["espionage", "espionage"],
        },
        {
            'name': 'firstorder',
            'description': "A traffic analyzer to evade Empire communication from Anomaly-Based IDS.",
            'aliases': ["firstorder", "firstorder"],
        },
        {
            'name': 'hexinject',
            'description': "A very versatile packet injector and sniffer that provides a command-line framework for raw network access.",
            'aliases': ["hexinject", "hexinject"],
        },
        {
            'name': 'httpry',
            'description': "A specialized packet sniffer designed for displaying and logging HTTP traffic.",
            'aliases': ["httpry", "httpry"],
        },
        {
            'name': 'httpsniff',
            'description': "Tool to sniff HTTP responses from TCP/IP based networks and save contained files locally for later review.",
            'aliases': ["httpsniff", "httpsniff"],
        },
        {
            'name': 'hubbit-sniffer',
            'description': "Simple application that listens for WIFI-frames and records the mac-address of the sender and posts them to a REST-api.",
            'aliases': ["hubbit-sniffer", "hubbit sniffer"],
        },
        {
            'name': 'hungry-interceptor',
            'description': "Intercepts data, does something with it, stores it.",
            'aliases': ["hungry-interceptor", "hungry interceptor"],
        },
        {
            'name': 'issniff',
            'description': "Internet Session Sniffer.",
            'aliases': ["issniff", "issniff"],
        },
        {
            'name': 'junkie',
            'description': "A modular packet sniffer and analyzer.",
            'aliases': ["junkie", "junkie"],
        },
        {
            'name': 'katsnoop',
            'description': "Utility that sniffs HTTP Basic Authentication information and prints the base64 decoded form.",
            'aliases': ["katsnoop", "katsnoop"],
        },
        {
            'name': 'mfsniffer',
            'description': "A python script for capturing unencrypted TSO login credentials.",
            'aliases': ["mfsniffer", "mfsniffer"],
        },
        {
            'name': 'mitmer',
            'description': "A man-in-the-middle and phishing attack tool that steals the victim\'s credentials of some web services like Facebook.",
            'aliases': ["mitmer", "mitmer"],
        },
        {
            'name': 'mots',
            'description': "Man on the Side Attack - experimental packet injection and detection.",
            'aliases': ["mots", "mots"],
        },
        {
            'name': 'net-creds',
            'description': "Sniffs sensitive data from interface or pcap.",
            'aliases': ["net-creds", "net creds"],
        },
        {
            'name': 'nsntrace',
            'description': "Perform network trace of a single process by using network namespaces.",
            'aliases': ["nsntrace", "nsntrace"],
        },
        {
            'name': 'ofp-sniffer',
            'description': "An OpenFlow sniffer to help network troubleshooting in production networks.",
            'aliases': ["ofp-sniffer", "ofp sniffer"],
        },
        {
            'name': 'ostinato',
            'description': "An open-source, cross-platform packet/traffic generator and analyzer with a friendly GUI. It aims to be \"Wireshark in Reverse\" and thus become complementary to Wireshark.",
            'aliases': ["ostinato", "ostinato"],
        },
        {
            'name': 'passivedns',
            'description': "A network sniffer that logs all DNS server replies for use in a passive DNS setup.",
            'aliases': ["passivedns", "passivedns"],
        },
        {
            'name': 'pcapteller',
            'description': "A tool designed for traffic manipulation and replay.",
            'aliases': ["pcapteller", "pcapteller"],
        },
        {
            'name': 'pth-toolkit',
            'description': "Modified version of the passing-the-hash tool collection made to work straight out of the box.",
            'aliases': ["pth", "pth toolkit", "pass the hash"],
        },
        {
            'name': 'pyrdp',
            'description': "Python 3 RDP MITM and library.",
            'aliases': ["pyrdp", "pyrdp"],
        },
        {
            'name': 'pytacle',
            'description': "Automates the task of sniffing GSM frames",
            'aliases': ["pytacle", "pytacle"],
        },
        {
            'name': 'rvi-capture',
            'description': "Capture packets sent or received by iOS devices.",
            'aliases': ["rvi-capture", "rvi capture"],
        },
        {
            'name': 'sipffer',
            'description': "SIP protocol command line sniffer.",
            'aliases': ["sipffer", "sipffer"],
        },
        {
            'name': 'snapception',
            'description': "Intercept and decrypt all snapchats received over your network.",
            'aliases': ["snapception", "snapception"],
        },
        {
            'name': 'ssldump',
            'description': "An SSLv3/TLS network protocol analyzer.",
            'aliases': ["ssldump", "ssldump"],
        },
        {
            'name': 'sslsniff',
            'description': "A tool to MITM all SSL connections on a LAN and dynamically generate certs for the domains that are being accessed on the fly.",
            'aliases': ["sslsniff", "sslsniff"],
        },
        {
            'name': 'stenographer',
            'description': "A packet capture solution which aims to quickly spool all packets to disk, then provide simple, fast access to subsets of those packets.",
            'aliases': ["stenographer", "stenographer"],
        },
        {
            'name': 'wifi-monitor',
            'description': "Prints the IPs on your local network that\'re sending the most packets.",
            'aliases': ["wifi-monitor", "wifi monitor"],
        },
        {
            'name': 'xcavator',
            'description': "Man-In-The-Middle and phishing attack tool that steals the victim\'s credentials of some web services like Facebook.",
            'aliases': ["xcavator", "xcavator"],
        },
    ],

    # Malware (32 tools)
    'blackarch-malware': [
        {
            'name': 'balbuzard',
            'description': "A package of malware analysis tools in python to extract patterns of interest from suspicious files (IP addresses, domain names, known file headers, interesting strings, etc).",
            'aliases': ["balbuzard", "balbuzard"],
        },
        {
            'name': 'bamf-framework',
            'description': "A modular framework designed to be a platform to launch attacks against botnets.",
            'aliases': ["bamf-framework", "bamf framework"],
        },
        {
            'name': 'bdlogparser',
            'description': "This is a utility to parse a Bit Defender log file, in order to sort them into a malware archive for easier maintenance of your malware collection.",
            'aliases': ["bdlogparser", "bdlogparser"],
        },
        {
            'name': 'box-js',
            'description': "A tool for studying JavaScript malware.",
            'aliases': ["box-js", "box js"],
        },
        {
            'name': 'clamscanlogparser',
            'description': "This is a utility to parse a Clam Anti Virus log file, in order to sort them into a malware archive for easier maintanence of your malware collection.",
            'aliases': ["clamscanlogparser", "clamscanlogparser"],
        },
        {
            'name': 'cuckoo',
            'description': "Automated malware analysis system.",
            'aliases': ["cuckoo", "cuckoo"],
        },
        {
            'name': 'damm',
            'description': "Differential Analysis of Malware in Memory.",
            'aliases': ["damm", "damm"],
        },
        {
            'name': 'fakenet-ng',
            'description': "Next Generation Dynamic Network Analysis Tool.",
            'aliases': ["fakenet-ng", "fakenet ng"],
        },
        {
            'name': 'fileintel',
            'description': "A modular Python application to pull intelligence about malicious files.",
            'aliases': ["fileintel", "fileintel"],
        },
        {
            'name': 'flare-floss',
            'description': "Obfuscated String Solver - Automatically extract obfuscated strings from malware.",
            'aliases': ["flare-floss", "flare floss"],
        },
        {
            'name': 'fprotlogparser',
            'description': "This is a utility to parse a F-Prot Anti Virus log file, in order to sort them into a malware archive for easier maintanence of your collection.",
            'aliases': ["fprotlogparser", "fprotlogparser"],
        },
        {
            'name': 'gcat',
            'description': "A fully featured backdoor that uses Gmail as a C&C server.",
            'aliases': ["gcat", "gcat"],
        },
        {
            'name': 'malboxes',
            'description': "Builds malware analysis Windows VMs so that you don\'t have to.",
            'aliases': ["malboxes", "malboxes"],
        },
        {
            'name': 'malscan',
            'description': "A Simple PE File Heuristics Scanner.",
            'aliases': ["malscan", "malscan"],
        },
        {
            'name': 'maltrieve',
            'description': "Originated as a fork of mwcrawler. It retrieves malware directly from the sources as listed at a number of sites.",
            'aliases': ["maltrieve", "maltrieve"],
        },
        {
            'name': 'malware-check-tool',
            'description': "Python script that detects malicious files via checking md5 hashes from an offline set or via the virustotal site. It has http proxy support and an update feature.",
            'aliases': ["malware-check-tool", "malware check tool"],
        },
        {
            'name': 'noriben',
            'description': "Portable, Simple, Malware Analysis Sandbox.",
            'aliases': ["noriben", "noriben"],
        },
        {
            'name': 'origami',
            'description': "Aims at providing a scripting tool to generate and analyze malicious PDF files.",
            'aliases': ["origami", "origami"],
        },
        {
            'name': 'peframe',
            'description': "Tool to perform static analysis on (portable executable) malware.",
            'aliases': ["peframe", "peframe"],
        },
        {
            'name': 'pepper',
            'description': "An open source script to perform malware static analysis on Portable Executable.",
            'aliases': ["pepper", "pepper"],
        },
        {
            'name': 'pftriage',
            'description': "Python tool and library to help analyze files during malware triage and analysis.",
            'aliases': ["pftriage", "pftriage"],
        },
        {
            'name': 'polyswarm',
            'description': "An interface to the public and private PolySwarm APIs.",
            'aliases': ["polyswarm", "polyswarm"],
        },
        {
            'name': 'pyew',
            'description': "A python tool to analyse malware.",
            'aliases': ["pyew", "pyew"],
        },
        {
            'name': 'python-mmbot',
            'description': "Powerful malicious file triage tool for cyber responders.",
            'aliases': ["python-mmbot", "python mmbot"],
        },
        {
            'name': 'sea',
            'description': "A tool to help to create exploits of binary programs.",
            'aliases': ["sea", "sea"],
        },
        {
            'name': 'ssma',
            'description': "Simple Static Malware Analyzer.",
            'aliases': ["ssma", "ssma"],
        },
        {
            'name': 'thezoo',
            'description': "A project created to make the possibility of malware analysis open and available to the public.",
            'aliases': ["thezoo", "thezoo"],
        },
        {
            'name': 'vba2graph',
            'description': "Generate call graphs from VBA code, for easier analysis of malicious documents.",
            'aliases': ["vba2graph", "vba2graph"],
        },
        {
            'name': 'virustotal',
            'description': "Command-line utility to automatically lookup on VirusTotal all files recursively contained in a directory.",
            'aliases': ["virustotal", "virustotal"],
        },
        {
            'name': 'vmcloak',
            'description': "Automated Virtual Machine Generation and Cloaking for Cuckoo Sandbox.",
            'aliases': ["vmcloak", "vmcloak"],
        },
        {
            'name': 'vt-cli',
            'description': "VirusTotal Command Line Interface.",
            'aliases': ["vt-cli", "vt cli"],
        },
        {
            'name': 'zerowine',
            'description': "Malware Analysis Tool - research project to dynamically analyze the behavior of malware",
            'aliases': ["zerowine", "zerowine"],
        },
    ],

    # Reversing (32 tools)
    'blackarch-reversing': [
        {
            'name': 'android-apktool',
            'description': "A tool for reverse engineering Android apk files.",
            'aliases': ["android-apktool", "android apktool"],
        },
        {
            'name': 'apkstudio',
            'description': "An IDE for decompiling/editing & then recompiling of android application binaries.",
            'aliases': ["apkstudio", "apkstudio"],
        },
        {
            'name': 'binaryninja',
            'description': "A new kind of reversing platform (demo version).",
            'aliases': ["binaryninja", "binaryninja"],
        },
        {
            'name': 'ctypes-sh',
            'description': "Allows you to call routines in shared libraries from within bash.",
            'aliases': ["ctypes-sh", "ctypes sh"],
        },
        {
            'name': 'elidecode',
            'description': "A tool to decode obfuscated shellcodes using the unicorn-engine for the emulation and the capstone-engine to print the asm code.",
            'aliases': ["elidecode", "elidecode"],
        },
        {
            'name': 'frida-extract',
            'description': "Frida.re based RunPE (and MapViewOfSection) extraction tool.",
            'aliases': ["frida-extract", "frida extract"],
        },
        {
            'name': 'ghidriff',
            'description': "Python Command-Line Ghidra Binary Diffing Engine.",
            'aliases': ["ghidriff", "ghidriff"],
        },
        {
            'name': 'gostringsr2',
            'description': "Extract strings from a Go binary using radare2.",
            'aliases': ["gostringsr2", "gostringsr2"],
        },
        {
            'name': 'hopper',
            'description': "Reverse engineering tool that lets you disassemble, decompile and debug your applications.",
            'aliases': ["hopper", "hopper"],
        },
        {
            'name': 'ida-free',
            'description': "Freeware version of the world\'s smartest and most feature-full disassembler.",
            'aliases': ["ida-free", "ida free"],
        },
        {
            'name': 'innounp',
            'description': "Inno Setup Unpacker.",
            'aliases': ["innounp", "innounp"],
        },
        {
            'name': 'javasnoop',
            'description': "A tool that lets you intercept methods, alter data and otherwise hack Java applications running on your computer.",
            'aliases': ["javasnoop", "javasnoop"],
        },
        {
            'name': 'jeb-android',
            'description': "Android decompiler.",
            'aliases': ["jeb-android", "jeb android"],
        },
        {
            'name': 'jeb-arm',
            'description': "Arm decompiler.",
            'aliases': ["jeb-arm", "jeb arm"],
        },
        {
            'name': 'jeb-intel',
            'description': "Intel decompiler.",
            'aliases': ["jeb-intel", "jeb intel"],
        },
        {
            'name': 'jeb-mips',
            'description': "Mips decompiler.",
            'aliases': ["jeb-mips", "jeb mips"],
        },
        {
            'name': 'jeb-webasm',
            'description': "WebAssembly decompiler.",
            'aliases': ["jeb-webasm", "jeb webasm"],
        },
        {
            'name': 'jwscan',
            'description': "Scanner for Jar to EXE wrapper like Launch4j, Exe4j, JSmooth, Jar2Exe.",
            'aliases': ["jwscan", "jwscan"],
        },
        {
            'name': 'libc-database',
            'description': "Database of libc offsets to simplify exploitation.",
            'aliases': ["libc-database", "libc database"],
        },
        {
            'name': 'malwasm',
            'description': "Offline debugger for malware\'s reverse engineering.",
            'aliases': ["malwasm", "malwasm"],
        },
        {
            'name': 'mikrotik-npk',
            'description': "Python tools for manipulating Mikrotik NPK format.",
            'aliases': ["mikrotik-npk", "mikrotik npk"],
        },
        {
            'name': 'netzob',
            'description': "An open source tool for reverse engineering, traffic generation and fuzzing of communication protocols.",
            'aliases': ["netzob", "netzob"],
        },
        {
            'name': 'pintool',
            'description': "This tool can be useful for solving some reversing challenges in CTFs events.",
            'aliases': ["pintool", "pintool"],
        },
        {
            'name': 'pintool2',
            'description': "Improved version of pintool.",
            'aliases': ["pintool2", "pintool2"],
        },
        {
            'name': 'pyinstxtractor',
            'description': "PyInstaller Extractor.",
            'aliases': ["pyinstxtractor", "pyinstxtractor"],
        },
        {
            'name': 'python-frida',
            'description': "Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers.",
            'aliases': ["python-frida", "python frida"],
        },
        {
            'name': 'python2-frida',
            'description': "Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers.",
            'aliases': ["python2-frida", "python2 frida"],
        },
        {
            'name': 'radare2-keystone',
            'description': "Keystone assembler plugins for radare2.",
            'aliases': ["radare2-keystone", "radare2 keystone"],
        },
        {
            'name': 'seccomp-tools',
            'description': "Seccomp analysis toolkit.",
            'aliases': ["seccomp-tools", "seccomp tools"],
        },
        {
            'name': 'swfintruder',
            'description': "First tool for testing security in Flash movies. A runtime analyzer for SWF external movies. It helps to find flaws in Flash.",
            'aliases': ["swfintruder", "swfintruder"],
        },
        {
            'name': 'syms2elf',
            'description': "A plugin for Hex-Ray\'s IDA Pro and radare2 to export the symbols recognized to the ELF symbol table.",
            'aliases': ["syms2elf", "syms2elf"],
        },
        {
            'name': 'udis86',
            'description': "A minimalistic disassembler library.",
            'aliases': ["udis86", "udis86"],
        },
    ],

    # Proxy (31 tools)
    'blackarch-proxy': [
        {
            'name': '3proxy',
            'description': "Tiny free proxy server.",
            'aliases': ["3proxy", "3proxy"],
        },
        {
            'name': 'bdfproxy',
            'description': "Patch Binaries via MITM: BackdoorFactory + mitmProxy",
            'aliases': ["bdfproxy", "bdfproxy"],
        },
        {
            'name': 'binproxy',
            'description': "A proxy for arbitrary TCP connections.",
            'aliases': ["binproxy", "binproxy"],
        },
        {
            'name': 'cntlm',
            'description': "An NTLM, NTLM2SR, and NTLMv2 authenticating HTTP proxy.",
            'aliases': ["cntlm", "cntlm"],
        },
        {
            'name': 'datajackproxy',
            'description': "A proxy which allows you to intercept TLS traffic in native x86 applications across platform.",
            'aliases': ["datajackproxy", "datajackproxy"],
        },
        {
            'name': 'dns-reverse-proxy',
            'description': "A reverse DNS proxy written in Go.",
            'aliases': ["dns-reverse-proxy", "dns reverse proxy"],
        },
        {
            'name': 'dnschef',
            'description': "A highly configurable DNS proxy for pentesters.",
            'aliases': ["dnschef", "dnschef"],
        },
        {
            'name': 'elite-proxy-finder',
            'description': "Finds public elite anonymity proxies and concurrently tests them.",
            'aliases': ["elite-proxy-finder", "elite proxy finder"],
        },
        {
            'name': 'fakedns',
            'description': "A regular-expression based python MITM DNS server with correct DNS request passthrough and \"Not Found\" responses.",
            'aliases': ["fakedns", "fakedns"],
        },
        {
            'name': 'fireprox',
            'description': "AWS API Gateway management tool for creating on the fly HTTP pass-through proxies for unique IP rotation.",
            'aliases': ["fireprox", "fireprox"],
        },
        {
            'name': 'jondo',
            'description': "Redirects internet traffic trough a mix of proxy servers to hide the origin of the requests.",
            'aliases': ["jondo", "jondo"],
        },
        {
            'name': 'mallory',
            'description': "HTTP/HTTPS proxy over SSH.",
            'aliases': ["mallory", "mallory"],
        },
        {
            'name': 'mitm-relay',
            'description': "Hackish way to intercept and modify non-HTTP protocols through Burp & others.",
            'aliases': ["mitm-relay", "mitm relay"],
        },
        {
            'name': 'modlishka',
            'description': "A powerful and flexible HTTP reverse proxy.",
            'aliases': ["modlishka", "modlishka"],
        },
        {
            'name': 'mubeng',
            'description': "An incredibly fast proxy checker & IP rotator with ease.",
            'aliases': ["mubeng", "mubeng"],
        },
        {
            'name': 'obfs4proxy',
            'description': "A pluggable transport proxy written in Go.",
            'aliases': ["obfs4proxy", "obfs4proxy"],
        },
        {
            'name': 'pr0cks',
            'description': "python script setting up a transparent proxy to forward all TCP and DNS traffic through a SOCKS / SOCKS5 or HTTP(CONNECT) proxy using iptables -j REDIRECT target.",
            'aliases': ["pr0cks", "pr0cks"],
        },
        {
            'name': 'proxify',
            'description': "Swiss Army knife Proxy tool for HTTP/HTTPS traffic capture, manipulation, and replay on the go.",
            'aliases': ["proxify", "proxify"],
        },
        {
            'name': 'proxyp',
            'description': "Small multithreaded Perl script written to enumerate latency, port numbers, server names, & geolocations of proxy IP addresses.",
            'aliases': ["proxyp", "proxyp"],
        },
        {
            'name': 'redsocks',
            'description': "Transparent redirector of any TCP connection to proxy.",
            'aliases': ["redsocks", "redsocks"],
        },
        {
            'name': 'rpivot',
            'description': "Socks4 reverse proxy for penetration testing.",
            'aliases': ["rpivot", "rpivot"],
        },
        {
            'name': 'sergio-proxy',
            'description': "A multi-threaded transparent HTTP proxy for manipulating web traffic.",
            'aliases': ["sergio-proxy", "sergio proxy"],
        },
        {
            'name': 'soapui',
            'description': "The Swiss-Army Knife for SOAP Testing.",
            'aliases': ["soapui", "soapui"],
        },
        {
            'name': 'sslstrip',
            'description': "Python tool to hijack HTTPS connections during a MITM attack.",
            'aliases': ["sslstrip", "sslstrip"],
        },
        {
            'name': 'ssrf-proxy',
            'description': "Facilitates tunneling HTTP communications through servers vulnerable to Server-Side Request Forgery.",
            'aliases': ["ssrf-proxy", "ssrf proxy"],
        },
        {
            'name': 'starttls-mitm',
            'description': "A mitm proxy that will transparently proxy and dump both plaintext and TLS traffic.",
            'aliases': ["starttls-mitm", "starttls mitm"],
        },
        {
            'name': 'stowaway',
            'description': "A Multi-hop proxy tool for security researchers and pentesters.",
            'aliases': ["stowaway", "stowaway"],
        },
        {
            'name': 'striptls',
            'description': "Proxy PoC implementation of STARTTLS stripping attacks.",
            'aliases': ["striptls", "striptls"],
        },
        {
            'name': 'tftp-proxy',
            'description': "This tool accepts connection on tftp and reloads requested content from an upstream tftp server.",
            'aliases': ["tftp-proxy", "tftp proxy"],
        },
        {
            'name': 'trevorproxy',
            'description': "A SOCKS proxy written in Python that randomizes your source IP address.",
            'aliases': ["trevorproxy", "trevorproxy"],
        },
        {
            'name': 'webfixy',
            'description': "On-the-fly decryption proxy for MikroTik RouterOS WebFig sessions.",
            'aliases': ["webfixy", "webfixy"],
        },
    ],

    # Code Audit (30 tools)
    'blackarch-code-audit': [
        {
            'name': 'bof-detector',
            'description': "A simple detector of BOF vulnerabilities by source-code-level check.",
            'aliases': ["bof-detector", "bof detector"],
        },
        {
            'name': 'brakeman',
            'description': "A static analysis security vulnerability scanner for Ruby on Rails applications.",
            'aliases': ["brakeman", "brakeman"],
        },
        {
            'name': 'cflow',
            'description': "A C program flow analyzer.",
            'aliases': ["cflow", "cflow"],
        },
        {
            'name': 'checkov',
            'description': "Prevent cloud misconfigurations and find vulnerabilities during build-time in infrastructure as code, container images and open source packages.",
            'aliases': ["checkov", "checkov"],
        },
        {
            'name': 'cpptest',
            'description': "A portable and powerful, yet simple, unit testing framework for handling automated tests in C++.",
            'aliases': ["cpptest", "cpptest"],
        },
        {
            'name': 'dependency-check',
            'description': "A tool that attempts to detect publicly disclosed vulnerabilities contained within a project\'s dependencies.",
            'aliases': ["dependency-check", "dependency check"],
        },
        {
            'name': 'detect-secrets',
            'description': "An enterprise friendly way of detecting and preventing secrets in code.",
            'aliases': ["detect-secrets", "detect secrets"],
        },
        {
            'name': 'devaudit',
            'description': "An open-source, cross-platform, multi-purpose security auditing tool targeted at developers and teams.",
            'aliases': ["devaudit", "devaudit"],
        },
        {
            'name': 'githound',
            'description': "Find secret information in git repositories.",
            'aliases': ["githound", "git hound"],
        },
        {
            'name': 'graudit',
            'description': "Grep rough source code auditing tool.",
            'aliases': ["graudit", "graudit"],
        },
        {
            'name': 'horusec',
            'description': "Static code analysis to identify security flaws for many languages.",
            'aliases': ["horusec", "horusec"],
        },
        {
            'name': 'local-php-security-checker',
            'description': "A command line tool that checks your PHP application packages with known security vulnerabilities.",
            'aliases': ["local-php-security-checker", "local php security checker"],
        },
        {
            'name': 'mosca',
            'description': "Static analysis tool to find bugs like a grep unix command.",
            'aliases': ["mosca", "mosca"],
        },
        {
            'name': 'njsscan',
            'description': "A static application testing (SAST) tool that can find insecure code patterns in your node.js applications.",
            'aliases': ["njsscan", "njsscan"],
        },
        {
            'name': 'phpstan',
            'description': "PHP Static Analysis Tool - discover bugs in your code without running it.",
            'aliases': ["phpstan", "phpstan"],
        },
        {
            'name': 'pscan',
            'description': "A limited problem scanner for C source files",
            'aliases': ["pscan", "pscan"],
        },
        {
            'name': 'rats',
            'description': "A rough auditing tool for security in source code files.",
            'aliases': ["rats", "rats"],
        },
        {
            'name': 'semgrep',
            'description': "Lightweight static analysis for many languages.",
            'aliases': ["semgrep", "semgrep"],
        },
        {
            'name': 'slither',
            'description': "Solidity static analysis framework written in Python 3.",
            'aliases': ["slither", "slither"],
        },
        {
            'name': 'snyk',
            'description': "CLI and build-time tool to find and fix known vulnerabilities in open-source dependencies.",
            'aliases': ["snyk", "snyk"],
        },
        {
            'name': 'sonar-scanner',
            'description': "Generic CLI tool to launch project analysis on SonarQube servers.",
            'aliases': ["sonar-scanner", "sonar scanner"],
        },
        {
            'name': 'spotbugs',
            'description': "A tool for static analysis to look for bugs in Java code.",
            'aliases': ["spotbugs", "spotbugs"],
        },
        {
            'name': 'stoq',
            'description': "An open source framework for enterprise level automated analysis.",
            'aliases': ["stoq", "stoq"],
        },
        {
            'name': 'tell-me-your-secrets',
            'description': "Find secrets on any machine from over 120 Different Signatures.",
            'aliases': ["tell-me-your-secrets", "tell me your secrets"],
        },
        {
            'name': 'trufflehog',
            'description': "Searches through git repositories for high entropy strings, digging deep into commit history.",
            'aliases': ["trufflehog", "truffle hog"],
        },
        {
            'name': 'whispers',
            'description': "Identify hardcoded secrets in static structured text.",
            'aliases': ["whispers", "whispers"],
        },
        {
            'name': 'wpbullet',
            'description': "A static code analysis for WordPress (and PHP).",
            'aliases': ["wpbullet", "wpbullet"],
        },
        {
            'name': 'wscript',
            'description': "Emulator/tracer of the Windows Script Host functionality.",
            'aliases': ["wscript", "wscript"],
        },
        {
            'name': 'yasca',
            'description': "Multi-Language Static Analysis Toolset.",
            'aliases': ["yasca", "yasca"],
        },
        {
            'name': 'zarn',
            'description': "A lightweight static security analysis tool for modern Perl Apps.",
            'aliases': ["zarn", "zarn"],
        },
    ],

    # Fingerprinting (30 tools)
    'blackarch-fingerprint': [
        {
            'name': 'asp-audit',
            'description': "An ASP fingerprinting tool and vulnerability scanner.",
            'aliases': ["asp-audit", "asp audit"],
        },
        {
            'name': 'blindelephant',
            'description': "A web application fingerprinter. Attempts to discover the version of a (known) web application by comparing static files at known locations",
            'aliases': ["blindelephant", "blindelephant"],
        },
        {
            'name': 'cms-explorer',
            'description': "Designed to reveal the specific modules, plugins, components and themes that various cms driven websites are running.",
            'aliases': ["cms-explorer", "cms explorer"],
        },
        {
            'name': 'detectem',
            'description': "Detect software and its version on websites.",
            'aliases': ["detectem", "detectem"],
        },
        {
            'name': 'dhcpf',
            'description': "Passive DHCP fingerprinting implementation.",
            'aliases': ["dhcpf", "dhcpf"],
        },
        {
            'name': 'dnsmap',
            'description': "Passive DNS network mapper.",
            'aliases': ["dnsmap", "dnsmap"],
        },
        {
            'name': 'fl0p',
            'description': "A passive L7 flow fingerprinter that examines TCP/UDP/ICMP packet sequences, can peek into cryptographic tunnels, can tell human beings and robots apart, and performs a couple of other infosec-related tricks.",
            'aliases': ["fl0p", "fl0p"],
        },
        {
            'name': 'fpdns',
            'description': "Program that remotely determines DNS server versions.",
            'aliases': ["fpdns", "fpdns"],
        },
        {
            'name': 'ftpmap',
            'description': "Scans remote FTP servers to identify what software and what versions they are running.",
            'aliases': ["ftpmap", "ftpmap"],
        },
        {
            'name': 'htrosbif',
            'description': "Active HTTP server fingerprinting and recon tool.",
            'aliases': ["htrosbif", "htrosbif"],
        },
        {
            'name': 'httprint',
            'description': "A web server fingerprinting tool.",
            'aliases': ["httprint", "httprint"],
        },
        {
            'name': 'kolkata',
            'description': "A web application fingerprinting engine written in Perl that combines cryptography with IDS evasion.",
            'aliases': ["kolkata", "kolkata"],
        },
        {
            'name': 'lbmap',
            'description': "Proof of concept scripts for advanced web application fingerprinting, presented at OWASP AppSecAsia 2012.",
            'aliases': ["lbmap", "lbmap"],
        },
        {
            'name': 'mercury',
            'description': "Network metadata capture and analysis.",
            'aliases': ["mercury", "mercury"],
        },
        {
            'name': 'mwebfp',
            'description': "Mass Web Fingerprinter.",
            'aliases': ["mwebfp", "mwebfp"],
        },
        {
            'name': 'neighbor-cache-fingerprinter',
            'description': "An ARP based Operating System version scanner.",
            'aliases': ["neighbor-cache-fingerprinter", "neighbor cache fingerprinter"],
        },
        {
            'name': 'nerva',
            'description': "Fast service fingerprinting CLI for 170+ protocols (TCP/UDP/SCTP).",
            'aliases': ["nerva", "nerva"],
        },
        {
            'name': 'nimbostratus',
            'description': "Tools for fingerprintinging and exploiting Amazon cloud infrastructures.",
            'aliases': ["nimbostratus", "nimbostratus"],
        },
        {
            'name': 'ntp-fingerprint',
            'description': "An active fingerprinting utility specifically designed to identify the OS the NTP server is running on.",
            'aliases': ["ntp-fingerprint", "ntp fingerprint"],
        },
        {
            'name': 'operative',
            'description': "Framework based on fingerprint action, this tool is used for get information on a website or a enterprise target with multiple modules (Viadeo search,Linkedin search, Reverse email whois, Reverse ip whois, SQL file forensics ...).",
            'aliases': ["operative", "operative"],
        },
        {
            'name': 'scannerl',
            'description': "The modular distributed fingerprinting engine.",
            'aliases': ["scannerl", "scannerl"],
        },
        {
            'name': 'sinfp',
            'description': "A full operating system stack fingerprinting suite.",
            'aliases': ["sinfp", "sinfp"],
        },
        {
            'name': 'smtpmap',
            'description': "Tool to identify the running smtp software on a given host.",
            'aliases': ["smtpmap", "smtpmap"],
        },
        {
            'name': 'smtpscan',
            'description': "An SMTP scanner",
            'aliases': ["smtpscan", "smtpscan"],
        },
        {
            'name': 'spartan',
            'description': "Frontpage and Sharepoint fingerprinting and attack tool.",
            'aliases': ["spartan", "spartan"],
        },
        {
            'name': 'thcrut',
            'description': "Network discovery and OS Fingerprinting tool.",
            'aliases': ["thcrut", "thcrut"],
        },
        {
            'name': 'tls-fingerprinting',
            'description': "Tool and scripts to perform TLS Fingerprinting.",
            'aliases': ["tls-fingerprinting", "tls fingerprinting"],
        },
        {
            'name': 'tls-prober',
            'description': "A tool to fingerprint SSL/TLS servers.",
            'aliases': ["tls-prober", "tls prober"],
        },
        {
            'name': 'xprobe2',
            'description': "An active OS fingerprinting tool.",
            'aliases': ["xprobe2", "xprobe2"],
        },
        {
            'name': 'zgrab2',
            'description': "Fast Application Layer Scanner.",
            'aliases': ["zgrab2", "zgrab2"],
        },
    ],

    # Radio/SDR (30 tools)
    'blackarch-radio': [
        {
            'name': 'airspyhf',
            'description': "Host code for AirspyHF+ SDR.",
            'aliases': ["airspyhf", "airspyhf"],
        },
        {
            'name': 'aptdec',
            'description': "NOAA APT satellite imagery decoder.",
            'aliases': ["aptdec", "aptdec"],
        },
        {
            'name': 'csdr',
            'description': "A simple DSP library and command-line tool for Software Defined Radio.",
            'aliases': ["csdr", "csdr"],
        },
        {
            'name': 'cubicsdr',
            'description': "Cross-Platform Software-Defined Radio Application.",
            'aliases': ["cubicsdr", "cubicsdr"],
        },
        {
            'name': 'deskhpsdr',
            'description': "SDR App for HPSDR protocol and Soapy-API.",
            'aliases': ["deskhpsdr", "deskhpsdr"],
        },
        {
            'name': 'gpredict',
            'description': "A real-time satellite tracking and orbit prediction application.",
            'aliases': ["gpredict", "gpredict"],
        },
        {
            'name': 'gps-sdr-sim',
            'description': "Software-Defined GPS Signal Simulator.",
            'aliases': ["gps-sdr-sim", "gps sdr sim"],
        },
        {
            'name': 'gqrx-scanner',
            'description': "A frequency scanner for Gqrx Software Defined Radio receiver.",
            'aliases': ["gqrx-scanner", "gqrx scanner"],
        },
        {
            'name': 'gr-air-modes',
            'description': "Gnuradio tools for receiving Mode S transponder signals, including ADS-B.",
            'aliases': ["gr-air-modes", "gr air modes"],
        },
        {
            'name': 'gr-dect2',
            'description': "Real-time DECT voice channel decoding by Gnuradio.",
            'aliases': ["gr-dect2", "gr dect2"],
        },
        {
            'name': 'gr-gsm',
            'description': "Gnuradio blocks and tools for receiving GSM transmissions.",
            'aliases': ["gr-gsm", "gnuradio gsm"],
        },
        {
            'name': 'gr-paint',
            'description': "An OFDM Spectrum Painter for GNU Radio.",
            'aliases': ["gr-paint", "gr paint"],
        },
        {
            'name': 'gsmevil2',
            'description': "Python web-based tool which use for capturing imsi numbers and sms.",
            'aliases': ["gsmevil2", "gsmevil2"],
        },
        {
            'name': 'hacktv',
            'description': "Analogue TV transmitter for the HackRF.",
            'aliases': ["hacktv", "hacktv"],
        },
        {
            'name': 'libosmocore',
            'description': "Collection of common code used in various sub-projects inside the Osmocom family of projects.",
            'aliases': ["libosmocore", "libosmocore"],
        },
        {
            'name': 'lte-cell-scanner',
            'description': "An OpenCL accelerated TDD/FDD LTE Scanner.",
            'aliases': ["lte-cell-scanner", "lte cell scanner"],
        },
        {
            'name': 'openwebrx',
            'description': "Open source, multi-user SDR receiver software with a web interface.",
            'aliases': ["openwebrx", "openwebrx"],
        },
        {
            'name': 'qradiolink',
            'description': "Multimode SDR transceiver for GNU radio, ADALM-Pluto, LimeSDR, USRP.",
            'aliases': ["qradiolink", "qradiolink"],
        },
        {
            'name': 'rfcat',
            'description': "Swiss-army knife of ISM band radio.",
            'aliases': ["rfcat", "rfcat"],
        },
        {
            'name': 'rtl',
            'description': "A generic software defined radio data receiver, mainly for the 433.92 MHz, 868 MHz (SRD), 315 MHz, 345 MHz, and 915 MHz ISM bands.",
            'aliases': ["rtl", "rtl"],
        },
        {
            'name': 'rtl-wmbus',
            'description': "Software defined receiver for wireless M-Bus with RTL-SDR.",
            'aliases': ["rtl-wmbus", "rtl wmbus"],
        },
        {
            'name': 'rtlamr',
            'description': "An rtl-sdr receiver for smart meters operating in the 900MHz ISM band.",
            'aliases': ["rtlamr", "rtlamr"],
        },
        {
            'name': 'sdrangel',
            'description': "Qt6/OpenGL SDR and signal analyzer frontend.",
            'aliases': ["sdrangel", "sdrangel"],
        },
        {
            'name': 'sdrpp',
            'description': "The bloat-free SDR receiver.",
            'aliases': ["sdrpp", "sdrpp"],
        },
        {
            'name': 'sdrsharp',
            'description': "The most popular SDR program.",
            'aliases': ["sdrsharp", "sdrsharp"],
        },
        {
            'name': 'sdrtrunk',
            'description': "A cross-platform java application for decoding, monitoring, recording and streaming trunked mobile and related radio protocols using SDR.",
            'aliases': ["sdrtrunk", "sdrtrunk"],
        },
        {
            'name': 'simtrace2',
            'description': "Host utilities to communicate with SIMtrace2 USB Devices.",
            'aliases': ["simtrace2", "simtrace2"],
        },
        {
            'name': 'spektrum',
            'description': "rtl-sdr spectrum analyzer.",
            'aliases': ["spektrum", "spektrum"],
        },
        {
            'name': 'wmbusmeters',
            'description': "Read the wired or wireless mbus protocol to acquire utility meter readings.",
            'aliases': ["wmbusmeters", "wmbusmeters"],
        },
        {
            'name': 'yate-bts',
            'description': "An open source GSM Base Station software.",
            'aliases': ["yate-bts", "yate bts"],
        },
    ],

    # Denial of Service (27 tools)
    'blackarch-dos': [
        {
            'name': '42zip',
            'description': "Recursive Zip archive bomb.",
            'aliases': ["42zip", "42zip"],
        },
        {
            'name': 'blacknurse',
            'description': "A low bandwidth ICMP attack that is capable of doing denial of service to well known firewalls.",
            'aliases': ["blacknurse", "blacknurse"],
        },
        {
            'name': 'bonesi',
            'description': "The DDoS Botnet Simulator.",
            'aliases': ["bonesi", "bonesi"],
        },
        {
            'name': 'davoset',
            'description': "A tool for using Abuse of Functionality and XML External Entities vulnerabilities on some websites to attack other websites.",
            'aliases': ["davoset", "davoset"],
        },
        {
            'name': 'ddosify',
            'description': "High-performance load testing tool, written in Golang.",
            'aliases': ["ddosify", "ddosify"],
        },
        {
            'name': 'dnsdrdos',
            'description': "Proof of concept code for distributed DNS reflection DoS.",
            'aliases': ["dnsdrdos", "dnsdrdos"],
        },
        {
            'name': 'goldeneye',
            'description': "A HTTP DoS test tool. Attack Vector exploited: HTTP Keep Alive + NoCache.",
            'aliases': ["goldeneye", "goldeneye"],
        },
        {
            'name': 'hulk',
            'description': "A webserver DoS tool (Http Unbearable Load King) ported to Go with some additional features.",
            'aliases': ["hulk", "hulk"],
        },
        {
            'name': 'iaxflood',
            'description': "IAX flooder.",
            'aliases': ["iaxflood", "iaxflood"],
        },
        {
            'name': 'impulse',
            'description': "Modern Denial-of-service ToolKit.",
            'aliases': ["impulse", "impulse"],
        },
        {
            'name': 'inviteflood',
            'description': "Flood a device with INVITE requests.",
            'aliases': ["inviteflood", "inviteflood"],
        },
        {
            'name': 'mausezahn',
            'description': "A free fast traffic generator written in C which allows you to send nearly every possible and impossible packet.",
            'aliases': ["mausezahn", "mausezahn"],
        },
        {
            'name': 'network-app-stress-tester',
            'description': "Network Application Stress Testing Yammer.",
            'aliases': ["network-app-stress-tester", "network app stress tester"],
        },
        {
            'name': 'nkiller2',
            'description': "A TCP exhaustion/stressing tool.",
            'aliases': ["nkiller2", "nkiller2"],
        },
        {
            'name': 'ntpdos',
            'description': "PoC for distributed NTP reflection DoS (CVE-5211)",
            'aliases': ["ntpdos", "ntpdos"],
        },
        {
            'name': 'phpstress',
            'description': "A PHP denial of service / stress test for Web Servers running PHP-FPM or PHP-CGI.",
            'aliases': ["phpstress", "phpstress"],
        },
        {
            'name': 'pwnloris',
            'description': "An improved slowloris DOS tool which keeps attacking until the server starts getting exhausted.",
            'aliases': ["pwnloris", "pwnloris"],
        },
        {
            'name': 'shitflood',
            'description': "A Socks5 clone flooder for the Internet Relay Chat (IRC) protocol.",
            'aliases': ["shitflood", "shitflood"],
        },
        {
            'name': 'slowloris',
            'description': "A tool which is written in perl to test http-server vulnerabilities for connection exhaustion denial of service (DoS) attacks so you can enhance the security of your webserver.",
            'aliases': ["slowloris", "slowloris"],
        },
        {
            'name': 'slowloris-py',
            'description': "Low bandwidth DoS tool.",
            'aliases': ["slowloris-py", "slowloris py"],
        },
        {
            'name': 'synflood',
            'description': "A very simply script to illustrate DoS SYN Flooding attack.",
            'aliases': ["synflood", "synflood"],
        },
        {
            'name': 't50',
            'description': "Experimental Multi-protocol Packet Injector Tool.",
            'aliases': ["t50", "t50"],
        },
        {
            'name': 'tcgetkey',
            'description': "A set of tools that deal with acquiring physical memory dumps via FireWire and then scan the memory dump to locate TrueCrypt keys and finally decrypt the encrypted TrueCrypt container using the keys.",
            'aliases': ["tcgetkey", "tcgetkey"],
        },
        {
            'name': 'thc-ssl-dos',
            'description': "A tool to verify the performance of SSL. To be used in your authorized and legitimate area ONLY. You need to accept this to make use of it, no use for bad intentions, you have been warned!",
            'aliases': ["thc-ssl-dos", "thc ssl dos"],
        },
        {
            'name': 'torshammer',
            'description': "A slow POST Denial of Service testing tool written in Python.",
            'aliases': ["torshammer", "torshammer"],
        },
        {
            'name': 'ufonet',
            'description': "A tool designed to launch DDoS attacks against a target, using \'Open Redirect\' vectors on third party web applications, like botnet.",
            'aliases': ["ufonet", "ufonet"],
        },
        {
            'name': 'wreckuests',
            'description': "Yet another one hard-hitting tool to run DDoS attacks with HTTP-flood.",
            'aliases': ["wreckuests", "wreckuests"],
        },
    ],

    # Bluetooth (26 tools)
    'blackarch-bluetooth': [
        {
            'name': 'blue-hydra',
            'description': "A Bluetooth device discovery service built on top of the bluez library.",
            'aliases': ["blue-hydra", "blue hydra"],
        },
        {
            'name': 'bluebugger',
            'description': "An implementation of the bluebug technique which was discovered by Martin Herfurt.",
            'aliases': ["bluebugger", "bluebugger"],
        },
        {
            'name': 'bluediving',
            'description': "A Bluetooth penetration testing suite.",
            'aliases': ["bluediving", "bluediving"],
        },
        {
            'name': 'bluefog',
            'description': "A tool that can generate an essentially unlimited number of phantom Bluetooth devices.",
            'aliases': ["bluefog", "bluefog"],
        },
        {
            'name': 'bluelog',
            'description': "A Bluetooth scanner and sniffer written to do a single task, log devices that are in discoverable mode.",
            'aliases': ["bluelog", "blue log"],
        },
        {
            'name': 'bluepot',
            'description': "A Bluetooth Honeypot written in Java, it runs on Linux.",
            'aliases': ["bluepot", "bluepot"],
        },
        {
            'name': 'blueprint',
            'description': "A perl tool to identify Bluetooth devices.",
            'aliases': ["blueprint", "blueprint"],
        },
        {
            'name': 'bluescan',
            'description': "A Bluetooth Device Scanner.",
            'aliases': ["bluescan", "bluescan"],
        },
        {
            'name': 'bluesnarfer',
            'description': "A bluetooth attacking tool.",
            'aliases': ["bluesnarfer", "blue snarfer"],
        },
        {
            'name': 'bluphish',
            'description': "Bluetooth device and service discovery tool that can be used for security assessment and penetration testing.",
            'aliases': ["bluphish", "bluphish"],
        },
        {
            'name': 'braces',
            'description': "A Bluetooth Tracking Utility.",
            'aliases': ["braces", "braces"],
        },
        {
            'name': 'bss',
            'description': "Bluetooth stack smasher / fuzzer.",
            'aliases': ["bss", "bss"],
        },
        {
            'name': 'bt_audit',
            'description': "Bluetooth audit",
            'aliases': ["bt_audit", "bt audit"],
        },
        {
            'name': 'btcrack',
            'description': "The world\'s first Bluetooth Pass phrase (PIN) bruteforce tool. Bruteforces the Passkey and the Link key from captured Pairing exchanges.",
            'aliases': ["btcrack", "btcrack"],
        },
        {
            'name': 'btlejack',
            'description': "Bluetooth Low Energy Swiss-army knife.",
            'aliases': ["btlejack", "btlejack"],
        },
        {
            'name': 'btproxy-mitm',
            'description': "Man in the Middle analysis tool for Bluetooth.",
            'aliases': ["btproxy-mitm", "btproxy mitm"],
        },
        {
            'name': 'btscanner',
            'description': "Bluetooth device scanner.",
            'aliases': ["btscanner", "bt scanner"],
        },
        {
            'name': 'carwhisperer',
            'description': "Sensibilise manufacturers of carkits and other Bluetooth appliances without display and keyboard for the possible security threat evolving from the use of standard passkeys.",
            'aliases': ["carwhisperer", "carwhisperer"],
        },
        {
            'name': 'ghettotooth',
            'description': "Ghettodriving for bluetooth.",
            'aliases': ["ghettotooth", "ghettotooth"],
        },
        {
            'name': 'hidattack',
            'description': "HID Attack (attacking HID host implementations).",
            'aliases': ["hidattack", "hidattack"],
        },
        {
            'name': 'obexstress',
            'description': "Script for testing remote OBEX service for some potential vulnerabilities.",
            'aliases': ["obexstress", "obexstress"],
        },
        {
            'name': 'redfang',
            'description': "Finds non-discoverable Bluetooth devices by brute-forcing the last six bytes of the devices\' Bluetooth addresses and calling read_remote_name().",
            'aliases': ["redfang", "redfang"],
        },
        {
            'name': 'sparrow-wifi',
            'description': "Next-Gen GUI-based WiFi and Bluetooth Analyzer.",
            'aliases': ["sparrow-wifi", "sparrow wifi"],
        },
        {
            'name': 'spooftooph',
            'description': "Designed to automate spoofing or cloning Bluetooth device Name, Class, and Address. Cloning this information effectively allows Bluetooth device to hide in plain sight.",
            'aliases': ["spooftooph", "spooftooph"],
        },
        {
            'name': 'tbear',
            'description': "Transient Bluetooth Environment Auditor includes an ncurses-based Bluetooth scanner (a bit similar to kismet), a Bluetooth DoS tool, and a Bluetooth hidden device locator.",
            'aliases': ["tbear", "tbear"],
        },
        {
            'name': 'ubertooth',
            'description': "A 2.4 GHz wireless development board suitable for Bluetooth experimentation. Open source hardware and software. Tools only.",
            'aliases': ["ubertooth", "uber tooth"],
        },
    ],

    # VoIP (22 tools)
    'blackarch-voip': [
        {
            'name': 'ace',
            'description': "A simple yet powerful VoIP Corporate Directory enumeration tool that mimics the behavior of an IP Phone in order to download the name and extension entries that a given phone can display on its screen interface.",
            'aliases': ["ace", "ace"],
        },
        {
            'name': 'bluebox-ng',
            'description': "A GPL VoIP/UC vulnerability scanner.",
            'aliases': ["bluebox-ng", "bluebox ng"],
        },
        {
            'name': 'erase-registrations',
            'description': "An IAX flooder.",
            'aliases': ["erase-registrations", "erase registrations"],
        },
        {
            'name': 'ilty',
            'description': "An interception phone system for VoIP network.",
            'aliases': ["ilty", "ilty"],
        },
        {
            'name': 'isip',
            'description': "Interactive sip toolkit for packet manipulations, sniffing, man in the middle attacks, fuzzing, simulating of dos attacks.",
            'aliases': ["isip", "isip"],
        },
        {
            'name': 'isme',
            'description': "Scans a VOIP environment, adapts to enterprise VOIP, and exploits the possibilities of being connected directly to an IP Phone VLAN.",
            'aliases': ["isme", "isme"],
        },
        {
            'name': 'mrsip',
            'description': "SIP-Based Audit and Attack Tool.",
            'aliases': ["mrsip", "mrsip"],
        },
        {
            'name': 'pcapsipdump',
            'description': "A tool for dumping SIP sessions (+RTP traffic, if available) to disk in a fashion similar to \'tcpdump -w\' (format is exactly the same), but one file per sip session (even if there is thousands of concurrent SIP sessions).",
            'aliases': ["pcapsipdump", "pcapsipdump"],
        },
        {
            'name': 'protos-sip',
            'description': "SIP test suite.",
            'aliases': ["protos-sip", "protos sip"],
        },
        {
            'name': 'redirectpoison',
            'description': "A tool to poison a targeted issuer of SIP INVITE requests with 301 (i.e. Moved Permanently) redirection responses.",
            'aliases': ["redirectpoison", "redirectpoison"],
        },
        {
            'name': 'rtp-flood',
            'description': "RTP flooder",
            'aliases': ["rtp-flood", "rtp flood"],
        },
        {
            'name': 'siparmyknife',
            'description': "A small command line tool for developers and administrators of Session Initiation Protocol (SIP) applications.",
            'aliases': ["siparmyknife", "siparmyknife"],
        },
        {
            'name': 'sipbrute',
            'description': "A utility to perform dictionary attacks against the VoIP SIP Register hash.",
            'aliases': ["sipbrute", "sipbrute"],
        },
        {
            'name': 'sipp',
            'description': "A free Open Source test tool / traffic generator for the SIP protocol.",
            'aliases': ["sipp", "sipp"],
        },
        {
            'name': 'sippts',
            'description': "Set of tools to audit SIP based VoIP Systems.",
            'aliases': ["sippts", "sippts"],
        },
        {
            'name': 'sipsak',
            'description': "A small command line tool for developers and administrators of Session Initiation Protocol (SIP) applications.",
            'aliases': ["sipsak", "sipsak"],
        },
        {
            'name': 'storm-ring',
            'description': "This simple tool is useful to test a PABX with \"allow guest\" parameter set to \"yes\" (in this scenario an anonymous caller could place a call).",
            'aliases': ["storm-ring", "storm ring"],
        },
        {
            'name': 'teardown',
            'description': "Command line tool to send a BYE request to tear down a call.",
            'aliases': ["teardown", "teardown"],
        },
        {
            'name': 'vnak',
            'description': "Aim is to be the one tool a user needs to attack multiple VoIP protocols.",
            'aliases': ["vnak", "vnak"],
        },
        {
            'name': 'voiper',
            'description': "A VoIP security testing toolkit incorporating several VoIP fuzzers and auxiliary tools to assist the auditor.",
            'aliases': ["voiper", "voiper"],
        },
        {
            'name': 'voipong',
            'description': "A utility which detects all Voice Over IP calls on a pipeline, and for those which are G711 encoded, dumps actual conversation to separate wave files.",
            'aliases': ["voipong", "voipong"],
        },
        {
            'name': 'vsaudit',
            'description': "VOIP Security Audit Framework.",
            'aliases': ["vsaudit", "vsaudit"],
        },
    ],

    # Decompiler (18 tools)
    'blackarch-decompiler': [
        {
            'name': 'avaloniailspy',
            'description': ".NET Decompiler (port of ILSpy)",
            'aliases': ["avaloniailspy", "avaloniailspy"],
        },
        {
            'name': 'beebug',
            'description': "A tool for checking exploitability.",
            'aliases': ["beebug", "beebug"],
        },
        {
            'name': 'cafebabe',
            'description': "Java bytecode editor & decompiler.",
            'aliases': ["cafebabe", "cafebabe"],
        },
        {
            'name': 'fernflower',
            'description': "An analytical decompiler for Java.",
            'aliases': ["fernflower", "fernflower"],
        },
        {
            'name': 'flasm',
            'description': "Disassembler tool for SWF bytecode.",
            'aliases': ["flasm", "flasm"],
        },
        {
            'name': 'gadgetinspector',
            'description': "A byte code analyzer for finding deserialization gadget chains in Java applications.",
            'aliases': ["gadgetinspector", "gadgetinspector"],
        },
        {
            'name': 'jbe',
            'description': "Java bytecode editor suitable for viewing and modifying java class files.",
            'aliases': ["jbe", "jbe"],
        },
        {
            'name': 'jd-cli',
            'description': "Command line Java Decompiler.",
            'aliases': ["jd-cli", "jd cli"],
        },
        {
            'name': 'jd-gui',
            'description': "A standalone graphical utility that displays Java source codes of .class files.",
            'aliases': ["jd-gui", "jd gui"],
        },
        {
            'name': 'jpexs-decompiler',
            'description': "JPEXS Free Flash Decompiler.",
            'aliases': ["jpexs-decompiler", "jpexs decompiler"],
        },
        {
            'name': 'luyten',
            'description': "An Open Source Java Decompiler Gui for Procyon.",
            'aliases': ["luyten", "luyten"],
        },
        {
            'name': 'pcode2code',
            'description': "VBA p-code decompiler.",
            'aliases': ["pcode2code", "pcode2code"],
        },
        {
            'name': 'procyon',
            'description': "A suite of Java metaprogramming tools focused on code generation and analysis.",
            'aliases': ["procyon", "procyon"],
        },
        {
            'name': 'python-uncompyle6',
            'description': "A Python cross-version decompiler.",
            'aliases': ["python-uncompyle6", "python uncompyle6"],
        },
        {
            'name': 'recaf',
            'description': "Modern Java bytecode editor.",
            'aliases': ["recaf", "recaf"],
        },
        {
            'name': 'rej',
            'description': "An API and a graphical tool for inspection and manipulation of classfiles for the Java platform.",
            'aliases': ["rej", "rej"],
        },
        {
            'name': 'retdec',
            'description': "Retargetable machine-code decompiler based on LLVM.",
            'aliases': ["retdec", "retdec"],
        },
        {
            'name': 'shuji',
            'description': "Reverse engineering JavaScript and CSS sources from sourcemaps.",
            'aliases': ["shuji", "shuji"],
        },
    ],

    # Spoofing (18 tools)
    'blackarch-spoof': [
        {
            'name': 'admid-pack',
            'description': "ADM DNS spoofing tools - Uses a variety of active and passive methods to spoof DNS packets. Very powerful.",
            'aliases': ["admid-pack", "admid pack"],
        },
        {
            'name': 'aranea',
            'description': "A fast and clean dns spoofing tool.",
            'aliases': ["aranea", "aranea"],
        },
        {
            'name': 'arpspoof-smikims',
            'description': "Performs an ARP spoofing attack using the Linux kernel\'s raw sockets.",
            'aliases': ["arpspoof-smikims", "arpspoof smikims"],
        },
        {
            'name': 'cisco-snmp-slap',
            'description': "IP address spoofing tool in order to bypass an ACL protecting an SNMP service on Cisco IOS devices.",
            'aliases': ["cisco-snmp-slap", "cisco snmp slap"],
        },
        {
            'name': 'dns-spoof',
            'description': "Yet another DNS spoof utility.",
            'aliases': ["dns-spoof", "dns spoof"],
        },
        {
            'name': 'evil-ssdp',
            'description': "Spoof SSDP replies to phish for NetNTLM challenge/response on a network.",
            'aliases': ["evil-ssdp", "evil ssdp"],
        },
        {
            'name': 'fakenetbios',
            'description': "A family of tools designed to simulate Windows hosts (NetBIOS) on a LAN.",
            'aliases': ["fakenetbios", "fakenetbios"],
        },
        {
            'name': 'lans',
            'description': "A Multithreaded asynchronous packet parsing/injecting arp spoofer.",
            'aliases': ["lans", "lans"],
        },
        {
            'name': 'lsrtunnel',
            'description': "Spoofs connections using source routed packets.",
            'aliases': ["lsrtunnel", "lsrtunnel"],
        },
        {
            'name': 'mailsend-go',
            'description': "A multi-platform command line tool to send mail via SMTP protocol.",
            'aliases': ["mailsend-go", "mailsend go"],
        },
        {
            'name': 'motsa-dns-spoofing',
            'description': "ManOnTheSideAttack-DNS Spoofing.",
            'aliases': ["motsa-dns-spoofing", "motsa dns spoofing"],
        },
        {
            'name': 'multimac',
            'description': "Multiple MACs on an adapter.",
            'aliases': ["multimac", "multimac"],
        },
        {
            'name': 'nbnspoof',
            'description': "NetBIOS Name Service Spoofer.",
            'aliases': ["nbnspoof", "nbnspoof"],
        },
        {
            'name': 'netcommander',
            'description': "An easy-to-use arp spoofing tool.",
            'aliases': ["netcommander", "netcommander"],
        },
        {
            'name': 'rbndr',
            'description': "Simple DNS Rebinding Service.",
            'aliases': ["rbndr", "rbndr"],
        },
        {
            'name': 'spoofy',
            'description': "Check if a list of domains can be spoofed based on SPF and DMARC records.",
            'aliases': ["spoofy", "spoofy"],
        },
        {
            'name': 'sylkie',
            'description': "IPv6 address spoofing with the Neighbor Discovery Protocol.",
            'aliases': ["sylkie", "sylkie"],
        },
        {
            'name': 'synner',
            'description': "A custom eth->ip->tcp packet generator (spoofer) for testing firewalls and dos attacks.",
            'aliases': ["synner", "synner"],
        },
    ],

    # Tunneling (18 tools)
    'blackarch-tunnel': [
        {
            'name': 'chisel',
            'description': "A fast TCP tunnel over HTTP.",
            'aliases': ["chisel", "chisel"],
        },
        {
            'name': 'chownat',
            'description': "Allows two peers behind two separate NATs with no port forwarding and no DMZ setup on their routers to directly communicate with each other",
            'aliases': ["chownat", "chownat"],
        },
        {
            'name': 'ctunnel',
            'description': "Tunnel and/or proxy TCP or UDP connections via a cryptographic tunnel.",
            'aliases': ["ctunnel", "ctunnel"],
        },
        {
            'name': 'dns2tcp',
            'description': "A tool for relaying TCP connections over DNS.",
            'aliases': ["dns2tcp", "dns2tcp"],
        },
        {
            'name': 'fraud-bridge',
            'description': "ICMP and DNS tunneling via IPv4 and IPv6.",
            'aliases': ["fraud-bridge", "fraud bridge"],
        },
        {
            'name': 'icmptx',
            'description': "IP over ICMP tunnel.",
            'aliases': ["icmptx", "icmptx"],
        },
        {
            'name': 'ip-https-tools',
            'description': "Tools for the IP over HTTPS (IP-HTTPS) Tunneling Protocol.",
            'aliases': ["ip-https-tools", "ip https tools"],
        },
        {
            'name': 'ligolo-ng',
            'description': "An advanced, yet simple, tunneling tool that uses a TUN interface.",
            'aliases': ["ligolo-ng", "ligolo ng"],
        },
        {
            'name': 'matahari',
            'description': "A reverse HTTP shell to execute commands on remote machines behind firewalls.",
            'aliases': ["matahari", "matahari"],
        },
        {
            'name': 'morxtunel',
            'description': "Network Tunneling using TUN/TAP interfaces over TCP tool.",
            'aliases': ["morxtunel", "morxtunel"],
        },
        {
            'name': 'multitun',
            'description': "Tunnel arbitrary traffic through an innocuous WebSocket.",
            'aliases': ["multitun", "multitun"],
        },
        {
            'name': 'neo-regeorg',
            'description': "Improved version of reGeorg, HTTP tunneling pivot tool",
            'aliases': ["neo-regeorg", "neo regeorg"],
        },
        {
            'name': 'ngrok',
            'description': "A tunneling, reverse proxy for developing and understanding networked, HTTP services.",
            'aliases': ["ngrok", "ngrok"],
        },
        {
            'name': 'oniongrok',
            'description': "Onion addresses for anything.",
            'aliases': ["oniongrok", "oniongrok"],
        },
        {
            'name': 'regeorg',
            'description': "The successor to reDuh, pwn a bastion webserver and create SOCKS proxies through the DMZ. Pivot and pwn.",
            'aliases': ["regeorg", "regeorg"],
        },
        {
            'name': 'stegosip',
            'description': "TCP tunnel over RTP/SIP.",
            'aliases': ["stegosip", "stegosip"],
        },
        {
            'name': 'vstt',
            'description': "VSTT is a multi-protocol tunneling tool. It accepts input by TCP stream sockets and FIFOs, and can send data via TCP, POP3, and ICMP tunneling.",
            'aliases': ["vstt", "vstt"],
        },
        {
            'name': 'xfltreat',
            'description': "Tunnelling framework.",
            'aliases': ["xfltreat", "xfltreat"],
        },
    ],

    # Disassembler (17 tools)
    'blackarch-disassembler': [
        {
            'name': 'abcd',
            'description': "ActionScript ByteCode Disassembler.",
            'aliases': ["abcd", "abcd"],
        },
        {
            'name': 'binnavi',
            'description': "A binary analysis IDE that allows to inspect, navigate, edit and annotate control flow graphs and call graphs of disassembled code.",
            'aliases': ["binnavi", "binnavi"],
        },
        {
            'name': 'chiasm-shell',
            'description': "Python-based interactive assembler/disassembler CLI, powered byKeystone/Capstone.",
            'aliases': ["chiasm-shell", "chiasm shell"],
        },
        {
            'name': 'exe2hex',
            'description': "Inline file transfer using in-built Windows tools (DEBUG.exe or PowerShell).",
            'aliases': ["exe2hex", "exe2hex"],
        },
        {
            'name': 'libdisasm',
            'description': "A disassembler library.",
            'aliases': ["libdisasm", "libdisasm"],
        },
        {
            'name': 'lief',
            'description': "Library to instrument executable formats.",
            'aliases': ["lief", "lief"],
        },
        {
            'name': 'marc4dasm',
            'description': "A disassembler for the Atmel MARC4 (a 4 bit Harvard micro).",
            'aliases': ["marc4dasm", "marc4dasm"],
        },
        {
            'name': 'plasma-disasm',
            'description': "An interactive disassembler for x86/ARM/MIPS. It can generates indented pseudo-code with colored syntax.",
            'aliases': ["plasma-disasm", "plasma disasm"],
        },
        {
            'name': 'python-lief',
            'description': "Library to instrument executable formats.",
            'aliases': ["python-lief", "python lief"],
        },
        {
            'name': 'python-pcodedmp',
            'description': "A VBA p-code disassembler.",
            'aliases': ["python-pcodedmp", "python pcodedmp"],
        },
        {
            'name': 'python2-capstone',
            'description': "A disassembly framework with the target of becoming the ultimate disasm engine for binary analysis and reversing in the security community.",
            'aliases': ["python2-capstone", "python2 capstone"],
        },
        {
            'name': 'python2-pcodedmp',
            'description': "A VBA p-code disassembler.",
            'aliases': ["python2-pcodedmp", "python2 pcodedmp"],
        },
        {
            'name': 'radare2-unicorn',
            'description': "Unicorn Emulator Plugin for radare2.",
            'aliases': ["radare2-unicorn", "radare2 unicorn"],
        },
        {
            'name': 'redasm',
            'description': "Interactive, multiarchitecture disassembler written in C++ using Qt5 as UI Framework.",
            'aliases': ["redasm", "redasm"],
        },
        {
            'name': 'scratchabit',
            'description': "Easily retargetable and hackable interactive disassembler with IDAPython-compatible plugin API.",
            'aliases': ["scratchabit", "scratchabit"],
        },
        {
            'name': 'unstrip',
            'description': "ELF Unstrip Tool.",
            'aliases': ["unstrip", "unstrip"],
        },
        {
            'name': 'viper',
            'description': "A Binary analysis framework.",
            'aliases': ["viper", "viper"],
        },
    ],

    # Honeypot (16 tools)
    'blackarch-honeypot': [
        {
            'name': 'beeswarm',
            'description': "Honeypot deployment made easy.",
            'aliases': ["beeswarm", "beeswarm"],
        },
        {
            'name': 'conpot',
            'description': "ICS honeypot with the goal to collect intelligence about the motives and methods of adversaries targeting industrial control systems.",
            'aliases': ["conpot", "conpot"],
        },
        {
            'name': 'fakeap',
            'description': "Black Alchemy\'s Fake AP generates thousands of counterfeit 802.11b access points. Hide in plain sight amongst Fake AP\'s cacophony of beacon frames.",
            'aliases': ["fakeap", "fakeap"],
        },
        {
            'name': 'fiked',
            'description': "Fake IDE daemon.",
            'aliases': ["fiked", "fiked"],
        },
        {
            'name': 'heartbleed-honeypot',
            'description': "Script that listens on TCP port 443 and responds with completely bogus SSL heartbeat responses, unless it detects the start of a byte pattern similar to that used in Jared Stafford\'s",
            'aliases': ["heartbleed-honeypot", "heartbleed honeypot"],
        },
        {
            'name': 'honeyd',
            'description': "A small daemon that creates virtual hosts on a network.",
            'aliases': ["honeyd", "honeyd"],
        },
        {
            'name': 'honeypy',
            'description': "A low interaction Honeypot.",
            'aliases': ["honeypy", "honeypy"],
        },
        {
            'name': 'honssh',
            'description': "A high-interaction Honey Pot solution designed to log all SSH communications between a client and server.",
            'aliases': ["honssh", "honssh"],
        },
        {
            'name': 'hpfeeds',
            'description': "Honeynet Project generic authenticated datafeed protocol.",
            'aliases': ["hpfeeds", "hpfeeds"],
        },
        {
            'name': 'kippo',
            'description': "A medium interaction SSH honeypot designed to log brute force attacks and most importantly, the entire shell interaction by the attacker.",
            'aliases': ["kippo", "kippo"],
        },
        {
            'name': 'pshitt',
            'description': "A lightweight fake SSH server designed to collect authentication data sent by intruders.",
            'aliases': ["pshitt", "pshitt"],
        },
        {
            'name': 'python2-hpfeeds',
            'description': "Honeynet Project generic authenticated datafeed protocol.",
            'aliases': ["python2-hpfeeds", "python2 hpfeeds"],
        },
        {
            'name': 'snare',
            'description': "Super Next generation Advanced Reactive honeypot.",
            'aliases': ["snare", "snare"],
        },
        {
            'name': 'ssh-honeypot',
            'description': "Fake sshd that logs ip addresses, usernames, and passwords.",
            'aliases': ["ssh-honeypot", "ssh honeypot"],
        },
        {
            'name': 'wifi-honey',
            'description': "A management tool for wifi honeypots.",
            'aliases': ["wifi-honey", "wifi honey"],
        },
        {
            'name': 'wordpot',
            'description': "A Wordpress Honeypot.",
            'aliases': ["wordpot", "wordpot"],
        },
    ],

    # Steganography (11 tools)
    'blackarch-stego': [
        {
            'name': 'matroschka',
            'description': "Python steganography tool to hide images or text in images.",
            'aliases': ["matroschka", "matroschka"],
        },
        {
            'name': 'openpuff',
            'description': "Yet not another steganography SW.",
            'aliases': ["openpuff", "openpuff"],
        },
        {
            'name': 'pngcheck',
            'description': "Verifies the integrity of PNG, JNG and MNG files by checking the CRCs and decompressing the image data.",
            'aliases': ["pngcheck", "pngcheck"],
        },
        {
            'name': 'silenteye',
            'description': "A cross-platform application design for an easy use of steganography.",
            'aliases': ["silenteye", "silenteye"],
        },
        {
            'name': 'stegcracker',
            'description': "Steganography brute-force utility to uncover hidden data inside files.",
            'aliases': ["stegcracker", "stegcracker"],
        },
        {
            'name': 'stegdetect',
            'description': "An automated tool for detecting steganographic content in images.",
            'aliases': ["stegdetect", "stegdetect"],
        },
        {
            'name': 'stegolego',
            'description': "Simple program for using stegonography to hide data within BMP images.",
            'aliases': ["stegolego", "stegolego"],
        },
        {
            'name': 'stegseek',
            'description': "Lightning fast steghide cracker.",
            'aliases': ["stegseek", "stegseek"],
        },
        {
            'name': 'stegsolve',
            'description': "Steganography Solver.",
            'aliases': ["stegsolve", "stegsolve"],
        },
        {
            'name': 'stepic',
            'description': "A python image steganography tool.",
            'aliases': ["stepic", "stepic"],
        },
        {
            'name': 'zsteg',
            'description': "Detect stegano-hidden data in PNG and BMP.",
            'aliases': ["zsteg", "zsteg"],
        },
    ],

    # Debugger (10 tools)
    'blackarch-debugger': [
        {
            'name': 'edb',
            'description': "A cross platform AArch32/x86/x86 debugger.",
            'aliases': ["edb", "edb"],
        },
        {
            'name': 'electric-fence',
            'description': "A malloc(3) debugger that uses virtual memory hardware to detect illegal memory accesses.",
            'aliases': ["electric-fence", "electric fence"],
        },
        {
            'name': 'gdbgui',
            'description': "Browser-based gdb frontend using Flask and JavaScript to visually debug C, C++, Go, or Rust.",
            'aliases': ["gdbgui", "gdbgui"],
        },
        {
            'name': 'heaptrace',
            'description': "Helps visualize heap operations for pwn and debugging.",
            'aliases': ["heaptrace", "heaptrace"],
        },
        {
            'name': 'ollydbg',
            'description': "A 32-bit assembler-level analysing debugger.",
            'aliases': ["ollydbg", "olly debugger"],
        },
        {
            'name': 'rr',
            'description': "A Record and Replay Framework.",
            'aliases': ["rr", "rr"],
        },
        {
            'name': 'saleae-logic',
            'description': "Debug happy.",
            'aliases': ["saleae-logic", "saleae logic"],
        },
        {
            'name': 'shellnoob',
            'description': "A toolkit that eases the writing and debugging of shellcode.",
            'aliases': ["shellnoob", "shellnoob"],
        },
        {
            'name': 'vivisect',
            'description': "A Python based static analysis and reverse engineering framework.",
            'aliases': ["vivisect", "vivisect"],
        },
        {
            'name': 'voltron',
            'description': "UI for GDB, LLDB and Vivisect\'s VDB.",
            'aliases': ["voltron", "voltron"],
        },
    ],

    # AI/ML (5 tools)
    'blackarch-ai': [
        {
            'name': 'adversarial-robustness-toolbox',
            'description': "Python Library for Machine Learning Security.",
            'aliases': ["adversarial-robustness-toolbox", "adversarial robustness toolbox"],
        },
        {
            'name': 'aimap',
            'description': "Security scanner and fingerprinter for AI/ML infrastructure. Identifies 23 service types including LLMs, vector databases, and model servers.",
            'aliases': ["aimap", "aimap"],
        },
        {
            'name': 'cai',
            'description': "The framework for AI Security.",
            'aliases': ["cai", "cai"],
        },
        {
            'name': 'cleverhans',
            'description': "Python library to benchmark machine learning systems vulnerability to adversarial examples.",
            'aliases': ["cleverhans", "cleverhans"],
        },
        {
            'name': 'promptfoo',
            'description': "Test and evaluate LLM outputs - AI red teaming, pentesting, and vulnerability scanning.",
            'aliases': ["promptfoo", "promptfoo"],
        },
    ],

    # Database (5 tools)
    'blackarch-database': [
        {
            'name': 'blindsql',
            'description': "Set of bash scripts for blind SQL injection attacks.",
            'aliases': ["blindsql", "blindsql"],
        },
        {
            'name': 'getsids',
            'description': "Enumerate Oracle Sids by sending the services command to the Oracle TNS listener.",
            'aliases': ["getsids", "getsids"],
        },
        {
            'name': 'metacoretex',
            'description': "MetaCoretex is an entirely JAVA vulnerability scanning framework for databases.",
            'aliases': ["metacoretex", "metacoretex"],
        },
        {
            'name': 'mysql2sqlite',
            'description': "Converts a mysqldump file into a Sqlite 3 compatible file.",
            'aliases': ["mysql2sqlite", "mysql2sqlite"],
        },
        {
            'name': 'pgdbf',
            'description': "Convert XBase / FoxPro databases to PostgreSQL",
            'aliases': ["pgdbf", "pgdbf"],
        },
    ],

    # Hardware (5 tools)
    'blackarch-hardware': [
        {
            'name': 'chipsec',
            'description': "Platform Security Assessment Framework.",
            'aliases': ["chipsec", "chipsec"],
        },
        {
            'name': 'dex2jar',
            'description': "A tool for converting Android\'s .dex format to Java\'s .class format",
            'aliases': ["dex2jar", "dex2jar"],
        },
        {
            'name': 'hdmi-sniff',
            'description': "HDMI DDC (I2C) inspection tool. It is designed to demonstrate just how easy it is to recover HDCP crypto keys from HDMI devices.",
            'aliases': ["hdmi-sniff", "hdmi sniff"],
        },
        {
            'name': 'kautilya',
            'description': "Pwnage with Human Interface Devices using Teensy++2.0 and Teensy 3.0 devices.",
            'aliases': ["kautilya", "kautilya"],
        },
        {
            'name': 'pcileech',
            'description': "Tool, which uses PCIe hardware devices to read and write from the target system memory.",
            'aliases': ["pcileech", "pcileech"],
        },
    ],

    # Wordlists (5 tools)
    'blackarch-wordlist': [
        {
            'name': 'assetnote-wordlists',
            'description': "Assetnote generated wordlists.",
            'aliases': ["assetnote-wordlists", "assetnote wordlists"],
        },
        {
            'name': 'country-ip-blocks',
            'description': "CIDR country-level IP data, straight from the Regional Internet Registries, updated hourly.",
            'aliases': ["country-ip-blocks", "country ip blocks"],
        },
        {
            'name': 'ldapwordlistharvester',
            'description': "Tool to generate wordlist from information present in LDAP, in order to crack passwords of domain accounts.",
            'aliases': ["ldapwordlistharvester", "ldapwordlistharvester"],
        },
        {
            'name': 'seclists',
            'description': "A collection of multiple types of lists used during security assessments.",
            'aliases': ["seclists", "sec lists", "fuzzdb"],
        },
        {
            'name': 'wdict',
            'description': "Create dictionaries by scraping webpages or crawling local files.",
            'aliases': ["wdict", "wdict"],
        },
    ],

    # Automobile (4 tools)
    'blackarch-automobile': [
        {
            'name': 'can-utils',
            'description': "Linux-CAN / SocketCAN user space applications.",
            'aliases': ["can-utils", "can utils"],
        },
        {
            'name': 'canalyzat0r',
            'description': "Security analysis toolkit for proprietary car protocols.",
            'aliases': ["canalyzat0r", "canalyzat0r"],
        },
        {
            'name': 'cantoolz',
            'description': "Framework for black-box CAN network analysis.",
            'aliases': ["cantoolz", "cantoolz"],
        },
        {
            'name': 'savvycan',
            'description': "QT-based CAN bus analysis tool.",
            'aliases': ["savvycan", "savvycan"],
        },
    ],

    # Drone (4 tools)
    'blackarch-drone': [
        {
            'name': 'crozono',
            'description': "A modular framework designed to automate the penetration testing of wireless networks from drones and such unconventional devices.",
            'aliases': ["crozono", "crozono"],
        },
        {
            'name': 'missionplanner',
            'description': "A GroundControl Station for Ardupilot.",
            'aliases': ["missionplanner", "missionplanner"],
        },
        {
            'name': 'skyjack',
            'description': "Takes over Parrot drones, deauthenticating their true owner and taking over control, turning them into zombie drones under your own control.",
            'aliases': ["skyjack", "skyjack"],
        },
        {
            'name': 'snoopy-ng',
            'description': "A distributed, sensor, data collection, interception, analysis, and visualization framework.",
            'aliases': ["snoopy-ng", "snoopy ng"],
        },
    ],

    # Firmware (4 tools)
    'blackarch-firmware': [
        {
            'name': 'firmwalker',
            'description': "Script for searching the extracted firmware file system for goodies.",
            'aliases': ["firmwalker", "firmwalker"],
        },
        {
            'name': 'firmware-mod-kit',
            'description': "Modify firmware images without recompiling.",
            'aliases': ["firmware-mod-kit", "firmware mod kit"],
        },
        {
            'name': 'meanalyzer',
            'description': "Intel Engine Firmware Analysis Tool.",
            'aliases': ["meanalyzer", "meanalyzer"],
        },
        {
            'name': 'uefi-firmware-parser',
            'description': "Parse BIOS/Intel ME/UEFI firmware related structures: Volumes, FileSystems, Files, etc.",
            'aliases': ["uefi-firmware-parser", "uefi firmware parser"],
        },
    ],

    # Keylogger (3 tools)
    'blackarch-keylogger': [
        {
            'name': 'logkeys',
            'description': "A GNU/Linux keylogger that worked.",
            'aliases': ["logkeys", "logkeys"],
        },
        {
            'name': 'python-keylogger',
            'description': "Simple keystroke logger.",
            'aliases': ["python-keylogger", "python keylogger"],
        },
        {
            'name': 'xspy',
            'description': "A utility for monitoring keypresses on remote X servers",
            'aliases': ["xspy", "xspy"],
        },
    ],

    # Anti-Forensic (2 tools)
    'blackarch-anti-forensic': [
        {
            'name': 'ropeadope',
            'description': "A linux log cleaner.",
            'aliases': ["ropeadope", "ropeadope"],
        },
        {
            'name': 'secure-delete',
            'description': "Secure file, disk, swap, memory erasure utilities.",
            'aliases': ["secure-delete", "secure delete"],
        },
    ],

    # Packer (2 tools)
    'blackarch-packer': [
        {
            'name': 'sherlocked',
            'description': "Universal script packer-- transforms any type of script into a protected ELF executable, encrypted with anti-debugging.",
            'aliases': ["sherlocked", "sherlocked"],
        },
        {
            'name': 'vbsmin',
            'description': "VBScript minifier.",
            'aliases': ["vbsmin", "vbsmin"],
        },
    ],

    # Ids (1 tools)
    'blackarch-ids': [
        {
            'name': 'sagan',
            'description': "A snort-like log analysis engine.",
            'aliases': ["sagan", "sagan"],
        },
    ],

    # NFC (1 tools)
    'blackarch-nfc': [
        {
            'name': 'nfcutils',
            'description': "A simple command that lists tags which are in your NFC device field.",
            'aliases': ["nfcutils", "nfcutils"],
        },
    ],

    # Threat-Model (1 tools)
    'blackarch-threat-model': [
        {
            'name': 'threat-dragon',
            'description': "Electron Threat Modelling and diagramming tool.",
            'aliases': ["threat-dragon", "threat dragon"],
        },
    ],

}


def search_tools(query):
    """Search for tools by name, description, or alias."""
    query = query.lower().strip()
    results = []
    for category, tools in TOOL_DATABASE.items():
        for tool in tools:
            if query in tool["name"].lower():
                results.append((category, tool))
                continue
            if query in tool["description"].lower():
                results.append((category, tool))
                continue
            for alias in tool["aliases"]:
                if query in alias.lower():
                    results.append((category, tool))
                    break
    return results


def get_tools_by_category(category):
    """Get all tools in a specific category."""
    full_cat = category if category.startswith("blackarch-") else f"blackarch-{category}"
    return TOOL_DATABASE.get(full_cat, [])


def get_all_categories():
    """Get a list of all available tool categories."""
    return list(TOOL_DATABASE.keys())


def suggest_tools(task_description):
    """Suggest relevant tools based on a task description using keyword matching."""
    task_lower = task_description.lower()

    keyword_map = {
        'scan': ['blackarch-scanner'],
        'port': ['blackarch-scanner'],
        'nmap': ['blackarch-scanner'],
        'network scan': ['blackarch-scanner', 'blackarch-recon'],
        'recon': ['blackarch-recon'],
        'reconnaissance': ['blackarch-recon'],
        'dns': ['blackarch-recon', 'blackarch-scanner'],
        'subdomain': ['blackarch-recon'],
        'enumerate': ['blackarch-recon', 'blackarch-scanner'],
        'osint': ['blackarch-recon'],
        'crack': ['blackarch-cracker'],
        'password': ['blackarch-cracker', 'blackarch-recon'],
        'hash': ['blackarch-cracker', 'blackarch-crypto'],
        'brute': ['blackarch-cracker'],
        'bruteforce': ['blackarch-cracker'],
        'web': ['blackarch-webapp'],
        'webapp': ['blackarch-webapp'],
        'sql': ['blackarch-webapp'],
        'sqli': ['blackarch-webapp'],
        'xss': ['blackarch-webapp'],
        'exploit': ['blackarch-exploitation'],
        'exploitation': ['blackarch-exploitation'],
        'shell': ['blackarch-exploitation', 'blackarch-backdoor'],
        'payload': ['blackarch-exploitation', 'blackarch-backdoor'],
        'backdoor': ['blackarch-backdoor'],
        'c2': ['blackarch-exploitation', 'blackarch-backdoor'],
        'post-exploit': ['blackarch-exploitation', 'blackarch-windows'],
        'privesc': ['blackarch-exploitation', 'blackarch-windows'],
        'privilege escalation': ['blackarch-exploitation', 'blackarch-windows'],
        'wireless': ['blackarch-wireless'],
        'wifi': ['blackarch-wireless'],
        'wpa': ['blackarch-wireless', 'blackarch-cracker'],
        'bluetooth': ['blackarch-bluetooth'],
        'fuzz': ['blackarch-fuzzer'],
        'fuzzing': ['blackarch-fuzzer'],
        'sniff': ['blackarch-sniffer', 'blackarch-networking'],
        'packet': ['blackarch-sniffer', 'blackarch-networking'],
        'dos': ['blackarch-dos'],
        'ddos': ['blackarch-dos'],
        'denial': ['blackarch-dos'],
        'forensic': ['blackarch-forensic'],
        'forensics': ['blackarch-forensic'],
        'memory': ['blackarch-forensic', 'blackarch-binary'],
        'disk': ['blackarch-forensic'],
        'binary': ['blackarch-binary', 'blackarch-reversing'],
        'reverse': ['blackarch-reversing', 'blackarch-binary', 'blackarch-disassembler'],
        'disassemble': ['blackarch-disassembler'],
        'decompile': ['blackarch-decompiler'],
        'malware': ['blackarch-malware'],
        'phish': ['blackarch-social'],
        'social': ['blackarch-social'],
        'engineering': ['blackarch-social'],
        'spoof': ['blackarch-spoof'],
        'arp': ['blackarch-spoof', 'blackarch-networking'],
        'proxy': ['blackarch-proxy', 'blackarch-tunnel'],
        'tunnel': ['blackarch-tunnel'],
        'vpn': ['blackarch-networking', 'blackarch-tunnel'],
        'automation': ['blackarch-automation'],
        'auto': ['blackarch-automation'],
        'defense': ['blackarch-defensive'],
        'defensive': ['blackarch-defensive'],
        'honeypot': ['blackarch-honeypot'],
        'mobile': ['blackarch-mobile'],
        'android': ['blackarch-mobile'],
        'iphone': ['blackarch-mobile'],
        'ios': ['blackarch-mobile'],
        'windows': ['blackarch-windows'],
        'active directory': ['blackarch-windows', 'blackarch-exploitation'],
        'ad': ['blackarch-windows'],
        'ldap': ['blackarch-recon', 'blackarch-windows'],
        'kerberos': ['blackarch-exploitation', 'blackarch-windows'],
        'smb': ['blackarch-recon', 'blackarch-scanner', 'blackarch-windows'],
        'voip': ['blackarch-voip'],
        'sip': ['blackarch-voip'],
        'radio': ['blackarch-radio'],
        'sdr': ['blackarch-radio'],
        'gsm': ['blackarch-radio'],
        'crypto': ['blackarch-crypto'],
        'encrypt': ['blackarch-crypto'],
        'decrypt': ['blackarch-crypto'],
        'ssl': ['blackarch-scanner', 'blackarch-crypto'],
        'tls': ['blackarch-scanner', 'blackarch-crypto'],
        'certificate': ['blackarch-scanner'],
        'stego': ['blackarch-stego'],
        'steganography': ['blackarch-stego'],
        'code audit': ['blackarch-code-audit'],
        'static analysis': ['blackarch-code-audit'],
        'fingerprint': ['blackarch-fingerprint'],
        'os detection': ['blackarch-fingerprint', 'blackarch-scanner'],
        'rfid': ['blackarch-nfc'],
        'nfc': ['blackarch-nfc'],
        'hardware': ['blackarch-hardware'],
        'wordlist': ['blackarch-wordlist', 'blackarch-misc'],
        'dictionary': ['blackarch-wordlist', 'blackarch-misc', 'blackarch-cracker'],
        'database': ['blackarch-database'],
        'ai': ['blackarch-ai'],
        'machine learning': ['blackarch-ai'],
        'llm': ['blackarch-ai'],
    }

    matched_categories = set()
    for keyword, cats in keyword_map.items():
        if keyword in task_lower:
            matched_categories.update(cats)

    results = []
    for cat in matched_categories:
        results.extend((cat, tool) for tool in TOOL_DATABASE.get(cat, []))
    return results