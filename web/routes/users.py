from fastapi import APIRouter


users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.post('/add_user')
def add_user():
    return None

@users_router.get('/{user_id}')
def get_user_by_id(user_id: int):
    return None