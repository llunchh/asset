from fastapi import APIRouter
from api import asset

api_router = APIRouter()
api_router.include_router(asset.router, prefix="/asset", tags=["asset"])
