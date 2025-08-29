from typing import Optional

from pydantic import BaseModel, Field


class CreateTaskSchema(BaseModel):
    owner_id: str = Field(title="Owner id")
    task_text: Optional[str] = Field(title="Text of user's task", default=None)

class TaskSchema(CreateTaskSchema):
    id: str = Field(title="Uniq task id")
    is_done: bool = Field(title="Task is done", default=False)

    model_config = {
        "from_attributes": True
    }