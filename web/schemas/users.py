from pydantic import BaseModel


class UserSchema(BaseModel):
    tg_id: int
    name: str
    email: str

class CreateUserSchema(BaseModel):
    tg_id: int
    name: str
    email: str