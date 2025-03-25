
from utils.imports import EmailStr, UUID, BaseModel



class StudentUserCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    password: str

class StudentUserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    phone_number: str