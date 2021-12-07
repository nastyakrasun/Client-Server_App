"""Программа-клиент"""

import sys
import json
import socket
import time
import variables
import utils

if __name__ == '__main__':
    CLIENT_NAME = input('Введите имя клиента: ')

    parser = utils.create_parser()
    namespace = parser.parse_args()

    CLIENT_SOCK = utils.get_client_socket(namespace.addr, namespace.port)

    SERV_ADDR = CLIENT_SOCK.getpeername()
    print(f'Подключение к серверу: {SERV_ADDR[0]}:{SERV_ADDR[1]}')

    variables.PRESENCE['user']['account_name'] = CLIENT_NAME
    utils.send_data(CLIENT_SOCK, variables.PRESENCE)

    while True:
        DATA = utils.get_data(CLIENT_SOCK)

        if DATA['response'] != '200':
            break

        MSG = input('Введите сообщение ("exit" для выхода): ')
        variables.MESSAGE['message'] = MSG
        utils.send_data(CLIENT_SOCK, variables.MESSAGE)

    CLIENT_SOCK.close()

# if __name__ == '__main__':
#     main()
