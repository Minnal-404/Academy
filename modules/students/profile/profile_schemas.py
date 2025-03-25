

from utils.imports import BaseModel, HttpUrl, List
from .projects.project_schemas import ProjectSchema
from .english.english_schemas import EnglishSchema


class UrlValidator(BaseModel):
    url: HttpUrl

class ProfileCreate(BaseModel):
    projects: List[ProjectSchema]
    english: EnglishSchema