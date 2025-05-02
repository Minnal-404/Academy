

from utils.imports import BaseModel, UUID, List

class LanguageList(BaseModel):
    languages: List[str]

class LanguageListResponse(BaseModel):
    id: UUID
    language: str