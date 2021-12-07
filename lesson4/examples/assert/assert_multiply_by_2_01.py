"""
Module with function multiply_by_2 and its tests
для простоты рассм умножение целых чисел
"""


def multiply_by_2(num: int) -> int or str:
    """
    Function returns integer <num> multiplied by 2.
    """

    if isinstance(num, int):  # обязательно описывается ошибка
        return 2 * num
    return 'Error!!! Argument <num> must be integer!!!'


# пример теста
# берем любое число, удовлетворяющее условию теста, создаём тестируемую функцию с этим аргументом
# и приравниваем эту функцию к правильному решению
# в случае провала решения пишем соответствующую надпись
def test_correct_multiply_positive():  # здорово если из названия тестирующей функции понятно, о чём тест
    assert multiply_by_2(2) == 4, 'Correct multiply positive is not true!'


def test_correct_multiply_negative():
    assert multiply_by_2(-2) == -4, 'Correct multiply negative is not true!'


def test_incorrect_multiply_positive():
    assert multiply_by_2(2) != 5, 'Incorrect multiply positive is not true!'


def test_incorrect_multiply_negative():
    assert multiply_by_2(-2) != -5, 'Incorrect multiply negative is not true!'


def test_correct_multiply_by_zero():
    assert multiply_by_2(0) == 0, 'Multiply by zero is not equal zero!'


# по логике нужно тестить на некорректнось умножения на 0

# программа не должна работать с другими типами данных! проверяем выполнение заявленного
def test_incorrect_multiply_by_str():
    assert multiply_by_2("str") == 'Error!!! Argument <num> must be integer!!!', \
        'Wrong answer if <num> is not integer!'


def test_incorrect_multiply_by_float():
    assert multiply_by_2(0.1) == 'Error!!! Argument <num> must be integer!!!', \
        'Wrong answer if <num> is not integer!'


print(multiply_by_2(5))

# добавляем тесты, чтобы они срабатывали в момент очередного запуска функции
# при каждом вызове функции мы будем понимать, правильно ли она у нас работает в принципе
# if __name__ == "__main__" указ на работу только в этом коде (при импорте функции тесты работать не будут)
if __name__ == "__main__":
    test_correct_multiply_positive()
    test_correct_multiply_negative()
    test_incorrect_multiply_positive()
    test_incorrect_multiply_negative()
    test_correct_multiply_by_zero()
    test_incorrect_multiply_by_str()
    test_incorrect_multiply_by_float()
# если что-то пошло не так, выйдет инфа только о том, что должно быть
