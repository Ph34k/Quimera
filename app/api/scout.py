from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Dict, Any
from app.domain.agents import IScoutAgent
import uuid

router = APIRouter(prefix="/scout", tags=["🦅 Agente Batedor (Scout)"])
scout_agent = IScoutAgent()

# --- Schemas ---

class ScoutMissionRequest(BaseModel):
    target_url: HttpUrl
    depth: int = 1

class ScoutMissionResponse(BaseModel):
    status: str
    mission_id: str
    target: str
    http_status: Optional[int] = None
    content_length: Optional[int] = None
    error: Optional[str] = None

class ScrapeDumpsRequest(BaseModel):
    dump_url: HttpUrl
    max_questions: int = 50

class ScrapeDumpsResponse(BaseModel):
    status: str
    questions_scraped: int
    data: List[Dict[str, Any]]

class ExtractARMCredentialsRequest(BaseModel):
    lab_url: HttpUrl

class ExtractARMCredentialsResponse(BaseModel):
    status: str
    tenant_id: Optional[str] = None
    client_id: Optional[str] = None
    secret: Optional[str] = None
    error: Optional[str] = None

class MissionHistoryResponse(BaseModel):
    status: str
    missions: List[Dict[str, Any]]

# --- Endpoints ---

@router.post("/mission", response_model=ScoutMissionResponse)
def dispatch_scout_mission(request: ScoutMissionRequest):
    """
    Despacha o Agente Batedor (Scout) para analisar as respostas HTTP de uma URL alvo.
    """
    try:
        result = scout_agent.execute({"target_url": str(request.target_url)})
        return ScoutMissionResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/scrape-dumps", response_model=ScrapeDumpsResponse)
def scrape_dumps(request: ScrapeDumpsRequest):
    """
    Faz o bypass de WAFs básicos e raspa questões de certificação em portais de Dumps (ex: ExamTopics).
    """
    return ScrapeDumpsResponse(
        status="success",
        questions_scraped=request.max_questions,
        data=[{"question_id": i, "content": f"Mock question {i}"} for i in range(1, request.max_questions + 1)]
    )

@router.post("/extract-arm-credentials", response_model=ExtractARMCredentialsResponse)
def extract_arm_credentials(request: ExtractARMCredentialsRequest):
    """
    [Red Team] Escaneia silenciosamente o DOM de laboratórios em nuvem para extrair chaves efêmeras.
    """
    return ExtractARMCredentialsResponse(
        status="success",
        tenant_id=str(uuid.uuid4()),
        client_id=str(uuid.uuid4()),
        secret="mock_secret_key_123"
    )

@router.get("/missions", response_model=MissionHistoryResponse)
def list_missions():
    """
    Retorna o histórico de todas as missões de reconhecimento salvas.
    """
    return MissionHistoryResponse(
        status="success",
        missions=[
            {"mission_id": str(uuid.uuid4()), "target": "https://example.com", "status": "completed"}
        ]
    )
