import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tasks.models import Task
from tasks.schemas import CreateTaskSchema


async def add_task(db: AsyncSession, task: CreateTaskSchema):
    """
    Add a record to the database
    """
    db_task = Task(**task.model_dump())
    db.add(db_task)
    await db.flush()
    await db.refresh(db_task)
    return db_task

async def get_user_tasks(db: AsyncSession, owner_id: uuid.UUID):
    """
    Get all records from the database
    """
    stmt = select(Task).where(Task.owner_id == owner_id)
    result = await db.execute(stmt)
    return result.scalars().all()

async def delete_task(db: AsyncSession, task_id: uuid.UUID):
    """
    Delete record from the database by id
    """
    stmt = select(Task).where(Task.id == task_id)
    result = await db.execute(stmt)
    task = result.scalar_one_or_none()
    if task:
        await db.delete(task)
        await db.flush()
    return task