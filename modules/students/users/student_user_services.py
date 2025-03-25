
from .student_user_schemas import StudentUserCreate, StudentUserResponse, UUID
from .student_user_models import StudentUser, StudentUserDAO
from .student_user_validator import StudentUserValidator
from ..profile.profile_services import ProfileServices


class StudentUserService():
    def student_create_user(student_user_create: StudentUserCreate):
        StudentUserValidator.validate_student_user_create(student_user_create)
        new_user = StudentUser(**student_user_create.model_dump())
        return StudentUserDAO.create_student_user(new_user)
    
    def get_student_user_by_email(email: str):
        StudentUserValidator.validate_student_user_email(email)
        user = StudentUserDAO.get_student_user_by_email(email)
        response = StudentUserResponse(**user.model_dump())
        return response
    
    def get_student_user_by_id(id: str):
        StudentUserValidator.validate_student_user_id(id)
        user_id = UUID(id)
        user = StudentUserDAO.get_student_user_by_id(user_id)
        response = StudentUserResponse(**user.model_dump())
        return response
    
    def get_all_student_users():
        return StudentUserDAO.get_all_student_users()
    
    def delete_student_user_by_id(id: str):
        StudentUserValidator.validate_student_user_id(id)
        ProfileServices.delete_profile(id)
        user_id = UUID(id)
        return StudentUserDAO.delete_student_user(user_id)