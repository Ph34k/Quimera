## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2026-05-30 - Server-Side Request Forgery (SSRF) in Agents
**Vulnerability:** Agents (Scout, Execution) accept unvalidated URLs and execute HTTP requests, allowing internal network scanning or metadata access (e.g., http://localhost, http://169.254.169.254).
**Learning:** URL validation must resolve hostnames to IPs and check if they are global to safely prevent SSRF, especially in cloud environments where link-local addresses are sensitive.
**Prevention:** Always validate user-provided URLs using socket resolution and ipaddress to ensure they don't point to non-global IPs before passing them to HTTP clients like httpx.
