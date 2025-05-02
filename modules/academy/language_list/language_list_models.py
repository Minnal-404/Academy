

from utils.database import SQLModel, Field, Session, select, engine
from utils.imports import UUID, uuid4, datetime, generate_time_stamps

class LanguageListBase(SQLModel):
    language: str = Field(min_length=1, max_length=50)

class LanguageList(LanguageListBase, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default_factory=generate_time_stamps)
    updated_at: datetime = Field(default_factory=generate_time_stamps)


class LanguageListDAO():
    def create_language_list(language):
        with Session(engine) as session:
            session.add(language)
            session.commit()
            session.refresh(language)
        return language
    
    def get_language(language: str):
        with Session(engine) as session:
            result = session.exec(select(LanguageList).where(LanguageList.language == language)).first()
        return result
    
    def get_language_by_id(id: UUID):
        with Session(engine) as session:
            result = session.exec(select(LanguageList).where(LanguageList.id == id)).first()
        return result
    
    def delete_language_list(language):
        with Session(engine) as session:
            session.delete(language)
            session.commit()
        return {
            "message": "Language Deleted Successfully"
        }
        
    def get_language_list():
        with Session(engine) as session:
            result = session.exec(select(LanguageList)).all()
        return result