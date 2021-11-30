import argparse
import socket
import json

ADDRESS = 'localhost'
PORT = 8000
CONNECTIONS = 5


def get_server_socket(addr, port):
    SERV_SOCK = socket.socket()
    SERV_SOCK.bind((addr, port))
    SERV_SOCK.listen(CONNECTIONS)
    return SERV_SOCK


def get_client_socket(addr, port):
    CLIENT_SOCK = socket.socket()
    CLIENT_SOCK.connect((addr, port))
    return CLIENT_SOCK


def send_data(recipient, data):
    recipient.send(json.dumps(data).encode('utf-8'))


def get_data(sender):
    return json.loads(sender.recv(1024).decode("utf-8"))


def create_parser():
    parser = argparse.ArgumentParser(
        description='обмен сообщениями в формате JSON'
    )

    parser_group = parser.add_argument_group(title='Parameters')
    parser_group.add_argument('-a', '--addr', default=ADDRESS, help='IP address')
    parser_group.add_argument('-p', '--port', type=int, default=PORT, help='TCP port')

    return parser
