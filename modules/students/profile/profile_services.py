
from .profile_schemas import ProfileCreate
from utils.imports import UUID, EmailStr
from .profile_validator import ProfileValidator
from .projects.project_services import ProjectServices
from .english.english_services import EnglishServices
from ...users.user_models import UserDAO
from ...users.user_schemas import UserRes
from .english.english_validator import EnglishValidator
from .english.english_models import EnglishDAO
from .language.language_services import LanguageServices
from ...company.likes.like_services import LikeServices
from .profile_models import ProfileDAO



class ProfileServices():
    def create_profile(id: UUID, profile_create: ProfileCreate):
        ProfileValidator.validate_profile_create(id, profile_create)
        project_response = ProjectServices.create_project(id, profile_create.projects)
        language_response = LanguageServices.create_language(id, profile_create.language)
        english_response = EnglishServices.create_english(id, profile_create.english)
        return {"message": "Profile Is Send For Approval",
                "language": language_response,
                "projects": project_response,
                "english": english_response}
    
    def get_profile_by_student_id(id: UUID):
        ProfileValidator.validate_get_profile(id)
        projects = ProjectServices.get_all_projects_by_student_id(id)
        english = EnglishServices.get_english_by_student_id(id)
        language = LanguageServices.get_language_by_student_id(id)
        return {
            "language": language,
            "projects": projects,
            "english": english
            }
        
    def get_profile_by_email(email: EmailStr):
        ProfileValidator.validate_get_profile(id)
        projects = ProjectServices.get_all_projects_by_student_id(id)
        english = EnglishServices.get_english_by_student_id(id)
        language = LanguageServices.get_language_by_student_id(id)
        return {
            "language": language,
            "projects": projects,
            "english": english
            }
    
    def delete_profile(id: UUID):
        ProfileValidator.validate_get_profile(id)
        ProjectServices.delete_all_projects(id)
        EnglishServices.delete_english_by_student_id(id)
        return
    
    def get_all_profiles():

        
        users = UserDAO.get_all_student_users()
        profiles = []
        for u in users:
            
            profile = ProfileDAO.get_full_profile_by_user_id(u.id)
            profiles.append(profile)
        return {"profiles": profiles}
        
    
    def get_all_profiles_with_like(company_id: UUID):
        users = UserDAO.get_all_student_users()
        profiles = []
        for u in users:
            
            profile = ProfileDAO.get_full_profile_by_user_id(u.id)
            like_id = str(company_id)+str(u.id)
            is_liked = LikeServices.get_like(like_id)
            if is_liked:
                profile['is_liked'] = True
            else:
                profile['is_liked'] = False
            profiles.append(profile)
        return {"profiles": profiles}
        
    
    def get_all_updates():
        projects = ProjectServices.get_all_project_updates()
        english = EnglishServices.get_all_english_updates()
        languages = LanguageServices.get_all_language_updates()
        return {
            "projects": projects,
            "english": english,
            "languages": languages
        }
    
    def rank_filter(rank: str):
        EnglishValidator.validate_english_rank(rank)
        users = EnglishDAO.rank_filter(rank)
        projects = []
        for user in users:
            user_id = user.student_id
            project = ProfileServices.get_profile_by_student_id(user_id)
            projects.append(project)
        return projects