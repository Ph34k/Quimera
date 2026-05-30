## 2026-05-27 - Elasticsearch Security
**Vulnerability:** Disabled Elasticsearch security (xpack.security.enabled=false).
**Learning:** Elasticsearch should have security enabled to prevent unauthorized access to data.
**Prevention:** Always set xpack.security.enabled=true and configure credentials.
## 2025-05-30 - Remove hardcoded configuration secrets
**Vulnerability:** Hardcoded PostgreSQL URL and API Secret Key exposed in configuration defaults.
**Learning:** Hardcoding credentials in config defaults leaks sensitive information even if overridden in production. It is a critical risk when repositories are shared or exposed.
**Prevention:** Always use environment variables without sensitive fallback defaults for credentials, and enforce configuration correctness explicitly at application startup.
