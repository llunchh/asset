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
        subcategory: Optional[str] = None,
        db: Session = Depends(get_db)
        ):

    assets = get_all_assets(
            db, 
            skip=skip, 
            status=status,
            type=type,
            category=category,
            subcategory=subcategory)
    
    return [
        AssetRead(
            id=a.id,
            status=a.status,
            type=a.type,
            category=a.category_obj.name if a.category_obj else "Unknown",
            subcategory=a.subcategory_obj.name if a.subcategory_obj else "Unknown",
            hostname=a.hostname,
            ip=a.ip,
            os=a.os_obj.name if a.os_obj else "Unknown"
        )
        for a in assets
    ]
