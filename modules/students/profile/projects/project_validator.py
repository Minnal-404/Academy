
from utils.validator import Validator
from .project_models import ProjectDAO
from utils.imports import UUID, HTTPException, status
from ....users.user_validator import UserValidator
from .project_schemas import ProjectUpdate





class ProjectValidator():
    def validate_project_id(id: UUID):        
        is_id = ProjectDAO.get_project_by_id(id)
        
        if not is_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project Not Found")
            
    def validate_project_create(id: UUID, projects):
        
        UserValidator.validate_user_id(id)
            
        
        if not projects or len(projects) == 1 and not projects[0].title and not projects[0].url and not projects[0].description:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Project Feild Required")
        
        
        for project in projects:
            
            if not project.title:    
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title Is Required")
                
            ProjectValidator.validate_project_title(project.title)

            if not project.url:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Url Is Required")
                
            Validator.validate_url(project.url)
            
            if not project.description:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Description Is Required")
            
            ProjectValidator.validate_project_description(project.description)
    
    def validate_project_update(id: UUID, project_update: ProjectUpdate):
        
        ProjectValidator.validate_project_id(id)
        project = ProjectDAO.get_project_by_id(id)

        
        if not project_update.title and not project_update.url and not project_update.description:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Body Is Required")
        
        if project_update.title:
            ProjectValidator.validate_project_title(project_update.title)
            if project.title == project_update.title:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title Already Updated")
        
        if project_update.description:
            ProjectValidator.validate_project_description(project_update.description)
            if project.description == project_update.description:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Description Already Updated")
            
        if project_update.url:
            Validator.validate_url(project_update.url)
            if project.url == project_update.url:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="URL Already Updated")
    
    def validate_project_title(title: str):
        if len(title) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title Must Contain Atleat 3 Characters")
    
        if len(title) > 50:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title Cannot Contain More Than 50 Characters")
    
    def validate_project_description(description: str):
        if len(description) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Description Must Contain Atleat 3 Characters")
    
        if len(description) > 2048:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Description Cannot Contain More Than 255 Characters")
    
    def validate_user_and_project(student_id: UUID, user_id):
        if not student_id == user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
            