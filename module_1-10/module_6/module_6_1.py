class Animal:
    """Родительский класс животных.
    По умолчанию, животные:
    живые, голодные, могут есть фрукты."""

    alive = True
    fed = False

    def __init__(self, name):
        self.name = name



    def eat(self, food):
        """Может есть фрукты.
        Если животное не есть, оно умирает"""

        if food.edible:
            print('{0} съел {1}'.format(self.name, food.name))
            self.fed = True
        else:
            print('{0} не стал есть {1}'.format(self.name, food.name))
            self.alive = False



class Plant:
    """Родительский класс растений
    По умолчанию, растение не съедобное"""

    edible = False

    def __init__(self, name):
        self.name = name



class Mammal(Animal):
    """Дочерний класс животного"""
    pass



class Predator(Animal):
    """Дочерний класс животного"""
    pass



class Flower(Plant):
    """Дочерний класс растения"""
    pass



class Fruit(Plant):
    """Дочерний класс растения
    Съедобное для класса Animal"""

    edible = True



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)