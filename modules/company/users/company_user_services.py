
from .company_user_schemas import CompanyUserCreate, CompanyUserResponse, UUID
from .company_user_models import CompanyUser, CompanyUserDAO
from .company_user_validator import CompanyUserValidator


class CompanyUserService():
    def company_create_user(company_user_create: CompanyUserCreate):
        CompanyUserValidator.validate_company_user_create(company_user_create)
        new_user = CompanyUser(**company_user_create.model_dump())
        return CompanyUserDAO.create_company_user(new_user)
    
    def get_company_user_by_email(email: str):
        CompanyUserValidator.validate_company_user_email(email)
        user = CompanyUserDAO.get_company_user_by_email(email)
        response = CompanyUserResponse(**user.model_dump())
        return response
    
    def get_company_user_by_id(id: str):
        CompanyUserValidator.validate_company_user_id(id)
        user_id = UUID(id)
        user = CompanyUserDAO.get_company_user_by_id(user_id)
        response = CompanyUserResponse(**user.model_dump())
        return response
    
    def get_all_company_users():
        return CompanyUserDAO.get_all_company_users()
    
    def delete_company_user_by_id(id: str):
        CompanyUserValidator.validate_company_user_id(id)
        user_id = UUID(id)
        return CompanyUserDAO.delete_company_user(user_id)