from sqlalchemy import Column, Integer, String
from db.base import Base
from db.session import engine

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True, nullable=False)
    status = Column(Integer, nullable=False)
    hostname = Column(String, nullable=False)
    ip = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)
