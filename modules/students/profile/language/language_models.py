
from utils.database import SQLModel, Field, Session, select, engine, Relationship
from utils.imports import UUID, uuid4, datetime, generate_time_stamps, Optional
from ....users.user_models import User




class LanguageBase(SQLModel):
    student_id: UUID = Field(foreign_key="user.id", primary_key=True)
    language: str = Field(min_length=1, max_length=50)

class Language(LanguageBase, table=True):
    created_at: datetime = Field(default_factory=generate_time_stamps)
    updated_at: datetime = Field(default_factory=generate_time_stamps)
    is_approved: bool = Field(default=False)
    is_rejected: bool = Field(default=False)
    
    user: Optional[User] = Relationship(back_populates="language")
    
    
    
class LanguageDAO():
    def create_language(new_language):
        with Session(engine) as session:
            session.add(new_language)
            session.commit()
            session.refresh(new_language)
        return new_language
    
    def get_languages():
        with Session(engine) as session:
            languages = session.exec(select(Language)).all()
        return languages
    
    def get_language_by_student_id(id: UUID):
        with Session(engine) as session:
            language = session.exec(select(Language).where(Language.student_id == id)).first()
        return language
    
    def get_all_languages_by_student_id(id: UUID):
        with Session(engine) as session:
            languages = session.exec(select(Language).where(Language.student_id == id)).all()
        return languages
    
    def get_approved_languages_by_student_id(id: UUID):
        with Session(engine) as session:
            languages = session.exec(select(Language).where((Language.student_id == id) & (Language.is_approved == True) & (Language.is_rejected == False))).all()
        return languages

    def delete_language(language_to_delete):
        with Session(engine) as session:
            session.delete(language_to_delete)
            session.commit()
        return {"message": "Language Deleted Successfully"}
        
    def update_language(id: UUID, language_update: str):
        with Session(engine) as session:
            language = session.get(Language, id)
            language.language = language_update
            language.is_approved = False
            language.is_rejected = False
            language.updated_at = generate_time_stamps()
            session.commit()
        return {
            "message": f"{language_update} Updated Successfully"
        }

    
    def get_all_language_updates():
        with Session(engine) as session:
            languages = session.exec(select(Language).where((Language.is_approved ==False) & (Language.is_rejected == False))).all()
        return languages
    
    def get_all_updates_by_student_id(id: UUID):
        with Session(engine) as session:
            languages = session.exec(select(Language).where((Language.student_id == id) & (Language.is_approved ==False) & (Language.is_rejected == False))).all()
        return languages
    
    def approve_language(id: UUID):
        with Session(engine) as session:
            language = session.get(Language, id)
            language.is_approved = True
            language.is_rejected = False
            session.commit()
        return {"message": "Language Approved"}
        
    def reject_language(id: UUID):
        with Session(engine) as session:
            language = session.get(Language, id)
            language.is_approved = False
            language.is_rejected = True
            session.commit()
        return
    
    def language_filter(language: str):
        with Session(engine) as session:
            users = session.exec(select(Language).where(Language.language == language)).all()
        return users