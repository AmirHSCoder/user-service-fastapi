from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .role import user_roles

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    profile = relationship("Profile", back_populates="user", uselist=False)
    roles = relationship(
        "Role", secondary=user_roles, back_populates="users", lazy="selectin"
    )
