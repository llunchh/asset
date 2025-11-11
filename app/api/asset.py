from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from schemas.asset import AssetRead
from crud.asset import get_all_assets, get_all_servers, get_all_networks, get_all_securities, get_all_storages
from api.deps import get_db

router = APIRouter()

def assets_to_schema(assets) -> List[AssetRead]:
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

@router.get("/all", response_model=List[AssetRead])
def read_assets(
        skip: int = 0,
        status: Optional[int] = None,
        type: Optional[str] = None,
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        db: Session = Depends(get_db)
        ):

    assets = get_all_assets(
            db, 
            skip=skip, 
            status=status,
            type=type,
            category=category,
            subcategory=subcategory,
            hostname=hostname,
            ip=ip)

    return assets_to_schema(assets)

@router.get("/servers", response_model=List[AssetRead])
def read_servers(
        skip: int = 0,
        status: Optional[int] = None,
        type: Optional[str] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        db: Session = Depends(get_db)
        ):

    servers = get_all_servers(
            db,
            skip=skip,
            status=status,
            type=type,
            subcategory=subcategory,
            hostname=hostname,
            ip=ip)

    return assets_to_schema(servers)


@router.get("/networks", response_model=List[AssetRead])
def read_networks(
        skip: int = 0,
        status: Optional[int] = None,
        type: Optional[str] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        db: Session = Depends(get_db)
        ):

    networks = get_all_networks(
            db,
            skip=skip,
            status=status,
            type=type,
            subcategory=subcategory,
            hostname=hostname,
            ip=ip)

    return assets_to_schema(networks)


@router.get("/securities", response_model=List[AssetRead])
def read_security(
        skip: int = 0,
        status: Optional[int] = None,
        type: Optional[str] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        db: Session = Depends(get_db)
        ):
    
    security = get_all_securities(
            db,
            skip=skip,
            status=status,
            type=type,
            subcategory=subcategory,
            hostname=hostname,
            ip=ip)
    
    return assets_to_schema(security)


@router.get("/storages", response_model=List[AssetRead])
def read_storage(
        skip: int = 0,
        status: Optional[int] = None,
        type: Optional[str] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        db: Session = Depends(get_db)
        ):
    
    storages = get_all_storages(
            db,
            skip=skip,
            status=status,
            type=type,
            subcategory=subcategory,
            hostname=hostname,
            ip=ip)
    
    return assets_to_schema(storages)
