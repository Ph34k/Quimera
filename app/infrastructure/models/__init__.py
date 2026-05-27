from app.infrastructure.models.base import Base
from app.infrastructure.models.scout_model import ScoutResultModel
from app.infrastructure.models.user_model import UserModel, HotspotModel

# Expose models for Alembic
__all__ = ["Base", "ScoutResultModel", "UserModel", "HotspotModel"]
