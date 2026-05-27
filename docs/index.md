# 🛡️ Projeto Quimera: Developer Documentation

Welcome to the official developer documentation for **Projeto Quimera**.

Quimera is a backend ecosystem built using **Clean Architecture**. It is primarily designed as a *Blue Team* fortress, providing resilience, integrity validation, and aggressive auditing against advanced fraud methods, academic scraping, and Cloud benefit abuse.

## 📚 Table of Contents

### 1. Core Architecture
Understand the philosophy and structure behind the Quimera ecosystem.
* [System Architecture](architecture.md)

### 2. Autonomous Agents
Detailed documentation, API schemas, and examples for each of the 6 specialized agents.
* [Scout (Reconnaissance)](agents/scout.md)
* [Analyst (Logic & Evaluation)](agents/analyst.md)
* [Execution (Platform Interaction)](agents/execution.md)
* [Persuasion (Social Engineering)](agents/persuasion.md)
* [Scribe (NLP Generation)](agents/scribe.md)
* [Learning (Heuristics & Moderation)](agents/learning.md)

### 3. Tutorials & Guides
Step-by-step instructions for developers and operators.
* [Getting Started](tutorials/getting_started.md)
* [Adding a New Agent](tutorials/adding_new_agent.md)

## 🎯 Quick Start

To spin up the project locally for development, ensure you have Python 3.10+ installed.

```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload
```

Then visit the interactive Swagger UI at `http://localhost:8000/docs`.

---

*This documentation is maintained by the Documentation Engineering team. Keep it in sync with the codebase.*
