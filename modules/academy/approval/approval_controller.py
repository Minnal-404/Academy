
from utils.imports import APIRouter, UUID, EmailStr

from utils.auth import authenticate, Request
from utils.validator import Validator
from .approval_services import ApprovalServices
from .approval_schemas import Reject, RejectLanguage



approval_router =  APIRouter(
    prefix="/approvals",
    tags=["approvals"]
)

@approval_router.put("/approve_project/")
def approve_project(req: Request, id: UUID):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return ApprovalServices.approve_project(id)

@approval_router.put("/reject_project/")
def reject_project(req: Request, reject: Reject):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return ApprovalServices.reject_project(reject)

@approval_router.put("/approve_english/")
def approve_english(req: Request, id: UUID):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return ApprovalServices.approve_english(id)

@approval_router.put("/reject_english/")
def reject_english(req: Request, reject: Reject):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return ApprovalServices.reject_english(reject)

@approval_router.put("/approve_language/")
def approve_language(req: Request, email: EmailStr):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    return ApprovalServices.approve_language(email)

@approval_router.put("/reject_language/")
def reject_language(req: Request, reject: RejectLanguage):
    user = authenticate(req)
    Validator.validate_roles(user.role, "academy")
    print(reject)
    return ApprovalServices.reject_language(reject)
