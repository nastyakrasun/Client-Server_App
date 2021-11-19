import subprocess
import chardet


def function_5(ARGS):
    YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    results = []
    for line in YA_PING.stdout:
        # print(type(line))
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        # print(type(line.decode('utf-8')))
        results.append(line.decode('utf-8'))
    return results

# print(type(YA_PING))



ARGS1 = ['ping', 'yandex.ru']
ARGS2 = ['ping', 'youtube.com']

print(function_5(ARGS1))
print(function_5(ARGS2))
