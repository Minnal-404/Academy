
from .company_user_schemas import  CompanyUserCreate, UUID
from utils.imports import HTTPException, status, re
from .company_user_models import CompanyUserDAO
from ...students.users.student_user_models import StudentUserDAO
from ...academy.users.academy_user_models import AcademyUserDAO


class CompanyUserValidator():
    def validate_company_user_create(company_user_create: CompanyUserCreate):
        if not company_user_create:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Body Is Required")
        
        if len(company_user_create.name) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name Must Contain Atleat 3 Characters")
        
        if len(company_user_create.name) > 50:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name Cannot Contain More Than 50 Characters")
        
        is_email_exists_in_academy = AcademyUserDAO.get_academy_user_by_email(company_user_create.email)
   
        is_email_exists_in_company = CompanyUserDAO.get_company_user_by_email(company_user_create.email)

        is_email_exists_in_student = StudentUserDAO.get_student_user_by_email(company_user_create.email)
        
        if is_email_exists_in_company or is_email_exists_in_academy or is_email_exists_in_student:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email Already Exists")
        
        if not re.match(r'^\d{10}$', company_user_create.phone_number) or not len(company_user_create.phone_number) == 10:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Phone Number Must Contain 10 Digits")
        
        if len(company_user_create.password) < 8:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password Must Contain Atleat 8 Characters")
        
        if len(company_user_create.password) > 20:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password Cannot Contain More Than 20 Characters")
        
    def validate_company_user_email(email: str):
        if not email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email Is Required")
        
        is_email_exists = CompanyUserDAO.get_company_user_by_email(email)
        
        if not is_email_exists:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    
    def validate_company_user_id(id: str):
        if not id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Id Is Required")
        
        try:
            user_id = UUID(id)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid User Id")
        
        is_id_in_table = CompanyUserDAO.get_company_user_by_id(user_id)
        if not is_id_in_table:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        