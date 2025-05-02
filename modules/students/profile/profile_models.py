
from utils.imports import UUID
from utils.database import Session, engine
from ...users.user_models import User
from ...users.user_schemas import UserRes
from .english.english_schemas import EnglishResponse
from .language.language_schemas import LanguageResponse
from .projects.project_schemas import ProjectResponse


class ProfileDAO():
    def get_full_profile_by_user_id(user_id: UUID):
        with Session(engine) as session:
            user = session.get(User, user_id)
            return {
                "user": UserRes(**user.model_dump()),
                "english": EnglishResponse(**user.english.model_dump()),
                "language": LanguageResponse(**user.language.model_dump()),
                "projects": [ProjectResponse(**project.model_dump()) for project in user.projects],
            }

