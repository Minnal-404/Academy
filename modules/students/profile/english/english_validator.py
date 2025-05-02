
from utils.validator import Validator
from utils.imports import HTTPException, status, re, UUID
from ....users.user_validator import UserValidator
from .english_schemas import EnglishSchema, EnglishUpdate
from .english_models import EnglishDAO


class EnglishValidator():
    def validate_english_create(id: UUID, english_create: EnglishSchema):
        UserValidator.validate_user_id(id)
                
        if not english_create:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="English Field Required")
        
        EnglishValidator.validate_english_rank(english_create.rank)
        
        Validator.validate_url(english_create.url)
    
    def validate_english_update(id: UUID, english_update: EnglishUpdate):
        EnglishValidator.validate_english_id(id)
        english = EnglishDAO.get_english_by_id((id))

        if not english_update.rank and not english_update.url:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Body Is Required")
        
        if english_update.rank:
            EnglishValidator.validate_english_rank(english_update.rank)
            if english.rank == english_update.rank:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Rank Already Updated")
                
        
        if english_update.url:
            Validator.validate_url(english_update.url)
            if english.url == english_update.url:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Url Already Updated")
        
    def validate_english_id(id: UUID):
        
        is_id = EnglishDAO.get_english_by_id(id)
        
        if not is_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="English Field Not Found")
    
    def validate_english_rank(rank: str):
        if not re.match(r"^[A-C][1-2]$", rank):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Rank")
        
    def validate_user_and_english(student_id: UUID, user_id):
        if not student_id == user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
