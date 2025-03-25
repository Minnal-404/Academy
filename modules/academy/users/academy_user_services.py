
from .academy_user_schemas import AcademyUserCreate, AcademyUserResponse, UUID
from .academy_user_models import AcademyUser, AcademyUserDAO
from .academy_user_validator import AcademyUserValidator


class AcademyUserService():
    def academy_create_user(academy_user_create: AcademyUserCreate):
        AcademyUserValidator.validate_academy_user_create(academy_user_create)
        new_user = AcademyUser(**academy_user_create.model_dump())
        return AcademyUserDAO.create_academy_user(new_user)
    
    def get_academy_user_by_email(email: str):
        AcademyUserValidator.validate_academy_user_email(email)
        user = AcademyUserDAO.get_academy_user_by_email(email)
        response = AcademyUserResponse(**user.model_dump())
        return response
    
    def get_academy_user_by_id(id: str):
        AcademyUserValidator.validate_academy_user_id(id)
        user_id = UUID(id)
        user = AcademyUserDAO.get_academy_user_by_id(user_id)
        response = AcademyUserResponse(**user.model_dump())
        return response
    
    def get_all_academy_users():
        return AcademyUserDAO.get_all_academy_users()
    
    def delete_academy_user_by_id(id: str):
        AcademyUserValidator.validate_academy_user_id(id)
        user_id = UUID(id)
        return AcademyUserDAO.delete_academy_user(user_id)