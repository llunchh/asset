from fastapi import FastAPI
from api.routers import api_router

app = FastAPI(
    title="Asset API",
    description="Asset documentation",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api")
