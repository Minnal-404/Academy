
from utils.imports import APIRouter, UUID
from .english_services import EnglishServices
from .english_schemas import EnglishUpdate
from utils.auth import Request, authenticate
from utils.validator import Validator



english_router =  APIRouter(
    prefix="/english",
    tags=["english"]
)



# @english_router.delete("/delete_english/")
# def delete_english(id: str):
#     return EnglishServices.delete_english(id)

# @english_router.get("/get_all_english/")
# def get_all_english():
#     return EnglishServices.get_all_english()

@english_router.put("/update_english/")
def update_english(req: Request, id: UUID, english_update: EnglishUpdate):
    user = authenticate(req)
    Validator.validate_roles(user.role, "student")
    return EnglishServices.update_english(user.id, id, english_update)

@english_router.get('/get_all_english_updates/')
def get_all_english_updates(req: Request):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return EnglishServices.get_all_english_updates()