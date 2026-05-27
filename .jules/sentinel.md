## 2024-05-27 - Disabled Elasticsearch Security

**Vulnerability:** Elasticsearch instance in docker-compose explicitly disabled security (`xpack.security.enabled=false`), exposing the database on port 9200 without authentication.
**Learning:** Default settings or quick-start examples often disable security features for ease of setup, creating significant risks if deployed. Elasticsearch 8.x introduces strict security by default, which is bypassed if `xpack.security.enabled` is explicitly turned off.
**Prevention:** Always enable built-in security features (`xpack.security.enabled=true`). When configuring for local/docker environments without SSL, ensure `xpack.security.http.ssl.enabled=false` is set, but still require authentication by providing an `ELASTIC_PASSWORD` and updating connection strings to use HTTP Basic Auth (`http://elastic:password@host`).
