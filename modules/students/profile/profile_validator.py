

from utils.imports import HTTPException, status, UUID, EmailStr
from .profile_schemas import UrlValidator, ProfileCreate
from ...users.user_validator import UserValidator
from .english.english_models import EnglishDAO
from .projects.project_validator import ProjectValidator
from .projects.project_models import ProjectDAO
from .english.english_validator import EnglishValidator
from ...academy.language_list.language_list_models import LanguageListDAO
from .language.language_validator import LanguageValidator


class ProfileValidator():
    def validate_profile_create(student_id: UUID, profile_create: ProfileCreate):
        
        if not profile_create:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Body Is Required")
            
        # ProjectValidator.validate_project_create(id, profile_create.projects)
        
        is_language = LanguageListDAO.get_language(profile_create.language)
        if not is_language:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Language")
        
        if EnglishDAO.get_english_by_student_id(student_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Profile Already Created")
        
        LanguageValidator.validate_language_create(profile_create.language, student_id)
        EnglishValidator.validate_english_create(student_id, profile_create.english)


        # EnglishValidator.validate_english_create(id, profile_create.english)
        
    def validate_get_profile(id: UUID):
        UserValidator.validate_user_id(id)
        
        is_id_in_projects = ProjectDAO.get_all_projects_by_student_id(id)
        is_id_in_english = EnglishDAO.get_english_by_student_id(id)
        
        if not is_id_in_projects and not is_id_in_english:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Profile Found")
            
