## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2024-05-31 - Enforce Explicit Database Configuration
**Vulnerability:** The application had hardcoded fallback database credentials (`POSTGRES_URL`) and a dummy `SECRET_KEY` in `app/core/config.py`.
**Learning:** Hardcoded credentials in fallback configurations are security vulnerabilities in this specific context, even if intended for local development. They can accidentally be deployed or expose default credentials to attackers.
**Prevention:** Remove fallback credentials and enforce explicit configuration by making sensitive variables `Optional` and raising an error downstream (e.g., during database initialization) if they are missing.
