
from utils.imports import APIRouter
from .project_services import ProjectServices
from .project_schemas import ProjectList, ProjectUpdate



project_router =  APIRouter(
    prefix="/project",
    tags=["project"]
)

@project_router.post("/create_project/")
def create_project(id: str, projects_create: ProjectList):
    response = ProjectServices.create_project(id, projects_create.projects)
    return {
        "message": "Project Has Been Sent For Approval",
        "projects": response
    }

@project_router.delete("/delete_project/")
def delete_project(id: str):
    return ProjectServices.delete_project(id)

@project_router.get("/get_projects/")
def get_projects():
    return ProjectServices.get_projects()

@project_router.put("/update_project/")
def update_project(id: str, project_update: ProjectUpdate):
    return ProjectServices.update_project(id, project_update)