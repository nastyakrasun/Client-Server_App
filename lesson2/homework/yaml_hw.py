"""
3. Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
Подготовить данные для записи в виде словаря,
в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь,
где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы с юникодом:
allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

# данные для записи в виде словаря
DATA_TO_YAML = {
    'actions': ['download', 'delete', 'upgrade', 'fill', 'update'],  # первому ключу соответствует список
    'to': 5,  # второму — целое число,
    # третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом
    # отсутствующим в кодировке ASCII (например, €)
    'currency': {
        'Argentina Peso': '$',
        'Costa Rica Colon': '₡',
        'Cuba Peso': '₱',
        'Ghana Cedi': '¢',
        'Gibraltar Pound': '£'
    }
}


def write_to_yaml(data):
    with open('file.yaml', 'w', encoding='utf-8') as file_in:  # сохранение данных в файл file.yaml
        yaml.dump(data, file_in, default_flow_style=False, allow_unicode=True, sort_keys=False)
    # стилизацию файла с пом default_flow_style, allow_unicode = True;
    return ' файл записан '


def check_data(filename, data):
    print(' чтение .yaml-файла ')
    with open(filename, 'r', encoding='utf-8') as file_out:  # Реализовать считывание данных из созданного файла
        print(file_out.read())
        # data_out = yaml.load(file_out, Loader=yaml.SafeLoader)
        # if data == data_out:  # проверить, совпадают ли они с исходными  -- не знаю как проверить
        #     # 'file.yaml' == DATA_TO_YAML)  -- False
        #     print(' файлы совпадают ')
        # else:
        #     print(' файлы не совпадают ')
    return ' файл прочитан '


print(write_to_yaml(DATA_TO_YAML))
print('-' * 50)
print(check_data('file.yaml', DATA_TO_YAML))
