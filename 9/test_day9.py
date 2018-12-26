import pytest
from common import high_score


@pytest.mark.parametrize('players,goal,score', [
    (9, 25, 32),
    (9, 48, 63),
    (1, 48, 95),
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305)
])
def test_high_score(players, goal, score):
    assert high_score(players, goal) == score
