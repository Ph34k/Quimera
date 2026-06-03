## 2024-06-03 - Connection Pooling for Sync Agents
**Learning:** Implementing connection pooling by using a persistent synchronous `httpx.Client()` in singletons/long-lived agents provides a measurable performance win without the architectural disruption of migrating synchronous agents to async.
**Action:** Apply persistent `httpx.Client` instances with a `__del__` lifecycle hook to safely close connections when maintaining synchronous agent constraints.
