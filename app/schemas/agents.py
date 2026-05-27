from pydantic import BaseModel
from typing import Optional, Any, Dict

class GenericRequest(BaseModel):
    payload: Dict[str, Any]

class GenericResponse(BaseModel):
    result: Dict[str, Any]

class ScoutMissionRequest(BaseModel):
    target_url: str
    depth: int = 1

class ScoutMissionResponse(BaseModel):
    status: str
    mission_id: str
    target: str
    http_status: Optional[int] = None
    content_length: Optional[int] = None
    error: Optional[str] = None
