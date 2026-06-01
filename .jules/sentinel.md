## 2024-06-01 - SSRF Prevention via Global IP Validation and Redirect Handling
**Vulnerability:** Execution and Scout agents accepted arbitrary URLs allowing internal network enumeration (SSRF).
**Learning:** Checking for explicit private lists is insufficient. You must check `not ip.is_global` to block link-local addresses (e.g. 169.254.169.254). Additionally, automatic redirects in `httpx` can bypass URL validation.
**Prevention:** Always validate resolved IPs via `ip.is_global` and disable `follow_redirects` in HTTP requests taking user input.
