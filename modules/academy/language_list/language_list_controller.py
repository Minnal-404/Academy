
from utils.imports import APIRouter, Request, UUID
from utils.auth import authenticate
from utils.validator import Validator
from .language_list_services import LanguageListServices
from .language_list_schemas import LanguageList


language_list_router = APIRouter(
    prefix="/language_lists",
    tags=["language_lists"]
)


@language_list_router.post("/create_language_list")
def create_language_list(req: Request, languages: LanguageList):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return LanguageListServices.create_language_list(languages)

@language_list_router.delete("/delete_language/")
def delete_language(req: Request, id: str):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return LanguageListServices.delete_language_list(id)

@language_list_router.get("/get_language_list/")
def get_language_list(req: Request):
    user = authenticate(req)
    Validator.validate_three_roles(user.role, "student", "academy", 'company')
    return LanguageListServices.get_language_list()