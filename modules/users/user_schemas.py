

from utils.imports import BaseModel, EmailStr, UUID

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    password: str
    role: str
    
class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    phone_number: str
    token: str

class Login(BaseModel):
    email: EmailStr
    password: str
    role: str
