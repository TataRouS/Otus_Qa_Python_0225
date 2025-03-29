from src.Square import Square
import pytest


@pytest.mark.parametrize(
    "type_of_figures",
    [
        ("Circle", "Circle"),
        ("Rectangle", "Circle"),
        ("Square", "Circle"),
        ("Triangle", "Circle"),
    ],
)
def test_add_area_positive(create_figure, type_of_figures):
    first_figure = create_figure(type_of_figure=type_of_figures[0])
    second_figure = create_figure(type_of_figure=type_of_figures[1])
    area = first_figure.add_area(second_figure)
    assert area == first_figure.get_area() + second_figure.get_area()


@pytest.mark.parametrize("f", [5, "figure"], ids=["integer", "string"])
def test_add_area_negative(f):
    first_figure = Square(5)
    with pytest.raises(ValueError):
        first_figure.add_area(f)
