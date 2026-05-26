## 2024-05-26 - Server-Side Request Forgery in HTTP Requests
**Vulnerability:** Agents (IScoutAgent and IExecutionAgent) allowed arbitrary target URLs via httpx without validating the resolved IP, allowing an attacker to ping internal networks (e.g., localhost, 127.0.0.1, 169.254.169.254).
**Learning:** Checking a URL string is not enough. You must validate the fully resolved IP using `socket.getaddrinfo` and apply event hooks (`event_hooks={'request': [verify_request]}`) to an `httpx.Client` so that even internal redirects are intercepted safely.
**Prevention:** Always use a persistent `httpx.Client` with request event hooks configured to resolve and block private/loopback IP requests on every connection attempt.
