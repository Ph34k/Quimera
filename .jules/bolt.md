## 2024-05-27 - HTTP Connection Pooling in ScoutAgent
**Learning:** Instantiating a new `httpx` connection for every request is expensive and creates unnecessary overhead for long-lived components.
**Action:** When implementing agents or services that perform repetitive external HTTP calls, instantiate a persistent `httpx.Client()` at initialization and reuse it via `self.client.get(...)`. Always ensure resource lifecycle safety with a corresponding `__del__` block.
