
from utils.imports import UUID, EmailStr
from ...students.profile.projects.project_validator import ProjectValidator
from ...students.profile.projects.project_models import ProjectDAO
from .approval_model import RejectionDAO, Rejected
from .approval_schemas import Reject, RejectLanguage
from .approval_validator import ApprovalValidator
from ...students.profile.english.english_models import EnglishDAO
from ...students.profile.language.language_models import LanguageDAO
from ...users.user_models import UserDAO

    
class ApprovalServices():
    def approve_project(project_id: UUID):
        ApprovalValidator.validate_project_approval(project_id)
        try:
            rejection_to_delete = RejectionDAO.get_rejection(project_id)
            RejectionDAO.delete_rejection(rejection_to_delete)
        except:
            pass
        return ProjectDAO.approve_project(project_id)
    
    def reject_project(reject: Reject):
        ApprovalValidator.validate_reject_project(reject)
        project_id = reject.id
        ProjectDAO.reject_project(project_id)
        rejection = Rejected(field="project",**reject.model_dump())
        return RejectionDAO.create_rejection(rejection)
    
    def approve_english(english_id: UUID):
        ApprovalValidator.validate_english_approval(english_id)
        try:
            rejection_to_delete = RejectionDAO.get_rejection(english_id)
            RejectionDAO.delete_rejection(rejection_to_delete)
        except:
            pass
        return EnglishDAO.approve_english(english_id)
    
    def reject_english(reject: Reject):
        ApprovalValidator.validate_reject_english(reject)
        english_id = reject.id
        EnglishDAO.reject_english(english_id)
        rejection = Rejected(field="english",**reject.model_dump())
        return RejectionDAO.create_rejection(rejection)
    
    def approve_language(email: EmailStr):
        ApprovalValidator.validate_language_approval(email)
        student = UserDAO.get_user_by_email(email)
        student_id = student.id
        try:
            rejection_to_delete = RejectionDAO.get_rejection(student_id)
            RejectionDAO.delete_rejection(rejection_to_delete)
        except:
            pass
        return LanguageDAO.approve_language(student_id)
    
    def reject_language(reject: RejectLanguage):
        ApprovalValidator.validate_reject_language(reject)
        student = UserDAO.get_user_by_email(reject.email)
        student_id = student.id
        LanguageDAO.reject_language(student_id)
        rejection = Rejected(field="language",id=student_id, message=reject.message)
        return RejectionDAO.create_rejection(rejection)
    
    