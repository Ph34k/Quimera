from fastapi import FastAPI
from app.core.config import settings
from app.api.router import api_router

tags_metadata = [
    {
        "name": "System",
        "description": "Core system operations and health checks.",
    },
    {
        "name": "Scout",
        "description": "Reconnaissance operations, OSINT, and Target Identification.",
    },
    {
        "name": "Analyst",
        "description": "Semantic Processing, NLP Analysis, and Profile evaluation.",
    },
    {
        "name": "Execution",
        "description": "Direct platform interaction and stealth web driving.",
    },
    {
        "name": "Persuasion",
        "description": "Social engineering and application of psychological triggers.",
    },
    {
        "name": "Scribe",
        "description": "Persona-driven Natural Language Generation.",
    },
    {
        "name": "Learning",
        "description": "Heuristics and Behavioral validation/shadow-ban checks.",
    },
]

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="""
    # 🛡️ Quimera API
    Backend Ecosystem for Offensive/Defensive Auditing and Social Engagement Automation.

    This API provides direct access to the 6 specialized autonomous agents.

    See the [Developer Documentation](../docs) in the repository for detailed architecture and tutorials.
    """,
    openapi_tags=tags_metadata,
    contact={
        "name": "Documentation Engineering Team",
    }
)

# Include MVP routers
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "project": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT
    }
