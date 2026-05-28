## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2026-05-28 - SSRF Defense in Depth via HTTPx Event Hooks
**Vulnerability:** `IScoutAgent` and `IExecutionAgent` were performing unfiltered HTTP requests to arbitrary user-supplied target URLs via `httpx.get()`, leading to a high-severity Server-Side Request Forgery (SSRF) risk.
**Learning:** Resolving IPs and checking if they are global before making the request provides good baseline SSRF protection. Using an `httpx.Client` with `event_hooks={'request': [hook]}` is crucial because it ensures the protection hook evaluates not just the initial request, but also all subsequent redirects, mitigating a common SSRF bypass vector.
**Prevention:** Always validate resolved target IPs against global IP ranges (`ipaddress.ip_address(ip).is_global`) and leverage HTTP client hooks instead of static URL parsing to intercept all network calls reliably, including redirects.
