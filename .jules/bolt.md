## 2025-02-27 - Persistent HTTPx Client for Connection Pooling
**Learning:** `httpx.get()` creates and destroys a new connection pool for every request, which is a significant bottleneck in agents making frequent external calls.
**Action:** Use a persistent `httpx.Client()` at the module level to reuse connections across requests, reducing overhead and latency.
