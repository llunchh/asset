from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas.device import DeviceRead
from crud.device import get_devices
from api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[DeviceRead])
def read_devices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    devices = get_devices(db, skip=skip, limit=limit)
    return devices
