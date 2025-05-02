

from utils.imports import BaseModel, UUID, List, Optional



class ProjectSchema(BaseModel):
    title: str
    description: str
    url: str

class ProjectResponse(BaseModel):
    id: UUID
    title: str
    description: str
    url: str
    is_approved: bool
    is_rejected: bool
    message: Optional[str] = None

class ProjectList( BaseModel):
    projects: List[ProjectSchema]

class ProjectUpdate(BaseModel):
    title: str = None
    description: str = None
    url: str = None