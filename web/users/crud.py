import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from users.models import User
from users.schemas import UserSchema


async def add_user(db: AsyncSession, user: UserSchema):
    """
    Add a record to the database
    """
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.flush()
    await db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, user_id: uuid.UUID):
    """
    Get all records from the database
    """
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def delete_user(db: AsyncSession, user_id: uuid.UUID):
    """
    Delete record from the database by id
    """
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if user:
        await db.delete(user)
        await db.flush()
    return user