from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Boolean,
    DateTime, Enum, ForeignKey, Text
)

from tests.src.database.base import Base
from tests.src.enums.users import UserRole

class User(Base):
    __tablename__ = 'users'
    role=Column(Enum(UserRole), default=UserRole.CUSTOMER,nullable=False)
    id=Column(Integer, primary_key=True, index=True)
    email=Column(String(255), unique=True, nulltable=False, index=True)
    password = Column(String(255), nullable=False)
    phone        = Column(String(20), nullable=True)
    avatar_url   = Column(String(500), nullable=True)
    is_active    = Column(Boolean, default=True)
    is_verified  = Column(Boolean, default=False)   # Email verification
    created_at   = Column(DateTime, default=datetime.utcnow)
    updated_at   = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login   = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"
    
