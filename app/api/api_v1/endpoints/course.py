from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import serializers
from app.db import crud

from ... import dependencies

router = APIRouter()


@router.get('/courses')
def list_courses(
    db: Session = Depends(dependencies.get_db),
) -> list[serializers.Course]:
    return crud.course_crud.get_multi(db)
