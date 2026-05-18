## 2024-05-18 - HTTP Connection Pooling for External Requests
**Learning:** Instantiating new connections (`httpx.get()`) on every agent execution adds significant overhead due to DNS resolution, TCP handshakes, and SSL negotiation. In high-throughput environments, this can become a major bottleneck.
**Action:** Always initialize a persistent `httpx.Client()` session inside classes (like agents) that make frequent external requests. Manage the lifecycle safely by closing the client during cleanup (`__del__` with try/except blocks to prevent resource leak issues).
