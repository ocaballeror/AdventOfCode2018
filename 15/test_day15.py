import tempfile
import pytest

from sol1 import sol1
from common import Unit
from common import get_target
from common import read_input
from pathfind import shortest_path


def load_from_string(string):
    with tempfile.NamedTemporaryFile(mode='w+') as tmp:
        tmp.write(string)
        tmp.flush()
        state, units = read_input(tmp.name)
    return state, units


def test_read_input():
    state, units = read_input()
    assert isinstance(units, list)
    assert len(units) > 0
    assert all(isinstance(u, Unit) for u in units)

    assert isinstance(state, list)
    assert len(state) > 0
    for row in state:
        assert isinstance(row, list)
        assert len(row) > 0


state1 = """\
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
"""

state2 = """\
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
"""

state3 = """\
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
"""
state4 = """\
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
"""
state5 = """\
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
"""
state6 = """\
#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
"""
state7 = """\
####
##E#
#GG#
####
"""

state8 = """\
#####
#GG##
#.###
#..E#
#.#G#
#.E##
#####
"""

state9 = """\
######################
#...................E#
#.####################
#....................#
####################.#
#....................#
#.####################
#....................#
###.##################
#EG.#................#
######################       
"""

state10 = """\
################
#.......G......#
#G.............#
#..............#
#....###########
#....###########
#.......EG.....#
################
"""

@pytest.mark.parametrize('state,score', [
    (state1, 27730),
    (state2, 36334),
    (state3, 39514),
    (state4, 27755),
    (state5, 28944),
    (state6, 18740),
    (state7, 13400),
    (state8, 13987),
    (state9, 13332),
    (state10, 18468),
])
def test_sol1(state, score):
    state, units = load_from_string(state)
    _, _, result = sol1(state, units)
    assert result == score


map1 = [
    list('######'),
    list('#E...#'),
    list('#.G..#'),
    list('#....#'),
    list('######'),
]
map2 = [
    list('######'),
    list('#....#'),
    list('#.E#G#'),
    list('#....#'),
    list('######'),
]
map3 = [
    list('######'),
    list('#..#.#'),
    list('#.E#G#'),
    list('#....#'),
    list('######'),
]
map4 = [
    list('########'),
    list('#.E#...#'),
    list('#..#.#.#'),
    list('#..#G#.#'),
    list('#..###.#'),
    list('#......#'),
    list('#......#'),
    list('#......#'),
    list('########'),
]
map5 = [
    list('#######'),
    list('#.G...#'),
    list('#...EG#'),
    list('#.#.#G#'),
    list('#..G#E#'),
    list('#.....#'),
    list('#######'),
]
map6 = [
    list('#########'),
    list('#.G.....#'),
    list('#.E.#...#'),
    list('#..##..G#'),
    list('#...##..#'),
    list('#...#...#'),
    list('#.G...G.#'),
    list('#.....G.#'),
    list('#########'),
]
map7 = [
    list('###############'),
    list('###.......##G.#'),
    list('###.....G.#GEG#'),
    list('##........G.G.#'),
    list('#####..G.....##'),
    list('#####.GEG...###'),
    list('##.#.GEG....###'),
    list('#........G..###'),
    list('###.........###'),
    list('##.......E..###'),
    list('#....##..EGE.##'),
    list('###..##...E...#'),
    list('###########..##'),
    list('###############'),
]
map8 = [
    list('###############'),
    list('#....#......###'),
    list('#.G.........#.#'),
    list('#.........G...#'),
    list('#.G.G.G...E#..#'),
    list('#..GEGE......##'),
    list('#..........####'),
    list('###############'),
]


@pytest.mark.parametrize('state, unit, expect', [
    (map1, (1, 1), ((2, 2), (2, 1), 1)),
    (map1, (1, 1), ((2, 2), (2, 1), 1)),
    (map1, (2, 2), ((1, 1), (2, 1), 1)),
    (map2, (2, 2), ((4, 1), (2, 1), 3)),
    (map3, (2, 2), ((4, 3), (2, 3), 3)),
    (map4, (2, 1), ((4, 2), (2, 2), 15)),
    (map5, (5, 3), ((5, 4), (5, 3), 0)),
    (map6, (2, 2), ((2, 1), (2, 2), 0)),
    (map7, (9, 9), ((9, 7), (9, 8), 1)),
    (map8, (2, 2), ((7, 5), (3, 2), 8)),
])
def test_get_target(state, unit, expect):
    state = '\n'.join(''.join(t) for t in state)
    state, units = load_from_string(state)
    # get the actual Unit from its coordinates
    for u in units:
        if (u.x, u.y) == unit:
            unit = u
            break
    else:
        raise ValueError('Unit', unit, 'not in map', units)
    assert get_target(unit, units, state) == expect


@pytest.mark.parametrize('state, unit, target, expect', [
    (map2, Unit(2, 2), [Unit(4, 2)], ((4, 1), (2, 1), 3)),
    (map3, Unit(2, 2), [Unit(4, 2)], ((4, 3), (2, 3), 3)),
    (map4, Unit(2, 1), [Unit(4, 3)], ((4, 2), (2, 2), 15)),
    (map8, Unit(2, 2), [Unit(4, 5), Unit(6, 5), Unit(10, 4)],
     ((7, 5), (3, 2), 8)),
])
def test_dijkstra(state, unit, target, expect):
    assert shortest_path(unit, target, state) == expect
