import os
from typing import NoReturn

import zmq
from custom_types import CoinGeckoRequest, Data, Pair, Payload
from pycoingecko import CoinGeckoAPI

COINGECKO_COINNAME_TO_ID_MAPPING = {
    'USD': 'USD',
    'RUB': 'RUB',

    # Got IDs from https://api.coingecko.com/api/v3/coins/list
    'BTC': 'BITCOIN',
    'ETH': 'ETHEREUM',
    'USDTTRC': 'TETHER',
    'USDTERC': 'TETHER-USD-WORMHOLE-FROM-ETHEREUM',
}


def prepare_payload_from_coingecko_response(
    response: dict,
    pair: Pair,
) -> Payload:
    """Prepare payload from CoinGecko.

    Response has the following structure:
    {
        'coin_name': {'currency_name': float value}
    }

    Example:
        {
            'bitcoin': {'rub': 3413396}
        }

    """
    coin_id = COINGECKO_COINNAME_TO_ID_MAPPING[pair.coin.upper()]
    currency_id = COINGECKO_COINNAME_TO_ID_MAPPING[pair.currency.upper()]
    return Payload(
        direction=f'{pair.coin}{pair.currency}',
        value=response[coin_id.lower()][currency_id.lower()],
    )


def prepare_request_to_coingecko(pair: Pair) -> CoinGeckoRequest:
    return CoinGeckoRequest(
        ids=COINGECKO_COINNAME_TO_ID_MAPPING[pair.coin.upper()],
        vs_currencies=COINGECKO_COINNAME_TO_ID_MAPPING[pair.currency.upper()],
    )


def start(scheduler_addr: str, receiver_addr: str) -> NoReturn:
    """Start worker app.

    Get tasks from scheduler and send data to receiver.

    """
    coingecko_client = CoinGeckoAPI()
    context = zmq.Context()

    # Socket to receive messages on
    scheduler = context.socket(zmq.PULL)
    scheduler.connect(scheduler_addr)

    # Socket to send messages to
    receiver = context.socket(zmq.PUSH)
    receiver.connect(receiver_addr)

    while True:
        print('Ready to get task')
        data: Data = scheduler.recv_json()
        pair = Pair(*data['pair'])

        request_data = prepare_request_to_coingecko(pair)
        print(f'Make request: {request_data}')
        response = coingecko_client.get_price(**request_data)
        print(f'Get response: {response}')

        payload = prepare_payload_from_coingecko_response(
            response=response,
            pair=pair,
        )
        print(f'Send payload: {payload}')
        receiver.send_json(payload)


if __name__ == '__main__':
    RECEIVER_ADDR = os.environ.get('RECEIVER_ADDR', 'tcp://localhost:5558')
    SCHEDULER_ADDR = os.environ.get('SCHEDULER_ADDR', 'tcp://localhost:5559')

    print('Run worker')
    start(receiver_addr=RECEIVER_ADDR, scheduler_addr=SCHEDULER_ADDR)
