import re

from pydantic import BaseModel, Field, field_validator


class CreateUserSchema(BaseModel):
    username: str = Field(title="User's name and login", min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(title="User's password", min_length=8, max_length=64)

    @field_validator("password")
    def validate_password(cls, value):
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")
        return value

class UserSchema(CreateUserSchema):
    id: int = Field(title="User id")