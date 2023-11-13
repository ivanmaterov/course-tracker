from typing import TypedDict

type COIN_VALUE = float


class Data(TypedDict):
    direction: str
    value: COIN_VALUE
