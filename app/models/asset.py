import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db.base import Base
from db.session import engine

class Asset(Base):
    __tablename__ = "asset"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    status = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    category = Column(Integer, ForeignKey("category.code"), nullable=False)
    subcategory = Column(Integer, ForeignKey("subcategory.code"), nullable=False)
    os = Column(Integer, ForeignKey("os.code"), nullable=False)
    hostname = Column(String, nullable=False)
    ip = Column(String, nullable=False)

    category_obj = relationship("Category", back_populates="assets")
    subcategory_obj = relationship("SubCategory", back_populates="assets")
    os_obj = relationship("Os", back_populates="assets")
    accounts = relationship("Account", back_populates="asset_obj")

class Category(Base):
    __tablename__ = "category"

    code = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    assets = relationship("Asset", back_populates="category_obj")

class SubCategory(Base):
    __tablename__ = "subcategory"

    code = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    assets = relationship("Asset", back_populates="subcategory_obj")

class Os(Base):
    __tablename__ = "os"

    code = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    assets = relationship("Asset", back_populates="os_obj")

Base.metadata.create_all(bind=engine)
