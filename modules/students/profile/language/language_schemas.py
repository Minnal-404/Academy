

from utils.imports import BaseModel, UUID, List, Optional


class LanguageResponse(BaseModel):
    language: str
    is_approved: bool
    is_rejected: bool
    message:  Optional[str] = None