
from .language_list_schemas import LanguageList, LanguageListResponse
from .language_list_models import LanguageListDAO, LanguageList
from .language_list_validator import LanguageListValidator
from utils.imports import UUID 


class LanguageListServices():
    def create_language_list(languages: LanguageList):
        LanguageListValidator.validate_language_create(languages)
        response = []
        for language in languages.languages:
            is_language = LanguageListDAO.get_language(language)
            if not is_language:
                language_create = LanguageList(language=language)
                result = LanguageListDAO.create_language_list(language_create)
                result = LanguageListResponse(**result.model_dump())
                response.append(result)
        return {
            "message": "Language List Created Successfully",
            "languages": response
        }
    
    def get_language_list():
        lists = LanguageListDAO.get_language_list()
        language_list = [{"id": list.id, "language": list.language} for list in lists]
        return {
            "language_list": language_list
        }
    
    def delete_language_list(id: str):
        LanguageListValidator.validate_language_delete(id)
        id = UUID(id)
        language_to_delete = LanguageListDAO.get_language_by_id(id)
        return LanguageListDAO.delete_language_list(language_to_delete)