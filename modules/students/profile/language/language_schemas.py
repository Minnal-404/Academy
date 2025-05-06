

from utils.imports import BaseModel, UUID, List, Optional, ConfigDict


class LanguageResponse(BaseModel):
    language: str
    is_approved: bool
    is_rejected: bool
    message:  Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
