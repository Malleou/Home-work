# здесь код
def counting(add_num: int, del_num: int) -> list:


    new_index = 0
    peoples = list(range(1, add_num + 1))

    for _ in range(len(peoples) - 1):
        print()
        print('Текущий круг людей:', peoples)
        print('Начало счёта с номера:', peoples[new_index])

        leave_num = (del_num + new_index - 1) % len(peoples)
        print('Выбывает участник:', peoples[leave_num])
        del peoples[leave_num]
        new_index = leave_num % len(peoples)
    return peoples



add_people = int(input('Кол-во человек: '))
leave = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {leave}-й человек')
ppl = counting(add_people, leave)
print('Остался человек под номером:', *ppl)
