from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database import get_db


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/api/v1/health")
def health_check(
    database_session: Session = Depends(get_db),
) -> dict[str, str]:
    database_session.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
    }