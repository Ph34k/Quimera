## 2025-05-25 - Server-Side Request Forgery (SSRF) in Agents
**Vulnerability:** IScoutAgent and IExecutionAgent were making arbitrary HTTP requests to user-provided URLs using `httpx.get` without validating the resolved IP address, allowing an attacker to probe internal network resources (SSRF).
**Learning:** Even if a URL looks external, DNS resolution can point it to an internal IP (DNS rebinding) or the user can directly provide an internal IP. Validating the IP address *after* resolution is crucial.
**Prevention:** Implement an HTTP client event hook (`verify_request`) that resolves the hostname using `socket.getaddrinfo` and verifies the resulting IP address is not private, loopback, link-local, or unspecified before allowing the request to proceed.
