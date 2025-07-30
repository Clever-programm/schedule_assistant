from pydantic import BaseModel


class UserSchema(BaseModel):
    tg_id: int
    name: str
    password: str
    email: str

class CreateUserSchema(BaseModel):
    tg_id: int
    name: str
    password: str

class SetUserEmail(BaseModel):
    tg_id: int
    email: str