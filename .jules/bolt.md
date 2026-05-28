## 2024-05-28 - HTTPx Client Pooling
**Learning:** Instantiating `httpx.get` on every request introduces significant overhead due to establishing a new TCP connection for every request.
**Action:** Use a persistent `httpx.Client()` object initialized in the class constructor or as a singleton, and properly close it with `__del__` if part of an object lifecycle.
