
from fastapi import FastAPI
from contextlib import asynccontextmanager
from utils.database import create_db_and_table
from modules.company.users.company_user_controller import company_user_router
from modules.students.users.student_user_controller import student_user_router
from modules.students.profile.profile_contoller import profile_router
from modules.students.profile.projects.project_controller import project_router
from modules.students.profile.english.english_controller import english_router
from modules.academy.users.academy_user_controller import academy_user_router
from modules.users.user_controller import user_router


@asynccontextmanager
async def lifespan(app):
    create_db_and_table()
    yield

app = FastAPI(title="title", lifespan=lifespan)

app.include_router(student_user_router)
app.include_router(academy_user_router)
app.include_router(company_user_router)
app.include_router(profile_router)
app.include_router(project_router)
app.include_router(english_router)
app.include_router(user_router)