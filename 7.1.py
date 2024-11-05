import os
class Product:

    def __init__(self, *args):
        self.name = args[0]
        self.weight = args[1]
        self.category = args[2]
        self.__info = args

    def __str__(self):
        return str(self.__info)

class Shop(Product):

    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        with open(self.__file_name, "r") as f:
            tmp = ""
            for i in f.readlines():
                tmp = f'{tmp} {i}'
            return tmp

    def add(self, *args):
        if os.path.exists(self.__file_name) == False:
            with open(self.__file_name, "w+") as f:
                for i in args:
                    f.write(f'{i.name}, {i.weight}, {i.category}\n')
            return self
        with open(self.__file_name, "r+") as f:
            products = f.readlines()
            products_names = []
            for product in products:
                product = product.split(", ")[0]
                products_names.append(product)
            for i in args:
                if i.name not in products_names:
                    f.write(f'{i.name}, {i.weight}, {i.category}\n')
                    continue
                print(f'Продукт {i.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

