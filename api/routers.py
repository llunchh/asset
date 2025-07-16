from fastapi import APIRouter
from api import device

api_router = APIRouter()
api_router.include_router(device.router, prefix="/devices", tags=["devices"])
