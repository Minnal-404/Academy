
from utils.validator import Validator
from utils.imports import HTTPException, status, re, UUID, EmailStr
from ...students.profile.projects.project_validator import ProjectValidator
from ...students.profile.projects.project_models import ProjectDAO
from ...students.profile.english.english_validator import EnglishValidator
from ...students.profile.english.english_models import EnglishDAO
from .approval_model import RejectionDAO
from .approval_schemas import Reject, RejectLanguage
from ...users.user_models import UserDAO
from ...students.profile.language.language_models import LanguageDAO
from ...students.profile.language.language_validator import LanguageValidator


class ApprovalValidator():
    def validate_reject_project(reject: Reject):
        ProjectValidator.validate_project_id(reject.id)
        if not reject.message:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message Is Required")
        if len(reject.message) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message Must Be Atleast 3 Characters")
        if len(reject.message) > 255:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message Must Not Contain More Than 255 Characters")
        project = RejectionDAO.get_rejection(reject.id)
        if project:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Project Already Rejected")
        
    def validate_project_approval(id: UUID):
        ProjectValidator.validate_project_id(id)
        project = ProjectDAO.get_project_by_id(id)
        if project.is_approved:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Project Already Approved")
    
    def validate_reject_english(reject: Reject):
        EnglishValidator.validate_english_id(reject.id)
        if not reject.message:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message Is Required")
        if len(reject.message) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message Must Be Atleast 3 Characters")
        if len(reject.message) > 255:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message Must Not Contain More Than 255 Characters")
        english = RejectionDAO.get_rejection(reject.id)
        if english:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="English Already Rejected")
        
    def validate_english_approval(id: UUID):
        EnglishValidator.validate_english_id(id)
        english = EnglishDAO.get_english_by_id(id)
        if english.is_approved:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="English Already Approved")
        
    def validate_language_approval(email: EmailStr):
        is_email = UserDAO.get_user_by_email(email)
        if not is_email:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        student = UserDAO.get_user_by_email(email)
        language = LanguageDAO.get_language_by_student_id(student.id)
        if language.is_approved:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Language Already Approved")
        
    def validate_reject_language(reject: RejectLanguage):
        is_email = UserDAO.get_user_by_email(reject.email)
        if not is_email:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        if not reject.message:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message Is Required")
        if len(reject.message) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message Must Be Atleast 3 Characters")
        if len(reject.message) > 255:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message Must Not Contain More Than 255 Characters")
        student = UserDAO.get_user_by_email(reject.email)
        language = RejectionDAO.get_rejection(student.id)
        if language:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Language Already Rejected")