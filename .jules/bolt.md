## 2025-03-01 - HTTP Connection Pooling with httpx
**Learning:** Using `httpx.get()` directly inside high-throughput or repeatedly instantiated agents creates a new HTTP connection for every request, which is inefficient.
**Action:** Always instantiate a globally shared `httpx.HTTPTransport()` and pass it to short-lived `with httpx.Client(transport=shared_transport) as client:` blocks. This preserves connection pooling while keeping request state isolated per-request.
