from src.Rectangle import Rectangle
import pytest

@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_rectangle_area_positive(create_rectangle, type_of_number):
    side_a, side_b  = create_rectangle(type_of_number=type_of_number)
    print(side_a, side_b)
    r = Rectangle(side_a, side_b)
    assert r.get_area == side_a*side_b


@pytest.mark.parametrize(
    ("side_a", "side_b"), [(0, 5), (-1, 5.5)], ids=["zero value", "negative value"]
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    ("side_a", "side_b", "perimeter"),
    [(3, 5, 16), (2.2, 5.5, 15.4)],
    ids=["integer_number_of_side_for_perimetr", "float_number_of_side_for_perimetr"],
)
def test_rectangle_perimeter(side_a, side_b, perimeter):
    # Вызов тестируемой функции
    rect = Rectangle(side_a, side_b)
    # Проверка результата
    assert rect.get_perimeter() == perimeter, (
        f"Expected perimetr should be {side_a * side_b}"
    )
