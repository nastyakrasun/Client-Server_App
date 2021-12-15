"""
Служебный скрипт запуска/остановки серверного и нескольких клиентских приложений
на отправку/приём сообщений (о текущем времени)
"""

from subprocess import Popen, CREATE_NEW_CONSOLE


P_LIST = []

while True:
    USER = input("Запустить 3 клиентов (s) / Закрыть клиентов (x) / Выйти (q) ")

    if USER == 'q':
        break

    elif USER == 's':
        P_LIST.append(Popen('python time_server_select.py', creationflags=CREATE_NEW_CONSOLE))
        for _ in range(3):

            P_LIST.append(Popen('python time_client_random.py', creationflags=CREATE_NEW_CONSOLE))

        print('Запущено 3 клиента')
    elif USER == 'x':
        for p in P_LIST:
            p.kill()
        P_LIST.clear()
