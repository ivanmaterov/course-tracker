from pydantic import BaseModel


class CourseBase(BaseModel):
    direction: str | None = None
    value: float | None = None


class CourseToCreate(CourseBase):
    direction: str


class CourseToUpdate(CourseToCreate):
    pass
