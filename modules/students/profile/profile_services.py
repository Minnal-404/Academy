
from .profile_schemas import ProfileCreate
from utils.imports import UUID
from .profile_validator import ProfileValidator
from .projects.project_services import ProjectServices
from .english.english_services import EnglishServices
from ..users.student_user_validator import StudentUserValidator




class ProfileServices():
    def create_profile(id: str, profile_create: ProfileCreate):
        ProfileValidator.validate_profile_create(id, profile_create)
        project_response = ProjectServices.create_project(id, profile_create.projects)
        english_response = EnglishServices.create_english(id, profile_create.english)
        return {"message": "Profile Is Send For Approval",
                "projects": project_response,
                "english": english_response}
    
    def get_profile_by_student_id(id: str):
        ProfileValidator.validate_get_profile(id)
        student_id = UUID(id)
        projects = ProjectServices.get_all_projects_by_student_id(student_id)
        english = EnglishServices.get_english_by_student_id(student_id)
        return {
            "projects": projects,
            "english": english
            }
    
    def delete_profile(id: str):
        ProfileValidator.validate_get_profile(id)
        student_id = UUID(id)
        ProjectServices.delete_all_projects(student_id)
        EnglishServices.delete_english_by_student_id(student_id)
        return
    
    def get_all_updates():
        projects = ProjectServices.get_all_project_updates()
        english = EnglishServices.get_all_english_updates()
        