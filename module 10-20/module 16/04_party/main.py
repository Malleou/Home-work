# здесь код

def control_people(guest_list: list) -> list:
    """Редактирует список"""

    while True:
        print()
        print('Сейчас на вечеринке', len(guest_list), 'человек:', guest_list)
        action = input('Гость пришёл или ушёл?\n')
        if (action.lower() == 'пришёл' or action.lower() == 'пришел') and len(guest_list) < 6:
            name = input('Имя гостя: ')
            name = name[0].upper() + name[1:].lower()
            guest_list.append(name)
            print(f'Привет, {name}!')
        elif action.lower() == 'ушёл' or action.lower() == 'ушел':
            name = input('Имя гостя: ')
            name = name[0].upper() + name[1:].lower()
            if name in guest_list:
                guest_list.remove(name)
                print(f'Пока, {name}!')
            else:
                print('Такого человека не нашлось среди гостей')
        elif (action.lower() == 'пришёл' or action.lower() == 'пришел') and len(guest_list) >= 6:
            name = input('Имя гостя: ')
            print(f'Прости, {name}, мест нет.')
        elif action.lower() == 'пора спать':
            print('Вечеринка закончилась, все легли спать.')
            break
        else:
            print('Ошибка ввода! Давай попробуем ещё раз')
    return guest_list




guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
control_people(guests)
print('Оставшиеся гости:', guests)