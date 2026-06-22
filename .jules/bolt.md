## 2024-05-24 - httpx Client Pooling vs Isolated Requests
**Learning:** Using `httpx.get()` directly in agent functions creates a new connection for every request, abandoning TCP/TLS connections. Since the application makes repeated calls out to web assets, we're wasting time on handshakes.
**Action:** Replace `httpx.get(...)` with a globally shared `httpx.Client()` to enable connection pooling and persistent TCP connections, drastically improving performance.
