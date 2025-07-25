# TODO здесь писать код
from typing import Any


def grouping(number_participants) -> list:
    """Создаёт список с участниками"""

    tournament_participants: list = []

    for _ in range(number_participants):
        name: str = input('Введите имя участника: ')
        tournament_participants.append(name)
    return tournament_participants




def separation(tournament_participants) -> tuple[list[Any], list[Any]]:
    """Создаёт 2 списка с именами. 1 список с именами
    под чётным индексом, другой с именами под нечётным индексом"""

    team_1: list = []
    team_2: list = []

    for index, name in enumerate(tournament_participants):
        if (index + 1) % 2 != 0:
            team_1.append(name)
        else:
            team_2.append(name)
    return team_1, team_2



num_part: int = int(input('Введите количество участников: '))
separation: tuple = separation(grouping(num_part))
print('Первая группа:', separation[0])
print('Вторая группа:', separation[1])

