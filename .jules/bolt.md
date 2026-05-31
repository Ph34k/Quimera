## 2024-05-31 - Use Connection Pooling for HTTPx Clients
**Learning:** Using `httpx.get()` directly in long-lived agents (like `IScoutAgent` and `IExecutionAgent`) opens a new connection for every request, which is inefficient. Instantiating a persistent `httpx.Client()` enables connection pooling, significantly reducing latency on repeated external API calls.
**Action:** When singletons or long-lived agents instantiate persistent connections like `httpx.Client()`, always implement connection pooling and implement a `__del__` method that cleanly closes the resource to prevent leaks.
