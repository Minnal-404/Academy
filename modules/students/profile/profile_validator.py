

from utils.imports import HTTPException, status, UUID
from .profile_schemas import UrlValidator, ProfileCreate
from ..users.student_user_validator import StudentUserValidator
from .english.english_models import EnglishDAO
from .projects.project_validator import ProjectValidator
from .projects.project_models import ProjectDAO
from .english.english_validator import EnglishValidator


class ProfileValidator():
    def validate_profile_create(id: str, profile_create: ProfileCreate):
        
        if not profile_create:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Body Is Required")
            
        ProjectValidator.validate_project_create(id, profile_create.projects)
        
        
        if EnglishDAO.get_english_by_student_id(UUID(id)):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Profile Already Created")
        
        EnglishValidator.validate_english_create(id, profile_create.english)
        
    def validate_get_profile(id: str):
        StudentUserValidator.validate_student_user_id(id)
        
        student_id = UUID(id)
        
        is_id_in_projects = ProjectDAO.get_all_projects_by_student_id(student_id)
        is_id_in_english = EnglishDAO.get_english_by_student_id(student_id)
        
        if not is_id_in_projects and not is_id_in_english:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Profile Found")
            
    

