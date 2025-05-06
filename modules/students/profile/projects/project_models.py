
from utils.database import SQLModel, Field, Session, select, engine, Relationship
from utils.imports import UUID, uuid4, datetime, generate_time_stamps, Optional
from .project_schemas import ProjectUpdate
from ....users.user_models import User




class ProjectBase(SQLModel):
    student_id: UUID = Field(foreign_key="user.id")
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=2048)
    url: str = Field(min_length=10, max_length=2048)

class Project(ProjectBase, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default_factory=generate_time_stamps)
    updated_at: datetime = Field(default_factory=generate_time_stamps)
    is_approved: bool = Field(default=False)
    is_rejected: bool = Field(default=False)
    
    user: Optional[User] = Relationship(back_populates="projects")

    
    
    
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
    
    def get_approved_projects_by_student_id(id: UUID):
        with Session(engine) as session:
            projects = session.exec(select(Project).where((Project.student_id == id) & (Project.is_approved == True) & (Project.is_rejected == False))).all()
        return projects
    # def get_approved_projects_by_student_id(id: UUID):
    #     with Session(engine) as session:
    #         projects = session.exec(select(Project).where((Project.student_id == id) & (Project.is_approved == True) & (Project.is_rejected == False))).all()
    #     return projects

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
                project.is_rejected = False
                project.is_approved = False
                session.commit()
        
        if project_update.url:
            with Session(engine) as session:
                project = session.get(Project, id)
                project.url = project_update.url
                project.updated_at = generate_time_stamps()
                project.is_rejected = False
                project.is_approved = False
                session.commit()
        
        return {"message": "Project Updated Successfully"}
    
    def get_all_project_updates_users():
        with Session(engine) as session:
            users = session.exec(select(Project.student_id).distinct().where((Project.is_approved ==False) & (Project.is_rejected == False))).all()
        return users
    
    def get_all_updates_by_student_id(id: UUID):
        with Session(engine) as session:
            projects = session.exec(select(Project).where((Project.student_id == id) & (Project.is_approved ==False) & (Project.is_rejected == False))).all()
        return projects
    
    def approve_project(id: UUID):
        with Session(engine) as session:
            project = session.get(Project, id)
            project.is_approved = True
            project.is_rejected = False
            session.commit()
        return {"message": "Project Approved"}
        
    def reject_project(id: UUID):
        with Session(engine) as session:
            project = session.get(Project, id)
            project.is_approved = False
            project.is_rejected = True
            session.commit()
        return