import random

class Animal:
    """Родительский класс животных
    live - живые
    sound - немые
    _DEGREE_OF_DANGER - ур.опасности

    Методы:
    move, get_cords, attack"""

    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):

        self._cords = [0, 0, 0]
        self.speed = speed



    def move(self, dx,dy,dz):
        """Логика перемещения.
        dz - не может быть меньше 0"""

        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords[0] -= dx * self.speed
            self._cords[1] -= dy * self.speed
            self._cords[2] -= dz * self.speed



    def get_cords(self):
        """Вывод координат"""

        print('X: {}, Y: {}, Z: {}'.format(self._cords[0], self._cords[1], self._cords[2]))



    def attack(self):
        """Логика атаки"""

        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")




class Bird(Animal):
    """Птицы. Дочерний класс животных"""

    beak = True

    def lay_eggs(self):
        """Дают яйца"""

        print(f'Here are(is) {random.randint(1,4)} eggs for you')



class AquaticAnimal(Animal):
    """Водные животные. Дочерний класс животных"""

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        """Логика погружения"""

        if self._cords[2] - abs(dz) * self.speed / 2 < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] -= abs(dz) * self.speed // 2



class PoisonousAnimal(Animal):
    """Ядовитые животные. Дочерний класс животных"""

    _DEGREE_OF_DANGER = 8



class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    """Утконос. Имеет множественное наследование

    sound - звуковой сигнал"""

    sound = 'Click-click-click'

    def speak(self):
        """Выводит звуковой сигнал"""

        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()