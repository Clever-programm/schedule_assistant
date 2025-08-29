from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import engine, Base
from tasks.routes import task_router
from users.routes import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
app.include_router(user_router)