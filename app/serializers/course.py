from pydantic import BaseModel


class Course(BaseModel):
    direction: str | None = None
    value: float | None = None


class CourseToCreate(Course):
    direction: str


class CourseToUpdate(Course):
    pass


# class CourseInBDBase(CourseBase):
#     id: int
#     direction: str
#     value: float

#     class Config:
#         from_attributes = True


# # Properties to return to client
# class Course(CourseInBDBase):
#     pass
