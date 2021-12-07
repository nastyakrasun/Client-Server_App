"""
3. Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.
"""


# префикс b создаёт экземпляр типа bytes вместо типа string
# они могут содержать только символы ASCII


def function_3(myvar):
    print('невозможно записать в байтовом типе: ')
    result = []
    for v in myvar:
        if not v.isascii():
            result.append(v)
    return result


def function_3_2(myvar):
    result = {}
    KEY = 'невозможно записать в байтовом типе'
    result.setdefault(KEY, [])
    for v in myvar:
        try:
            bytes(v, 'ascii')
            # v.encode('ascii')
            # 2 сп-б v = eval(f"b'{v}'")
        except UnicodeEncodeError:
            result[KEY].append(v)
        # 2 сп-б except SyntaxError:  # SyntaxError сложнее перехватить потому что она возникает в случае неверного
        # написания (интерпритатор просто не запустится при ошибках в написании)
        # result[KEY].append(v)
    return result


def function_3_3(myvar):
    result = {}
    KEY = 'невозможно записать в байтовом типе'
    result.setdefault(KEY, [])
    for v in myvar:
        for myitem in v:
            if ord(myitem) > 127:  # через ф-ю ord - отлавливаем символ, не входящий в ascii
                # (ord определяет код символа)
                result[KEY].append(v)
                break
    return result


TASK_3 = ('attribute', 'класс', 'функция', 'type')

print(function_3_2(TASK_3))
print(function_3_3(TASK_3))
