from Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()  # Конструктор базового класса Figure
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника не могут быть отрицательным и 0")
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = self.get_perimeter()
        surf = p * (p - self.a) * (p - self.b) * (p - self.c)
        return math.sqrt(surf)

    def get_perimeter(self):
        return self.a + self.b + self.c
