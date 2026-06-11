## 2024-05-30 - Add Persistent HTTPX Client
**Learning:** Creating a new `httpx.get` client for every request significantly impacts performance due to the overhead of setting up and tearing down TCP connections. Reusing a persistent client pool minimizes connection latency and overhead.
**Action:** Implement connection pooling by using a persistent `httpx.Client()` object in agents (`IScoutAgent`, `IExecutionAgent`) rather than short-lived `httpx.get()` calls.
