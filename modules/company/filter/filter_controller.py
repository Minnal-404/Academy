
from utils.imports import APIRouter, Request, UUID, Query, Optional
from utils.auth import authenticate
from utils.validator import Validator
from ...students.profile.english.english_services import EnglishServices
from ...students.profile.language.language_services import LanguageServices
from .filter_models import FilterDAO
from .filter_services import FilterServices


filter_router = APIRouter(
    prefix="/filters",
    tags=["filters"]
)

@filter_router.get("/rank_filter/")
def rank_filter(req: Request, rank: str):
    user = authenticate(req)
    Validator.validate_roles(user.role, "company")

    return EnglishServices.rank_filter(rank)

@filter_router.get("/language_filter/")
def rank_filter(req: Request, language: str):
    user = authenticate(req)
    Validator.validate_roles(user.role, "company")

    return LanguageServices.language_filter(language)

@filter_router.get("/filter_profiles")
def filter_profiles(
    rank: Optional[str] = Query(None),
    tech: Optional[str] = Query(None)
):
    return FilterServices.filter_profiles(rank, tech)