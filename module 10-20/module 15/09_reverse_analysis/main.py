# TODO здесь писать код

def even_order(numbers_list) -> list:
    """Возвращает список чётных чисел в обратном порядке"""

    for index, num in enumerate(numbers_list):
        if num % 2 != 0:
            numbers_list.remove(num)
    return numbers_list[::-1]


num_list: list = [7, 14, 3, 18, 21, 10, 9, 6]
print('Список чисел:', num_list)
print('Чётные числа в обратном порядке:', even_order(num_list))