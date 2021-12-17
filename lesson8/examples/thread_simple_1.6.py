"""Простой поток"""

import time
from threading import Thread


def clock(interval):
    """Функция, которая может быть запущена в потоке"""

    while True:
        start = time.time()
        time.sleep(interval)
        print(interval)
        end = time.time()
        print(f"Время окончания программы {interval}: {time.ctime()}")
        print('end-start =', end - start)
        # break


THR1 = Thread(target=clock, args=(2, ))
THR2 = Thread(target=clock, args=(3, ))

"""
Обычно Python-приложение не завершается, пока работает хоть один его поток. 
Но есть особые потоки, которые не мешают закрытию программы и останавливается вместе с ней. 
Их называют демонами (daemons). Проверить, является ли поток демоном, можно методом isDaemon(). 
Если является, метод вернёт истину.
"""
print(f"Время запуска основной программы: {time.ctime()}")
start = time.time()
THR1.daemon = True
# параметр daemon можно указать сразу в описании процесса
# THR1 = Thread(target=clock, args=(2, ), daemon=True)
THR2.daemon = True
THR1.start()
THR2.start()
THR1.join()
THR2.join()
end = time.time()
print(f"Время окончания основной программы: {time.ctime()}")
print('end-start =', end-start)

# первый, второй и основной потоки начинают одновременно
# все потоки завершаются после завершения основного
