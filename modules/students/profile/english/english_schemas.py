

from utils.imports import BaseModel, UUID, Optional





class EnglishSchema(BaseModel):
    rank: str
    url: str

class EnglishResponse(BaseModel):
    id: UUID
    rank: str
    url: str
    is_approved: bool
    is_rejected: bool
    message: Optional[str] = None

class EnglishUpdate(BaseModel):
    rank: str = None
    url: str = None