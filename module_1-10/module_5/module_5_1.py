class House:
    """Позволяет создать объект, содержащий имя и число"""

    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors



    def go_tu(self, new_floor):
        """Метод выводит в консоль числа от 1 до new_floor
        если new_floor больше 1 и НЕ больше number_of_floors"""

        if 1 <= new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for num in range(1, new_floor + 1):
                print(num)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_tu(5)
h2.go_tu(10)