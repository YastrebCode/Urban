class Figure:
    sides_count = 0

    def __init__(self, color):
        self.__sides = []
        self.__color = []
        self.filled = False
        self.set_color(*color)

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, args):
        for i in args:
            if type(i) == int:
                if i in range(0, 256):
                    continue
            return
        return True

    def set_color(self, *args):
        if self.__is_valid_color(args):
            self.__color = args
        if len(self.__color) == 0:
            self.__color = [0,0,0]

    def __is_valid_sides(self, *args):
        if self.sides_count == len(args):
            for i in args:
                if type(i) != int:
                    return False
            return True
        return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        tmp = 0
        for i in self.__sides:
            tmp = tmp +i
        return tmp

    def set_sides(self, *args):
        if self.__is_valid_sides(*args):
            self.__sides = args
        if len(self.__sides) == 0:
            for i in range(0, self.sides_count):
                self.__sides.append(1)
        return self.__sides



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        super().__init__(color)
        self.set_sides(*args)
        self.__radius = self.get_sides()[0] / (2 * 3.1415926)
    def get_square(self):
        return 3.1415926*self.__radius*self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        super().__init__(color)
        self.__sides = self.set_sides(*args)

    def get_square(self):
        p = 0
        for i in self.__sides:
            p = p + i
        p = p / 2
        return (p*(p - self.__sides[0])*(p - self.__sides[1])*(p - self.__sides[2]))**0.5


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *side):
        super().__init__(color)
        self.set_sides(*side)


    def set_sides(self, *side):
        tmp = []
        if len(self.get_sides()) == 0 and len(side) > 1:
            side = [1]
        elif len(side) > 1:
            side = ["error"]
        for i in range(0, self.sides_count):
            tmp.append(side[0])
        super().set_sides(*tmp)


    def get_volume(self):
        return self.get_sides()[0]**3

#print(Circle((200, 200, 100), 10,20).get_sides())
#print(Triangle((200, 200, 100), 10, 6).get_sides())
#print(Cube((200, 200, 100), 9, 20).get_sides())
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