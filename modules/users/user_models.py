
from utils.database import SQLModel, Field, Session, select, engine
from utils.imports import datetime, timezone, uuid4
from .user_schemas import UUID, UserCreate, EmailStr


def generate_time_stamps():
    return datetime.now(timezone.utc)


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
    
    def delete_user(id: UUID):
        with Session(engine) as session:
            user_to_delete = UserDAO.get_user_by_id(id)
            session.delete(user_to_delete)
            session.commit()
        return {"message": "User Deleted Successfuly"}