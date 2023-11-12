from ...serializers.course import CourseToCreate, CourseToUpdate
from ..models.course import Course
from .base import CRUDBase


class CRUDCourse(CRUDBase[Course, CourseToCreate, CourseToUpdate]):
    """CRUD operations for `Course` model."""


course_crud = CRUDCourse(Course)
