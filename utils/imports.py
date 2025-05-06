
from fastapi import HTTPException, status, APIRouter, Request, Response, Query
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from uuid import UUID, uuid4
import re
from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.orm import selectinload
from pydantic.config import ConfigDict



def generate_time_stamps():
    return datetime.now(timezone.utc)