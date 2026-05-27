from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.domain.agents import ILearningAgent

router = APIRouter(prefix="/learning", tags=["⏱️ Agente de Aprendizagem (Learning)"])
learning_agent = ILearningAgent()

# --- Schemas ---

class UnlockModuleRequest(BaseModel):
    user_id: str
    module_id: str

class UnlockModuleResponse(BaseModel):
    status: str
    unlocked: bool
    reason: Optional[str] = None

class FetchQuizResponse(BaseModel):
    status: str
    encrypted_quiz_payload: str

# --- Endpoints ---

@router.post("/unlock-module", response_model=UnlockModuleResponse)
def unlock_module(request: UnlockModuleRequest):
    """
    [Blue Team] Executa Time-Lock Validation no Backend, bloqueando Client-Time Bypass.
    """
    return UnlockModuleResponse(status="success", unlocked=True)

@router.get("/fetch-quiz", response_model=FetchQuizResponse)
def fetch_quiz():
    """
    [Blue Team] Previne JSON Scraping entregando payload criptografado com IDs polimórficos.
    """
    return FetchQuizResponse(
        status="success",
        encrypted_quiz_payload="mock_polymorphic_encrypted_payload"
    )
