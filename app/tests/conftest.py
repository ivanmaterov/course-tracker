from typing import Any, Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists

from app.db.models import BaseModel, Course
from app.factories import CourseFactory, ScopedFactorySession
from settings.config import settings


def _get_or_create_engine(db_uri: str) -> Engine:
    """Get or create engine for testing database."""
    engine = create_engine(url=db_uri)
    if not database_exists(engine.url):
        create_database(engine.url)

    return engine


@pytest.fixture(scope='session')
def testing_db_engine() -> Generator[Engine, Any, None]:
    """Get testing db engine.

    This function get db engine and creates database schema.
    After test session it drops database schema.

    """
    testing_db_uri = str(settings.SQLALCHEMY_TESTING_DATABASE_URI)

    # Use exist database or create a new one
    engine = _get_or_create_engine(db_uri=testing_db_uri)

    # Create database schema
    BaseModel.metadata.create_all(engine)
    yield engine
    BaseModel.metadata.drop_all(engine)


@pytest.fixture(autouse=True)
def configure_session_factory(testing_db_engine: Engine) -> None:
    """Set up db engine for testing session."""
    ScopedFactorySession.configure(bind=testing_db_engine)


@pytest.fixture
def db(testing_db_engine: Engine) -> Session:
    """Testing database session.

    Creates a fresh sqlalchemy session for each test that operates in a
    transaction. The transaction is rolled back at the end of each test ensuring
    a clean state.

    """
    connection = testing_db_engine.connect()
    transaction = connection.begin()
    session = ScopedFactorySession()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def course() -> Course:
    """Get `Course` instance."""
    return CourseFactory()
