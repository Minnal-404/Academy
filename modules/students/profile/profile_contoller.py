
from utils.imports import APIRouter
from .profile_schemas import ProfileCreate
from .profile_services import ProfileServices
from ...users.auth import authenticate



profile_router =  APIRouter(
    prefix="/profile",
    tags=["profile"]
)

@profile_router.post("/create_profile/")
def create_profile(id: str, profile_create: ProfileCreate):
    authenticate()
    return ProfileServices.create_profile(id, profile_create)

@profile_router.get("/get_profile_by_student_id/")
def get_profile_by_student_id(id: str):
    return ProfileServices.get_profile_by_student_id(id)