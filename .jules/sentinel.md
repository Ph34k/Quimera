## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2026-06-22 - Server-Side Request Forgery (SSRF)
**Vulnerability:** Agents (like IScoutAgent and IExecutionAgent) accept user-controlled URLs and execute HTTP requests without validating the resolved IP address, leading to a critical SSRF vulnerability that allows access to private/internal network addresses.
**Learning:** Checking the domain string is insufficient; the final resolved IP must be validated at the transport level. When following redirects, every intermediate request must also be validated to prevent bypasses.
**Prevention:** Always implement an event hook on the `httpx.Client` (e.g., `event_hooks={'request': [_validate_ssrf]}`) that resolves the URL's hostname using `socket.getaddrinfo` (to catch IPv4 and IPv6) and explicitly blocks private, loopback, link-local, and unspecified (0.0.0.0) IPs via Python's `ipaddress` module. Fail closed on DNS resolution errors.
