from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()  # Конструктор базового класса Figure
        if radius <= 0:
            raise ValueError("Радиус не может быть отрицательным и 0")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius  # pi * R ^ 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius  # 2 * pi * R

    def add_area(self, f):
        if not isinstance(f, Figure):
            raise ValueError("Параметр f не является фигурой!")
        return self.get_area() + f.get_area()
