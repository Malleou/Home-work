from math import inf

def divide(first, second):
    """Функция позволяет делить на 0"""

    if second == 0:
        return inf
    else:
        first /= second
        return first