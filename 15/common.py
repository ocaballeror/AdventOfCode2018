from pathfind import get_target
from pathfind import combine_state_units


class Unit:
    def __init__(self, x, y, side='E'):
        self.x = x
        self.y = y
        self.side = side
        self.attack_power = 3
        self.hp = 200

    def __repr__(self):
        return f"Unit({self.x}, {self.y}, '{self.side}', {self.hp})"

    def __eq__(self, other):
        if isinstance(other, tuple):
            return (self.x, self.y) == (other[0], other[1])
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        """
        "Less than" method for insertion in heapq's.
        """
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x

    def __hash__(self):
        return hash((self.x, self.y))

    def move(self, x, y):
        self.x = x
        self.y = y


def read_input(filename='input'):
    with open(filename) as f:
        state = [list(line.strip()) for line in f]

    units = []
    for y, row in enumerate(state):
        for x, col in enumerate(row):
            if col in ('G', 'E'):
                units.append(Unit(x, y, col))
                state[y][x] = '.'

    return state, units


def draw_map(state, units=None):
    if units:
        state = combine_state_units(state, units)
    print('\n'.join(''.join(t) for t in state))


def tick(state, units):
    pending = set(units)
    for unit in sorted(units):
        pending.remove(unit)
        if unit.side == 'X':
            continue

        target = get_target(unit, units, state)
        if target is None:
            continue

        target, move, distance = target
        if distance in (0, 1):
            index = units.index(target)
            enemy = units[index]
            enemy.hp -= unit.attack_power
            if enemy.hp <= 0:
                enemy.side = 'X'
                units.pop(index)
                if len(set(u.side for u in units).difference({'X'})) == 1:
                    unitsleft = [u for u in pending if u.side != 'X']
                    return units, (len(unitsleft) == 0)
        if distance == 0:
            continue
        unit.move(*(move))
    return units, True
