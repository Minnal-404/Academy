
from utils.imports import UUID
from .language_models import LanguageDAO, Language
from utils.validator import Validator
from .language_validator import LanguageValidator
from ....users.user_models import UserDAO
from ....users.user_schemas import UserRes
from ....academy.approval.approval_model import RejectionDAO
from .language_schemas import LanguageResponse


class LanguageServices():
    def create_language(student_id: UUID, language: str):
        language_create = Language(language=language, student_id=student_id)
        result = LanguageDAO.create_language(language_create)
        return result.language
    
    # def get_all_languages_by_student_id(id: UUID):
        
    #     result = LanguageDAO.get_all_languages_by_student_id(id)
    #     return [LanguageResponse(**res.model_dump()) for res in result]
    
    # def get_approved_languages_by_student_id(id: UUID):
        
    #     result = LanguageDAO.get_approved_languages_by_student_id(id)
    #     return [LanguageResponse(**res.model_dump()) for res in result]
            
    # def delete_language(user_id: UUID, id: str):
    #     LanguageValidator.validate_language_id(id)
    #     language_id = UUID(id)
    #     language_to_delete = LanguageDAO.get_language_by_id(language_id)
    #     LanguageValidator.validate_user_and_language(language_to_delete.student_id, user_id)
    #     return LanguageDAO.delete_language(language_to_delete)
    
    def get_languages():
        return LanguageDAO.get_languages()
    
    def get_language_by_student_id(id: UUID):
        language = LanguageDAO.get_language_by_student_id(id)
        if language.is_rejected:
                reject = RejectionDAO.get_rejection(language.student_id)
                project_data = {**language.model_dump(), **reject.model_dump()}
                return LanguageResponse(**project_data)
        else:
            return LanguageResponse(**language.model_dump())
    
    def update_language(user_id: UUID, language: str):
        LanguageValidator.validate_language_update(user_id, language)
        try:
            rejection_to_delete = RejectionDAO.get_rejection(user_id)
            RejectionDAO.delete_rejection(rejection_to_delete)
        except:
            pass
        return LanguageDAO.update_language(user_id, language)
    
    def delete_all_languages(id: UUID):

        
        languages = LanguageDAO.get_all_languages_by_student_id(id)
        for language in languages:
            LanguageDAO.delete_language(language)
        return True
    
    # def get_all_language_updates():
    #     ids = LanguageDAO.get_all_language_updates_users()
    #     languages = []
    #     for id in ids:
    #         user = UserDAO.get_user_by_id(id)
    #         user = UserRes(**user.model_dump())
    #         language = LanguageDAO.get_all_updates_by_student_id(id)
    #         res = []
    #         for pro in language:
                
    #             proj = LanguageResponse(**pro.model_dump())
    #             res.append(proj)
    #         languages.append({
    #             "user": user,
    #             "languages": res
    #         })
    #     return languages
    
    def get_all_language_updates():
        languages =  LanguageDAO.get_all_language_updates()
        result = []
        for language in languages:
            user_id = language.student_id
            user = UserDAO.get_user_by_id(user_id)
            user = UserRes(**user.model_dump())
            response = {
                "user": user,
                "language": language.language
            }
            result.append(response)
        return result
    
    def language_filter(language: str):
        from ..profile_services import ProfileServices
        LanguageValidator.validate_language(language)
        users = LanguageDAO.language_filter(language)
        profiles = []
        for user in users:
            user_id = user.student_id
            profile = ProfileServices.get_profile_by_student_id(user_id)
            student = UserDAO.get_user_by_id(user_id)
            student = UserRes(**student.model_dump())
            profile["user"] = student
            profiles.append(profile)
        return {'profiles': profiles}