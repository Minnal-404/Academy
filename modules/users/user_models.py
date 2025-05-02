
from utils.database import SQLModel, Field, Session, select, engine, Relationship
from utils.imports import datetime, uuid4, generate_time_stamps, Optional, List
from .user_schemas import UUID, UserCreate, EmailStr



class UserBase(SQLModel):
    name: str = Field(min_length=3, max_length=50)
    email: str = Field(unique=True)
    phone_number: str = Field(min_length=10, max_length=10)
    password: str
    role: str = Field(min_length=7, max_length=7)
    

    


class User(UserBase, table = True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default_factory=generate_time_stamps)
    updated_at: datetime = Field(default_factory=generate_time_stamps)
    
    english: Optional["English"] = Relationship(back_populates="user")
    language: Optional["Language"] = Relationship(back_populates="user")
    projects: List["Project"] = Relationship(back_populates="user")



class UserDAO():
    def create_user(new_user: UserCreate):
        with Session(engine) as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        return new_user
    
    def get_user_by_email(email: EmailStr):
        with Session(engine) as session:
            user = session.exec(select(User).where(User.email == email)).first()
        return user
    
    def get_user_by_id(id: UUID):
        with Session(engine) as session:
            user = session.exec(select(User).where(User.id == id)).first()
        return user
    
    def get_all_users():
        with Session(engine) as session:
            users = session.exec(select(User)).all()
        return users
    
    def get_all_student_users():
        with Session(engine) as session:
            users = session.exec(select(User).where(User.role == "student")).all()
        return users
    
    def get_all_company_users():
        with Session(engine) as session:
            users = session.exec(select(User).where(User.role == "company")).all()
        return users
    

    
    def delete_user(id: UUID):
        with Session(engine) as session:
            user_to_delete = UserDAO.get_user_by_id(id)
            session.delete(user_to_delete)
            session.commit()
        return {"message": "User Deleted Successfuly"}