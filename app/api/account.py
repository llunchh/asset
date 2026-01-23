from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List

from schemas.account import AccountRead
from crud.account import get_password, get_usernames
from api.deps import get_db

router = APIRouter()

@router.get("/usernames", response_model=List[str])
def read_usernames(
    ip: Optional[str] = None,
    hostname: Optional[str] = None,
    db: Session = Depends(get_db)
):
    accounts = get_usernames(db, ip=ip, hostname=hostname)

    if not accounts:
        raise HTTPException(status_code=404, detail="Asset not found")
    return [account.username for account in accounts]


@router.get("/password", response_model=AccountRead)
def read_password(
    ip: str,
    username: str,
    db: Session = Depends(get_db)
):
    password = get_password(db, ip=ip, username=username)

    if not password:
        raise HTTPException(status_code=404, detail="Account not found")

    return password
