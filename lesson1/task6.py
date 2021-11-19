import locale

print('создаём и заполняем текстовый файл')
F_N = open('test_file.txt', 'w', encoding='utf-8')
F_N.write('сетевое программирование\nсокет\nдекоратор')
F_N.close()
# Проверить кодировку файла по умолчанию.
default_encoding = locale.getpreferredencoding()
print(f'кодировка файла по умолчанию: ', default_encoding)
# print(type(F_N))

# явное указание кодировки при работе с файлом
print('принудительно открываем файл в формате Unicode и выводим его содержимое:')
with open('test_file.txt', encoding='utf-8') as F_N:
    for el_str in F_N:
        print(el_str, end='')
    print()
F_N.close()
