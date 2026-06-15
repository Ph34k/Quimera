## 2025-03-01 - HTTP Connection Pooling for Agents

**Learning:** Agents like `IScoutAgent` and `IExecutionAgent` instantiate a new HTTP connection for each request (via `httpx.get(...)`), creating overhead from DNS resolution and TCP/TLS handshakes every time an agent runs. This causes unnecessary delay, particularly when making multiple requests or re-running agents.

**Action:** Implement `httpx.Client()` at the class level to enable connection pooling for repeated use. However, remember to either clear cookies (`self.client.cookies.clear()`) between runs or explicitly disable cookie persistence, as web-fetching agents across independent tasks should maintain statelessness. Ensure the `client` is properly cleaned up/closed to prevent resource leaks.
