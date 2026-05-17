## 2024-05-17 - Fix Server-Side Request Forgery (SSRF) in Agents
**Vulnerability:** The `IScoutAgent` and `IExecutionAgent` allowed HTTP requests to arbitrary user-provided URLs without validation, allowing a malicious user to scan or interact with internal network resources (e.g., `127.0.0.1`, `localhost`, `169.254.169.254`).
**Learning:** Even internal helper agents must validate target URLs. The reliance on default behavior allowed for SSRF and DNS rebinding risks.
**Prevention:** Always validate target URLs via `socket.getaddrinfo` to resolve the actual IPs and check against private/loopback/link-local boundaries (`ipaddress.ip_address`) *before* issuing requests, ideally hooking the validation into the HTTP client (`httpx` `event_hooks`).
