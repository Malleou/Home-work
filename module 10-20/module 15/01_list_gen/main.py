# TODO здесь писать код

def not_even_list(number) -> list:
    """Находит начётные числа от 1 до number

    num_list - список нечётных чисел"""

    num_list: list = []

    while number <= 0:
        print('Ошибка ввода! Введите положительное число, больше нуля')
        number: int = int(input('Введите число: '))

    for n in range(1, number + 1):
        if n % 2 != 0:
            num_list.append(n)
    return num_list




num: int = int(input('Введите число: '))
print(f'Список из нечётных чисел от одного до {num}:', not_even_list(num))