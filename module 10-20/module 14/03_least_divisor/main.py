# TODO здесь писать код

def divider(number):
    div_1 = 0
    div_2 = number
    for div in range(2, number + 1):
        if number % div == 0:
            div_1 = div
            if div_1 < div_2:
                div_2 = div_1
    return div_2


num = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', divider(num))
