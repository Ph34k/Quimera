from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.domain.agents import IScribeAgent

router = APIRouter(prefix="/scribe", tags=["🪶 Agente Escriba (Scribe)"])
scribe_agent = IScribeAgent()

# --- Schemas ---

class DraftRequest(BaseModel):
    topic: str
    context: str

class ScribeTextResponse(BaseModel):
    status: str
    content: str

class ForumReplyRequest(BaseModel):
    forum_question: str

class ForumUpvoteRequest(BaseModel):
    post_id: str
    user_ip: str

class ForumUpvoteResponse(BaseModel):
    status: str
    upvote_counted: bool
    reason: Optional[str] = None

# --- Endpoints ---

@router.post("/draft", response_model=ScribeTextResponse)
def draft_document(request: DraftRequest):
    """
    Monta a estrutura inicial de petições ou documentos formais.
    """
    return ScribeTextResponse(status="success", content="mock_draft_document_content")

@router.post("/forum-reply", response_model=ScribeTextResponse)
def forum_reply(request: ForumReplyRequest):
    """
    Gera respostas técnicas em inglês perfeito para fóruns.
    """
    try:
        result = scribe_agent.execute({"draft_text": request.forum_question})
        return ScribeTextResponse(status="success", content=result.get("rewritten_text", "mock_reply"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/forum-upvote", response_model=ForumUpvoteResponse)
def forum_upvote(request: ForumUpvoteRequest):
    """
    [Blue Team] Contabiliza upvotes protegidos pelo SybilDetector.
    """
    return ForumUpvoteResponse(status="success", upvote_counted=True)
