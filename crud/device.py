from sqlalchemy.orm import Session
from models.device import Device
from schemas.device import DeviceRead

def get_devices(db: Session, skip: int = 0, limit: int = 10) -> list[Device]:
    return db.query(Device).offset(skip).limit(limit).all()
