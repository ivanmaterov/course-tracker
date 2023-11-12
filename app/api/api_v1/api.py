from fastapi import APIRouter

from .endpoints import course

api_router = APIRouter()
api_router.include_router(course.router, tags=['Course'])
