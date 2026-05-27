import os
from dataclasses import dataclass
from typing import Optional

def _get_secret_key() -> str:
    env = os.getenv("ENVIRONMENT", "development")
    secret = os.getenv("SECRET_KEY")
    if env == "production" and not secret:
        raise ValueError("SECRET_KEY must be provided in production environment")
    return secret or "default_secret_key_for_dev"

@dataclass
class Settings:
    PROJECT_NAME: str = "Projeto Quimera"
    VERSION: str = "0.1.0"

    # API / Security
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    SECRET_KEY: str = _get_secret_key()
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Database
    POSTGRES_URL: str = os.getenv(
        "POSTGRES_URL",
        "postgresql://quimera_user:quimera_password@localhost:5432/quimera_db"
    )

    # Cache / Search
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    ELASTICSEARCH_URL: str = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")

settings = Settings()
