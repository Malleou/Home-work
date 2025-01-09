class Vehicle:

    __COLOR_VARIANTS: list = ['Blue', 'Red', 'Green', 'Black', 'White']
    def __init__(self, owen, model, color, engine_power):
        self.owen: str = owen
        self.__model: str = model
        self.__engine_power: int = engine_power
        self.__color: str = color



    def get_model(self):

        return 'Модель: {}'.format(self.__model)



    def get_horsepower(self):

        return 'Мощность двигателя: {}'.format(self.__engine_power)



    def get_color(self):

        return 'Цвет: {}'.format(self.__color)



    def print_info(self):

        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец: {}'.format(self.owen))



    def set_color(self, new_color: str):

        if new_color[0].upper() + new_color[1:].lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print('Нельзя сменить цвет на {}'.format(new_color))



class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()