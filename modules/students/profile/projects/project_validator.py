
from utils.validator import Validator
from .project_models import ProjectDAO
from utils.imports import UUID, HTTPException, status
from ...users.student_user_validator import StudentUserValidator
from .project_schemas import ProjectUpdate





class ProjectValidator():
    def validate_project_id(id: str):
        Validator.validate_uuid(id)
        
        is_id = ProjectDAO.get_project_by_id(UUID(id))
        
        if not is_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project Not Found")
            
    def validate_project_create(id: str, projects):
        
        StudentUserValidator.validate_student_user_id(id)
            
        
        if not projects or len(projects) == 1 and not projects[0].title and not projects[0].url:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Project Feild Required")
        
        
        for project in projects:
            
            if not project.title:    
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title Is Required")
                
            ProjectValidator.validate_project_title(project.title)

            if not project.url:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Url Is Required")
                
            Validator.validate_url(project.url)
            
    
    def validate_project_update(id: str, project_update: ProjectUpdate):
        
        ProjectValidator.validate_project_id(id)
        
        if not project_update.title and not project_update.url:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Body Is Required")
        
        if project_update.title:
            ProjectValidator.validate_project_title(project_update.title)
            
        if project_update.url:
            Validator.validate_url(project_update.url)
    
    def validate_project_title(title: str):
        if len(title) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title Must Contain Atleat 3 Characters")
    
        if len(title) > 50:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title Cannot Contain More Than 50 Characters")