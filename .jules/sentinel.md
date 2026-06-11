## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2025-03-05 - Prevented SSRF in HTTP agents
**Vulnerability:** Unrestricted Server-Side Request Forgery (SSRF) allowed the scout and execution agents to query private/internal IPs.
**Learning:** The external target URLs were passed directly to `httpx.get` without any validation. Following redirects also could bypass validation.
**Prevention:** Always validate the IP resolved from a user-supplied URL to ensure it is public before executing a request, and always disable automatic redirects `follow_redirects=False` in HTTP clients to prevent external-to-internal redirect bypasses.
