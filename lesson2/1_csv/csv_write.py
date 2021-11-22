""" Модуль csv_write """

import csv

DATA = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', 2960, 'Moscow, str'],
        ['kp2', 'Cisco', 2960, 'Novosibirsk, str'],
        ['kp3', 'Cisco', 2960, 'Kazan, str'],
        ['kp4', 'Cisco', 2960, 'Tomsk, str']]

print()
print('----- простая запись данных в файл .csv построчно -----')
with open('kp_data_write_1.csv', 'w', encoding='utf-8') as f_n:
    F_N_WRITER = csv.writer(f_n)  # итерируемый объект writer
    for row in DATA:  # загоняем строки, обращаясь к объекту построчно (нужно следовать условию)
        F_N_WRITER.writerow(row)

print('----- простая запись данных в файл .csv всего массива сразу -----')
with open('kp_data_write_1_1.csv', 'w', encoding='utf-8') as f_n:
    F_N_WRITER = csv.writer(f_n)
    F_N_WRITER.writerows(DATA)  # записыаем всё сразу одной строкой (условий не нужно)

print()
print('----- читаем как txt файл -----')
with open('kp_data_write_1.csv', encoding='utf-8') as f_n:
    LINES = f_n.read()  # можем прочитать всё как обычный текст
    print(LINES)

print('----- читаем как csv файл -----')
with open('kp_data_write_1.csv', encoding='utf-8') as f_n:
    LINES = csv.reader(f_n)
    for row in LINES:
        print(row)

print()
print('----- quoting=csv.QUOTE_NONNUMERIC только при записи -----')  # csv в отл от текста позв нам разделять по типам данные, которые там записываются
with open('kp_data_write_2.csv', 'w', encoding='utf-8') as f_n:
    F_N_WRITER = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)  # указываем при записи параметр, что брать в кавычки надо нечисловые значения
    for row in DATA:
        F_N_WRITER.writerow(row)  # есть возм при чтении отличить числа от строк

with open('kp_data_write_2.csv', encoding='utf-8') as f_n:
    LINES = csv.reader(f_n)
    for row in LINES:
        # print(row, type(row[2]))
        print(row)

print()
print('----- quoting=csv.QUOTE_NONNUMERIC и при записи, и при чтении -----')
with open('kp_data_write_3.csv', 'w', encoding='utf-8') as f_n:
    F_N_WRITER = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)  # ! nonnumeric
    F_N_WRITER.writerows(DATA)

with open('kp_data_write_3.csv', encoding='utf-8') as f_n:
    LINES = csv.reader(f_n, quoting=csv.QUOTE_NONNUMERIC)
    for row in LINES:
        # print(row, type(row[2]))
        print(row)

print()
print('----- изменение формата разделителя delimiter="|" -----')
with open('kp_data_delimiter.csv', 'w', encoding='utf-8') as f_n:
    F_N_WRITER = csv.writer(f_n, delimiter="|")
    F_N_WRITER.writerows(DATA)

with open('kp_data_delimiter.csv', encoding='utf-8') as f_n:
    F_N_READER = csv.reader(f_n)
    for row in F_N_READER:
        print(row)

print()
print('----- список словарей в качестве исходных данных -----') # очень строго записывать с пом словаря - один тип, одно кол-во ключей-значений
DATA = [{'hostname': 'kp1',
         'location': 'Moscow',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp2',
         'location': 'Novosibirsk',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp3',
         'location': 'Kazan',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp4',
         'location': 'Tomsk',
         'model': '2960',
         'vendor': 'Cisco'}]

with open('kp_data_dictwriter.csv', 'w', encoding='utf-8') as f_n:  # берём ключи в кач-ве заголовков
    F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(DATA[0].keys()))  # превращаем автоматически ключи словаря в список
    F_N_WRITER.writeheader()
    for d in DATA:  # или без пробега сразу записать всю DATA -->  F_N_WRITER.writerows(DATA)
        F_N_WRITER.writerow(d)

with open('kp_data_dictwriter.csv', encoding='utf-8') as f_n:
    F_N_READER = csv.reader(f_n)
    for row in F_N_READER:
        print(row)
