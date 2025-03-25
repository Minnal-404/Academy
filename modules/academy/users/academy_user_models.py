
from utils.database import SQLModel, Field, Session, select, engine
from utils.imports import uuid4, datetime, timezone, EmailStr, UUID
from .academy_user_schemas import AcademyUserCreate

def generate_time_stamps():
    return datetime.now(timezone.utc)


class AcademyUserBase(SQLModel):
    name: str = Field(min_length=3, max_length=50)
    email: str = Field(unique=True)
    phone_number: str
    password: str = Field(min_length=8, max_length=20)


class AcademyUser(AcademyUserBase, table = True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default_factory=generate_time_stamps)
    updated_at: datetime = Field(default_factory=generate_time_stamps)
    
class AcademyUserDAO():
    def create_academy_user(new_user: AcademyUserCreate):
        with Session(engine) as session:
            session.add(new_user)
            session.commit()
        return {"message": "User Created Successfully"}
    
    def get_academy_user_by_email(email: EmailStr):
        with Session(engine) as session:
            user = session.exec(select(AcademyUser).where(AcademyUser.email == email)).first()
        return user
    
    def get_academy_user_by_id(id: UUID):
        with Session(engine) as session:
            user = session.exec(select(AcademyUser).where(AcademyUser.id == id)).first()
        return user
    
    def get_all_academy_users():
        with Session(engine) as session:
            users = session.exec(select(AcademyUser)).all()
        return users
    
    def delete_academy_user(id: UUID):
        with Session(engine) as session:
            user_to_delete = AcademyUserDAO.get_academy_user_by_id(id)
            session.delete(user_to_delete)
            session.commit()
        return {"message": "User Deleted Successfuly"}
    
