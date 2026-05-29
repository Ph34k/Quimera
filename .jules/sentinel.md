## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.

## 2026-05-29 - Hardcoded Database Credentials
**Vulnerability:** Hardcoded PostgreSQL connection string with credentials in default fallback configuration (`app/core/config.py`).
**Learning:** Hardcoding credentials, even as defaults for local development, is a security vulnerability as they might end up in production or exposed. Configuration variables should fail securely if undefined.
**Prevention:** Remove sensitive default credentials and raise exceptions at runtime if critical configurations are missing.
