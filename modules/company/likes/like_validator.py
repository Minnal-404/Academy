

from utils.imports import HTTPException, status, UUID
from ...users.user_validator import UserValidator
from ...users.user_models import UserDAO
from utils.validator import Validator
from .like_models import LikeDAO


class LikeValidator():
    def validate_like_email(email: str):
        UserValidator.validate_user_email(email)
        user = UserDAO.get_user_by_email(email)
        Validator.validate_roles(user.role, "student")
    
    def validate_get_like(id: str):
        like = LikeDAO.get_like(id)
        if like:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already Liked")
    
    def validate_unlike(id: str):
        like = LikeDAO.get_like(id)
        if not like:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This Profile is Not Liked")
