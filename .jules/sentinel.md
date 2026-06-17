## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2024-05-28 - SSRF Vulnerability via Unsanitized External Fetch
**Vulnerability:** Agents (Scout and Execution) fetch arbitrary URLs using `httpx.get` without SSRF protection, allowing access to internal endpoints (e.g., localhost/127.0.0.1) or bypasses through unroutable ranges (e.g., 0.0.0.0).
**Learning:** Using `httpx.get` direct calls for user-provided URLs is insecure as it blindly follows the URL to any resolved IP, including private internal networks, and may also bypass basic URL validation if redirects occur.
**Prevention:** Always use an `httpx.Client` instance combined with `event_hooks` on the `request` object. In the hook, resolve the hostname to an IP and enforce restrictions against private, loopback, link-local, and unspecified ranges.
