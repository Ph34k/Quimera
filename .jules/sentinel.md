## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-11 - SSRF Prevention and Redirects
**Vulnerability:** The HTTP agents (Scout and Execution) accepted any URL without validation, allowing Server-Side Request Forgery (SSRF) against internal resources (e.g., `127.0.0.1` or AWS metadata endpoints).
**Learning:** When mitigating SSRF via IP validation on the initial URL, an attacker could still bypass the check by providing a valid external URL that redirects to an internal IP.
**Prevention:** In addition to validating the hostname resolves to a public IP, explicitly disable automatic redirects (e.g., `follow_redirects=False` in `httpx.get`) so the HTTP client does not blindly follow unsafe redirects.
