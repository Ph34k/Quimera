## 2024-05-18 - [SSRF in HTTPx Agents]
**Vulnerability:** Agents using `httpx` to fetch user-provided URLs did not validate the resolved IP, allowing Server-Side Request Forgery (SSRF) against internal resources (e.g., localhost, AWS metadata).
**Learning:** Even if the initial URL is validated, `httpx` follows redirects by default (`follow_redirects=True`). Attackers can supply a harmless external URL that responds with an HTTP 302 redirecting the client to an internal IP, bypassing the initial validation.
**Prevention:** Always validate the URL before the initial request *and* use `httpx.Client` with an event hook (`event_hooks={'response': [verify_redirect]}`) to inspect and validate the `Location` header before any redirect is followed.
