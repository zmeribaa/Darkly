# Hidden Form Field Manipulation

## Vulnerability
Insecure Access Control via Client-Side Enforcement

## Target
`http://10.14.58.57/?page=recover`

## Mechanism
- A form field was hidden using HTML's `type="hidden"` attribute
- The server trusted the submitted value of this field without validation
- Modifying this value changed application behavior

## Exploit
1. Inspected page source / used developer tools
2. Located and modified the `value` attribute of the hidden field
3. Submitted the form with the elevated privilege value

## Impact
Privilege escalation or unauthorized action, leading to flag disclosure.

## Severity
High (OWASP Top 10: Broken Access Control)