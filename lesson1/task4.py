"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование
(используя методы encode и decode).
"""


def function_4(myvar):
    print('используем encode')
    result_1 = []
    result_2 = []
    for v in myvar:
        v = v.encode('utf-8', errors='replace')
        result_1.append(v)
    for k in result_1:
        result_2.append(k.decode('utf-8'))
    return result_1, result_2


TODO_4 = ('разработка', 'администрирование', 'protocol', 'standard')

print(function_4(TODO_4))
