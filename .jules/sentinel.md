## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2024-06-09 - SSRF Vulnerability in Agents
**Vulnerability:** Unrestricted HTTP requests allowing Server-Side Request Forgery (SSRF) to internal IP addresses and bypasses via redirects.
**Learning:** Validating the initial URL against internal IP ranges is insufficient if automatic redirects are enabled (`follow_redirects=True`), as a public endpoint can redirect to internal IPs.
**Prevention:** Implement IP validation using `socket.getaddrinfo` (to cover IPv6) and explicitly disable redirects (`follow_redirects=False`) in `httpx` to ensure requests only hit safe, public targets.
