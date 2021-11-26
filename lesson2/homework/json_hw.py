""""
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными.
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров —
товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
 Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.
"""
import json


# # Создать функцию write_order_to_json(), в которую передается 5 параметров
# def write_order_to_json(item, quantity, price, buyer, date):
#     result = {}
#     with open('orders.json', encoding="utf-8") as outfile:
#         result = json.loads(outfile.read())
#     # Функция должна предусматривать запись данных в виде словаря в файл orders.json
#     result['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})
#     with open('orders.json', 'w', encoding='utf-8') as outfile:
#         json.dump(result, outfile, sort_keys=True, indent=4, ensure_ascii=False)
#         # величину отступа в 4 пробельных символа --> indent=4
#     print('запись в файл выполнена')
#     return result
#
#
# write_order_to_json('12hj123', 25, 2500, 'Sghjhg', '20.10.25')
# write_order_to_json('1546рл', 205, 255900, 'Sghспаjhg', '20.10.25')

# решение препода (дополнила своё)
# Создать функцию write_order_to_json(), в которую передается 5 параметров
def write_order_to_json(item: str, quantity: str, price: str, buyer: str, date: str) -> None:
    """
    Writing function arguments to json file (in dictionary format)
    :param item: good
    :param quantity: quantity
    :param price: price
    :param buyer: buyer
    :param date: datein string formate
    :return: result - writing to a json file
    """

    with open('orders.json', 'r', encoding="utf-8") as file_out:
        result = json.load(file_out)
    with open('orders.json', 'w', encoding='utf-8') as file_in:
        orders_list = result
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_info)
        json.dump(result, file_in, sort_keys=True, indent=4, ensure_ascii=False)
        # величину отступа в 4 пробельных символа --> indent=4
    print('запись в файл выполнена')
    return result


print(write_order_to_json('printer', '10', '6700', 'Ivanov I. I.', '27.10.2017'))
write_order_to_json('laptop', '20', '60700', 'Petrov P. P.', '27.10.2020')
write_order_to_json('mouse', '25', '670', 'Sidorov S. S.', '27.10.2007')
