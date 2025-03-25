
from .user_schemas import  UserCreate, UUID, Login
from utils.imports import HTTPException, status, re
from .user_models import UserDAO
from .auth import verify_password, Request, bcrypt, jwt_token_decrypt



class UserValidator():
    def validate_user_create(user_create: UserCreate):
        if not user_create:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Body Is Required")
        
        if len(user_create.name) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name Must Contain Atleat 3 Characters")
        
        if len(user_create.name) > 50:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name Cannot Contain More Than 50 Characters")
        
        # is_email_exists_in_academy = AcademyUserDAO.get_academy_user_by_email(user_create.email)
   
        # is_email_exists_in_ = UserDAO.get_user_by_email(user_create.email)

        is_email_exists = UserDAO.get_user_by_email(user_create.email)
        
        if is_email_exists:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email Already Exists")
        
        if not re.match(r'^\d{10}$', user_create.phone_number) or not len(user_create.phone_number) == 10:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Phone Number Must Contain 10 Digits")
        
        if len(user_create.password) < 8:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password Must Contain Atleat 8 Characters")
        
        if len(user_create.password) > 20:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password Cannot Contain More Than 20 Characters")
        
        UserValidator.validate_user_role(user_create.role)
        
    def validate_login(login: Login):
        UserValidator.validate_user_email(login.email)
        UserValidator.validate_user_role(login.role)
        user = UserDAO.get_user_by_email(login.email)
        UserValidator.validate_password(login.password, user.password)
        if not user.role == login.role:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
            
    def validate_user_role(role):
        if not role == "academy" and not role == "student" and not role == "company":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
        
    def validate_user_email(email: str):
        if not email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email Is Required")
        
        is_email_exists = UserDAO.get_user_by_email(email)
        
        if not is_email_exists:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    
    def validate_user_id(id: UUID):
        if not id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Id Is Required")
        
        
        is_id_in_table = UserDAO.get_user_by_id(id)
        if not is_id_in_table:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
    def validate_password(login_password: str, user_password: str):
        verified = verify_password(login_password, user_password)
        if not verified:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Password")
        
    def validate_request(request: Request):
        if not request:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Request Is Required")
        if not request.headers.get("Authorization"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token Required")
        
        try:
            bearer_token = request.headers.get("Authorization")
            jwt_token=bearer_token.split(" ")[1]
            payload=jwt_token_decrypt(jwt_token)
            email=payload["email"]
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Token")
        UserValidator.validate_user_email(email)
