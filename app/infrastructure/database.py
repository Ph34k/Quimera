from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

if not settings.POSTGRES_URL:
    raise RuntimeError("POSTGRES_URL is not set. Database credentials must be explicitly configured.")

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
