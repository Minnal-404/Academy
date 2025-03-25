
from utils.imports import UUID
from .project_models import ProjectDAO, Project
from .project_schemas import ProjectResponse, ProjectUpdate
from utils.validator import Validator
from .project_validator import ProjectValidator



class ProjectServices():
    def create_project(id: str, projects):
        ProjectValidator.validate_project_create(id, projects)
        student_id = UUID(id)
        response = []
        for project in projects:
            
            new_project = Project(
                student_id=student_id, 
                **project.model_dump()  
            )
            result = ProjectDAO.create_project(new_project)
            response.append(ProjectResponse(**result.model_dump()))
        return response
    
    def get_all_projects_by_student_id(id: UUID):
        
        result = ProjectDAO.get_all_projects_by_student_id(id)
        return [ProjectResponse(**res.model_dump()) for res in result]
            
    def delete_project(id: str):
        ProjectValidator.validate_project_id(id)
        project_id = UUID(id)
        project_to_delete = ProjectDAO.get_project_by_id(project_id)
        return ProjectDAO.delete_project(project_to_delete)
    
    def get_projects():
        return ProjectDAO.get_projects()
    
    def update_project(id: str, project_update: ProjectUpdate):
        ProjectValidator.validate_project_update(id, project_update)
        
        project_id = UUID(id)
        
        return ProjectDAO.update_project(project_id, project_update)
    
    def delete_all_projects(id: UUID):

        
        projects = ProjectDAO.get_all_projects_by_student_id(id)
        for project in projects:
            ProjectDAO.delete_project(project)
        return True
    
    def get_all_project_updates():
        return ProjectDAO.get_all_project_updates()