## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2026-05-27 - SSRF in Web Requesting Agents
**Vulnerability:** Agents (IScoutAgent, IExecutionAgent) accept user-supplied URLs and make HTTP requests via `httpx.get` without validating the destination, allowing SSRF (Server-Side Request Forgery) attacks against internal networks (e.g., localhost, cloud metadata at 169.254.169.254).
**Learning:** Using `socket.getaddrinfo` with `ipaddress.ip_address(ip).is_global` is critical to safely resolve hostnames (supporting IPv6) and robustly block non-global/link-local/private IP ranges.
**Prevention:** Always validate user-provided URLs by resolving their IP addresses and asserting they are globally routable before making outbound HTTP requests.

## 2026-05-27 - SSRF Redirect Vulnerability
**Vulnerability:** Even if the initial URL is validated to not point to a local IP address, the HTTP client may automatically follow redirects (`follow_redirects=True`). An attacker can provide a valid public URL that redirects to an internal IP (like 169.254.169.254), bypassing the SSRF protection.
**Learning:** SSRF mitigation must account for HTTP redirects. Validating only the initial URL is insufficient if the client blindly follows redirects to anywhere.
**Prevention:** Always disable automatic redirects (`follow_redirects=False`) when fetching user-supplied URLs, or implement a custom transport that validates the destination of every redirect before following it.
