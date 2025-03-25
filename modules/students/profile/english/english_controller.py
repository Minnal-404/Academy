
from utils.imports import APIRouter
from .english_services import EnglishServices
from .english_schemas import EnglishUpdate



english_router =  APIRouter(
    prefix="/english",
    tags=["english"]
)



@english_router.delete("/delete_english/")
def delete_english(id: str):
    return EnglishServices.delete_english(id)

@english_router.get("/get_all_english/")
def get_all_english():
    return EnglishServices.get_all_english()

@english_router.put("/update_english/")
def update_english(id: str, english_update: EnglishUpdate):
    return EnglishServices.update_english(id, english_update)