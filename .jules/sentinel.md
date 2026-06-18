## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-05-24 - Prevent SSRF with httpx and Follow Redirects
**Vulnerability:** The codebase uses `httpx.get` to fetch targets directly, which is vulnerable to SSRF if the user inputs `localhost` or similar IP addresses. Using `follow_redirects=True` further exposes it.
**Learning:** Validating the initial URL is insufficient. However, completely disabling automatic redirects can cause functional regressions for web-fetching agents. A secure approach requires handling and validating the URL at each redirect step.
**Prevention:** Use `httpx.Client(event_hooks={'request': [...]})` to attach a validation hook that evaluates the resolved IP of `request.url` at every redirect step, preventing bypasses. Ensure `ip_obj.is_unspecified` is checked alongside `is_private`, `is_loopback`, and `is_link_local`.
## 2024-05-24 - Prevent SSRF with IPv6 and DNS fail closed
**Vulnerability:** The SSRF protection originally used `socket.gethostbyname()`, which only supports IPv4. When provided an IPv6 address, it raises a `socket.gaierror`. Catching the error and ignoring it (failing open) allows a trivial bypass to hit internal network resources via IPv6.
**Learning:** Security controls must evaluate all inputs the underlying system supports (IPv4 and IPv6) and fail closed on errors.
**Prevention:** Use `socket.getaddrinfo(host, None)` to resolve both IPv4 and IPv6 addresses. Iterate over all resolved IPs and fail closed on resolution errors (`socket.gaierror`).
