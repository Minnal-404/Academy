

from utils.imports import HTTPException, status, UUID
from ...users.user_validator import UserValidator
from ...users.user_models import UserDAO
from utils.validator import Validator
from .language_list_schemas import LanguageList
from .language_list_models import LanguageListDAO



class LanguageListValidator():
    def validate_language_create(languages: LanguageList):
        if not languages:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Body Is Required")
        
        if not languages.languages:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Languages Required")
        
        for language in languages.languages:
            is_language = LanguageListDAO.get_language(language)
            
            if is_language:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"'{language}' Already Exists")
        
    def validate_language_delete(id: str):
        Validator.validate_uuid(id)
        is_id = LanguageListDAO.get_language_by_id(UUID(id))
        if not is_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Language Not Found")