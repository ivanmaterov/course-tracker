from typing import NamedTuple, TypedDict

type Seconds = int


class Pair(NamedTuple):
    coin: str
    currency: str


class Payload(TypedDict):
    """Payload to send queue."""
    pair: Pair
