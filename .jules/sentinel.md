## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-12 - Prevent SSRF via IP Validation and Disabled Redirects
**Vulnerability:** The application was vulnerable to Server-Side Request Forgery (SSRF) because `httpx.get` calls in agent implementations accepted user-provided URLs without validating whether they resolved to internal network addresses, and implicitly allowed auto-redirects.
**Learning:** Checking the initial hostname is insufficient because DNS resolution can return private IPs, and even if safe initially, the public server might redirect the client to an internal IP (e.g. 169.254.169.254 or localhost).
**Prevention:** Always validate the IP addresses obtained via `socket.getaddrinfo()` against private/loopback/link-local ranges, and disable HTTP redirects (`follow_redirects=False`) when performing outbound requests to user-provided URLs.
