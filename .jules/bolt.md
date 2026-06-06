## 2026-06-06 - Connection Pooling over Async Conversion
**Learning:** In agent architectures using Fastapi/httpx, converting synchronous methods to async (`httpx.AsyncClient`) requires significant architectural changes to the `BaseAgent` signature.
**Action:** For less disruptive performance wins, prefer implementing a persistent, shared `httpx.Client()` at the module level to gain connection pooling benefits.
