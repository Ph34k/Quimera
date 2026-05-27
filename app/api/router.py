from fastapi import APIRouter
from app.api import scout, analyst, execution, persuasion, scribe, learning

api_router = APIRouter()

@api_router.get("/health", tags=["System"])
def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "healthy"}

api_router.include_router(scout.router)
api_router.include_router(analyst.router)
api_router.include_router(execution.router)
api_router.include_router(persuasion.router)
api_router.include_router(scribe.router)
api_router.include_router(learning.router)
