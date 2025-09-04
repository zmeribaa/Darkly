# Open Redirect Vulnerability

## Vulnerability
Unvalidated Redirects and Forwards (OWASP A10:2021)

## Target
`http://10.14.58.57/index.php?page=redirect&site=twitter`

## Mechanism
- The `site` parameter was used to build redirect URLs without validation
- No whitelist or sanitization of user-supplied input
- Allowed manipulation of redirect destination

## Exploit
1. Inspected social media icon links
2. Modified the `site` parameter value from `twitter` to an arbitrary value
3. Submitted request: `index.php?page=redirect&site=random_value`

## Impact
- Redirect manipulation bypassed intended functionality
- Triggered server-side flag reveal mechanism

## Severity
Medium (Could enable phishing attacks if exploited maliciously)