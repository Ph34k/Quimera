## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-10 - SSRF via Unrestricted Agent HTTP Requests
**Vulnerability:** IScoutAgent and IExecutionAgent were performing raw HTTP GET requests (httpx.get) to user-supplied URLs without validating the resolved IP address, enabling Server-Side Request Forgery (SSRF) against internal networks.
**Learning:** When mitigating SSRF via IP validation, validating the initial URL is insufficient. Attackers can bypass protections by providing a public URL that redirects to an internal IP.
**Prevention:** Always implement an `is_safe_url` helper that resolves hostnames (preferring socket.getaddrinfo over gethostbyname for IPv6 compatibility) and checks against private/loopback/link-local ranges. Furthermore, always disable automatic redirects (e.g., follow_redirects=False in httpx.get) when making requests to untrusted targets.
