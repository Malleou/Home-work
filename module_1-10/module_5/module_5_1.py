class House:
    """Позволяет создать объект, содержащий имя и число"""

    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors



    def go_to(self, new_floor):
        """Метод выводит в консоль числа от 1 до new_floor
        если new_floor больше 1 и НЕ больше number_of_floors"""

        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for num in range(1, new_floor + 1):
                print(num)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)