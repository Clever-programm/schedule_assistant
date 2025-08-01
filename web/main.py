from fastapi import FastAPI
from routes.users import users_router
from routes.tasks import tasks_router


app = FastAPI()
app.include_router(users_router)
app.include_router(tasks_router)