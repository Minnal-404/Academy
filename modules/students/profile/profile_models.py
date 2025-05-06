
from utils.imports import UUID, selectinload, HTTPException
from utils.database import Session, engine, select
from ...users.user_models import User
from ...users.user_schemas import UserRes
from .english.english_schemas import EnglishResponse
from .english.english_models import English
from .language.language_schemas import LanguageResponse
from .language.language_models import Language
from .projects.project_schemas import ProjectResponse
from .projects.project_models import Project


class ProfileDAO():
    def get_full_profile_by_user_id(user_id: UUID):
        with Session(engine) as session:
            stmt = (
    select(User)
    .where(User.id == user_id)
    .options(
        selectinload(User.english.and_(
            English.is_approved == True,
            English.is_rejected == False
        )),
        selectinload(User.language.and_(
            Language.is_approved == True,
            Language.is_rejected == False
        )),
        selectinload(User.projects.and_(
            Project.is_approved == True,
            Project.is_rejected == False
        ))
    )
)
            user = session.scalars(stmt).first()
            print(user)
            if user.english is None:
                return
            return {
                "user": UserRes(**user.model_dump()),
                "english": EnglishResponse(**user.english.model_dump()) if user.english else None,
"language": LanguageResponse(**user.language.model_dump()) if user.language else None,
"projects": [ProjectResponse(**p.model_dump()) for p in user.projects] if user.projects else [],

            }

