
from utils.imports import HTTPException, status, UUID, re
from modules.students.profile.profile_schemas import UrlValidator

class Validator():
    def validate_uuid(id: str):
        try:
            id = UUID(id)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Id")
    
    def validate_url(url: str):
        try:
            UrlValidator(url=url)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Url")
    
    def validate_roles(acutal_role, expected_role):
        if not acutal_role == expected_role:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
    
    def resticted_roles(actual_role, restircted_role):
        if actual_role == restircted_role:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
        
    def validate_two_roles(actual_role, role_one, role_two):
        if not actual_role == role_one and not actual_role == role_two:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
        
    def validate_three_roles(actual_role, role_one, role_two, role_three):
        if not actual_role == role_one and not actual_role == role_two and not actual_role == role_three:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")