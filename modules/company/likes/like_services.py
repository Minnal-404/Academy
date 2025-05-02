

from utils.imports import UUID
from ...users.user_models import UserDAO
from ...users.user_schemas import UserRes
from ...users.user_validator import UserValidator
from .like_models import LikeDAO, Like
from .like_validator import LikeValidator




class LikeServices():
    def like(company_id: str, email: str):
        LikeValidator.validate_like_email(email)
        user = UserDAO.get_user_by_email(email)
        id = str(company_id)+str(user.id)
        LikeValidator.validate_get_like(id)
        like_create = Like(id=id)
        return LikeDAO.like(like_create)
    
    def unlike(company_id: str, email: str):
        LikeValidator.validate_like_email(email)
        user = UserDAO.get_user_by_email(email)
        id = str(company_id)+str(user.id)
        LikeValidator.validate_unlike(id)
        like_to_delete = LikeDAO.get_like(id)
        return LikeDAO.unlike(like_to_delete)
    
    def get_all_likes():
        ids = LikeDAO.get_all_likes()
        likes = []
        for id in ids:
            length = int(len(id.id)/2)
            company_id = id.id[:length]
            student_id = id.id[length:]
            company_user = UserDAO.get_user_by_id(UUID(company_id))
            student_user = UserDAO.get_user_by_id(UUID(student_id))
            company = UserRes(**company_user.model_dump())
            student = UserRes(**student_user.model_dump())
            likes.append({
                "company": company,
                "student": student
            })
        return likes
    
    def get_all_likes_by_company_id(company_id: UUID):
        ids = LikeDAO.get_all_likes()
        likes = []
        for id in ids:
            length = int(len(id.id)/2)
            company = id.id[:length]
            if company_id == company:
                student_id = id.id[length:]
                student_user = UserDAO.get_user_by_id(UUID(student_id))
                student = UserRes(**student_user.model_dump())
                likes.append(student)
        return {'likes': likes}

    def get_like(like_id: str):
        like = LikeDAO.get_like(like_id)
        
        return like