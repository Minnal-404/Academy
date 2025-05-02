
from utils.database import SQLModel, Field, Session, select, engine, Relationship
from utils.imports import datetime, uuid4, generate_time_stamps, Optional
from ...users.user_models import User


class LikeBase(SQLModel):
    id: str = Field(primary_key=True)

class Like(LikeBase, table=True):
    created_at: datetime = Field(default_factory=generate_time_stamps)
    



class LikeDAO():
    def like(like_create):
        with Session(engine) as session:
            session.add(like_create)
            session.commit()
        return {"message": "Liked"}
    
    def get_like(id: str):
        with Session(engine) as session:
            like = session.exec(select(Like).where(Like.id == id)).first()
        return like
    
    def unlike(like_to_delete):
        with Session(engine) as session:
            session.delete(like_to_delete)
            session.commit()
        return {"message": "Unliked"}
    
    def get_all_likes():
        with Session(engine) as session:
            likes = session.exec(select(Like)).all()
        return likes