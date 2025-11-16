from fastapi import APIRouter
from api import asset
from api import account

api_router = APIRouter()
api_router.include_router(asset.router, prefix="/asset", tags=["asset"])
api_router.include_router(account.router, prefix="/account", tags=["account"])
