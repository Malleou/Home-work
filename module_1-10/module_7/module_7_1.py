class Product:
    """Создаёт строку с данными о продукте"""

    def __init__(self, name: str, weight: float, category: str):

        self.name = name
        self.weight = weight
        self.category = category



    def __str__(self):

        return '{}, {}, {}'.format(self.name, self.weight, self.category)




class Shop:
    """"Создаёт файл с данными о множестве продуктов"""

    def __init__(self):

        self.__file_name = 'Products.txt'


    def get_products(self):

        file = open(self.__file_name, 'r')
        return file.read()



    def add(self, *products):

        file = open(self.__file_name, 'a')
        for prod in products:
            if str(prod) not in self.get_products():
                file.write(str(prod) + '\n')
            else:
                print(f'Продукт {prod.name} уже есть в магазине')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())