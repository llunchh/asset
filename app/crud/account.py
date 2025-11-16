from sqlalchemy.orm import Session
from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import INET
from typing import Optional

from models.asset import Asset
from models.account import Account
from schemas.account import AccountRead

def get_account_password(
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
