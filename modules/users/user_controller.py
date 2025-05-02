
from utils.imports import APIRouter, Request, UUID, Response
from .user_schemas import UserCreate, Login
from .user_services import UserService
from utils.auth import authenticate, jwt_token_encrypt
from utils.validator import Validator


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

user_router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@auth_router.post("/sign_up/")
def sign_up( user_create: UserCreate):
    result = UserService.sign_up(user_create)
    
    return result

@auth_router.post("/login/")
def login(login: Login):
    return UserService.login(login)
     

# @user_router.get("/get_user_by_id/{id}")
# def get_user_by_id(id: str):
#     return UserService.get_user_by_id(id)

# @user_router.get("/")
# def get_all_users():
#     return UserService.get_all_users()

@user_router.delete("/delete_user/")
def delete_user(req: Request):
    user = authenticate(req)
    return UserService.delete_user_by_id(user.id)

# @user_router.delete("/delete_user_by_id/")
# def delete_user(id: UUID):
#     return UserService.delete_user_by_id(id)

@user_router.get("/get_all_students/")
def get_all_students(req: Request):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return UserService.get_all_students()

@user_router.get("/get_all_companies/")
def get_all_companies(req: Request):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return UserService.get_all_companies()

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3RyaW5nIiwiZW1haWwiOiJ1c2VyYUBleGFtcGxlLmNvbSIsInBob25lIjoiMTIzNDU2Nzg5MCIsInJvbGUiOiJhY2FkZW15In0.6tNZlad4NktpqSOxC2KNvTkBQuPHYVut-Y_lmwS4mao
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3RyaW5nIiwiZW1haWwiOiJ1c2Vyc0BleGFtcGxlLmNvbSIsInBob25lIjoiMTIzNDU2Nzg5MCIsInJvbGUiOiJzdHVkZW50In0.ZLW7AStS34rUgREmQzlKYP4_5Iizq191hCYYNzxZq1Y