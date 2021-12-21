""""вариант запуска чисто вычислений функции без потоков
объём вычислений делится на 2 этапа"""

import time
from threading import Thread


def create_list(min_index, max_index):
    """"Функция, которая может быть запущена в потоке"""

    amount = 0
    for x in range(min_index, max_index):
        amount += (x * x) ** x


print(f"Время запуска основной программы: {time.ctime()}")
time1 = time.time()
create_list(0, 5000)
create_list(5000, 10000)
time2 = time.time()
print(f'total = {time2 - time1:.2f}')
