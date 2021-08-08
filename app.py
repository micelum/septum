import os
import sys
import logging
import json
import socket

from dotenv import load_dotenv
from nameko.rpc import rpc

load_dotenv()
logging.basicConfig(stream=sys.stdout, level=os.environ.get('LOG_LEVEL'))  # TODO Add normal logger


class Septum:
    name = "septum"

    def __init__(self):
        pass  # TODO Add service who manage other service configs

    @rpc  # TODO Add config processing
    def get_connection_info(self):  # TODO Find another way
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.connect(('10.255.255.255', 1))
            result = sock.getsockname()[0]
        except Exception:
            result = '127.0.0.1'
        finally:
            s.close()
        return result

