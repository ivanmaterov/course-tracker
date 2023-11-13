from app.db import base


def init_db(engine) -> None:
    """Create database tables."""
    base.BaseModel.metadata.create_all(bind=engine)
