## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-20 - SSRF Vulnerability in Web Scraping Agents
**Vulnerability:** IScoutAgent and IExecutionAgent were directly using httpx.get() on user-provided target_urls without IP validation, allowing Server-Side Request Forgery (SSRF) attacks against internal network resources (e.g., localhost, private IPs, and 0.0.0.0 bypasses) as well as following redirects to internal IPs.
**Learning:** Validating the initial URL string is insufficient because attackers can use DNS rebinding or redirects. An event hook on the HTTP client is required to resolve and validate the IP address at every step of the request (including redirects). Additionally, `socket.getaddrinfo` must be used instead of `socket.gethostbyname` to catch IPv6 bypasses.
**Prevention:** Always instantiate a shared HTTP client (e.g., `httpx.Client()`) configured with an event hook (`event_hooks={'request': [...]}`) that resolves the hostname to its IP addresses via `socket.getaddrinfo`, and validates that none of the resolved IPs are private, loopback, link-local, or unspecified (`0.0.0.0`), failing closed on resolution errors.
