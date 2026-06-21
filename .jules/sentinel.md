## 2025-02-12 - Prevent SSRF via IP Validation in `httpx`

**Vulnerability:** Server-Side Request Forgery (SSRF) vulnerabilities in agents making outward web requests (`IScoutAgent`, `IExecutionAgent`) allowed bypassing standard checks to access localhost and internal network infrastructure.
**Learning:** URL hostnames can be resolved to internal IP addresses (like `127.0.0.1` or `::1`), which bypasses simple string-based checks on the URL. Additionally, `httpx` redirects might also redirect a legitimate external request to an internal IP.
**Prevention:** Always validate the resolved IP address of the destination URL *before* making the request or during redirection using an `httpx` event hook (`event_hooks={'request': [_validate_ssrf]}`). The hook should resolve the URL's hostname using `socket.getaddrinfo(..., None)` to handle both IPv4 and IPv6, check if the IP is private, loopback, link-local, or unspecified, and if so, raise an `httpx.RequestError`.
