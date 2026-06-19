## 2025-02-27 - SSRF Protection via HTTPX Event Hooks
**Vulnerability:** The `httpx.get` calls in `IScoutAgent` and `IExecutionAgent` allowed fetching arbitrary user-supplied URLs without IP validation, introducing a Server-Side Request Forgery (SSRF) risk.
**Learning:** Initial URL validation is insufficient when redirects are enabled (`follow_redirects=True`). Mitigating SSRF securely requires validating the resolved IP of the URL at every redirect step to prevent bypasses.
**Prevention:** Always use `httpx.Client(event_hooks={'request': [validate_request_ip]})` to attach a validation hook that evaluates the resolved IP of `request.url` before every request, explicitly blocking private, loopback, link-local, and unspecified (`0.0.0.0`) IPs via `socket.getaddrinfo` (which handles IPv6).
