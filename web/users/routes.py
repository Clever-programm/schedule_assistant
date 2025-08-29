from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from users.crud import add_user, get_user
from users.schemas import CreateUserSchema

user_router = APIRouter(prefix="/users")

@user_router.post("/")
async def create_user(new_user: CreateUserSchema, db: AsyncSession = Depends(get_db)):
    await add_user(db, new_user)
    return new_user

@user_router.get("/{user_id}")
async def get_any_user(user_id: str, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    return user