# TODO здесь писать код

def order(list_) -> list:
    """Упорядочивает список от меньшего к большему"""

    for count in range(len(list_)):

        min_index: int = count
        for index in range(count, len(list_)):
            if list_[index] < list_[min_index]:

                min_index: int = index

        list_[count], list_[min_index] = list_[min_index], list_[count]
    return list_




old_list = [20, 10, 5, 15, 25]
print('Изначальный список:', old_list)
print('Отсортированный список:', order(old_list))