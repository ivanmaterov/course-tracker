from pydantic import BaseModel


class Course(BaseModel):
    direction: str | None = None
    value: float | None = None


class CourseToCreate(Course):
    direction: str


class CourseToUpdate(Course):
    pass
