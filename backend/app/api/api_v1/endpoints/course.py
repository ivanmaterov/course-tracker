from typing import Annotated

from app import serializers
from app.db import crud
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ... import dependencies

router = APIRouter()


@router.get('/courses')
def list_courses(
    db: Session = Depends(dependencies.get_db),
    directions: Annotated[list[str] | None, Query()] = None,
) -> list[serializers.Course]:
    return crud.course_crud.get_multi(db, directions=directions)
