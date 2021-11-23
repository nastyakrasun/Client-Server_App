"""Модуль json_write"""

import json

DICT_TO_JSON = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

print('----- преобразование python-объекта (словаря) в строку в формате json -----')
with open('mes_example_write_1.json', 'w', encoding='utf-8') as f_n:
    f_n_str = json.dumps(DICT_TO_JSON)  # сначала получаем строку
    print('type(f_n_str): ',type(f_n_str))  # важно понимать для след лекции
    f_n.write(f_n_str)

with open('mes_example_write_1.json') as f_n:
    print(f_n.read())  # считываем содержимое, не оч удобно - записано в строку

print()
print('----- запись python-объекта в файл в формате json -----')
with open('mes_example_write_2.json', 'w', encoding='utf-8') as f_n:
    json.dump(DICT_TO_JSON, f_n)  # одной командой записываем словарь в json

with open('mes_example_write_2.json') as f_n:
    print(f_n.read())  # считываем содержимое, не оч удобно - записано в строку

print()
print('----- использование дополнительных параметров записи -----')
with open('mes_example_write_3.json', 'w', encoding='utf-8') as f_n:
    json.dump(DICT_TO_JSON, f_n, sort_keys=True, indent=4)
# добавляет отступы при записи
# sort_keys - сортировка ключей - по умолчанию False (ключи сортируются по алфавиту)

with open('mes_example_write_3.json') as f_n:
    print(f_n.read())

print()
print('----- запись символов вместо записи кодовых точек -----')

DICT_TO_JSON_2 = {
    "action": "msg",
    "to": "Иванову И.И.",
    "from": "Петрова П.П.",
    "encoding": "ascii",
    "message": "Привет!"
    }

with open('mes_example_write_4.json', 'w', encoding='utf-8') as f_n:
    # json.dump(DICT_TO_JSON_2, f_n, sort_keys=True, indent=4)
    # сформирует выходящий файл в виде одовых точек - нечитаемо
    json.dump(DICT_TO_JSON_2, f_n, sort_keys=True, indent=4, ensure_ascii=False)
    # указываем, что не обязательно должны быть символы ascii
with open('mes_example_write_4.json') as f_n:
    print(f_n.read())
