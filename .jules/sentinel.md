## 2024-05-24 - Hardcoded Database Credentials in Fallback URL
**Vulnerability:** Hardcoded Default Credentials
**Learning:** Hardcoded credentials acting as defaults in `os.getenv` fallback values constitute a security vulnerability as they get committed to source control and could be inadvertently used in production or staging if the explicit configuration is missing.
**Prevention:** Use `os.environ["VAR_NAME"]` to enforce mandatory explicit configuration so the application fails fast securely instead of silently defaulting to known passwords.
