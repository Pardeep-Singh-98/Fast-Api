from sqlalchemy import Column, Integer, String, Numeric, DateTime, Enum, Boolean
from database.connection import Base
from datetime import datetime

import enum

class UserRole(enum.Enum):
    superadmin = "superadmin"
    student = "student"
    teacher = "teacher"
    driver = "driver"
    parent = "parent"
    watchman = "watchman"
    peon = "peon"
    hr = "hr"


class User(Base):

    __tablename__ = "users"

    #primary key
    id = Column(Integer, primary_key=True, index=True)

    #name
    name = Column(String(60))

    # lambda parameters: return_value
    #role
    role = Column(
        Enum(UserRole),
        default=UserRole.student,
        nullable=False
    )

    #email
    email = Column(String(70),unique=True,index=True)

    #password
    password = Column(String(255))

    #slug
    slug = Column(String(100))

    #active
    active = Column(Boolean, default=True)

    #verified
    verified = Column(Boolean, default=False)

    #is_deleted
    is_deleted = Column(Boolean, default=False)

    #create_at
    created_at = Column(DateTime,default= datetime.utcnow)

    #updated_at
    updated_at = Column(DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)



