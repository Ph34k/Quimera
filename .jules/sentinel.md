## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2026-05-27 - Server-Side Request Forgery (SSRF) in httpx
**Vulnerability:** The `httpx.get` calls in agents accepted any user-supplied URL and followed redirects, allowing attackers to reach internal IPs (127.0.0.1, 0.0.0.0, etc.) causing an SSRF vulnerability.
**Learning:** Checking the initial URL is insufficient for SSRF protection when following redirects. Bypasses using `0.0.0.0` or custom DNS pointing to localhost can evade simple validation.
**Prevention:** Always use `httpx.Client(event_hooks={'request': [...]})` to evaluate the resolved IP of the URL at every request and redirect step, verifying `ip_obj.is_private`, `is_loopback`, `is_link_local`, and `is_unspecified`.
