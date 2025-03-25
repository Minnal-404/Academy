

from utils.imports import BaseModel, EmailStr, UUID

class CompanyUserCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    password: str
    
class CompanyUserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    phone_number: str



