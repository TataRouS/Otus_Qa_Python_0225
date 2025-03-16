from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__()  # Конструктор базового класса Figure
        if a <= 0 or b <= 0:
            raise ValueError("Стороны прямоугольника не могут быть отрицательным и  0")
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return (self.a + self.b) * 2

    def add_area(self, f):
        if not isinstance(f, Figure):
            raise ValueError("Параметр f не является фигурой!")
        return self.get_area() + f.get_area()
