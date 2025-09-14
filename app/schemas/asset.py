from uuid import UUID
from pydantic import BaseModel

class AssetRead(BaseModel):
    id:             UUID
    status:         int
    type:           str
    category:       str
    subcategory:    str
    hostname:       str
    ip:             str
    os:             str

    class Config:
        orm_mode = True
