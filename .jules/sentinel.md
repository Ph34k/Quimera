## 2024-05-17 - Prevent Server-Side Request Forgery (SSRF) in AI Agents

**Vulnerability:** The AI agents (`IScoutAgent` and `IExecutionAgent`) executed HTTP requests using URLs directly provided by the user via the API payload without validating the target domains or IPs. This allowed an attacker to instruct the agents to request internal services (like `http://localhost`, `http://127.0.0.1`) or cloud metadata endpoints (like `http://169.254.169.254/latest/meta-data/`).

**Learning:** When building agents that perform actions on behalf of the user (like fetching web pages), it's crucial to realize that the server executing the agent holds a privileged network position. Trusting user-provided URLs blindly leads to SSRF, enabling internal network scanning and cloud metadata exfiltration.

**Prevention:** Implemented an `is_safe_url` validation utility that parses user URLs and blocks private, loopback, link-local, multicast, and unspecified IP ranges, as well as the 'localhost' hostname. This check is applied both directly within the agent execution flow and via an `httpx` event hook (`verify_request`) to catch redirects to malicious destinations. The agents were updated to use a persistent `httpx.Client` to leverage the event hook functionality.
