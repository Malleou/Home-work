# TODO здесь писать код
# Хотел добавить контроль регистра, через .lower() но это работает только для строк :(

def cinema(quantity) -> list:
    """Функция сравнивает имеющийся список с тем, что вводит пользователь
    Если то, что ввёл пользователь есть в списке, оно добавляется в новый список.
    Иначе пропуск"""

    films: list = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
    my_list: list = []

    for _ in range(quantity):
        film = input('Введите название фильма: ')
        if film in films:
            my_list.append(film)
        else:
            print(f'Ошибка: фильма {film} у нас нет :(')
            continue
    return my_list




quan: int = int(input('Сколько фильмов хотите добавить? '))
favorite_films = cinema(quan)
print('Ваш список любимых фильмов:', favorite_films)