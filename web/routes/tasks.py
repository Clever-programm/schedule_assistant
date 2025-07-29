from fastapi import APIRouter


tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])

@tasks_router.post('/add_task')
def add_task():
    return None

@tasks_router.get('/{task_id}')
def get_task_by_id(task_id: int):
    return None