
from utils.database import SQLModel, Field, Session, select, engine, Relationship
from utils.imports import UUID, uuid4, datetime, generate_time_stamps, Optional
from .english_schemas import EnglishSchema, EnglishUpdate
from ....users.user_models import User




class EnglishBase(SQLModel):
    student_id: UUID = Field(foreign_key="user.id")
    rank: str = Field(min_length=2, max_length=2)
    url: str = Field(min_length=10, max_length=2048)

class English(EnglishBase, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default_factory=generate_time_stamps)
    updated_at: datetime = Field(default_factory=generate_time_stamps)
    is_approved: bool = Field(default=False)
    is_rejected: bool = Field(default=False)
    
    user: Optional[User] = Relationship(back_populates="english")

    
    
    
class EnglishDAO():
    def create_english(new_english: EnglishSchema):
        with Session(engine) as session:
            session.add(new_english)
            session.commit()
            session.refresh(new_english)
        return new_english
    
    def get_all_english():
        with Session(engine) as session:
            all_english = session.exec(select(English)).all()
        return all_english
    
    def get_english_by_id(id: UUID):
        with Session(engine) as session:
            english = session.exec(select(English).where(English.id == id)).first()
        return english
    
    def get_english_by_student_id(id: UUID):
        with Session(engine) as session:
            english = session.exec(select(English).where(English.student_id == id)).first()
        return english
    
    def get_approved_english_by_student_id(id: UUID):
        with Session(engine) as session:
            english = session.exec(select(English).where((English.student_id == id) & (English.is_approved ==True) & (English.is_rejected == False))).first()
        return english

    def delete_english(english_to_delete):
        with Session(engine) as session:
            session.delete(english_to_delete)
            session.commit()
        return {"message": "English Field Deleted Successfully"}
    
    def update_english(id: UUID, english_update: EnglishUpdate):
        if english_update.rank:
            with Session(engine) as session:
                english = session.get(English, id)
                english.rank = english_update.rank
                english.updated_at = generate_time_stamps()
                english.is_approved = False
                english.is_rejected = False
                session.commit()
        if english_update.url:
            with Session(engine) as session:
                english = session.get(English, id)
                english.url = english_update.url
                english.updated_at = generate_time_stamps()
                english.is_approved = False
                english.is_rejected = False
                session.commit()
        return {"message": "English Updated Successfully"}
    
    def get_all_english_updates_users():
        with Session(engine) as session:
            users = session.exec(select(English.student_id).distinct().where((English.is_approved ==False) & (English.is_rejected == False))).all()
        return users
    
    def approve_english(id: UUID):
        with Session(engine) as session:
            english = session.get(English, id)
            english.is_approved = True
            english.is_rejected = False
            session.commit()
        return {"message": "English Approved"}
        
    def reject_english(id: UUID):
        with Session(engine) as session:
            english = session.get(English, id)
            english.is_approved = False
            english.is_rejected = True
            session.commit()
        return
    
    def rank_filter(rank: str):
        with Session(engine) as session:
            users = session.exec(select(English).where(English.rank == rank)).all()
        return users