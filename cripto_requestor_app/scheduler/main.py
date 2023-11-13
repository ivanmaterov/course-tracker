import os
import time
from typing import NoReturn

import zmq
from custom_types import Pair, Payload, Seconds

PAIRS = (
    Pair('BTC', 'RUB'),
    Pair('BTC', 'USD'),
    Pair('ETH', 'RUB'),
    Pair('ETH', 'USD'),
    Pair('USDTTRC', 'RUB'),
    Pair('USDTTRC', 'USD'),
    Pair('USDTERC', 'RUB'),
    Pair('USDTERC', 'USD'),
)


def start(addr: str, delay: Seconds) -> NoReturn:
    """Start scheduler app.

    Schedule tasks for workers. Send tasks every `delay` seconds.

    """
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind(addr)

    while True:
        print('Sending tasks...')
        for pair in PAIRS:
            payload = Payload(pair=pair)
            socket.send_json(payload)
        time.sleep(delay)
        print('Tasks are sent.')


if __name__ == '__main__':
    REQUEST_DELAY: Seconds = int(os.environ.get('REQUEST_DELAY', 5))
    SCHEDULER_ADDR = os.environ.get('SCHEDULER_ADDR', 'tcp://*:5559')

    print('Run scheduler')
    start(addr=SCHEDULER_ADDR, delay=REQUEST_DELAY)
