from pydantic import BaseModel

class DeviceRead(BaseModel):
    id:         int
    category:   str
    status:     int
    hostname:   str
    ip:         str

    class Config:
        orm_mode = True
