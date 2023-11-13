from app.db.models import Course
from app.factories.course import CourseFactory
from fastapi.testclient import TestClient
from settings.config import settings


def test_get_courses(client: TestClient, course: Course) -> None:
    """Test `/courses` endpoint."""
    response = client.get(f"{settings.API_V1_STR}/courses/")
    assert response.status_code == 200

    data = response.json()
    assert data[0]['direction'] == course.direction


def test_get_courses_with_query_param(
    client: TestClient,
    course: Course,
) -> None:
    """Test `/courses` endpoint with `directions` query param."""
    extra_course = course  # noqa
    courses = CourseFactory.create_batch(size=2)

    response = client.get(
        f"{settings.API_V1_STR}/courses/",
        params={'directions': [course.direction for course in courses]},
    )
    assert response.status_code == 200

    data = response.json()
    assert len(data) == len(courses)
