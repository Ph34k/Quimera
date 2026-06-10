## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-10 - [SSRF Mitigation with IP Validation]
**Vulnerability:** Found multiple `httpx` HTTP calls making unverified requests to user-controlled URLs in `IScoutAgent` and `IExecutionAgent`, which were susceptible to Server-Side Request Forgery (SSRF).
**Learning:** `httpx` and automatic redirects can bypass basic validation. Disabling redirects via `follow_redirects=False` is necessary alongside IP evaluation (`socket.getaddrinfo()` and `ipaddress.ip_address()`) to ensure no loopback, private, or metadata IPs are queried.
**Prevention:** Before hitting arbitrary URLs, resolve and check its IPs using `socket.getaddrinfo()` mapping to `ipaddress` rules. Additionally, explicitly set `follow_redirects=False` for any network calls.
