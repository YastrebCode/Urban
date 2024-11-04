class Vehicle:
    __COLOR_VARIANTS = ['black', "white", "metallic"]

    def __init__(self, *args):
        self.owner = str(args[0])
        self.__model = str(args[1])
        self.__engine_power = int(args[3])
        self.__color = str(args[2])

    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nвладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
            return self
        print(f'Нельзя сменить цвет на {new_color}')
        return self


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
