from uuid import UUID
from pydantic import BaseModel, IPvAnyAddress

class AssetRead(BaseModel):
    id:             UUID
    status:         int
    type:           str
    category:       str
    subcategory:    str
    hostname:       str
    ip:             IPvAnyAddress
    os:             str

    class Config:
        orm_mode = True
