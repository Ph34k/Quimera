## 2025-04-18 - [SSRF Protection]
**Vulnerability:** Found unvalidated URLs being passed to `httpx.get` in `IScoutAgent` and `IExecutionAgent` (`app/domain/agents.py`), which could lead to Server-Side Request Forgery (SSRF). An attacker could supply internal IPs (e.g., `http://localhost:6379`) to probe or exploit internal services like Redis.
**Learning:** Even MVP features must not trust user-provided URLs blindly. External-facing fetch functionality often overlooks internal network protections.
**Prevention:** Always parse and resolve hostnames to IP addresses, explicitly blocking private, loopback, and link-local ranges before issuing HTTP requests. Additionally, disable auto-following of redirects to prevent redirection to internal IPs.
