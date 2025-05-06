

from utils.imports import BaseModel, UUID, Optional, ConfigDict





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
    
    model_config = ConfigDict(from_attributes=True)


class EnglishUpdate(BaseModel):
    rank: str = None
    url: str = None