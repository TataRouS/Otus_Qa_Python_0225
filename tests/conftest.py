import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture()
def create_figure():
    def _wrapper(type_of_figure: str):
        if type_of_figure == "Circle":
            return Circle(5)
        elif type_of_figure == "Rectangle":
            return Rectangle(5, 5)
        elif type_of_figure == "Square":
            return Square(5)
        elif type_of_figure == "Triangle":
            return Triangle(5, 5, 5)
        else:
            raise ValueError(f"type must be figure")
    yield _wrapper

@pytest.fixture()
def create_square():
    def _wrapper(type_of_number: str):
        if type_of_number == "integer":
            return 3
        elif type_of_number == "float":
            return 3.5
        else:
            raise ValueError(f"sides must be integer or float")
    yield _wrapper

@pytest.fixture()
def create_triangle():
    def _wrapper(type_of_number: str):
        if type_of_number == "integer":
            return 3, 3, 3
        elif type_of_number == "float":
            return 2.2, 2.2, 2.2
        else:
            raise ValueError(f"sides must be integer or float")

    yield _wrapper


@pytest.fixture()
def create_circle():
    def _wrapper(type_of_number: str):
        if type_of_number == "integer":
            return 3
        elif type_of_number == "float":
            return 2.2
        else:
            raise ValueError(f"sides must be integer or float")

    yield _wrapper

@pytest.fixture()
def create_rectangle():
    def _wrapper(type_of_number: str):
        if type_of_number == "integer":
            return 3, 5
        elif type_of_number == "float":
            return 3.5, 5.5
        else:
            raise ValueError(f"sides must be integer or float")

    yield _wrapper
