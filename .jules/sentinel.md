## 2025-04-18 - [SSRF Protection in httpx Agent Requests]
**Vulnerability:** Server-Side Request Forgery (SSRF) allowed agents to make HTTP requests to internal networks, link-local metadata servers, and follow redirects to internal addresses.
**Learning:** `ipaddress.ip_address.is_private` in Python does not cover `169.254.x.x` (link-local) addresses, leaving cloud metadata vulnerable. Standard `httpx` follows redirects blindly, bypassing initial URL validation.
**Prevention:** Use `ip.is_global` check alongside `is_link_local` to cover all internal spaces. Manually handle HTTP redirects (`follow_redirects=False`) to validate the Location header at every step using a `safe_http_get` wrapper.
