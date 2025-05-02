
from utils.imports import BaseModel, UUID, EmailStr


class Reject(BaseModel):
    id: UUID
    message: str

class RejectLanguage(BaseModel):
    email: EmailStr
    message: str