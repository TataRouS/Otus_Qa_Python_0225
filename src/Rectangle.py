from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__()  # Конструктор базового класса Figure
        self.get_perimetr = None
        if a <= 0 or b <= 0:
            raise ValueError("Стороны прямоугольника не могут быть отрицательным и  0")
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return (self.a + self.b) * 2
