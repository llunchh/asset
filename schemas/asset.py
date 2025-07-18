from pydantic import BaseModel

class AssetRead(BaseModel):
    id:         str
    status:     int
    type:       str
    category:   str
    hostname:   str
    ip:         str
    os_name:    str

    class Config:
        orm_mode = True
