# Hidden Option Value Manipulation

## Vulnerability
Insecure Access Control via Client-Side Validation

## Target
Survey page grade selection input

## Mechanism
- A grade selection field contained a hidden option with a value (`69`)
- The server trusted the submitted `value` attribute without validation
- Client-side HTML limited visible options, but hidden values were still submittable

## Exploit
1. Inspected the page's HTML source code
2. Located the hidden `<option value="9999999">10</option>` element
3. Selected the manipulated high-value option (9999999) and submitted the form

## Impact
Bypassed intended business logic, triggering an abnormal condition that revealed the flag.

## Severity
Medium-High (Improper Input Validation / Broken Access Control)