import pytest
from sol1 import sol1
from sol2 import sol2
from sol2 import endswith


@pytest.mark.parametrize('target,expected', [
    (9, '5158916779'),
    (5, '0124515891'),
    (18, '9251071085'),
    (2018, '5941429882'),
])
def test_sol1(target, expected):
    assert sol1(target) == expected


@pytest.mark.parametrize('recipes, pattern, expect', [
    ([1], '1234', False),
    ([1, 2, 3], '123', True),
    ([1, 2, 3, 4, 5, 6], '6', True),
    ([1, 2, 3, 4, 5, 6], '56', True),
    ([1, 2, 3, 4, 5, 6], '456', True),
    ([1, 2, 3, 4, 5, 6], '457', False),
    ([1, 2, 3, 4, 5, 6], '345', False),
])
def test_endswith(recipes, pattern, expect):
    assert endswith(recipes, pattern) == expect


@pytest.mark.parametrize('recipes, pattern, expect', [
    ([1], '1234', False),
    ([1, 2, 3], '123', True),
    ([1, 2, 3, 4, 5, 6], '6', True),
    ([1, 2, 3, 4, 5, 6], '56', True),
    ([1, 2, 3, 4, 5, 6], '456', True),
    ([1, 2, 3, 4, 5, 6], '457', False),
    ([1, 2, 3, 4, 5, 6], '345', True),
])
def test_endswith_double(recipes, pattern, expect):
    assert endswith(recipes, pattern, double=True) == expect


@pytest.mark.parametrize('target, expect', [
    ('51589', 9),
    ('01245', 5),
    ('92510', 18),
    ('59414', 2018),
])
def test_sol2(target, expect):
    assert sol2(target) == expect
