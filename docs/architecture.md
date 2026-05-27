# 🏛️ Architecture & Philosophy

The foundation of Quimera is highly modular, strictly adhering to **Clean Architecture** principles.

## The Separation of Concerns

All fraud detection rules and core logic reside in the **Application/Domain Layer**. They are framework-independent (decoupled from FastAPI) and abstracted through Protocols and Dependency Injection. The HTTP router never makes blocking decisions; it simply receives data and surfaces exceptions thrown by the deep domain logic.

### Folder Structure

*   **`app/domain/`**: Base entities (e.g., `BaseAgent`) and contractual abstractions for defense.
*   **`app/core/`**: Central configuration (Settings, Environment variables).
*   **`app/api/`**: Clean FastAPI endpoints (`router.py`) acting solely as the delivery mechanism.
*   **`infrastructure/`** *(Future Scope)*: Heavy anti-bot machinery (Scrapers, Cryptography, AST Parsing).

## ⚔️ The 6 Specialized Agents

The system routes operations through six distinct agents, each specializing in countering specific threats or executing targeted maneuvers:

1.  **🕵️ Scout**: Poisoning and Dump Scraping detection.
2.  **✍️ Scribe**: Sybil attacks and Forum upvote farming.
3.  **💬 Persuasion**: VCC Trial abuse for economic gain.
4.  **🧠 Learning**: Speedrunning, Time Travel headers.
5.  **⚙️ Analyst**: Autograder Bypass and JSON Exfiltration.
6.  **🚀 Execution**: OOB Deploy and Sandbox Crypto-mining.

## 🧱 The 10 Lines of Cyber-Defense

In response to aggressive automation, the backend is designed to execute physical barriers:

| Attack Vector | Offensive Action | Quimera Active Defense |
| :--- | :--- | :--- |
| **1. Time-Travel Header** | Falsifying client-side DOM time | Absolute Server-Side Clock (`time_service.py`). |
| **2. Shadow Botting** | Simultaneous requests (Sybil) | IP Tracking & Behavioral Rate Limiting. |
| **3. Virtual Credit Cards** | Mass use of VCCs for free trials | Strict BIN Analysis blocking pre-paid cards. |
| **4. Cloud Hit-and-Run** | Stopping labs right after API 100% | Sustained Uptime Metrics. |
| **5. Camera Spoofing OBS** | Injecting fake WebRTC | Onfido Biometric liveness 3D. |
| **6. Credential Scraping** | Stealing brute vouchers | Geolocking, Humanity Checks, Token Watermarking. |
| **7. IAM Escalation Abuse** | Crypto mining in labs | Sandboxing and VPC privilege stripping. |
| **8. Quiz JSON Exfiltration** | Direct API scraping to Github | AES payloads and ID Polymorphism. |
| **9. Autograder Hardcoding** | Direct assert values | Structural AST (Abstract Syntax Tree) inspection. |
| **10. CLI Remote Deploy** | Stolen Service Principal usage | Conditional Access IPs and Bastion Iframes. |
