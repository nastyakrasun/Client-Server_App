import chat
import jim

client_name = ''

if __name__ == '__main__':
    parser = chat.create_parser()
    namespace = parser.parse_args()

    SERV_SOCK = chat.get_server_socket(namespace.addr, namespace.port)

    SERV_ADDR = SERV_SOCK.getsockname()
    print(f'Адрес сервера: {SERV_ADDR[0]}:{SERV_ADDR[1]}')

    CLIENT_SOCK, CLIENT_ADDR = SERV_SOCK.accept()
    print(f'Адрес клиента: {CLIENT_ADDR[0]}:{CLIENT_ADDR[1]}')

    print('Соединение установлено')

    while True:
        DATA = chat.get_data(CLIENT_SOCK)

        if client_name == '':
            if DATA['action'] == 'presence' and DATA['user']['account_name'] != '':
                client_name = DATA['user']['account_name']
                jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERV_RESP[0]
                print(f'{DATA["time"]} - {DATA["user"]["account_name"]}: {DATA["user"]["status"]}')
            else:
                jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERV_RESP[1]

        if client_name != '' and DATA['action'] == 'msg':
            print(f'{DATA["time"]} - {client_name}: {DATA["message"]}')
            jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERV_RESP[0]

            if DATA["message"] == 'exit':
                jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERV_RESP[2]

        chat.send_data(CLIENT_SOCK, jim.RESPONSE)

        if jim.RESPONSE['response'] != '200':
            print('Клиент отсоединился')
            CLIENT_SOCK.close()
            break

    SERV_SOCK.close()
