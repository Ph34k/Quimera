## 2025-03-05 - Fix SSRF Vulnerability in Web Agents
**Vulnerability:** Server-Side Request Forgery (SSRF) allowed `IScoutAgent` and `IExecutionAgent` to make HTTP requests to internal IP addresses (e.g., localhost, 169.254.169.254) because user-provided URLs were fetched without validation.
**Learning:** Initial URL validation is not enough; HTTP clients (like `httpx`) will automatically follow redirects which an attacker could point to internal IPs, bypassing the initial check.
**Prevention:** Always validate the URL by resolving its hostname to an IP and ensuring it is public, AND explicitly disable automatic redirects (e.g., `follow_redirects=False` in `httpx`) to prevent redirection to internal IPs.
