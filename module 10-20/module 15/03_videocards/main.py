# TODO здесь писать код

def group(summ) -> list:
    """Создаёт список видеокарт"""

    card_list: list = []

    for i in range(summ):
        card: int = int(input(f'Видеокарта {i + 1}: '))
        card_list.append(card)
    return card_list



def separation(card_list) -> list:
    """Убирает из списка самую последнюю модель"""

    n_list: list = card_list.copy()
    max_model: int = card_list[0]
    for model in card_list:
        if model > max_model:
            max_model = model

    for index, mod in enumerate(card_list):
        if mod == max_model:
            n_list.remove(mod)
    return n_list



sum_card: int = int(input('Укажите количество видеокарт: '))
old_list: list = group(sum_card)
new_list: list = separation(old_list)
print('Старый список видеокарт:', old_list)
print('Новый список видеокарт:', new_list)

