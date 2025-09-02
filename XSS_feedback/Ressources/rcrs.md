# Obtaining the Flag via XSS Attack

## Target
The **Feedback Page** of the application.
## Vulnerability
The **name field** in the feedback form was **not properly sanitized**, making it vulnerable to **Cross-Site Scripting (XSS)** attacks.

## Exploit
I injected the following payload into the **name field**:

```html
<script>alert('XSS')</script>
