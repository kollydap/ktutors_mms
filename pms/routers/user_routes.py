from fastapi import APIRouter, Body

from typing import Annotated
import pms.service.user_service as user_service
from uuid import UUID


AnProfilePicture = Annotated[UUID, Body(embed=True)]
api_router = APIRouter(tags=["user"], prefix="/api/v1/profile")

