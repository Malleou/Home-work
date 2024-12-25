class House:
    """Позволяет создать объект, содержащий имя и число"""

    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors



    def go_to(self, new_floor):
        """Метод выводит в консоль числа от 1 до new_floor
        если new_floor больше 1 и НЕ больше number_of_floors"""

        if 1 <= new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for num in range(1, new_floor + 1):
                print(num)



    def __len__(self):
        """Возвращает только number_of_floors"""

        return self.number_of_floors



    def __str__(self):
        """Выводит текст с name и number_of_floors"""

        print(f'Название "{self.name}",  кол-во этажей: {self.number_of_floors}')




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# h1.go_tu(5)
# h2.go_tu(10)
h1.__str__()
h2.__str__()
print(len(h1))
print(len(h2))