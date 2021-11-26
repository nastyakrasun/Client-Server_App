""" Module csv_read """

import csv  # импортируем ссылку на пакет перед работой

print('----- Простое чтение из файла kp_data.csv ------')
print('----- Получаем итератор объекта ------')
with open('kp_data.csv', encoding='utf-8') as f_n:  # открываем файл помня о кодировке
    F_N_READER = csv.reader(f_n)  # создаём итерируемый объект с именем пакета и аналогом reader-a
    print(type(F_N_READER))
    for row in F_N_READER:
        print(row)  # открываем как список

print()
print('----- Можно прочитать как обычный текстовой файл ------')  # принцип везде один
with open('kp_data.csv', encoding='utf-8') as f_n:
    F_N_READER = f_n.read()
    print(type(F_N_READER))
    print(F_N_READER)  # открываем как обычный текст, но преимущество csv-файла теряется

print()
print('----- Преобразование итератора в список ------')
with open('kp_data.csv', encoding='utf-8') as f_n:
    F_N_READER = csv.reader(f_n)
    print(list(F_N_READER))


print()
print('----- Разделение строки заголовков от содержимого ------')  # иногда бывает полезно
with open('kp_data.csv', encoding='utf-8') as f_n:
    F_N_READER = csv.reader(f_n)
    F_N_HEADERS = next(F_N_READER)  # убрали первую строку из итератора
    print('Headers: ', F_N_HEADERS)
    for row in F_N_READER:  # поэлементно вывели кажд строку
        print(row)


print()
print('----- Вывод результата с помощью метода DictReader ------')  # позв выводить список словарей, оч удобен когда длинная строка
with open('kp_data.csv', encoding='utf-8') as f_n:
    F_N_READER = csv.DictReader(f_n)
    for row in F_N_READER:
        print(row)
        print(row['hostname'], row['model'])
