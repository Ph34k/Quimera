## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2024-03-22 - SSRF Mitigation via httpx Hook
**Vulnerability:** Server-Side Request Forgery (SSRF) allowed access to internal/private IPs.
**Learning:** `httpx` follows redirects by default, meaning validating just the initial URL is insufficient for SSRF protection. Using `socket.gethostbyname()` is also insufficient because it only resolves IPv4.
**Prevention:** Use an `httpx` event hook (`event_hooks={'request': [_validate_ssrf]}`) to validate the resolved IP address via `socket.getaddrinfo()` at every redirect step. Block `is_private`, `is_loopback`, `is_link_local`, and `is_unspecified` IPs. Always raise an exception on `socket.gaierror` to fail securely.
