
from utils.imports import APIRouter
from .company_user_schemas import CompanyUserCreate
from .company_user_services import CompanyUserService


company_user_router = APIRouter(
    prefix="/company_users",
    tags=["company_users"]
)

@company_user_router.post("/create_user/")
def company_create_user(company_user_create: CompanyUserCreate):
    return CompanyUserService.company_create_user(company_user_create)

@company_user_router.get("/get_user_by_email/{email}")
def get_company_user_by_email(email: str):
    return CompanyUserService.get_company_user_by_email(email)

@company_user_router.get("/get_user_by_id/{id}")
def get_company_user_by_id(id: str):
    return CompanyUserService.get_company_user_by_id(id)

@company_user_router.get("/")
def get_all_company_users():
    return CompanyUserService.get_all_company_users()

@company_user_router.delete("/delete_user/{id}")
def delete_company_user_by_id(id: str):
    return CompanyUserService.delete_company_user_by_id(id)

