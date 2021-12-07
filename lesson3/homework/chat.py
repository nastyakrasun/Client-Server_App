import argparse
import socket
import json

# Порт поумолчанию для сетевого ваимодействия
DEFAULT_PORT = 8000
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING = 'utf-8'

# Прококол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'


def get_server_socket(addr, port):
    SERV_SOCK = socket.socket()
    SERV_SOCK.bind((addr, port))
    SERV_SOCK.listen(MAX_CONNECTIONS)
    return SERV_SOCK


def get_client_socket(addr, port):
    CLIENT_SOCK = socket.socket()
    CLIENT_SOCK.connect((addr, port))
    return CLIENT_SOCK


def send_data(recipient, data):
    recipient.send(json.dumps(data).encode(ENCODING))


def get_data(sender):
    return json.loads(sender.recv(MAX_PACKAGE_LENGTH).decode(ENCODING))


def create_parser():
    parser = argparse.ArgumentParser(
        description='обмен сообщениями в формате JSON'
    )

    parser_group = parser.add_argument_group(title='Parameters')
    parser_group.add_argument('-a', '--addr', default=DEFAULT_IP_ADDRESS, help='IP address')
    parser_group.add_argument('-p', '--port', type=int, default=DEFAULT_PORT, help='TCP port')

    return parser
