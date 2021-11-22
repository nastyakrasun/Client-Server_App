""""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt
и формирующий новый «отчетный» файл в формате CSV.
Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений
извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка —
например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета —
например, main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка
и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
from chardet import detect  # для определения кодировки
import re  # для работы с рег выражениями
import csv  # для работы с csv


# from contextlib import ExitStack  # для открытия кучи файлов (не сработало с кодировкой)
# from itertools import zip_longest

# flist = ['info_1.txt', 'info_2.txt', 'info_3.txt'] with ExitStack() as stack: files = [stack.enter_context(open(
# fname)) for fname in flist] for lines in zip_longest(*files): print(lines)
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 in position 0: invalid continuation byte

def data_from_doc(doc):
    # 1 определяем кодировку
    with open(doc, 'rb') as F_N:  # rb указываем чтобы прочитать кодировку - read bytes
        CONTENT = F_N.read()
        ENCODING = detect(CONTENT)['encoding']
        # print(ENCODING)
    # 2 скрипт, осуществляющий выборку определенных данных
    with open(doc, 'rb') as f_n:
        for line in f_n:
            line = line.decode(ENCODING, errors='replace')
            res_line = re.split(r':', line)
            # print (res_line)
            if 'Изготовитель ОС' in res_line:
                # result['os_prod_list'].append(res_line[1].strip())  # strip() удаляет "лишние" пробелы вокруг элемента
                os_prod_list = res_line[1].strip()
            elif 'Название ОС' in res_line:
                # result['os_name_list'].append(res_line[1].strip())  # strip() удаляет "лишние" пробелы вокруг элемента
                os_name_list = res_line[1].strip()
            elif 'Код продукта' in res_line:
                # result['os_code_list'].append(res_line[1].strip())  # strip() удаляет "лишние" пробелы вокруг элемента
                os_code_list = res_line[1].strip()
            elif 'Тип системы' in res_line:
                # result['os_type_list'].append(res_line[1].strip())  # strip() удаляет "лишние" пробелы вокруг элемента
                os_type_list = res_line[1].strip()
    result = [os_prod_list, os_name_list, os_code_list, os_type_list]
    return result


# print(data_from_doc('info_1.txt'))
# print(data_from_doc('info_2.txt'))
# print(data_from_doc('info_3.txt'))
print('----- получение данных из документов .txt -----')
MAIN_DATA = [['os_prod_list', 'os_name_list', 'os_code_list', 'os_type_list'],
             [data_from_doc('info_1.txt')[0], data_from_doc('info_1.txt')[1], data_from_doc('info_1.txt')[2],
              data_from_doc('info_1.txt')[3]],
             [data_from_doc('info_2.txt')[0], data_from_doc('info_2.txt')[1], data_from_doc('info_2.txt')[2],
              data_from_doc('info_2.txt')[3]],
             [data_from_doc('info_3.txt')[0], data_from_doc('info_3.txt')[1], data_from_doc('info_3.txt')[2],
              data_from_doc('info_3.txt')[3]],
             ]

# print(MAIN_DATA)

print('----- простая запись данных в файл .csv построчно -----')
with open('hw_data_write.csv', 'w', encoding='utf-8') as f_n:
    F_N_WRITER = csv.writer(f_n)  # итерируемый объект writer
    for row in MAIN_DATA:  # загоняем строки, обращаясь к объекту построчно (нужно следовать условию)
        F_N_WRITER.writerow(row)

# удаление пустых строк из файла csv
with open('hw_data_write.csv') as data_input, open('hw_data_read.csv', 'w', newline='') as data_output:
    writer = csv.writer(data_output)
    for row in csv.reader(data_input):
        if any(field.strip() for field in row):
            writer.writerow(row)


print('----- простое чтение из файла hw_data_read.csv ------')
with open('hw_data_read.csv', encoding='utf-8') as f_n:  # открываем файл помня о кодировке
    F_N_READER = csv.reader(f_n)  # создаём итерируемый объект с именем пакета и аналогом reader-a
    # print(type(F_N_READER))
    for row in F_N_READER:
        print(row)  # открываем как список
        # последняя пустая строка не удаляется
