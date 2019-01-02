import tempfile
import pytest
import numpy as np

from day17 import read_input
from day17 import run


def read_string(string):
    state = []
    clay = set()
    for y, line in enumerate(string.strip().split('\n')):
        row = []
        for x, block in enumerate(line):
            row.append(block)
            if block == '#':
                clay.add((x, y))
            elif block == '+':
                fountain = (x, y)
        state.append(row)
    state = np.array(state)

    clay.add(fountain)
    minx = min(clay, key=lambda x: x[0])[0]
    maxx = max(clay, key=lambda x: x[0])[0] + 3
    miny = min(clay, key=lambda x: x[1])[1]
    maxy = max(clay, key=lambda x: x[1])[1] + 1
    clay.remove(fountain)

    clay = set((c[0] + 1, c[1]) for c in clay)
    # fountain = (fountain[0] + 1, fountain[1])

    print(fountain, maxx, maxy, minx, miny)
    return state, fountain, (maxx, maxy, minx, miny)


map1 = """\
..+..
#....
#....
#....
#....
"""
map2 = """\
..+..
#....
..#..
"""
map3 = """\
..+..
#....
.....
.###.
"""
map4 = """\
..+..
.#...
.#...
.###.
"""
map5 = """\
#.+..
.....
.#.#.
.###.
"""
map6 = """\
#..+..
......
..#...
..#.#.
..###.
"""
map7 = """\
#..+...
.......
.#...#.
.#####.
"""
map8 = """\
#.+......
.........
.........
..###....
.........
.........
.........
.#######.
"""
map9 = """\
#.....+..
.........
.#.....#.
.#.#.#.#.
.#.###.#.
.#.....#.
.#######.
"""
map10 = """\
#...+....
.........
.#.....#.
.#.#.#.#.
.#.###.#.
.#.....#.
.#######.
"""
map11 = """\
#...+..
.......
.###.#.
.#...#.
.#...#.
.#####.
"""
map12 = """\
#+.....
.......
.###.#.
.#...#.
.#...#.
.#####.
"""


@pytest.mark.parametrize('state,expect', [
    (map1, 4),
    (map2, 5),
    (map3, 8),
    (map4, 5),
    (map5, 10),
    (map6, 7),
    (map7, 14),
    (map8, 23),
    (map9, 34),
    (map10, 34),
    (map11, 22),
    (map12, 22),
], ids=[
    'Basic fall down',
    'Basic overflow',
    'Multiple overflow',
    'Overflow and fall to one side',
    'Single cup hold',
    'Cup hold and overflow to one side',
    'Bigger cup hold',
    'Double fall on still water',
    'Nested cup hold',
    'Nested cup hold 2',
    'The cage',
    'The cage 2',
])
def test_run(state, expect):
    with tempfile.NamedTemporaryFile(mode='w+') as tmp:
        tmp.write(state)
        tmp.flush()
        state, fountain, constraints = read_string(state)

    print('\n'.join(''.join(t) for t in state))
    flowing, stale = run(state, fountain, constraints)
    print('\n'.join(''.join(t) for t in state))
    assert len(flowing | stale) == expect
