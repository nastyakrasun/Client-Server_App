"""Программа сервера времени"""

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import time

SERV_SOCK = socket(AF_INET, SOCK_STREAM)
SERV_SOCK.bind(('', 8888))
SERV_SOCK.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
SERV_SOCK.listen()

try:
    while True:
        CLIENT_SOCK, ADDR = SERV_SOCK.accept()
        print(f'Получен запрос на соединение от клиента с адресом и портом: {ADDR}')
        TIMESTR = time.ctime(time.time()) + "\n"
        CLIENT_SOCK.send(TIMESTR.encode('utf-8'))
        CLIENT_SOCK.close()
finally:
    SERV_SOCK.close()
