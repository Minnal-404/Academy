
from ..users.academy_user_validator import AcademyUserValidator
from utils.imports import UUID
from ...students.profile.profile_services import ProfileServices


class UpdatesServices():
    def get_profile_updates(id: str):
        AcademyUserValidator.validate_academy_user_id(id)
        ProfileServices.get_all_updates()