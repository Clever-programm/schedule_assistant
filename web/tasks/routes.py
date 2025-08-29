from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from tasks.crud import add_task, get_user_tasks
from tasks.schemas import CreateTaskSchema

task_router = APIRouter(prefix="/tasks")

@task_router.post("/")
async def create_task(new_task: CreateTaskSchema, db: AsyncSession = Depends(get_db)) -> CreateTaskSchema:
    await add_task(db, new_task)
    return new_task

@task_router.get("/{user_id}")
async def read_tasks(user_id: str, db: AsyncSession = Depends(get_db)) -> list:
    tasks = await get_user_tasks(db, user_id)
    return tasks