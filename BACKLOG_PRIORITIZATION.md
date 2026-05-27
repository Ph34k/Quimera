# Backlog Prioritization: Projeto Quimera

We utilize the **RICE Scoring Model** (Reach, Impact, Confidence, Effort) to prioritize our backlog. This ensures we deliver the highest value to our enterprise users while managing engineering capacity efficiently.

* **Reach:** How many users/requests will this affect over a single quarter? (1-10)
* **Impact:** How much will this move the needle on our North Star metric (Fraud Mitigation)? (3 = massive, 2 = high, 1 = medium, 0.5 = low)
* **Confidence:** How confident are we in our estimates and technical approach? (100% = high, 80% = medium, 50% = low)
* **Effort:** How many "person-months" will this take? (1, 2, 3...)
* **RICE Score = (Reach * Impact * Confidence) / Effort**

---

## 1. High Priority (Do Now)

### Execution Agent: Stealth Logic & Cloud Sandboxing
- **Context:** Cloud resource hijacking (crypto mining) causes direct, immense financial loss. Stopping this is mission-critical for our cloud provider clients.
- **RICE Score:** **60.0**
  - **Reach:** 8 (Affects all cloud trial users)
  - **Impact:** 3 (Massive financial impact)
  - **Confidence:** 100%
  - **Effort:** 0.4 (approx 2 weeks)

### Analyst Agent: NLP "Big Five" & AST Inspection
- **Context:** Hardcoded autograder exploits destroy the integrity of certifications. This feature directly supports our core value proposition to EdTech platforms.
- **RICE Score:** **48.0**
  - **Reach:** 10 (Affects all assessment users)
  - **Impact:** 3 (Massive integrity impact)
  - **Confidence:** 80%
  - **Effort:** 0.5 (approx 2-3 weeks)

### Learning Agent: Redis Rate Limiting & Server-Time
- **Context:** Time-travel headers and speedrunning are common, low-barrier attacks that invalidate course completion metrics.
- **RICE Score:** **40.0**
  - **Reach:** 10 (Affects all video/course module interactions)
  - **Impact:** 2 (High impact on completion metrics)
  - **Confidence:** 100%
  - **Effort:** 0.5 (approx 2-3 weeks)

---

## 2. Medium Priority (Do Next)

### Scout Agent: Selenium/BS4 Data Extraction
- **Context:** Proactively finding leaked credentials/hotspots is important for threat intel, but less critical than stopping active attacks happening on our infrastructure.
- **RICE Score:** **24.0**
  - **Reach:** 6 (Affects a subset of compromised accounts)
  - **Impact:** 2 (High impact for intelligence)
  - **Confidence:** 100%
  - **Effort:** 0.5 (approx 2-3 weeks)

### CI/CD Pipelines & Pre-Commit Hooks
- **Context:** Essential for team velocity and platform stability, but does not directly deliver new user-facing value.
- **RICE Score:** **21.3**
  - **Reach:** 10 (Internal engineering team and all future code)
  - **Impact:** 1 (Medium - improves stability)
  - **Confidence:** 100%
  - **Effort:** 0.47 (approx 2 weeks)

---

## 3. Low Priority (Do Later)

### Persuasion Agent: Cialdini Triggers
- **Context:** Generating social engineering defenses is valuable, but the immediate threat of VCCs is better handled by deterministic BIN blocking.
- **RICE Score:** **12.0**
  - **Reach:** 5
  - **Impact:** 1
  - **Confidence:** 80%
  - **Effort:** 0.33 (approx 1.5 weeks)

### Scribe Agent: RAG Mapeamento
- **Context:** Countering forum spam is a lower priority compared to direct cloud resource and certification abuse.
- **RICE Score:** **10.6**
  - **Reach:** 4
  - **Impact:** 1
  - **Confidence:** 80%
  - **Effort:** 0.3 (approx 1.5 weeks)

### ElasticSearch MLOps Pipeline Integration
- **Context:** Complex architecture addition. Extremely valuable long-term, but requires foundational agents to be active to gather the necessary training data.
- **RICE Score:** **8.0**
  - **Reach:** 10
  - **Impact:** 2
  - **Confidence:** 50%
  - **Effort:** 1.25 (approx 5-6 weeks)
