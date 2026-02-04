from fastapi import FastAPI
from api.app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Image geolocation service (classification -> retrieval).",
)


@app.get("/")
def root():
    return {"service": "geovision", "env": settings.environment, "docs": "/docs"}


@app.get("/health")
def health():
    return {"ok": True}
