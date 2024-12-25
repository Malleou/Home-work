first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and first == third:
    print('3 одинаковых чиста')
elif first == second or first == third or second == third:
    print('2 одинаковых числа')
else:
    print('Одинаковых чисел нет')