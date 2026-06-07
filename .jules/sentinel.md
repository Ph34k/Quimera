## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2026-06-07 - SSRF via Redirection Bypass
**Vulnerability:** IScoutAgent and IExecutionAgent were vulnerable to Server-Side Request Forgery (SSRF) due to lack of IP validation and allowing automatic HTTP redirects (`follow_redirects=True`).
**Learning:** Validating the initial URL against private/internal IPs is insufficient if the HTTP client automatically follows redirects, as an attacker can provide a valid public URL that redirects to an internal endpoint (e.g., `169.254.169.254`).
**Prevention:** Always validate resolved IP addresses against private ranges, and explicitly set `follow_redirects=False` in HTTP clients to block redirection-based bypasses.
