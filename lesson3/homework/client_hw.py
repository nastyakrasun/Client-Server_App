import chat
import jim

if __name__ == '__main__':
    CLIENT_NAME = input('Введите имя клиента: ')

    parser = chat.create_parser()
    namespace = parser.parse_args()

    CLIENT_SOCK = chat.get_client_socket(namespace.addr, namespace.port)

    SERV_ADDR = CLIENT_SOCK.getpeername()
    print(f'Подключение к серверу: {SERV_ADDR[0]}:{SERV_ADDR[1]}')

    jim.PRESENCE['user']['account_name'] = CLIENT_NAME
    chat.send_data(CLIENT_SOCK, jim.PRESENCE)

    while True:
        DATA = chat.get_data(CLIENT_SOCK)

        if DATA['response'] != '200':
            break

        MSG = input('Введите сообщение ("exit" для выхода): ')
        jim.MESSAGE['message'] = MSG
        chat.send_data(CLIENT_SOCK, jim.MESSAGE)

    CLIENT_SOCK.close()
