from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.domain.agents import IScoutAgent

api_router = APIRouter()
scout_agent = IScoutAgent()

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

@api_router.get("/health")
def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "healthy"}

@api_router.post("/scout/mission", response_model=ScoutMissionResponse)
def dispatch_scout_mission(request: ScoutMissionRequest):
    """
    Despacha o Agente Batedor (Scout) para analisar um alvo executando uma chamada real.
    """
    try:
        result = scout_agent.execute({"target_url": request.target_url})
        return ScoutMissionResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
