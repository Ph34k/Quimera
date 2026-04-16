
## 2023-10-27 - httpx.Client vs httpx.get Connection Pooling
**Learning:** Using `httpx.get()` creates and destroys a new connection pool per request, incurring DNS and TCP/TLS handshake overhead every time. By moving to a single global `httpx.Client()` and reusing it for external queries in the `IScoutAgent` and `IExecutionAgent`, we utilize HTTP Keep-Alive, heavily accelerating subsequent requests to the same targets.
**Action:** Always consider using a persistent client (like `httpx.Client` or `httpx.AsyncClient`) for repeated HTTP requests instead of the top-level convenience methods.
