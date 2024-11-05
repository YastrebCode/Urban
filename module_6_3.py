class Horse:
    x_distance = 0
    sound='Frrr'

    def run(self, dx):
        self.x_distance = self.x_distance + dx
        return self

class Engle:
    y_distance = 0
    sound='I train, eat, sleep, and repeat'
    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance = self.y_distance + dy
        return self

class Pegasus(Horse, Engle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        super().__init__()
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()