def calculator(nums: dict, price: dict):
    """Рассчитывает количество и стоимость
    товаров на складе"""

    for key, value in nums.items():
        for k, v in price.items():
            if value == k:
                products = sum(sub_dict[k] for sub_dict in v for k in sub_dict if k == 'quantity')
                cost = sum(sub_dict['quantity'] * sub_dict['price'] for sub_dict in v)
                print('{} - {}, стоимость {} рублей'.format(key, products, cost))



goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# здесь код
calculator(goods, store)