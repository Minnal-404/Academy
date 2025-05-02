
from utils.imports import UUID
from .project_models import ProjectDAO, Project
from .project_schemas import ProjectResponse, ProjectUpdate
from utils.validator import Validator
from .project_validator import ProjectValidator
from ....users.user_models import UserDAO
from ....users.user_schemas import UserRes
from ....academy.approval.approval_model import RejectionDAO


class ProjectServices():
    def create_project(id: UUID, projects):
        ProjectValidator.validate_project_create(id, projects)
        response = []
        for project in projects:
            
            new_project = Project(
                student_id=id, 
                **project.model_dump()  
            )
            result = ProjectDAO.create_project(new_project)
            response.append(ProjectResponse(**result.model_dump()))
        return response
    
    def get_all_projects_by_student_id(id: UUID):
        
        result = ProjectDAO.get_all_projects_by_student_id(id)
        response = []
        for res in result:
            if res.is_rejected:
                reject = RejectionDAO.get_rejection(res.id)
                project_data = {**res.model_dump(), **reject.model_dump()}
                response.append(ProjectResponse(**project_data))
            else:
                response.append(ProjectResponse(**res.model_dump()))

        return response
    
    def get_approved_projects_by_student_id(id: UUID):
        
        result = ProjectDAO.get_approved_projects_by_student_id(id)
        
        return [ProjectResponse(**res.model_dump()) for res in result]
            
    def delete_project(user_id: UUID, project_id: UUID):
        ProjectValidator.validate_project_id(project_id)
        project_to_delete = ProjectDAO.get_project_by_id(project_id)
        ProjectValidator.validate_user_and_project(project_to_delete.student_id, user_id)
        return ProjectDAO.delete_project(project_to_delete)
    
    def get_projects():
        return ProjectDAO.get_projects()
    
    def update_project(user_id: UUID, project_id: UUID, project_update: ProjectUpdate):
        ProjectValidator.validate_project_update(project_id, project_update)
        
        try:
            rejection_to_delete = RejectionDAO.get_rejection(project_id)
            RejectionDAO.delete_rejection(rejection_to_delete)
        except:
            pass
        project_to_update = ProjectDAO.get_project_by_id(project_id)
        ProjectValidator.validate_user_and_project(project_to_update.student_id, user_id)
        return ProjectDAO.update_project(project_id, project_update)
    
    def delete_all_projects(id: UUID):

        
        projects = ProjectDAO.get_all_projects_by_student_id(id)
        for project in projects:
            ProjectDAO.delete_project(project)
        return True
    
    def get_all_project_updates():
        ids = ProjectDAO.get_all_project_updates_users()
        projects = []
        for id in ids:
            user = UserDAO.get_user_by_id(id)
            user = UserRes(**user.model_dump())
            project = ProjectDAO.get_all_updates_by_student_id(id)
            res = []
            for pro in project:
                
                proj = ProjectResponse(**pro.model_dump())
                res.append(proj)
            projects.append({
                "user": user,
                "projects": res
            })
        return projects
    
    