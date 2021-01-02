import time
import os
import sys
import logging
import zmq

HOST = '127.0.0.1'
PORT = '5556'

logging.basicConfig(filename='subscriber.log', level=logging.INFO)

class ZClient(object):
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self._context = zmq.Context()
        self._subscriber = self._context.socket(zmq.SUB)

    def receive_message(self):
        url = f'tcp://{self.host}:{self.port}'
        self._subscriber.connect(url)
        self._subscriber.setsockopt(zmq.SUBSCRIBE, b"")

        while True:
            print(f'listening on tcp://{self.host}:{self.port}')
            message = self._subscriber.recv()
            print(message)
            logging.info(f'{message} - {time.strftime("%Y-%m-%d %H:%M")}')

if __name__ == '__main__':
    zs = ZClient()
    zs.receive_message()