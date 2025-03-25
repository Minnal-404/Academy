

from utils.imports import BaseModel, UUID





class EnglishSchema(BaseModel):
    rank: str
    url: str

class EnglishResponse(BaseModel):
    id: UUID
    rank: str
    url: str

class EnglishUpdate(BaseModel):
    rank: str = None
    url: str = None