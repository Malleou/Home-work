import random

# здесь код
def new_list(size = 20) -> list:
    """Создаёт список из 20-ти случайных вещественных чисел"""

    new_group = [round(random.uniform(5, 10), 2) for _ in range(size)]
    return new_group




def winners_list(list_1: list, list_2: list) -> list:
    """Сравнивает 2 списка и сохраняет наибольшее число"""

    winner_group = [list_1[i] if list_1[i] > list_2[i] else list_2[i] for i in range(20)]
    return winner_group




team_1 = new_list()
team_2 = new_list()
winners = winners_list(team_1, team_2)
print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', winners)