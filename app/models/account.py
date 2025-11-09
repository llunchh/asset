import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db.base import Base
from db.session import engine

class Account(Base):
    __tablename__ = "account"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    asset_id = Column(UUID(as_uuid=True), ForeignKey("asset.id", ondelete="CASCADE"), nullable=False)
    create_at = Column(Datetime(timezone=True), server_default=text("timezone('Asia/Seoul', now())"), nullable=False)
    update_at = Column(Datetime(timezone=True), server_default=text("timezone('Asia/Seoul', now())"), server_onupdate=text("timezone('Asia/Seoul', now())"), nullable=False)

    asset_obj = relationship("Asset", back_populates="accounts")

Base.metadata.create_all(bind=engine)
