import pytest

from day20 import bracket_groups


@pytest.mark.parametrize('string,expect', [
    ('(ab|cd)', ['ab', 'cd']),
    ('(ab|)', ['ab', '']),
    ('(ab|c(d|e))', ['ab', 'c(d|e)']),
    ('(ab|c(de|f)h)', ['ab', 'c(de|f)h']),
    ('(ab|c(de|f(g|))h)', ['ab', 'c(de|f(g|))h']),
])
def test_bracket_groups(string, expect):
    assert bracket_groups(string) == expect
