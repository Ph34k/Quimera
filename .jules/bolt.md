## 2024-04-17 - HTTP Connection Pooling with httpx
**Learning:** Instantiating `httpx.get()` creates a new connection pool per request, adding significant latency. This is particularly noticeable in a microservices/agent architecture where external calls are frequent.
**Action:** Use a shared `httpx.Client()` at the module level or injected into agents to enable connection reuse (keep-alive). This reduces TLS/TCP handshake overhead for repeated requests to the same domains.
