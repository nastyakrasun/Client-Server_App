def function_4(var):
    print('используем encode')
    result_1 = []
    result_2 = []
    for v in var:
        v = v.encode('utf-8', errors='replace')
        result_1.append(v)
    for k in result_1:
        result_2.append(k.decode('utf-8'))
    return result_1, result_2


todo_4 = ('разработка', 'администрирование', 'protocol', 'standard')

print(function_4(todo_4))
