from abc import ABC, abstractmethod


# Абстрактный класс
class Figure(ABC):
    def __init__(self):
        pass  # Ничего не делаем, метод - абстрактный

    @abstractmethod
    def get_perimeter(self):
        pass  # Ничего не делаем, метод - абстрактный

    def add_area(self, f):
        if not isinstance(f, Figure):
            raise ValueError("Параметр f не является фигурой!")
        return self.get_area() + f.get_area()

    def get_area():
        pass  # Ничего не делаем, метод - абстрактный
