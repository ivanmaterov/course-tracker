from sqlalchemy.orm import Session

from ...serializers.course import CourseToCreate, CourseToUpdate
from ..models.course import Course
from .base import CRUDBase


class CRUDCourse(CRUDBase[Course, CourseToCreate, CourseToUpdate]):
    """CRUD operations for `Course` model."""

    def get_multi(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
        directions: list[str] | None = None,
    ) -> list[Course]:
        """Change default implementation to filter by directions."""
        if directions:
            return (
                db.query(self.model)
                .filter(Course.direction.in_(directions))
                .offset(skip)
                .limit(limit)
                .all()
            )
        return super().get_multi(db, skip=skip, limit=limit)


course_crud = CRUDCourse(Course)
