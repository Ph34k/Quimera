## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-06-02 - Server-Side Request Forgery (SSRF) Prevention
**Vulnerability:** IScoutAgent and IExecutionAgent accept user-provided URLs and make HTTP requests without validating if the resolved IP addresses are safe (e.g., preventing access to internal/loopback IPs like 127.0.0.1 or cloud metadata IP 169.254.169.254). Also, automatic redirects were enabled.
**Learning:** Checking the URL hostname is insufficient; we must resolve the hostname to its IPs and ensure they are global (using `socket.getaddrinfo` and `ip.is_global` from `ipaddress`). Furthermore, `follow_redirects=False` must be used to prevent attackers from providing a valid external URL that redirects to an internal IP.
**Prevention:** Always validate all resolved IPs for a URL before making requests, use `socket.getaddrinfo` to support IPv6, ensure `ip.is_global` is true, and disable automatic HTTP redirects.
