

from utils.imports import APIRouter, Request, UUID
from .like_services import LikeServices
from utils.auth import authenticate
from utils.validator import Validator


like_router = APIRouter(
    prefix="/likes",
    tags=["likes"]
)

@like_router.post("/like/")
def like(req: Request, email: str):
    user = authenticate(req)
    Validator.validate_roles(user.role, "company")
    return LikeServices.like(user.id, email)

@like_router.delete("/unlike/")
def unlike(req: Request, email: str):
    user = authenticate(req)
    Validator.validate_roles(user.role, "company")
    return LikeServices.unlike(user.id, email)

@like_router.get("/get_all_likes/")
def get_all_likes(req: Request):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return LikeServices.get_all_likes()

@like_router.get('/get_all_likes_by_company_id/')
def get_all_likes_by_company_id(req: Request):
    user = authenticate(req)
    Validator.validate_roles(user.role, "company")
    return LikeServices.get_all_likes_by_company_id(user.id)