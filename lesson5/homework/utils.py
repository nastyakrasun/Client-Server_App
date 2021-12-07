"""Утилиты"""

import json
import argparse
import socket

from variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_PACKAGE_LENGTH, ENCODING, MAX_CONNECTIONS


def get_server_socket(addr, port):
    '''
    вывод сокета сервера
    принимает адрес и порт, выдаёт сокет
    :param addr, port:
    :return:
    '''
    SERV_SOCK = socket.socket()
    SERV_SOCK.bind((addr, port))
    SERV_SOCK.listen(MAX_CONNECTIONS)
    return SERV_SOCK


def get_client_socket(addr, port):
    '''
    вывод сокета клиента
    принимает адрес и порт, выдаёт сокет
    :param addr:
    :param port:
    :return:
    '''
    CLIENT_SOCK = socket.socket()
    CLIENT_SOCK.connect((addr, port))
    return CLIENT_SOCK


def send_data(recipient, data):
    '''
    отправка данных
    :param recipient:
    :param data:
    :return:
    '''
    recipient.send(json.dumps(data).encode(ENCODING))


def get_data(sender):
    '''
    получение данных
    :param sender:
    :return:
    '''
    return json.loads(sender.recv(MAX_PACKAGE_LENGTH).decode(ENCODING))


def create_parser():
    parser = argparse.ArgumentParser(
        description='обмен сообщениями в формате JSON'
    )

    parser_group = parser.add_argument_group(title='Parameters')
    parser_group.add_argument('-a', '--addr', default=DEFAULT_IP_ADDRESS, help='IP address')
    parser_group.add_argument('-p', '--port', type=int, default=DEFAULT_PORT, help='TCP port')

    return parser
