## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2024-06-02 - Server-Side Request Forgery (SSRF)
**Vulnerability:** IScoutAgent and IExecutionAgent make unrestricted HTTP requests via `httpx.get` based on user-provided URLs, and implicitly follow redirects.
**Learning:** An attacker can provide local or internal network IPs (e.g., `127.0.0.1` or `169.254.169.254`) directly, or provide a safe public URL that redirects to an internal IP, bypassing naive domain blocklists.
**Prevention:** Validate IP addresses using `ipaddress` ensuring `ip.is_global` is true (after resolving domains to IPs via `socket.getaddrinfo`), AND set `follow_redirects=False` in HTTP clients to prevent redirect-based bypasses.
