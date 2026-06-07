## 2026-06-07 - HTTP Connection Pooling for Agents
**Learning:** Using httpx.get() creates a new TCP/TLS connection for every HTTP request. In synchronous agents, transitioning to async requires major architecture changes. However, using a persistent synchronous httpx.Client() provides connection pooling out-of-the-box, drastically reducing request latency without architectural disruption.
**Action:** Always prefer using a persistent httpx.Client() (or AsyncClient) instead of top-level httpx.get/post when making repeated HTTP requests to take advantage of connection pooling.
