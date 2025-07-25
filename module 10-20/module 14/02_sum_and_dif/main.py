# TODO здесь писать код

def summ(number):
    num = 0
    while number != 0:
        num += number % 10
        number //= 10
    return num


def figure_count(number):
    counter = 0
    while number != 0:
        number //= 10
        counter += 1
    return counter


n = int(input('Введите число: '))

sum_ = summ(n)
counter = figure_count(n)


print('Сумма чисел:', sum_)
print('Колличество цифр в числе:', counter)
print('Разность суммы и количества цифр:', sum_ - counter)
