from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class AccountRead(BaseModel):
    id:             UUID
    username:       str
    password:       str
    asset_id:       UUID
    create_at:      datetime
    update_at:      datetime

    class Config:
        orm_mode = True
