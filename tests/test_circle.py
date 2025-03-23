from src.Circle import Circle
import math
import pytest


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_circle_area_positive(create_circle, type_of_number):
    radius = create_circle(type_of_number=type_of_number)
    print(radius)
    circle = Circle(radius)
    assert circle.get_area == math.pi*radius*radius

@pytest.mark.parametrize(
    "radius", [0, -1], ids=["zero value", "negative value"]
)
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize(
    ("radius", "perimeter"),
    [(3, 18.84), (2.2, 13.82)],
    ids=["integer_number_of_side_for_perimetr", "float_number_of_side_for_perimetr"],
)
def test_circle_perimeter(radius, perimeter):
    # Вызов тестируемой функции
    circle = Circle(radius)
    # Проверка результата
    assert circle.get_perimeter() == perimeter, f"Expected perimeter should be {radius}"
