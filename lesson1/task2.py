def function_2(var):
    print('записываем в байтовом типе, не используя методы encode и decode')
    result = {}
    for v in var:
        v = bytes(v, encoding='utf-8')
        result[v] = (type(v), v, len(v))
    return result


def function_2_1(var):
    print('записываем в байтовом типе, не используя методы encode и decode')
    result = {}
    for v in var:
        if v.isascii():
            v = bytes(v, encoding='utf-8')
            result[v] = (type(v), v, len(v))
        else:
            print(f'слово "{v}" невозможно записать в байтовом типе')
    return result


# как добавить b в начало слова - ? (так и не додумалась с пом функции, но думала)
# def function_2_2(var):
#     pass


task_2 = ('class', 'function', 'method', 'мышеловка')

print(function_2(task_2))
print(function_2_1(task_2))
# print(function_2_2(task_2))
