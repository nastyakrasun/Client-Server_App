"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.
"""
import platform
import subprocess
import chardet


# print(platform.system())
def function_5(args):
    YA_PING = subprocess.Popen(args, stdout=subprocess.PIPE)
    results = []
    count = 0
    for line in YA_PING.stdout:
        # print(type(line))
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        # print(type(line.decode('utf-8')))
        results.append(line.decode('utf-8'))
        if count == 4:
            break
        count += 1
    return results


# print(type(YA_PING))

ARGS1 = ['ping', 'yandex.ru']
ARGS2 = ['ping', 'youtube.com']

print(function_5(ARGS1))
print(function_5(ARGS2))

# доп решение
# URLS = ['yandex.ru', 'youtube.com']
# CODE = '-n' if platform.system() == 'Windows' else '-c'
#
# for url in URLS:
#     args = ['ping', CODE, '4', url]
#     YA_PING = subprocess.Popen(args, stdout=subprocess.PIPE)
#     for line in YA_PING.stdout:
#         result = detect(line)
#         print(result)
#         line = line.decode(result['encoding']).encode('utf-8')
#         print(line.decode('utf-8'))
