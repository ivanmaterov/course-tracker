import os
from typing import NoReturn

import psycopg2
import zmq
from custom_types import Data

# SQL to insert or update data for `Course` table
INSERT_TO_COURSES_SQL = """
INSERT INTO
    course (direction, value)
VALUES (%s, %s)
ON CONFLICT ON CONSTRAINT course_direction_key
DO NOTHING;
"""


def insert_to_database(data: Data) -> None:
    with psycopg2.connect(**CONNECTION_PARAMS) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                INSERT_TO_COURSES_SQL,
                (data['direction'], data['value']),
            )


def start(addr: str) -> NoReturn:
    """Start receiver app.

    This app receives data from socket and writes it to a database.

    """
    context = zmq.Context()

    receiver = context.socket(zmq.PULL)
    receiver.bind(addr)

    while True:
        print('Ready to receive task')
        data = receiver.recv_json()
        insert_to_database(data)


if __name__ == '__main__':
    POSTGRES_SERVER = os.environ.get('POSTGRES_SERVER', 'postgres')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'manager')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'manager')

    CONNECTION_PARAMS = {
        'host': POSTGRES_SERVER,
        'database': POSTGRES_DB,
        'user': POSTGRES_USER,
        'password': POSTGRES_PASSWORD,
    }

    RECEIVER_ADDR = os.environ.get('RECEIVER_ADDR', 'tcp://*:5558')

    print('Run receiver')
    start(addr=RECEIVER_ADDR)
