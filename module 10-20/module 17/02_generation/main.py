# здесь код

def generation_list(number: int) -> list:
    """Создаёт заданный список и меняет его, в зависимости от индекса"""

    old_list = [i for i in range(number)]
    new_list = [1 if n % 2 == 0 or old_list[0] else n % 5 for n in old_list]
    return new_list

num = int(input('Введите длину списка: '))
print(generation_list(num))