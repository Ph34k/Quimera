## 2026-04-17 - [SSRF Vulnerability in Scout and Execution Agents]
**Vulnerability:** The IScoutAgent and IExecutionAgent made external HTTP requests using user-provided URLs (`target_url`) without any validation, allowing for Server-Side Request Forgery (SSRF) against internal network resources (e.g. localhost:5432, 127.0.0.1, or metadata services).
**Learning:** The project relies on real HTTP requests via `httpx` based on payload inputs instead of mocks. This direct bridging of user input to HTTP clients creates an immediate SSRF risk if URLs are not sanitized.
**Prevention:** Implement a utility function (`is_safe_url`) that resolves hostnames and explicitly blocks loopback, private, link-local IPs, and non-HTTP schemes, and ensure all outbound agent requests run this check first.
