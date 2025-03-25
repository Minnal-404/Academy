
from utils.database import SQLModel, Field, Session, select, engine
from utils.imports import datetime, timezone, uuid4
from .company_user_schemas import UUID, CompanyUserCreate, EmailStr


def generate_time_stamps():
    return datetime.now(timezone.utc)


class CompanyUserBase(SQLModel):
    name: str = Field(min_length=3, max_length=50)
    email: str = Field(unique=True)
    phone_number: str
    password: str = Field(min_length=8, max_length=20)
    

    


class CompanyUser(CompanyUserBase, table = True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default_factory=generate_time_stamps)
    updated_at: datetime = Field(default_factory=generate_time_stamps)


class CompanyUserDAO():
    def create_company_user(new_user: CompanyUserCreate):
        with Session(engine) as session:
            session.add(new_user)
            session.commit()
        return {"message": "User Created Successfully"}
    
    def get_company_user_by_email(email: EmailStr):
        with Session(engine) as session:
            user = session.exec(select(CompanyUser).where(CompanyUser.email == email)).first()
        return user
    
    def get_company_user_by_id(id: UUID):
        with Session(engine) as session:
            user = session.exec(select(CompanyUser).where(CompanyUser.id == id)).first()
        return user
    
    def get_all_company_users():
        with Session(engine) as session:
            users = session.exec(select(CompanyUser)).all()
        return users
    
    def delete_company_user(id: UUID):
        with Session(engine) as session:
            user_to_delete = CompanyUserDAO.get_company_user_by_id(id)
            session.delete(user_to_delete)
            session.commit()
        return {"message": "User Deleted Successfuly"}