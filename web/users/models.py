import uuid

from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    password = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True, index=True)

    __table_args__ = (
        CheckConstraint("length(password) >= 8", name="password_min_length"),
        CheckConstraint("length(password) <= 64", name="password_max_length"),
    )

    tasks = relationship("Task", back_populates="owner", cascade="all, delete")