
from .user_schemas import UserCreate, UserResponse, UUID, Login, UserRes
from .user_models import User, UserDAO
from .user_validator import UserValidator
from utils.auth import jwt_token_encrypt, hash_password
from ..students.profile.profile_services import ProfileServices


class UserService():
    def sign_up(user_create: UserCreate):
        UserValidator.validate_user_create(user_create)
        hashed_password = hash_password(user_create.password)
        user_create.password = hashed_password
        new_user = User(**user_create.model_dump())
        user_details = UserDAO.create_user(new_user)
        token = jwt_token_encrypt(user_details)
        response = UserResponse(token = token, **user_details.model_dump())
        return response
    
    def login(login: Login):
        UserValidator.validate_login(login)
        user_details = UserDAO.get_user_by_email(login.email)
        token = jwt_token_encrypt(user_details)
        result = UserResponse(token=token, **user_details.model_dump())
        return result
    
    def get_all_users():
        return UserDAO.get_all_users()
    
    def delete_user_by_id(id: UUID):
        UserValidator.validate_user_id(id)
        # user_id = UUID(id)
        try:
            ProfileServices.delete_profile(id)
        except:
            pass
        return UserDAO.delete_user(id)
    
    def get_all_students():
        users = UserDAO.get_all_student_users()
        students = []
        for user in users:
            students.append(UserRes(**user.model_dump()))
        return {
            "students": students
        }
    
    def get_all_companies():
        users = UserDAO.get_all_company_users()
        companies = []
        for user in users:
            companies.append(UserRes(**user.model_dump()))
        return {
            "companies": companies
        }