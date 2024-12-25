def divide(first, second):
    """Функция не позволяет делить на 0"""

    if second == 0:
        first = str('Ошибка ввода')
    else:
        first /= second
    return first