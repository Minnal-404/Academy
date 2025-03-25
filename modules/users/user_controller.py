
from utils.imports import APIRouter, Request
from .user_schemas import UserCreate, Login
from .user_services import UserService
from .auth import authenticate


user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.post("/create_user/")
def create_user(user_create: UserCreate):
    return UserService.create_user(user_create)

@user_router.post("/login/")
def login(login: Login):
    return UserService.login(login)

# @user_router.get("/get_user_by_id/{id}")
# def get_user_by_id(id: str):
#     return UserService.get_user_by_id(id)

# @user_router.get("/")
# def get_all_users():
#     return UserService.get_all_users()

@user_router.delete("/delete_user/")
def delete_user_by_id(req: Request):
    user = authenticate(req)
    return UserService.delete_user_by_id(user.id)

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3RyaW5nIiwiZW1haWwiOiJ1c2VyQGV4YW1wbGUuY29tIiwiaWQiOiIwYjc2YzQzZS1mYjhjLTRjMjMtOTM5OC02NGNmYTAxNGZjNjAiLCJyb2xlIjoiYWNhZGVteSJ9.I5dtvOkMKb35MJoNYk9OD8ZUdO4R1tJ1JqGTllzN56E