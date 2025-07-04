import logging
from fastapi import FastAPI

from app.core.config import settings
from app.core.observability import setup_observability
from app.api.v1.api import api_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

setup_observability(app)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}
