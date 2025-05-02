
from utils.validator import Validator
from .language_models import LanguageDAO
from utils.imports import UUID, HTTPException, status
from ....users.user_validator import UserValidator
from ....academy.language_list.language_list_models import LanguageListDAO





class LanguageValidator():
    def validate_language_id(id: str):
        Validator.validate_uuid(id)
        
        is_id = LanguageDAO.get_language_by_id(UUID(id))
        
        if not is_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Language Not Found")
            
    def validate_language_create(language: str, student_id: UUID):
                    
        
        if not language:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Language Feild Required")
        
        is_language = LanguageListDAO.get_language(language)
        if not is_language:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Language")
        is_updated = LanguageDAO.get_language_by_student_id(student_id)
        print(is_updated)
        if is_updated:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{language} Already Updated")
        
    def validate_language_update(user_id: UUID, language: str):
                    
        
        if not language:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Language Feild Required")
        
        is_language = LanguageListDAO.get_language(language)
        if not is_language:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Language")
        
        is_updated = LanguageDAO.get_language_by_student_id(user_id)
        # print(is_updated.language, language)
        if is_updated.language == language:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{language} Already Updated")
            
    
    # def validate_language_update(id: str, language_update: languageUpdate):
        
    #     languageValidator.validate_language_id(id)
    #     language = languageDAO.get_language_by_id(UUID(id))

        
    #     if not language_update.title and not language_update.url:
    #         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Body Is Required")
        
    #     if language_update.title:
    #         languageValidator.validate_language_title(language_update.title)
    #         if language.title == language_update.title:
    #             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Rank Already Updated")
            
    #     if language_update.url:
    #         Validator.validate_url(language_update.url)
    #         if language.url == language_update.url:
    #             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Rank Already Updated")
    
    def validate_language_title(title: str):
        if len(title) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title Must Contain Atleat 3 Characters")
    
        if len(title) > 50:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title Cannot Contain More Than 50 Characters")
    
    def validate_user_and_language(student_id: UUID, user_id):
        if not student_id == user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
    
    def validate_language(language: str):
        if not language:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Language Required")

        is_language = LanguageListDAO.get_language(language)
        if not is_language:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Language")
