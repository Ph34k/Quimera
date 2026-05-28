## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2025-02-20 - SSRF Vulnerability in Web Agents
**Vulnerability:** The `IScoutAgent` and `IExecutionAgent` accepted user-provided URLs (`target_url`) and executed HTTP GET requests without validation. This allowed Server-Side Request Forgery (SSRF), enabling access to internal network resources, local loopback, and cloud metadata services.
**Learning:** AI Agents that act on user-provided web targets are prime vectors for SSRF. The lack of network boundary checks allowed external requests to bounce into the internal network space.
**Prevention:** Always parse and resolve user-provided URLs to their IP addresses. Use the Python `ipaddress` library to verify `ip_address(ip).is_global` before dispatching requests, ensuring the target is a public, routable IP address.
