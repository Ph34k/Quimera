## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-03 - SSRF Vulnerability in Agents
**Vulnerability:** IScoutAgent and IExecutionAgent were vulnerable to Server-Side Request Forgery (SSRF) because they fetched arbitrary URLs passed by users via `httpx.get` without any validation. They also followed redirects which could bypass simple domain checks.
**Learning:** Even internal networking calls to non-public endpoints or metadata IPs (e.g., `169.254.169.254`) could be triggered. Using IP validation with `ipaddress` and ensuring `is_global` check is an effective mitigation. Also, `follow_redirects=False` must be explicitly set to prevent bypass via redirects.
**Prevention:** Always validate target URLs by resolving their hostnames and ensuring the resulting IPs are public/global before passing them to an HTTP client. Disable automatic redirect following on untrusted URLs to avoid bypassing IP checks.
