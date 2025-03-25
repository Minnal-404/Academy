
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