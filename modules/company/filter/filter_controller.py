
from utils.imports import APIRouter, Request, UUID, Query, Optional
from utils.auth import authenticate
from utils.validator import Validator
from ...students.profile.english.english_services import EnglishServices
from ...students.profile.language.language_services import LanguageServices
# from .filter_models import FilterDAO
from .filter_services import FilterServices


filter_router = APIRouter(
    prefix="/filters",
    tags=["filters"]
)

@filter_router.get("/rank_filter/")
def rank_filter(req: Request, rank: str):
    user = authenticate(req)
    Validator.validate_roles(user.role, "company")

    return FilterServices.rank_filter(rank, user.id)

@filter_router.get("/language_filter/")
def language_filter(req: Request, language: str):
    user = authenticate(req)
    Validator.validate_roles(user.role, "company")

    return FilterServices.language_filter(language, user.id)

@filter_router.get("/rank_and_language_filter/")
def rank_and_language_filter(req: Request, rank: str, language: str):
    user = authenticate(req)
    Validator.validate_roles(user.role, "company")
    return FilterServices.rank_and_language_filter(rank, language, user.id)