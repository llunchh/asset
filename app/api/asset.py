from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from schemas.asset import AssetRead
from crud.asset import get_all_assets
from api.deps import get_db

router = APIRouter()

@router.get("/all", response_model=List[AssetRead])
def read_assets(
        skip: int = 0,
        status: Optional[int] = None,
        type: Optional[str] = None,
        category: Optional[str] = None,
        db: Session = Depends(get_db)
        ):

    assets = get_all_assets(
            db, 
            skip=skip, 
            status=status,
            type=type,
            category=category)
    
    return [
        AssetRead(
            id=a.id,
            status=a.status,
            type=a.type,
            category=a.category,
            hostname=a.hostname,
            ip=a.ip,
            os_name=a.os_obj.name if a.os_obj else "Unknown"
        )
        for a in assets
    ]
