# Path Traversal Exploit to Retrieve a Flag

## Target
The target application allowed file inclusion through a URL parameter `page`.

## Exploit
By manipulating the `page` parameter, we were able to traverse directories on the server. The URL used:

http://{IP_ADDRESS}/?page=../../../../../../../etc/passwd


- `../../` sequences navigate up the directory tree.
- `/etc/passwd` is a sensitive system file on Linux systems, often used to test path traversal vulnerabilities.

## Result
Using this path traversal technique, we accessed server files outside the web root, eventually locating the **flag**.

## Explanation
This attack works because the application does not properly validate or sanitize input. By providing relative paths, an attacker can reach arbitrary files on the server, leading to potential information disclosure or further exploitation.
