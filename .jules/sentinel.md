## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-06 - Prevent SSRF in Agent Web Requests
**Vulnerability:** The `IScoutAgent` and `IExecutionAgent` were making HTTP requests to user-provided URLs without validating the IP addresses, potentially allowing Server-Side Request Forgery (SSRF) against internal resources (e.g., `127.0.0.1`, AWS metadata `169.254.169.254`). Also, `IExecutionAgent` had `follow_redirects=True`.
**Learning:** Validating the initial URL string is insufficient because a public URL can redirect to an internal IP. Hostnames must be resolved to IPs and checked against restricted ranges, and automatic redirects must be disabled to prevent bypasses.
**Prevention:** Use `socket.getaddrinfo()` to resolve hostnames and `ipaddress.ip_address().is_private` (and related checks) to validate all resulting IPs before making requests. Always disable `follow_redirects` (`follow_redirects=False`) when fetching user-provided URLs in these contexts.
