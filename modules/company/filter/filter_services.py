

from .filter_models import FilterDAO
from ..likes.like_services import LikeServices
from ...students.profile.english.english_schemas import EnglishResponse
from ...students.profile.language.language_schemas import LanguageResponse
from ...students.profile.projects.project_schemas import ProjectResponse
from ...users.user_schemas import UserRes
from ...students.profile.english.english_validator import EnglishValidator
from ...students.profile.language.language_validator import LanguageValidator




class FilterServices():
    def rank_filter(rank, company_id):
        EnglishValidator.validate_english_rank(rank)
        users = FilterDAO.rank_filter(rank, company_id)
        return users
        
    
    def language_filter(language, company_id):
        LanguageValidator.validate_language(language)
        users = FilterDAO.language_filter(language, company_id)
        return users
        
    def rank_and_language_filter(rank, language, company_id):
        EnglishValidator.validate_english_rank(rank)
        LanguageValidator.validate_language(language)
        users = FilterDAO.rank_and_language_filter(rank, language, company_id)
        return users