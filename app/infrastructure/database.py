from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Enforce POSTGRES_URL configuration to prevent using unconfigured or hardcoded credentials
if not settings.POSTGRES_URL:
    raise RuntimeError("POSTGRES_URL environment variable is not configured. Hardcoded fallback credentials have been removed for security.")

# Setup SQLAlchemy engine
engine = create_engine(settings.POSTGRES_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
