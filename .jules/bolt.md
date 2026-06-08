## 2024-06-08 - Persistent HTTPx Client for Connection Pooling
**Learning:** While asynchronous requests (`httpx.AsyncClient`) maximize concurrency, converting synchronous agents to async requires modifying the `BaseAgent` signature and FastAPI routes, which is a significant architectural change.
**Action:** For smaller, less disruptive performance wins, use a persistent synchronous `httpx.Client()` with connection pooling instead of top-level `httpx.get()` calls.
