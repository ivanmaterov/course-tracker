"""Initialize database session."""


from settings.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .utils import init_db

engine = create_engine(
    url=str(settings.SQLALCHEMY_DATABASE_URI),
    # checkout connection for liveness
    pool_pre_ping=True,
)
init_db(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
