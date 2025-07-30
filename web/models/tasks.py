from sqlalchemy import Column, Integer, String, Boolean
from web.database import Base


class User(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    owner_id = Column(Integer, index=True)
    date = Column(String, index=True)
    start_time = Column(String)
    end_time = Column(String)
    active = Column(Boolean, index=True)