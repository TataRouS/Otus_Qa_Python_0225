from abc import ABC

# Абстрактный класс
class Figure(ABC):
    def __init__(self):
        pass  # Ничего не делаем, метод - абстрактный

    def get_perimeter(self):
        pass  # Ничего не делаем, метод - абстрактный

    def add_area(self, f):
        pass
