## 2024-05-16 - SSRF Protection in Web Scraping Agents
**Vulnerability:** IScoutAgent was accepting unchecked URLs to fetch via `httpx.get`, exposing the backend to Server-Side Request Forgery (SSRF) where an attacker could probe internal endpoints (e.g., `http://127.0.0.1/admin`) or fetch local files (`file:///etc/passwd`).
**Learning:** Even internal toolings or scraping endpoints must treat `target_url` as completely untrusted input. The system needs to validate both the scheme and the resolved IP address to prevent exploiting internal network resources.
**Prevention:** Implemented a robust `validate_url_safety` utility that uses `urllib.parse` to enforce `http` / `https` and `socket`/`ipaddress` to block loopback, private, and link-local IPs before executing any HTTP request.
