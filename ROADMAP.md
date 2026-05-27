# Roadmap: Projeto Quimera

*Status: Q3/Q4 Planning*

## Strategic Themes
1. **Agent Expansion & Threat Mitigation:** Fully deploy the remaining 5 critical defense agents to cover all identified attack vectors.
2. **Advanced Analytics & MLOps:** Transition from purely deterministic rules to behavioral, machine learning-driven anomaly detection.
3. **Enterprise Readiness:** Ensure the platform is scalable, observable, and easy to deploy via CI/CD pipelines.

---

## Q3: Quarter of the Agents (Implementation Phase)
**Objective:** Deliver the core active defense mechanisms to mitigate the highest-impact threats (Fraud, Resource Abuse, Integrity).

### Month 1: Intelligence & Access Control
- **Scout Agent Enhancement:** Implement Selenium/BeautifulSoup extraction for hotspot data gathering to identify credential dumping early.
- **Execution Agent Launch:** Integrate stealth logic, proxy/user-agent rotation, and lab sandboxing (conditional access) to prevent remote deploy abuse and cloud resource hijacking.

### Month 2: Academic Integrity & Trust
- **Analyst Agent Integration:** Connect the NLP pipeline (OpenAI) to generate "Big Five" scoring for user profiles, alongside AST (Abstract Syntax Tree) inspection to block hardcoded autograder exploits.
- **Learning Agent Rollout:** Implement Redis-based rate limiting and absolute server-side time tracking to prevent time-travel headers and speedrunning of assessments.

### Month 3: Behavioral Defense
- **Scribe Agent Deployment:** Map Retrieval-Augmented Generation (RAG) to counter forum spam, shadow botting, and sybil attacks.
- **Persuasion Agent Rollout:** Create template engines for Cialdini triggers, paired with strict BIN analysis to defend against Virtual Credit Card trial farming.

---

## Q4: Quarter of Scale (Product Excellence Phase)
**Objective:** Solidify infrastructure, implement machine learning capabilities, and ensure enterprise-grade reliability.

### Month 1: Data Infrastructure & Search
- **ORM Completion:** Finalize all SQLAlchemy models.
- **Alembic Migrations:** Execute full database schema migrations for production readiness.
- **ElasticSearch Integration:** Connect ElasticSearch to the vectorization pipeline for fast, semantic search across user profiles and documentation.

### Month 2: Automation & DevOps
- **Code Quality Gates:** Implement pre-commit hooks (Black, isort, Ruff) to enforce the Clean Architecture standards.
- **CI/CD Pipelines:** Build GitHub Actions workflows for automated testing, linting, and Docker container deployment.

### Month 3: Launch & Iteration
- **Analytics Dashboarding:** Setup comprehensive dashboards for funnel analysis, agent success rates, and threat mitigation monitoring.
- **Post-Launch Iteration:** Conduct user interviews with early enterprise adopters, refine agent thresholds based on false-positive rates, and plan Q1 roadmap.
