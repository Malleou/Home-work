import math

class Figure:

    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if color else [0, 0, 0]
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.filled = False


    def get_color(self) -> list:

        return self.__color



    def __is_valid_color(self, color: list) -> bool:

        if len(color) != 3:
            return False
        for num in color:
            if num < 0 or num > 255 or not isinstance(num, int):
                return False
        return True



    def set_color(self, r: int, g: int, b: int):

        new_color = [r, g, b]
        if self.__is_valid_color(new_color):
            self.__color = new_color
        else:
            print('Ошибка! Цвет указан неверно.'
                  'Нужно указать 3 целых числа в диапазоне от 0 до 255.')



    def __is_valid_sides(self, *args) -> bool:

        if len(args) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in args)




    def get_sides(self):

        return self.__sides



    def __len__(self):

        return sum(self.__sides)



    def set_sides(self, *new_sides):

        if not self.__is_valid_sides(*new_sides):
            print("Ошибка! Неверное количество сторон или значения.")
            return
        self.__sides = list(new_sides)



class Circle(Figure):

    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) != self.sides_count:
            self._Figure__sides = [1]



    def __radius(self):

        return self.__sides[0] / (2 * math.pi)



    def get_square(self):

        return math.pi * self.__radius() ** 2



class Triangle(Figure):

    sides_count = 3



    def get_square(self):

        a, b, c = self.__sides[0], self.__sides[1], self.__sides[2]
        if not (a + b > c and a + c > b and b + c > a):
            return 'Стороны не образуют треугольник'
        p = len(self) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))



class Cube(Figure):

    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        side = sides[0] if sides else 1
        self._Figure__sides = [side] * self.sides_count

    def get_volume(self):
        return self._Figure__sides[0] ** 3




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())