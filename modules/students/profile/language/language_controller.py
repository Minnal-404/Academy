
from utils.imports import APIRouter
from .language_services import LanguageServices
from utils.auth import Request, authenticate
from utils.validator import Validator



language_router =  APIRouter(
    prefix="/language",
    tags=["language"]
)





# @language_router.get("/get_languages/")
# def get_languages():
#     return languageServices.get_languages()

@language_router.put("/update_language/")
def update_language(req: Request, language: str):
    user = authenticate(req)
    Validator.validate_roles(user.role, "student")
    return LanguageServices.update_language(user.id, language)

@language_router.get('/get_all_language_updates/')
def get_all_language_updates(req: Request):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return LanguageServices.get_all_language_updates()