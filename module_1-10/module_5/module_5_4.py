class House:
    """Позволяет создать объект, содержащий имя и число"""

    houses_history = []



    def __new__(cls, *args, **kwargs):
        """Создание объекта"""

        return object.__new__(cls)



    def __del__(self):
        """Выводит принт при удалении объекта"""

        print(self.name, 'снесён, но он останется в истории')
        del self



    def __init__(self, name, number_of_floors):
        """Инициализация объекта и сохранение имени в историю"""

        self.name = name
        House.houses_history.append(self.name)
        print(House.houses_history)
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

        return f'Название "{self.name}",  кол-во этажей: {self.number_of_floors}'



    def __eq__(self, other):
        """сравнивает переменные number_of_floors
        True - если числа одинаковые"""

        return self.number_of_floors == other.number_of_floors



    def __lt__(self, other):
        """сравнивает переменные number_of_floors
        True - если число первой переменной меньше второй"""

        return self.number_of_floors < other.number_of_floors



    def __le__(self, other):
        """сравнивает переменные number_of_floors
        True - если число первой переменной меньше или равно второй"""

        return self.number_of_floors <= other.number_of_floors



    def __gt__(self, other):
        """сравнивает переменные number_of_floors
        True - если число первой переменной больше второй"""

        return self.number_of_floors > other.number_of_floors



    def __ge__(self, other):
        """сравнивает переменные number_of_floors
        True - если число первой переменной больше или равно второй"""

        return self.number_of_floors >= other.number_of_floors



    def __ne__(self, other):
        """сравнивает переменные number_of_floors
        True - если числа не равны друг другу"""

        return self.number_of_floors != other.number_of_floors



    def __add__(self, value):
        """Сложение переменной number_of_floors и числа"""

        self.number_of_floors = self.number_of_floors + value
        return self



    def __iadd__(self, value):
        """Сложение переменной number_of_floors и числа"""

        self.number_of_floors += value
        return self



    def __radd__(self, value):
        """Сложение переменной числа и number_of_floors"""

        self.number_of_floors = value + self.number_of_floors
        return self





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Матрёшки', 20)

del h2
del h3
print(House.houses_history)
# h1.go_to(5)
# h2.go_to(10)
# h1.__str__()
# h2.__str__()
# print(len(h1))
# print(len(h2))
# print(h1)
# print(h2)
# print(h1 == h2) # __eq__
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
# h1 += 10 # __iadd__
# print(h1)
# h2 = 10 + h2 # __radd__
# print(h2)
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__