## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-05-27 - Server-Side Request Forgery (SSRF) in Agents
**Vulnerability:** Agents (Scout and Execution) accepted any URL and fetched them using HTTPx without validation or restricting redirects, exposing internal endpoints.
**Learning:** Checking hostnames is not enough. We must resolve the hostname to IP using socket.getaddrinfo (to support IPv6) and check against private/loopback IP ranges. We also must disable automatic redirects (`follow_redirects=False`) to avoid circumvention via open redirects.
**Prevention:** Always validate resolved IPs and disable automatic HTTP redirects on user-supplied URLs fetching content.
