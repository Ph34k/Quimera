from fastapi import FastAPI
from app.core.config import settings
from app.api.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend Ecosystem for Offensive/Defensive Auditing and Social Engagement Automation"
)

# Include MVP routers
app.include_router(api_router, prefix="/api/v1")

@app.on_event("shutdown")
def shutdown_event():
    from app.api.router import scout_agent, execution_agent
    scout_agent.close()
    execution_agent.close()

@app.get("/")
def read_root():
    return {
        "status": "online",
        "project": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT
    }
