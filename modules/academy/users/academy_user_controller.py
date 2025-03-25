
from utils.imports import APIRouter
from .academy_user_schemas import AcademyUserCreate
from .academy_user_services import AcademyUserService


academy_user_router = APIRouter(
    prefix="/academy_users",
    tags=["academy_users"]
)

@academy_user_router.post("/create_user/")
def academy_create_user(academy_user_create: AcademyUserCreate):
    return AcademyUserService.academy_create_user(academy_user_create)

@academy_user_router.get("/get_user_by_email/{email}")
def get_academy_user_by_email(email: str):
    return AcademyUserService.get_academy_user_by_email(email)

@academy_user_router.get("/get_user_by_id/{id}")
def get_academy_user_by_id(id: str):
    return AcademyUserService.get_academy_user_by_id(id)

@academy_user_router.get("/")
def get_all_academy_users():
    return AcademyUserService.get_all_academy_users()

@academy_user_router.delete("/delete_user/{id}")
def delete_academy_user_by_id(id: str):
    return AcademyUserService.delete_academy_user_by_id(id)

