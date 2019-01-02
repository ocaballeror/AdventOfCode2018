import time
from collections import deque
from itertools import chain
import numpy as np


def reverse(point):
    return point[1], point[0]


def down(point):
    return point[0] + 1, point[1]


def up(point):
    return point[0] - 1, point[1]


def left(point):
    return point[0], point[1] - 1


def right(point):
    return point[0], point[1] + 1


def is_out(point, constraints):
    _, maxy, _, miny = constraints
    return point[0] >= maxy or point[0] < miny


def read_input(fountain=(500, 0), fname='input'):
    clay = set()
    with open(fname) as f:
        for line in f:
            first, second = line.strip().split()
            first = int(first.split('=')[1][:-1])
            second = second.split('=')[1].split('..')
            second = range(int(second[0]), int(second[1]) + 1)
            for s in second:
                if line.startswith('x'):
                    clay.add((first, s))
                else:
                    clay.add((s, first))

    clay.add(fountain)
    minx = min(clay, key=lambda x: x[0])[0]
    maxx = max(clay, key=lambda x: x[0])[0] + 3
    miny = min(clay, key=lambda x: x[1])[1]
    maxy = max(clay, key=lambda x: x[1])[1] + 1
    clay.remove(fountain)

    clay = set((c[0] + 1, c[1]) for c in clay)
    fountain = (fountain[0] + 1, fountain[1])
    # maxx -= minx
    # maxy -= miny
    # minx = 0
    # miny = 0

    state = np.full((maxy, maxx), '.')
    for y in range(maxy):
        for x in range(maxx):
            if (x, y) in clay:
                state[y, x] = '#'
            elif (x, y) == fountain:
                state[y, x] = '+'

    return state, fountain, (maxx, maxy, minx, miny)


def move_to_side(pointer, move, state):
    blocked_move = False
    water = set()
    while state[down(pointer)] in '~#' and state[pointer] != '#':
        water.add(pointer)
        # print(f'add {move.__name__}', pointer)
        pointer = move(pointer)
    if state[pointer] == '#':
        blocked_move = True
    return water, pointer, blocked_move


def run(state, fountain, constraints):
    flowing = set()
    stale = set()
    pointers = deque()
    pointers.append(down(reverse(fountain)))
    while pointers:
        pointer = pointers.pop()
        # print('pointer:', pointer)
        if is_out(pointer, constraints) or state[pointer] == '#':
            continue
        if state[pointer] == '.' and\
                (is_out(down(pointer), constraints) or state[down(pointer)] in '|.'):
            flowing.add(pointer)
            state[pointer] = '|'
            # print('add down')
            pointers.append(down(pointer))
        elif state[pointer] in '|.' and state[down(pointer)] in '~#':
            old_pointer = pointer
            water_r, pointer_r, blocked_r = move_to_side(pointer, right, state)
            water_l, pointer_l, blocked_l = move_to_side(pointer, left, state)
            if blocked_r and blocked_l:
                for w in chain(water_r, water_l):
                    state[w] = '~'
                stale.update(water_r)
                stale.update(water_l)
            else:
                for w in chain(water_r, water_l):
                    state[w] = '|'
                flowing.update(water_r)
                flowing.update(water_l)

            if blocked_r and blocked_l:
                pointers.append(up(old_pointer))
            if not blocked_r:
                pointers.append(pointer_r)
            if not blocked_l:
                pointers.append(pointer_l)

    clay = ((x, y) for y, r in enumerate(state)
            for x, c in enumerate(r) if c == '#')
    miny = min(clay, key=lambda x: x[1])[1]
    stale = set(reverse(s) for s in stale if s[0] >= miny)
    flowing = set(reverse(f) for f in flowing if f[0] >= miny)
    # print('\n'.join(''.join(t) for t in state))
    return flowing, stale


if __name__ == '__main__':
    gstate, gfountain, gconstraints = read_input()
    gflowing, gstale = run(gstate, gfountain, gconstraints)
    gwater = gstale | gflowing
    print('Part 1:', len(gwater))
    print('Part 2:', len(gstale))
