
## 2025-02-24 - HTTP Connection Pooling for Singleton Agents
**Learning:** Initializing isolated `httpx.get()` calls for every request prevents underlying connection reuse. Since `IScoutAgent` and `IExecutionAgent` are initialized as singletons, connection pooling is highly effective and avoids the overhead of establishing new TCP/TLS connections per request.
**Action:** Always prefer instantiating a persistent `httpx.Client()` object inside singleton agents, and implement a `__del__` method with `client.close()` to avoid resource leaks.
