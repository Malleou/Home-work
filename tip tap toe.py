def tic_tac_toe(area):
    for map_ in area:
        print(*map_)
    print()


def check_win(area, player):
    # Проверяем строки, столбцы и диагонали
    for i in range(3):
        if area[i][0] == area[i][1] == area[i][2] == player:  # Строки
            return True
        if area[0][i] == area[1][i] == area[2][i] == player:  # Столбцы
            return True
    if area[0][0] == area[1][1] == area[2][2] == player:  # Главная диагональ
        return True
    if area[0][2] == area[1][1] == area[2][0] == player:  # Побочная диагональ
        return True
    return False


def step(area):
    for i in range(9):
        # Ход крестиков
        row = int(input('Крестики: Выберете ряд (1/2/3): '))
        col = int(input('Крестики: Выберете колонну (1/2/3): '))

        if area[row-1][col-1] != '*':
            print('Клетка занята! Пропускаешь ход.')
            continue
        area[row-1][col-1] = 'X'
        tic_tac_toe(area)

        if check_win(area, 'X'):
            print('Победили крестики!')
            break

        # Ход ноликов
        row_o = int(input('Нолики: Выберете ряд (1/2/3): '))
        col_o = int(input('Нолики: Выберете колонну (1/2/3): '))

        if area[row_o-1][col_o-1] != '*':
            print('Клетка занята! Пропускаешь ход.')
            continue
        area[row_o-1][col_o-1] = 'O'
        tic_tac_toe(area)

        if check_win(area, 'O'):
            print('Победили Нолики!')
            break

        if i == 8:
            print('Ничья!')
    return


game_map = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
tic_tac_toe(game_map)
step(game_map)