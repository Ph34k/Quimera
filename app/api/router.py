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

@api_router.get("/health", tags=["System"], summary="System Health Check")
def health_check():
    """Returns the operational status of the API."""
    return {"status": "healthy"}

@api_router.post("/scout/mission", response_model=ScoutMissionResponse, tags=["Scout"], summary="Dispatch Reconnaissance Mission")
def dispatch_scout_mission(request: ScoutMissionRequest):
    """
    Dispatches the Scout Agent to perform reconnaissance on a target URL.
    - Performs an actual HTTP GET request to the target.
    - Measures response time, status code, and payload size.
    """
    try:
        result = scout_agent.execute({"target_url": request.target_url})
        return ScoutMissionResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.post("/analyst/process", response_model=GenericResponse, tags=["Analyst"], summary="Execute Text Analysis")
def run_analyst(request: GenericRequest):
    """
    Executes the Analyst Agent on provided text.
    - Utilizes Large Language Models (LLM) to parse text.
    - Extracts semantic value, keywords, and overall sentiment.
    - **Requires**: valid OPENAI_API_KEY.
    """
    try:
        result = analyst_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/execution/run", response_model=GenericResponse, tags=["Execution"], summary="Execute Platform Action")
def run_execution(request: GenericRequest):
    """
    Commands the Execution Agent to interact with external platforms.
    - Uses advanced HTTP headers to mimic organic browsing behavior.
    - Handles target actions like `ping`, status checks, etc.
    """
    try:
        result = execution_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/persuasion/generate", response_model=GenericResponse, tags=["Persuasion"], summary="Generate Persuasive Copy")
def run_persuasion(request: GenericRequest):
    """
    Generates text using Robert Cialdini's psychological triggers.
    - Defaults to the 'reciprocity' trigger if not provided.
    - Highly contextualized to the specific target domain.
    - **Requires**: valid OPENAI_API_KEY.
    """
    try:
        result = persuasion_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/scribe/rewrite", response_model=GenericResponse, tags=["Scribe"], summary="Rewrite Text via Persona")
def run_scribe(request: GenericRequest):
    """
    The Scribe Agent acts as a linguistic filter.
    - Takes a raw draft text and rewrites it to match the confident 'Alex' persona.
    - Standardizes tone across automated outputs.
    - **Requires**: valid OPENAI_API_KEY.
    """
    try:
        result = scribe_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/learning/check", response_model=GenericResponse, tags=["Learning"], summary="Check Interaction Risk")
def run_learning(request: GenericRequest):
    """
    The Learning Agent validates behavioral rules to avoid shadow-bans.
    - Tracks recent interaction timestamps for specific targets.
    - Currently enforces a strict 60-second cooldown period per target.
    """
    try:
        result = learning_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
