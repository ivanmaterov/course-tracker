from app import factories
from app.db.crud import course_crud
from app.db.models import Course
from app.serializers import course as course_serializers
from sqlalchemy.orm import Session


def test_get_course(db: Session, course: Course) -> None:
    """Test `get` method for `Course` model."""
    course_from_db = course_crud.get(db, id=course.id)

    assert course_from_db.direction == course.direction
    assert course_from_db.value == course.value


def test_delete_course(db: Session, course: Course) -> None:
    """Test `remove` method for `Course` model."""
    course_crud.remove(db, id=course.id)
    course_from_db = course_crud.get(db, id=course.id)

    assert course_from_db is None


def test_update_course(db: Session, course: Course) -> None:
    """Test `update` method for `Course` model."""
    course_stub = factories.CourseFactory.stub()

    updated_course = course_crud.update(
        db,
        db_obj=course,
        obj_in=course_serializers.CourseToUpdate(
            direction=course_stub.direction,
            value=course_stub.value,
        ),
    )

    assert updated_course.id == course.id
    assert updated_course.direction == course.direction
    assert updated_course.value == course.value
