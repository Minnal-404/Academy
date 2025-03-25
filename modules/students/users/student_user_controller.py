
from utils.imports import APIRouter
from .student_user_schemas import StudentUserCreate
from .student_user_services import StudentUserService


student_user_router = APIRouter(
    prefix="/student_users",
    tags=["student_users"]
)

@student_user_router.post("/create_user/")
def student_create_user(student_user_create: StudentUserCreate):
    return StudentUserService.student_create_user(student_user_create)

@student_user_router.get("/get_user_by_email/{email}")
def get_student_user_by_email(email: str):
    return StudentUserService.get_student_user_by_email(email)

@student_user_router.get("/get_user_by_id/{id}")
def get_student_user_by_id(id: str):
    return StudentUserService.get_student_user_by_id(id)

@student_user_router.get("/")
def get_all_student_users():
    return StudentUserService.get_all_student_users()

@student_user_router.delete("/delete_user/{id}")
def delete_student_user_by_id(id: str):
    return StudentUserService.delete_student_user_by_id(id)

