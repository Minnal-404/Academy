
from fastapi import FastAPI
from contextlib import asynccontextmanager
from utils.database import create_db_and_table
from modules.students.profile.profile_contoller import profile_router
from modules.students.profile.projects.project_controller import project_router
from modules.students.profile.english.english_controller import english_router
from modules.users.user_controller import user_router, auth_router
from modules.academy.approval.approval_controller import approval_router
from modules.company.likes.like_controller import like_router
from fastapi.middleware.cors import CORSMiddleware
from modules.company.filter.filter_controller import filter_router
from modules.academy.language_list.language_list_controller import language_list_router
from modules.students.profile.language.language_controller import language_router







@asynccontextmanager
async def lifespan(app):
    create_db_and_table()
    yield

app = FastAPI(title="title", lifespan=lifespan)


app.include_router(profile_router)
app.include_router(project_router)
app.include_router(english_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(approval_router)
app.include_router(like_router)
app.include_router(filter_router)
app.include_router(language_list_router)
app.include_router(language_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)