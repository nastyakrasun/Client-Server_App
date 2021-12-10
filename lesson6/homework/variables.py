"""Константы"""
import logging
from datetime import datetime

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
# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG

# Прококол JIM основные ключи:
ACCOUNT_NAME = 'account_name'
ACTION = 'action'
TIME = datetime.now().replace(microsecond=0).isoformat(sep=' ')
USER = 'user'
RESPONSE = 'response'


# Прочие ключи, используемые в протоколе
ERROR = 'error'

MESSAGE = {
    "action": "msg",
    "time": str(TIME),
    "to": None,
    "message": None
}

PRESENCE = {
    "action": "presence",
    "time": str(TIME),
    "type": "status",
    "user": {
        "account_name": '',
        "status": "осуществляется передача сообщений"
    }
}

CLIENT_RESP = {
    "response": 'Соединение установлено',
    "time": str(TIME),
    "alert": None,
    "from": 'Server',
    "contacts": None
}

SERV_RESP = (
    ('200', 'OK'),
    ('401', 'Не авторизован'),
    ('404', 'Not found')
)
