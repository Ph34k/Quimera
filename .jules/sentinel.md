## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-01 - Fix SSRF in HTTP agents
**Vulnerability:** Agents (Scout and Execution) make HTTP requests to user-provided URLs without validating if they point to internal networks or cloud metadata IP addresses (SSRF).
**Learning:** Even internal helper tools that make outbound requests must validate their targets to prevent attackers from probing internal infrastructure.
**Prevention:** Always validate hostnames against internal/private IP blocks and disable automatic redirects before making outbound HTTP requests on behalf of users.
