

from utils.database import SQLModel, Field, Session, select, engine
from utils.imports import datetime, uuid4, generate_time_stamps, UUID
from .approval_schemas import Reject



class RejectedBase(SQLModel):
    id: UUID = Field(primary_key=True,foreign_key="project.id")
    field: str = Field(min_length = 3, max_length=20)
    message: str = Field(min_length = 3, max_length=255)

class Rejected(RejectedBase, table=True):
    created_at: datetime = Field(default_factory=generate_time_stamps)

class RejectionDAO():
    def create_rejection(rejection):
        with Session(engine) as session:
            session.add(rejection)
            session.commit()
        return {
            "message": "Rejected Successfully"
        }
    
    def delete_rejection(rejection_to_delete):
        with Session(engine) as session:
            session.delete(rejection_to_delete)
            session.commit()
        return
    
    def get_rejection(id :UUID):
        with Session(engine) as session:
            rejected = session.exec(select(Rejected).where(Rejected.id == id)).first()
        return rejected