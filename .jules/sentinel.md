## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-04 - SSRF in Web Agents
**Vulnerability:** Server-Side Request Forgery (SSRF) allowed agents to access local or cloud metadata IPs.
**Learning:** Validating the initial IP isn't enough; attackers can use public URLs that redirect to internal IPs.
**Prevention:** Always validate resolved IPs via `ipaddress` ensuring they are global, and explicitly disable redirects (e.g., `follow_redirects=False` in httpx).
