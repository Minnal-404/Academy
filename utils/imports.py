
from fastapi import HTTPException, status, APIRouter, Request
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from uuid import UUID, uuid4
import re
from datetime import datetime, timezone
from typing import List
