from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    phone_number = Column(String, nullable=True)
    preferences = Column(JSON, nullable=True)

    def __repr__(self):
        return f"<User {self.username}>"
