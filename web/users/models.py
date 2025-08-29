from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)
    username = Column(String, nullable=False, index=True)

    __table_args__ = (
        CheckConstraint("length(password) >= 8", name="password_min_length"),
        CheckConstraint("length(password) <= 64", name="password_max_length"),
    )

    tasks = relationship("Task", back_populates="owner", cascade="all, delete")