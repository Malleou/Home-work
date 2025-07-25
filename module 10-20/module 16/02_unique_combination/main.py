# TOD здесь писать код


# Решение 1:
def unification_1 (first: list, second: list) -> list:
    """Объединяет 2 списка и сортирует 2 списка, удаляет повторяющиеся элементы"""

    first.extend(second)
    first.sort()
    for index, num in enumerate(first):
        if 0 < index <= len(first):
            if num == first[index - 1]:
                first.remove(num)
    return first




# Решение 2:
def unification_2 (first: list, second: list) -> list:
    """Объединяет 2 списка и сортирует 2 списка, удаляет повторяющиеся элементы"""

    first.extend(second)
    first.sort()
    set1 = set(first)
    return list(set1)




list1 = [1, 2, 1, 3, 5, 7, 9, 10]
list2 = [2, 4, 5, 6, 8, 10]

print(unification_1(list1, list2))
print(unification_2(list1, list2))