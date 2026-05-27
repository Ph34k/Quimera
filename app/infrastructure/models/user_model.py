from sqlalchemy import Column, String, Boolean, DateTime
from app.infrastructure.models.base import Base
import uuid
from datetime import datetime

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class HotspotModel(Base):
    __tablename__ = "hotspots_digitais"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    url = Column(String, nullable=False)
    plataforma = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)
