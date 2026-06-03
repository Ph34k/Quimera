## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2024-06-03 - Server-Side Request Forgery (SSRF)
**Vulnerability:** HTTP requests were made to user-supplied URLs without resolving the hostnames to verify if the destination IPs were public.
**Learning:** Checking the hostname alone is insufficient to prevent SSRF because public domains can resolve to internal IP addresses (e.g., cloud metadata or localhost). Also, automatic redirects can bypass initial IP validations.
**Prevention:** Always resolve the hostname to its underlying IPs using `socket.getaddrinfo`, verify that all resolved IPs are global using `ipaddress.ip_address(ip).is_global`, and disable automatic HTTP redirects (`follow_redirects=False`).
