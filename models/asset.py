from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
from db.session import engine

class Asset(Base):
    __tablename__ = "asset"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    os = Column(Integer, ForeignKey("os.code"), nullable=False)
    hostname = Column(String, nullable=False)
    ip = Column(String, nullable=False)

    os_obj = relationship("Os", back_populates="assets")

class Os(Base):
    __tablename__ = "os"

    code = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    assets = relationship("Asset", back_populates="os_obj")

Base.metadata.create_all(bind=engine)
