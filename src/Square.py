from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)  # Конструктор базового класса Rectangle
