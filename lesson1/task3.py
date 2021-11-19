def function_3(var):
    print('невозможно записать в байтовом типе: ')
    result = []
    for v in var:
        if not v.isascii():
            result.append(v)
    return result


task_3 = ('attribute', 'класс', 'функция', 'type')

print(function_3(task_3))
