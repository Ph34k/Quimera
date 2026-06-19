## 2024-05-24 - SSRF vulnerability in httpx.get calls
**Vulnerability:** The application was vulnerable to Server-Side Request Forgery (SSRF) due to the use of `httpx.get` allowing direct access to localhost/internal IPs (e.g. `0.0.0.0`) when making requests based on user input.
**Learning:** Using `httpx` directly to fetch user-provided URLs is insecure, and completely disabling redirects can break web-fetching functionalities.
**Prevention:** We created `get_safe_httpx_client()` which uses an event hook to validate the resolved IP of the URL (and all subsequent redirects), blocking any private, loopback, link-local, or unspecified (0.0.0.0) IPs using both IPv4 and IPv6 resolution.

## 2024-05-24 - SSRF vulnerability in httpx.get calls
**Vulnerability:** The application was vulnerable to Server-Side Request Forgery (SSRF) due to the use of `httpx.get` allowing direct access to localhost/internal IPs (e.g. `0.0.0.0`) when making requests based on user input.
**Learning:** Using `httpx` directly to fetch user-provided URLs is insecure, and completely disabling redirects can break web-fetching functionalities.
**Prevention:** We created `get_safe_httpx_client()` which uses an event hook to validate the resolved IP of the URL (and all subsequent redirects), blocking any private, loopback, link-local, or unspecified (0.0.0.0) IPs using both IPv4 and IPv6 resolution.
