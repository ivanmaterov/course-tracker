"""Initialize database session."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings.config import settings

engine = create_engine(
    url=str(settings.SQLALCHEMY_DATABASE_URI),
    # checkout connection for liveness
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
