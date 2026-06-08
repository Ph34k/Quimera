## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2024-06-08 - Prevent SSRF in Scout and Execution Agents
**Vulnerability:** Server-Side Request Forgery (SSRF) allowed the `ScoutAgent` and `ExecutionAgent` to make arbitrary HTTP requests to internal IP addresses (e.g. `localhost`, `169.254.169.254`) via unsanitized `target_url` parameters. It also allowed redirect loops to internal IPs.
**Learning:** External user inputs passed to HTTP request functions (`httpx.get`) require strict hostname resolution and IP validation to prevent an attacker from bypassing external firewalls and scanning or exploiting internal services.
**Prevention:** Implement an `is_safe_url` helper using `socket.getaddrinfo()` to block any URL that resolves to a loopback, private, or link-local IP, and explicitly set `follow_redirects=False` in HTTP clients.
