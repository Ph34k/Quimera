## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-05-24 - Fix SSRF Vulnerability in Agent Web Requests
**Vulnerability:** The application was passing user-provided URLs (`target_url`) directly to `httpx.get()` in `IScoutAgent` and `IExecutionAgent` without IP validation. This allowed Server-Side Request Forgery (SSRF) bypasses where attackers could target internal IP addresses (e.g., `127.0.0.1`, loopback, or cloud metadata IPs).
**Learning:** Using `follow_redirects=True` with `httpx` requires continuous validation of IP addresses at every redirect step. Furthermore, resolving hostnames to IPs requires checking both IPv4 and IPv6 using `socket.getaddrinfo()` to avoid bypasses, and DNS resolution failures must fail closed (`socket.gaierror`). A shared `httpx.Client` is thread-safe and allows maintaining state across asynchronous requests.
**Prevention:** Always validate resolved IPs using an event hook (`event_hooks={'request': [check_ssrf]}`) for internal networks using `ipaddress` prior to performing HTTP requests on user-supplied input.
