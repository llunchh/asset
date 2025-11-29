from sqlalchemy.orm import Session
from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import INET
from typing import Optional

from models.asset import Asset
from models.account import Account
from schemas.account import AccountRead

def get_usernames(
        db: Session,
        ip: Optional[str] = None,
        hostname: Optional[str] = None
    ) -> list[Account]:

    query = db.query(Account).join(Asset)

    if ip is not None:
        query = query.filter(Asset.ip == cast(ip, INET))
    if hostname is not None:
        query = query.filter(Asset.hostname == hostname)

    return query.all()

def get_password(
        db: Session,
        ip: str,
        username: str
    ) -> Account:

    query = (
        db.query(Account)
        .join(Asset)
        .filter(Asset.ip == cast(ip, INET))
        .filter(Account.username == username)
    )

    return query.first()
