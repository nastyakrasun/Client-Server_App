"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

# import locale !!! - нельзя, тк так мы получаем кодировку системы
from chardet import detect

print('создаём и заполняем текстовый файл')
F_N = open('test_file.txt', 'w', encoding='utf-8')
F_N.write('сетевое программирование\nсокет\nдекоратор')
F_N.close()
# Проверить кодировку файла по умолчанию. хорошее
with open('test_file.txt', 'rb') as F_N:  # rb указываем чтобы прочитать кодировку - read bytes
    # - иначе кодировка не определится (при read)
    CONTENT = F_N.read()
    ENCODING = detect(CONTENT)['encoding']
print(f'кодировка файла по умолчанию: ', ENCODING)
# print(type(F_N))

# явное указание кодировки при работе с файлом
print('принудительно открываем файл в формате Unicode и выводим его содержимое:')
with open('test_file.txt', encoding='utf-8') as F_N:
    # for el_str in F_N:
    #     print(el_str, end='')
    # print()
    CONTENT = F_N.read()
print(CONTENT)

# если файл слишком большой можно исп UniversalDetector
# так можно считывать файл построчно и передавать тек строку
# для самых продвинутых
