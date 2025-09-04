# HTTP Header Manipulation

## Vulnerability
Client-Side Access Control via Header Checks

## Target
`http://10.14.58.57/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`

## Mechanism
- The page checked for two specific HTTP headers:
  1. **User-Agent**: Expected `ft_bornToSec`
  2. **Referer**: Expected `https://www.nsa.gov/`
- Server granted access only if both headers matched expected values

## Exploit
```bash
curl -A "ft_bornToSec" -e "https://www.nsa.gov/" http://10.14.58.57/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```
- `-A` flag set the User-Agent header
- `-e` flag set the Referer header

## Impact
Bypassed server-side access control by spoofing HTTP headers, revealing the flag.

## Severity
Medium (Broken Access Control)