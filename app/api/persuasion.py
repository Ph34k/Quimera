from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.domain.agents import IPersuasionAgent

router = APIRouter(prefix="/persuasion", tags=["🎭 Motor de Persuasão (Persuasion)"])
persuasion_agent = IPersuasionAgent()

# --- Schemas ---

class FinancialAidRequest(BaseModel):
    user_location: str
    target_course: str

class EssayResponse(BaseModel):
    status: str
    generated_essay: str

class ImpactEssayRequest(BaseModel):
    course_syllabus: str
    user_projects: str

class BusinessTrialRequest(BaseModel):
    credit_card_bin: str

class BusinessTrialResponse(BaseModel):
    status: str
    is_allowed: bool
    reason: Optional[str] = None

# --- Endpoints ---

@router.post("/financial-aid-essay", response_model=EssayResponse)
def financial_aid_essay(request: FinancialAidRequest):
    """
    Gera redações para bolsas de estudo usando gatilho matemático de PPP.
    """
    try:
        result = persuasion_agent.execute({
            "trigger": "liking/sympathy (PPP contextualized)",
            "context": f"Financial aid for {request.target_course} from {request.user_location}"
        })
        return EssayResponse(status="success", generated_essay=result.get("persuasive_text", "mock_essay"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/impact-essay", response_model=EssayResponse)
def impact_essay(request: ImpactEssayRequest):
    """
    Cruza ementa com projetos para justificar impacto social e empregabilidade.
    """
    return EssayResponse(status="success", generated_essay="mock_impact_essay_content")

@router.post("/start-business-trial", response_model=BusinessTrialResponse)
def start_business_trial(request: BusinessTrialRequest):
    """
    [Blue Team] Valida o BIN Level para bloquear Cartões Virtuais (VCCs).
    """
    # Mock validation: block if BIN starts with 4 (just as a mock example)
    is_vcc = request.credit_card_bin.startswith("4")
    return BusinessTrialResponse(
        status="success",
        is_allowed=not is_vcc,
        reason="VCC detected" if is_vcc else None
    )
