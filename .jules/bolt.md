## 2024-05-24 - httpx Client Connection Pooling
**Learning:** Instantiating new HTTP connections for every `httpx.get()` in the Scout/Execution agents is incredibly slow (16.27s for 500 requests). `httpx` documentation states that connection pooling only occurs when requests are routed through a shared `httpx.Client()` instance.
**Action:** Always replace bare `httpx.get` calls with calls through a globally instantiated `_http_client = httpx.Client()` to leverage persistent connection pooling, significantly speeding up agent execution.
