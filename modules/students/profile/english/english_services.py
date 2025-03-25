

from .english_models import EnglishDAO, English
from .english_schemas import EnglishResponse, UUID
from .english_validator import EnglishValidator
from .english_schemas import EnglishSchema, EnglishUpdate


class EnglishServices():
    def create_english(id: str, english_create: EnglishSchema):
        EnglishValidator.validate_english_create(id, english_create)
        student_id = UUID(id)
        new_english = English(
                student_id=student_id, 
                **english_create.model_dump()  
            )
        response = EnglishDAO.create_english(new_english)
        return EnglishResponse(**response.model_dump())
    
    def get_english_by_student_id(id: UUID):
        response = EnglishDAO.get_english_by_student_id(id)
        return EnglishResponse(**response.model_dump())
    
    def delete_english(id: str):
        english_to_delete = EnglishDAO.get_english_by_id(UUID(id))
        return EnglishDAO.delete_english(english_to_delete)
    
    def get_all_english():
        return EnglishDAO.get_all_english()
    
    def update_english(id: str, english_update: EnglishUpdate):
        EnglishValidator.validate_english_update(id, english_update)
        
        english_id = UUID(id)
        
        return EnglishDAO.update_english(english_id, english_update)
    
    def delete_english_by_student_id(id: UUID):
        english_to_delete = EnglishDAO.get_english_by_student_id(id)
        EnglishDAO.delete_english(english_to_delete)
        return
    
    def get_all_english_updates():
        EnglishDAO.get_all_english_updates()