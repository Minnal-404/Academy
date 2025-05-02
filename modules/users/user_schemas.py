

from utils.imports import BaseModel, EmailStr, UUID

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    password: str
    role: str
    
class UserResponse(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    token: str

class UserRes(BaseModel):
    name: str
    email: EmailStr
    phone_number: str

class Login(BaseModel):
    email: EmailStr
    password: str
    role: str

class Payload(BaseModel):
    id: UUID
    role: str