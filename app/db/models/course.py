from sqlalchemy import Column, Float, String

from .base_class import BaseModel


class Course(BaseModel):
    """Model stores current course for directions.

    Example:
        direction: BTCUSD
        value: 4.000002

    """
    direction = Column(
        String(length=32),
        primary_key=True,
        index=True,
    )
    value = Column(
        Float(precision=6),
        default=.0,
    )
