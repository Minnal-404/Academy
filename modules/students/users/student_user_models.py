
from utils.database import SQLModel, Field, Session, select, engine
from utils.imports import uuid4, datetime, timezone, EmailStr, UUID
from .student_user_schemas import StudentUserCreate

def generate_time_stamps():
    return datetime.now(timezone.utc)


class StudentUserBase(SQLModel):
    name: str = Field(min_length=3, max_length=50)
    email: str = Field(unique=True)
    phone_number: str
    password: str = Field(min_length=8, max_length=20)


class StudentUser(StudentUserBase, table = True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default_factory=generate_time_stamps)
    updated_at: datetime = Field(default_factory=generate_time_stamps)
    
class StudentUserDAO():
    def create_student_user(new_user: StudentUserCreate):
        with Session(engine) as session:
            session.add(new_user)
            session.commit()
        return {"message": "User Created Successfully"}
    
    def get_student_user_by_email(email: EmailStr):
        with Session(engine) as session:
            user = session.exec(select(StudentUser).where(StudentUser.email == email)).first()
        return user
    
    def get_student_user_by_id(id: UUID):
        with Session(engine) as session:
            user = session.exec(select(StudentUser).where(StudentUser.id == id)).first()
        return user
    
    def get_all_student_users():
        with Session(engine) as session:
            users = session.exec(select(StudentUser)).all()
        return users
    
    def delete_student_user(id: UUID):
        with Session(engine) as session:
            user_to_delete = StudentUserDAO.get_student_user_by_id(id)
            session.delete(user_to_delete)
            session.commit()
        return {"message": "User Deleted Successfuly"}
    
