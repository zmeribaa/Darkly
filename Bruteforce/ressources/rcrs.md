# Brute Force Attack Exploit

## Vulnerability
Weak Password Policy

## Target
`http://10.14.58.57/?page=signin`

## Mechanism
- Login form accepted unlimited password attempts
- Used a known username (`admin`) and brute-forced passwords from `rockyou-60.txt`
- Script automated POST requests with different passwords
- Grepped responses for the string "flag" to detect success
- passowrd is "shadow"

## Exploit Script
```bash
#!/bin/bash
# Iterated through password list
# Sent requests: /?page=signin&username=admin&password=$pswd&Login=Login
# Detected successful login by presence of "flag" in response
```

## Impact
Gained unauthorized admin access by discovering weak password.

## Severity
High (OWASP Top 10: Identification and Authentication Failures)