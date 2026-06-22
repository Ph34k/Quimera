## 2024-05-24 - SSRF vulnerability in httpx client
**Vulnerability:** The `httpx.Client` was missing SSRF protection when following redirects.
**Learning:** Automatically following redirects with `follow_redirects=True` without validating the resolved IP at each redirect step allows SSRF bypasses. Validating the initial URL is insufficient. Also, `socket.gethostbyname()` is insufficient as it only resolves IPv4. We must use `socket.getaddrinfo(host, None)` and `ipaddress` module checking `is_unspecified`, `is_private`, `is_loopback` and `is_link_local` to prevent SSRF bypasses on IPv4 and IPv6.
**Prevention:** Use a persistent `httpx.Client` instance with an `event_hooks={'request': [_validate_ssrf]}` to validate resolved IP addresses at every redirect step.
