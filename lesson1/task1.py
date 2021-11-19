def function_1(var):
    result = {}
    for v in var:
        result[str(v)] = (type(v), v)
    return result


todo_1 = ('разработка', 'сокет', 'декоратор')
todo_2 = ('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
          '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440')

print(function_1(todo_1))
print(function_1(todo_2))
