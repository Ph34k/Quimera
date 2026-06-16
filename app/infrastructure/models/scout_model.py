from sqlalchemy import Column, String, Integer, DateTime
from app.infrastructure.models.base import Base
import uuid
from datetime import datetime

class ScoutResultModel(Base):
    __tablename__ = "scout_results"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    target_url = Column(String, nullable=False)
    status = Column(String, nullable=False)
    http_status = Column(Integer, nullable=True)
    content_length = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
