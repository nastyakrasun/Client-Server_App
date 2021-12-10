"""Простейший декоратор-функция"""

import time
import requests


def decorator(func):
    """Сам декоратор"""
    def wrapper():
        """Обертка"""
        start = time.time()   # до начала выполнения функции узнаём абсолбтное время в секундах
        f = func()
        end = time.time()  # после вып-ия ф-ии узнаём абсолютное время окончания
        print(f'Время выполнения исходной ф-ции: {round(end-start, 2)} секунд')  # считаем разницу
        return f
    return wrapper


@decorator
def get_wp():
    """
    получаем ответ сервера
    200 - запрос успешно обработан
    """
    print('Выполняем расчет')
    res = requests.get('https://google.com')
    return res


print(get_wp())

# импортируя декоратор мы можем узнать время исполнения любой функции
