## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2025-06-12 - Fix SSRF Vulnerability in Agent Web Requests
**Vulnerability:** Agents (Scout/Execution) were performing `httpx.get` requests directly on user-provided URLs without validating whether the resolved IP addresses were private, enabling SSRF attacks against internal infrastructure.
**Learning:** Validating the initial hostname is insufficient due to DNS rebinding or redirects. The `httpx.get` client followed redirects by default, allowing a public URL to redirect to an internal IP (like `169.254.169.254`).
**Prevention:** Always validate resolved IP addresses (via `socket.getaddrinfo` and `ipaddress`) before fetching, and explicitly set `follow_redirects=False` to prevent redirect-based SSRF bypasses.
