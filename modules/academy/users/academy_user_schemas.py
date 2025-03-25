
from utils.imports import EmailStr, UUID, BaseModel



class AcademyUserCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    password: str

class AcademyUserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    phone_number: str