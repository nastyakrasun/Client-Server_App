"""
Задача:
ПЕРЕД выполнением и ПОСЛЕ выполнения определёных функций
печатать заданный текст (одинаковый для всех функций)
-------------------------------------------------------
Вариант с функцией обёртки
"""


def decorator(func):
    def wrap():
        print('Операция ДО выполнения функции some_func()')
        print('-' * 50)
        func()
        print('-' * 50)
        print('Операция ПОСЛЕ выполнения функции some_func()')
    return wrap


# @decorator  # добавляет новую функциональность? закомментили - получили старую функцию (без доп функционала)
def some_func():
    """Какая-то логика"""
    print('Выполнение самой функции some_func()')


decorator(some_func)
# Теперь этот вызов уже не работает

# ==========================================
# Но зато заработал вызов, который не работал в предыдущем примере!

func_with_decorator = decorator(some_func)
print('Тип функции func_with_decorator : ', type(func_with_decorator))
func_with_decorator()

# ==========================================
# Для этого случая в Python имеется "синтаксический сахар": @decorator
