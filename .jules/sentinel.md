## YYYY-MM-DD - [Title]
**Vulnerability:** [What you found]
**Learning:** [Why it existed]
**Prevention:** [How to avoid next time]

## 2024-05-24 - SSRF in Agent Web Interactions
**Vulnerability:** IScoutAgent and IExecutionAgent accepted user-provided target URLs and executed HTTP requests without validating the hostname, allowing Server-Side Request Forgery against internal infrastructure (e.g., localhost, internal IPs).
**Learning:** External dependencies that make outgoing HTTP calls (like httpx) do not automatically block private IPs. DNS rebinding allows attackers to bypass simple string-matching URL checks.
**Prevention:** Always implement DNS resolution (via socket.getaddrinfo) to resolve the underlying IP before initiating the request, validating that the IP is not in private, loopback, or unspecified ranges. Use an httpx event_hook (like `request` hook) with a persistent Client to reliably intercept and validate all requests, including redirects.
