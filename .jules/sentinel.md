## 2024-05-15 - Server-Side Request Forgery (SSRF) in ScoutAgent and ExecutionAgent

**Vulnerability:**
The `IScoutAgent` and `IExecutionAgent` methods took a user-supplied `target_url` payload and executed it directly using `httpx.get()` without resolving or validating the underlying IP addresses. This allowed for potential Server-Side Request Forgery (SSRF), enabling an attacker to instruct the application to access internal services, private subnets (e.g., `192.168.x.x`), or cloud metadata endpoints (e.g., `169.254.169.254`).

**Learning:**
Always assume that arbitrary URLs provided by a user can map to internal infrastructure. Relying solely on the domain name is insufficient due to DNS rebinding and internal DNS resolution. The IP address the URL resolves to must be explicitly checked against private, loopback, multicast, link-local, and reserved IP address spaces before initiating the connection.

**Prevention:**
Implemented an `is_safe_url` validation function that resolves the URL's hostname using `socket.getaddrinfo` and checks the resulting IP addresses against standard private IP ranges using Python's `ipaddress` module. This check is injected into a persistent `httpx.Client` instance via the `event_hooks={'request': [verify_request]}` configuration in both affected agents. This ensures that even if the request follows redirects, every intermediate request is validated before execution. Note that while this mitigates direct IP SSRF, it does not fully prevent Time-of-Check to Time-of-Use (TOCTOU) DNS rebinding attacks since the HTTP client will resolve the domain again during connection; a fully comprehensive defense would require a custom transport layer that passes the pre-resolved IP directly to the socket.
