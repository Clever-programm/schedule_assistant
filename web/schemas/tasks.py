from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    task: str
    owner_id: int
    date: str
    start_time: str
    end_time: str | None

class CreateTaskSchema(BaseModel):
    task: str
    owner_id: int
    date: str
    start_time: str
    end_time: str | None

