import pytest
from main import somme


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (2.5, 3.5, 6.0),
        (-1, -1, -2),
        (-2, 3, 1),
        (0, 10, 10),
    ],
)
def test_somme_param(a, b, expected):
    assert somme(a, b) == pytest.approx(expected)
