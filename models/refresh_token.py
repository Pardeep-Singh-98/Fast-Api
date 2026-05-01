from sqlalchemy import Column, Numeric, Boolean, Integer, String, DateTime, ForeignKey
from database.connection import Base
from datetime import datetime

class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    type = Column(String(50))

    token = Column(String(800), unique=True)

    #expires_at
    expires_at = Column(DateTime)

    #updated_at
    created_at = Column(DateTime, default=datetime.utcnow)