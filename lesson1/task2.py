"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode и decode)
 и определить тип, содержимое и длину соответствующих переменных.
"""


def function_2(myvar):
    print('записываем в байтовом типе, не используя методы encode и decode')
    result = {}
    for v in myvar:
        v = bytes(v, encoding='utf-8')
        result[v] = (type(v), v, len(v))
    return result


def function_2_1(myvar):
    print('записываем в байтовом типе, не используя методы encode и decode')
    result = {}
    for v in myvar:
        if v.isascii():
            v = bytes(v, encoding='utf-8')
            result[v] = (type(v), v, len(v))
        else:
            print(f'слово "{v}" невозможно записать в байтовом типе')
    return result


# как добавить b в начало слова с пом функции
def function_2_2(myvar):
    result = {}
    for v in myvar:
        if v.isascii():
            v = eval(f"b'{v}'")
            result[v] = (type(v), v, len(v))
        else:
            print(f'слово "{v}" невозможно записать в байтовом типе')
    return result


TASK_2 = ('class', 'function', 'method', 'мышеловка')

print(function_2(TASK_2))
print(function_2_1(TASK_2))
print(function_2_2(TASK_2))
