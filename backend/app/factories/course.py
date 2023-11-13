from uuid import uuid4

import factory

from ..db.models.course import Course
from .db_session import ScopedFactorySession


class CourseFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Factory for `Course` model."""
    direction = factory.LazyAttribute(lambda _: str(uuid4())[:32])
    value = factory.Faker('pyfloat', positive=True)

    class Meta:
        model = Course
        sqlalchemy_session = ScopedFactorySession
        sqlalchemy_session_persistence = 'flush'
