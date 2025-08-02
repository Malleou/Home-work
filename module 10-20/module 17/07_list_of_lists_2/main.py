nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# здесь код

def unpacking(list_: list) -> list:
    """Распаковывает цикл"""

    new_list = [num for list2 in list_ for list1 in list2 for num in list1]
    return new_list




print(unpacking(nice_list))