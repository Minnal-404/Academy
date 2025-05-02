
from utils.imports import APIRouter, UUID
from .project_services import ProjectServices
from .project_schemas import ProjectList, ProjectUpdate
from utils.auth import Request, authenticate
from utils.validator import Validator




project_router =  APIRouter(
    prefix="/project",
    tags=["project"]
)

@project_router.post("/create_project/")
def create_project(req: Request, projects_create: ProjectList):
    user = authenticate(req)
    Validator.validate_roles(user.role, "student")
    response = ProjectServices.create_project(user.id, projects_create.projects)
    return {
        "message": "Project Has Been Sent For Approval",
        "projects": response
    }

@project_router.delete("/delete_project/")
def delete_project( req: Request, project_id: UUID):
    user = authenticate(req) 
    Validator.validate_roles(user.role, "student")
    return ProjectServices.delete_project(user.id, project_id)

# @project_router.get("/get_projects/")
# def get_projects():
#     return ProjectServices.get_projects()

@project_router.put("/update_project/")
def update_project(project_id: UUID, req: Request, project_update: ProjectUpdate):
    user = authenticate(req) 
    Validator.validate_roles(user.role, "student")
    return ProjectServices.update_project(user.id, project_id, project_update)

@project_router.get('/get_all_project_updates/')
def get_all_project_updates(req: Request):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return ProjectServices.get_all_project_updates()