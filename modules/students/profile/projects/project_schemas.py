

from utils.imports import BaseModel, UUID, List



class ProjectSchema(BaseModel):
    title: str
    url: str

class ProjectResponse(BaseModel):
    id: UUID
    title: str
    url: str

class ProjectList( BaseModel):
    projects: List[ProjectSchema]

class ProjectUpdate(BaseModel):
    title: str = None
    url: str = None