from src.Square import Square
import pytest

@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_square_area_positive(create_square, type_of_number):
    side_a = create_square(type_of_number=type_of_number)
    print(side_a)
    square = Square(side_a)
    assert square.get_area == side_a*side_a


@pytest.mark.parametrize(
    ("side_a"), [0, -1], ids=["zero value", "negative value"]
)
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize(
    ("side_a", "perimeter"),
    [(3, 12), (2.2, 8.8 )],
    ids=["integer_number_of_side_for_perimetr", "float_number_of_side_for_perimetr"],
)
def test_square_perimeter(side_a, perimeter):
    # Вызов тестируемой функции
    square = Square(side_a)
    # Проверка результата
    assert square.get_perimeter() == perimeter, (
        f"Expected perimeter should be {perimeter}"
    )
