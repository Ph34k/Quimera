## 2024-06-14 - Persisting HTTP connections while avoiding state leakage
**Learning:** When reusing a persistent `httpx.Client()` across multiple independent tasks (e.g., in long-running or singleton agents like `IScoutAgent` or `IExecutionAgent` to gain connection pooling performance), the client will persist cookies across requests by default, leading to state leakage.
**Action:** Explicitly clear or disable the client's cookie jar (`self.client.cookies.clear()`) to maintain statelessness between tasks targeting the same domain.
