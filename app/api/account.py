from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.account import AccountRead
from crud.account import get_account_password
from api.deps import get_db

router = APIRouter()

@router.get("/password", response_model=AccountRead)
def read_password(
    ip: str,
    username: str,
    db: Session = Depends(get_db)
):
    account = get_account_password(db, ip=ip, username=username)

    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    return account
