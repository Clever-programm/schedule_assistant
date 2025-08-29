import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    owner_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    task_text = Column(String)
    is_done = Column(Boolean, nullable=False, default=False, index=True)

    owner = relationship("User", back_populates="tasks")