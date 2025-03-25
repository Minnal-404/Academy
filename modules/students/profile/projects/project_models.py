
from utils.database import SQLModel, Field, Session, select, engine
from utils.imports import UUID, uuid4, datetime, timezone
from .project_schemas import ProjectUpdate


def generate_time_stamps():
    return datetime.now(timezone.utc)

class ProjectBase(SQLModel):
    student_id: UUID = Field(foreign_key="studentuser.id")
    title: str = Field(min_length=3, max_length=50)
    url: str = Field(min_length=10, max_length=2048)

class Project(ProjectBase, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default_factory=generate_time_stamps)
    updated_at: datetime = Field(default_factory=generate_time_stamps)
    is_approved: bool = Field(default=False)
    is_rejected: bool = Field(default=False)
    
    
    
class ProjectDAO():
    def create_project(new_project):
        with Session(engine) as session:
            session.add(new_project)
            session.commit()
            session.refresh(new_project)
        return new_project
    
    def get_projects():
        with Session(engine) as session:
            projects = session.exec(select(Project)).all()
        return projects
    
    def get_project_by_id(id: UUID):
        with Session(engine) as session:
            project = session.exec(select(Project).where(Project.id == id)).first()
        return project
    
    def get_all_projects_by_student_id(id: UUID):
        with Session(engine) as session:
            projects = session.exec(select(Project).where(Project.student_id == id)).all()
        return projects

    def delete_project(project_to_delete):
        with Session(engine) as session:
            session.delete(project_to_delete)
            session.commit()
        return {"message": "Project Deleted Successfully"}
        
    def update_project(id: UUID, project_update: ProjectUpdate):
        
        if project_update.title:
            with Session(engine) as session:
                project = session.get(Project, id)
                project.title = project_update.title
                project.updated_at = generate_time_stamps()
                session.commit()
        
        if project_update.url:
            with Session(engine) as session:
                project = session.get(Project, id)
                project.url = project_update.url
                project.updated_at = generate_time_stamps()
                session.commit()
        
        return {"message": "Project Updated Successfully"}
    
    def get_all_project_updates():
        with Session(engine) as session:
            updates = session.exec(select(Project).where(Project.is_approved == False and Project.is_rejected == False)).all()
        return updates