

from utils.database import Session, engine, select
from utils.imports import selectinload
from ...users.user_models import User
from ...students.profile.english.english_models import English
from ...students.profile.language.language_models import Language
from ...students.profile.projects.project_models import Project
from ...users.user_schemas import UserRes
from ...students.profile.english.english_schemas import EnglishResponse
from ...students.profile.language.language_schemas import LanguageResponse
from ...students.profile.projects.project_schemas import ProjectResponse
from ..likes.like_services import LikeServices



class FilterDAO():
    def rank_filter(rank: str, company_id):
            with Session(engine) as session:
                stmt = (
      select(User)
         .join(User.english)
    .where(English.rank == rank)
    .options(
        selectinload(User.projects),
        selectinload(User.language),
        selectinload(User.english)
    )
                )
                users = session.exec(stmt).all()
                profiles = []
                for user in users:
                    like_id = f"{company_id}{user.id}"
                    is_liked = LikeServices.get_like(like_id)
                    profile = {
        "user": UserRes(**user.model_dump()),
        "english": EnglishResponse(**user.english.model_dump()),
        "language": LanguageResponse(**user.language.model_dump()),
        "projects": [ProjectResponse(**project.model_dump()) for project in user.projects],
        "is_liked": bool(is_liked)
    }
                    profiles.append(profile)
                return {"profiles": profiles}

    def language_filter(language: str, company_id):
            with Session(engine) as session:
                stmt = (
      select(User)
         .join(User.language)
    .where(Language.language == language)
    .options(
        selectinload(User.projects),
        selectinload(User.language),
        selectinload(User.english)
    )
                )
                users = session.exec(stmt).all()
                profiles = []
                for user in users:
                    like_id = f"{company_id}{user.id}"
                    is_liked = LikeServices.get_like(like_id)
                    profile = {
        "user": UserRes(**user.model_dump()),
        "english": EnglishResponse(**user.english.model_dump()),
        "language": LanguageResponse(**user.language.model_dump()),
        "projects": [ProjectResponse(**project.model_dump()) for project in user.projects],
        "is_liked": bool(is_liked)
    }
                    profiles.append(profile)
                return {"profiles": profiles}
    
    
    def rank_and_language_filter(rank: str, language: str, company_id):
            with Session(engine) as session:
                stmt = (
                   select(User)
                   .join(User.language)
                   .join(User.english)
                   .where(
                       (Language.language == language) & (English.rank == rank)
                       )
                   .options(
                       selectinload(User.projects),
                       selectinload(User.language),
                       selectinload(User.english)
                       )
                   )
                users = session.exec(stmt).all()
                profiles = []
                for user in users:
                    like_id = f"{company_id}{user.id}"
                    is_liked = LikeServices.get_like(like_id)
                    profile = {
        "user": UserRes(**user.model_dump()),
        "english": EnglishResponse(**user.english.model_dump()),
        "language": LanguageResponse(**user.language.model_dump()),
        "projects": [ProjectResponse(**project.model_dump()) for project in user.projects],
        "is_liked": bool(is_liked)
    }
                    profiles.append(profile)
                return {"profiles": profiles}

