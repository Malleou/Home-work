# TODO здесь писать код

def move_list(list_, step) -> list:
    """Сдвигает объекты списка на указанный шаг"""

    step %= len(list_)
    return list_[-step:] + list_[:-step]




old_list = list(input('Введите список чисел без пробелов: '))
ste = int(input('Укажите сдвиг: '))
print('Сдвинутый список:', move_list(old_list, ste))
