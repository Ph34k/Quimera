## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2026-05-28 - SSRF Prevention in HTTP clients
**Vulnerability:** The HTTP clients used by agents were vulnerable to Server-Side Request Forgery (SSRF) as they allowed requests to any resolved IP address, including local/private networks, potentially exposing internal services.
**Learning:** Validating the initial URL against a blacklist is insufficient. A secure approach requires hooking into the client to evaluate the resolved IP address (including handling redirects) before allowing the request.
**Prevention:** Always use `httpx.Client` with an `event_hooks` validation function that checks if the resolved IP object is private, loopback, link_local, or unspecified.
