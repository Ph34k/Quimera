from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from typing import Any, Dict
from app.domain.agents import (
    IScoutAgent, IAnalystAgent, IExecutionAgent,
    IPersuasionAgent, IScribeAgent, ILearningAgent
)

api_router = APIRouter()
scout_agent = IScoutAgent()
analyst_agent = IAnalystAgent()
execution_agent = IExecutionAgent()
persuasion_agent = IPersuasionAgent()
scribe_agent = IScribeAgent()
learning_agent = ILearningAgent()

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

@api_router.post("/analyst/process", response_model=GenericResponse)
def run_analyst(request: GenericRequest):
    """Executes the Analyst Agent."""
    try:
        result = analyst_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/execution/run", response_model=GenericResponse)
def run_execution(request: GenericRequest):
    """Executes the Execution Agent."""
    try:
        result = execution_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/persuasion/generate", response_model=GenericResponse)
def run_persuasion(request: GenericRequest):
    """Executes the Persuasion Agent."""
    try:
        result = persuasion_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/scribe/rewrite", response_model=GenericResponse)
def run_scribe(request: GenericRequest):
    """Executes the Scribe Agent."""
    try:
        result = scribe_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/learning/check", response_model=GenericResponse)
def run_learning(request: GenericRequest):
    """Executes the Learning Agent."""
    try:
        result = learning_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
