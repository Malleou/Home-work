shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# здесь писать код

def summator(list_: list, word: str) -> (int, int):
    """Считает кол-во искомых эл-тов в списке и
    выдаёт сумму чисел"""

    counter = 0
    summ = 0
    for sher_list in list_:
        if word.lower() in sher_list[0].lower():
            counter += 1
            summ += sher_list[1]
    return counter, summ

request = input('Название детали: ')
num, sum_ = summator(shop, request)
print('Количество деталей -', num)
print('Общая стоимость -', sum_)