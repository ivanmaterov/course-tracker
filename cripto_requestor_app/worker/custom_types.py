from typing import NamedTuple, TypedDict


class Pair(NamedTuple):
    coin: str
    currency: str


class Data(TypedDict):
    pair: Pair


type COIN_VALUE = float


class CoinGeckoRequest(TypedDict):
    ids: str
    vs_currencies: str


class Payload(TypedDict):
    direction: str
    value: COIN_VALUE
