

from .english_models import EnglishDAO, English
from .english_schemas import EnglishResponse, UUID
from .english_validator import EnglishValidator
from .english_schemas import EnglishSchema, EnglishUpdate
from ....users.user_models import UserDAO
from ....users.user_schemas import UserRes
from ....academy.approval.approval_model import RejectionDAO


class EnglishServices():
    def create_english(id: UUID, english_create: EnglishSchema):
        
        new_english = English(
                student_id=id,
                **english_create.model_dump()  
            )
        response = EnglishDAO.create_english(new_english)
        return EnglishResponse(**response.model_dump())
    
    def get_english_by_student_id(id: UUID):
        result = EnglishDAO.get_english_by_student_id(id)
        if result.is_rejected:
                reject = RejectionDAO.get_rejection(result.id)
                project_data = {**result.model_dump(), **reject.model_dump()}
                return EnglishResponse(**project_data)
        else:
            return EnglishResponse(**result.model_dump())
    
    def get_approved_english_by_student_id(id: UUID):
        response = EnglishDAO.get_english_by_student_id(id)
        return EnglishResponse(**response.model_dump())
    
    def delete_english(id: str):
        english_to_delete = EnglishDAO.get_english_by_id(UUID(id))
        return EnglishDAO.delete_english(english_to_delete)
    
    def get_all_english():
        return EnglishDAO.get_all_english()
    
    def update_english(user_id: UUID, english_id: UUID, english_update: EnglishUpdate):
        EnglishValidator.validate_english_update(english_id, english_update)
        
        try:
            rejection_to_delete = RejectionDAO.get_rejection(english_id)
            RejectionDAO.delete_rejection(rejection_to_delete)
        except:
            pass
        project_to_update = EnglishDAO.get_english_by_id(english_id)
        EnglishValidator.validate_user_and_english(project_to_update.student_id, user_id)
        return EnglishDAO.update_english(english_id, english_update)
    
    def delete_english_by_student_id(id: UUID):
        english_to_delete = EnglishDAO.get_english_by_student_id(id)
        EnglishDAO.delete_english(english_to_delete)
        return
    
    def get_all_english_updates():
        ids = EnglishDAO.get_all_english_updates_users()
        english = []
        for id in ids:
            user = UserDAO.get_user_by_id(id)
            user = UserRes(**user.model_dump())
            eng = EnglishDAO.get_english_by_student_id(id)
            eng = EnglishResponse(**eng.model_dump())
            english.append({
                "user": user,
                "english": eng
            })
        return english
    
    def rank_filter(rank: str):
        from ..profile_services import ProfileServices
        EnglishValidator.validate_english_rank(rank)
        users = EnglishDAO.rank_filter(rank)
        profiles = []
        for user in users:
            user_id = user.student_id
            profile = ProfileServices.get_profile_by_student_id(user_id)
            student = UserDAO.get_user_by_id(user_id)
            student = UserRes(**student.model_dump())
            profile["user"] = student
            profiles.append(profile)
        return {'profiles': profiles}
            