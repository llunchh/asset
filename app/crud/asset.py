from sqlalchemy.orm import Session
from models.asset import Asset, Category, SubCategory, Os
from schemas.asset import AssetRead
from typing import Optional
from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import INET

def get_all_assets(
        db: Session, 
        skip: int = 0,
        status: Optional[int] = None,
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        type: Optional[str] = None) -> list[Asset]: 

    query = db.query(Asset).join(Os).join(Category).join(SubCategory)

    if status is not None:
        query = query.filter(Asset.status == status)
    if type is not None:
        query = query.filter(Asset.type == type)
    if category is not None:
        query = query.filter(Category.name == category)
    if subcategory is not None:
        query = query.filter(SubCategory.name == subcategory)
    if hostname is not None:
        query = query.filter(Asset.hostname == hostname)
    if ip is not None:
        query = query.filter(Asset.ip == cast(ip, INET))

    return query.offset(skip).all()

def get_all_servers(
        db: Session,
        skip: int = 0,
        status: Optional[int] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        type: Optional[str] = None) -> list[Asset]:

    query = db.query(Asset).join(Os).join(Category).join(SubCategory)

    query = query.filter(Category.name == "server")

    if status is not None:
        query = query.filter(Asset.status == status)
    if type is not None:
        query = query.filter(Asset.type == type)
    if subcategory is not None:
        query = query.filter(SubCategory.name == subcategory)
    if hostname is not None:
        query = query.filter(Asset.hostname == hostname)
    if ip is not None:
        query = query.filter(Asset.ip == cast(ip, INET))

    return query.offset(skip).all()

def get_all_networks(
        db: Session,
        skip: int = 0,
        status: Optional[int] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        type: Optional[str] = None) -> list[Asset]:
    
    query = db.query(Asset).join(Os).join(Category).join(SubCategory)

    query = query.filter(Category.name == "network")

    if status is not None:
        query = query.filter(Asset.status == status)
    if type is not None:
        query = query.filter(Asset.type == type)
    if subcategory is not None:
        query = query.filter(SubCategory.name == subcategory)
    if hostname is not None:
        query = query.filter(Asset.hostname == hostname)
    if ip is not None:
        query = query.filter(Asset.ip == cast(ip, INET))

    return query.offset(skip).all()

def get_all_securities(
        db: Session,
        skip: int = 0,
        status: Optional[int] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        type: Optional[str] = None) -> list[Asset]:
    
    query = db.query(Asset).join(Os).join(Category).join(SubCategory)
    
    query = query.filter(Category.name == "security")
    
    if status is not None:
        query = query.filter(Asset.status == status)
    if type is not None:
        query = query.filter(Asset.type == type)
    if subcategory is not None:
        query = query.filter(SubCategory.name == subcategory)
    if hostname is not None:
        query = query.filter(Asset.hostname == hostname)
    if ip is not None:
        query = query.filter(Asset.ip == cast(ip, INET))
        
    return query.offset(skip).all()

def get_all_storages(
        db: Session,
        skip: int = 0,
        status: Optional[int] = None,
        subcategory: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        type: Optional[str] = None) -> list[Asset]:
    
    query = db.query(Asset).join(Os).join(Category).join(SubCategory)
    
    query = query.filter(Category.name == "storage")
    
    if status is not None:
        query = query.filter(Asset.status == status)
    if type is not None:
        query = query.filter(Asset.type == type)
    if subcategory is not None:
        query = query.filter(SubCategory.name == subcategory)
    if hostname is not None:
        query = query.filter(Asset.hostname == hostname)
    if ip is not None:
        query = query.filter(Asset.ip == cast(ip, INET))
        
    return query.offset(skip).all()
