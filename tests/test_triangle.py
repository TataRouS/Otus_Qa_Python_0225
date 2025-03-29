import math

from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_triangle_area_positive(create_triangle, type_of_number):
    side_a, side_b, side_c = create_triangle(type_of_number=type_of_number)
    print(side_a, side_b, side_c)
    triangle = Triangle(side_a, side_b, side_c)
    p = triangle.get_perimeter()
    assert triangle.get_area() == math.sqrt(
        p * (p - side_a) * (p - side_b) * (p - side_c)
    )


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [(0, 5, 5), (-1, 5.5, 5)],
    ids=["zero value", "negative value"],
)
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "perimeter"),
    [(3, 5, 5, 13), (2.2, 5.5, 5, 12.7)],
    ids=["integer_number_of_side_for_perimetr", "float_number_of_side_for_perimetr"],
)
def test_triangle_perimeter(side_a, side_b, side_c, perimeter):
    # Вызов тестируемой функции
    triangle = Triangle(side_a, side_b, side_c)
    # Проверка результата
    assert triangle.get_perimeter() == perimeter, (
        f"Expected perimeter should be {perimeter}"
    )
