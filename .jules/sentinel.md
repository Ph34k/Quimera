## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2026-05-28 - SSRF Prevention in Agents
**Vulnerability:** Agents (Scout and Execution) accepted any URL directly into httpx.get, allowing Server-Side Request Forgery (SSRF) against internal services and cloud metadata endpoints.
**Learning:** Always validate that URLs resolve to global IP addresses before dispatching HTTP requests to prevent SSRF vulnerabilities.
**Prevention:** Use httpx event hooks (`event_hooks={'request': [_verify_request]}`) coupled with `ipaddress` validation (`if not ip.is_global:`) to strictly block non-global IP addresses, even across redirects.
