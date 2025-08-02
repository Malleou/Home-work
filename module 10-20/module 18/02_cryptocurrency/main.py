def print_dict(some_dict: dict, indent=0):
    """Выводит значения словаря

    Этот метод сделал не полностью сам, а с помощью нейросети.
    Свой, закомментирован на строках с 75 по 93"""

    for key, value in some_dict.items():
        space = ' ' * indent
        if isinstance(value, dict):
            print(f'{space}{key}:')
            print_dict(value, indent + 1)
        elif isinstance(value, list):
            print(f'{space}{key}:')
            for index, item in enumerate(value):
                print(f'{space} Элемент {index + 1}:')
                if isinstance(item, dict):
                    print_dict(item, indent + 2)
                else:
                    print(space, item)
        else:
            print(space, key, '-', value)



data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


# здесь код
# 1. Вывести списки ключей и значений словаря.
print_dict(data)

# for key, value in data.items():
#     if isinstance(value, dict):
#         print(f'{key}:')
#         for k in value:
#             print(k, '-', value[k])
#     elif isinstance(value, list):
#         print(f'{key}:')
#         for index, item in enumerate(value):
#             print(f'Элемент: {index + 1}')
#             if isinstance(item, dict):
#                 for k, v in item.items() :
#                     if isinstance(v, dict):
#                         print(f'{k}:')
#                         for sub_key, sub_value in v.items():
#                             print(sub_key, '-', sub_value)
#                     else:
#                         print(k, '-', v)
#     else:
#         print(key, '-', value)

# 2. В ETH добавить ключ total_diff со значением 100.
print()
data['ETH'].update({'total_diff': 100})
print(data['ETH']['total_diff'])

# 3. Внутри fst_token_info значение ключа name поменять с fdf на doge.
print()
data['tokens'][0]['fst_token_info']['name'] = 'doge'
print(data['tokens'][0]['fst_token_info']['name'])

# 4. Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
print()
sum_ = sum(token.pop('total_out') for token in data['tokens'])
data['ETH']['total_out'] = sum_
print(data['ETH'])

# 5. Внутри sec_token_info изменить название ключа price на total_price.
print()
value = data['tokens'][1]['sec_token_info']['price']
data['tokens'][1]['sec_token_info'].pop('price')
data['tokens'][1]['sec_token_info']['total_price'] = value
print(data['tokens'][1]['sec_token_info']['total_price'])