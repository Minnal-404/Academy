
from utils.imports import APIRouter, EmailStr
from .profile_schemas import ProfileCreate
from .profile_services import ProfileServices
from utils.auth import authenticate, Request
from utils.validator import Validator



profile_router =  APIRouter(
    prefix="/profile",
    tags=["profile"]
)

@profile_router.post("/create_profile/")
def create_profile(req: Request, profile_create: ProfileCreate):
    user = authenticate(req)
    Validator.validate_roles(user.role, "student")
    return ProfileServices.create_profile(user.id, profile_create)

@profile_router.get("/get_profile/")
def get_profile(req: Request):
    user = authenticate(req)
    Validator.validate_roles(user.role, "student")
    return ProfileServices.get_profile_by_student_id(user.id)

@profile_router.get("/get_profile_by_email/")
def get_profile(req: Request, email: EmailStr):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return ProfileServices.get_profile_by_email(email)

# @profile_router.get("/get_all_profiles/")
# def get_all_profiles(req: Request):
#     user = authenticate(req)
#     Validator.validate_two_roles(user.role, "academy", "company")
#     return ProfileServices.get_all_profiles()

@profile_router.get("/get_all_profiles/")
def get_all_profiles(req: Request):
    user = authenticate(req)
    Validator.validate_two_roles(user.role, "academy", "company")
    if user.role == 'academy':
        return ProfileServices.get_all_profiles()
    if user.role == 'company':
        return ProfileServices.get_all_profiles_with_like(user.id)

# @profile_router.get("/get_all_project_updates/")
# def get_all_updates(req: Request):
#     user = authenticate(req)
#     Validator.validate_roles(user.role, "academy")
#     return ProfileServices.get_all_updates()

# @profile_router.get("/get_all_english_updates/")
# def get_all_updates(req: Request):
#     user = authenticate(req)
#     Validator.validate_roles(user.role, "academy")
#     return ProfileServices.get_all_updates()

# @profile_router.get("/get_all_language_updates/")
# def get_all_updates(req: Request):
#     user = authenticate(req)
#     Validator.validate_roles(user.role, "academy")
#     return ProfileServices.get_all_updates()

