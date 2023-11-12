from sqlalchemy import Column, Float, Integer, String

from .base_class import BaseModel


class Course(BaseModel):
    """Model stores current course for directions.

    Example:
        direction: BTCUSD
        value: 4.000002

    """
    id = Column(Integer, primary_key=True, index=True)
    direction = Column(String(length=32), unique=True)
    value = Column(
        Float(precision=6),
        default=.0,
    )
