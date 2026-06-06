## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-05-18 - SSRF Prevention in External Requests
**Vulnerability:** Server-Side Request Forgery (SSRF) allowed access to internal/private IPs and cloud metadata via unsanitized `target_url` in HTTPx requests.
**Learning:** Initial validation was missing. Using `socket.getaddrinfo` is required for comprehensive IPv6 support to resolve hostnames before checking IP ranges. Additionally, HTTPx's `follow_redirects=True` allowed bypassing domain checks by redirecting to a private IP post-validation.
**Prevention:** Always validate resolved IPs against private/loopback/link-local/multicast ranges before executing requests. Explicitly set `follow_redirects=False` (or validate at every redirect hop) to prevent bypasses.
