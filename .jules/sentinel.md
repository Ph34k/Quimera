## 2025-06-14 - Prevent SSRF by validating resolved IPs

**Vulnerability:** The `IScoutAgent` and `IExecutionAgent` used `httpx.get` directly on user-provided URLs without validating the resolved IP address, allowing Server-Side Request Forgery (SSRF) attacks against internal network resources (e.g. `127.0.0.1`, private subnets).
**Learning:** Checking the URL string is insufficient because attackers can use DNS rebinding or custom hostnames resolving to internal IPs. The validation must occur after DNS resolution but before the connection is established.
**Prevention:** Use a persistent `httpx.Client` with an event hook (`event_hooks={'request': [_validate_ssrf]}`) that resolves the hostname to an IP and validates it against restricted ranges (`is_private`, `is_loopback`, `is_link_local`, `is_unspecified`) using the Python `ipaddress` module.
