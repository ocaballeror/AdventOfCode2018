import sys
from collections import defaultdict


sys.setrecursionlimit(3000)
doors = defaultdict(set)
distances = defaultdict(int)

def north(point):
    return point[0], point[1] - 1

def east(point):
    return point[0] + 1, point[1]

def west(point):
    return point[0] - 1, point[1]

def south(point):
    return point[0], point[1] + 1


import collections
def dijkstra():
    to_visit = collections.deque([((0, 0), 0)])
    distances = defaultdict(lambda: float('inf'))
    seen = set()
    while to_visit:
        position, distance = to_visit.popleft()
        for direction in doors[position]:
            room = move[direction](position)
            distances[room] = min(distances[room], distance + 1)
            if room not in seen:
                if not any(room == field[0] for field in to_visit):
                    to_visit.append((room, distance + 1))
        seen.add(position)

    return distances

move = {
    'N': north,
    'E': east,
    'W': west,
    'S': south,
}


def closing_bracket(string):
    """
    Return the index of the bracket that closes the first one in this string.
    """
    first = string.index('(')
    assert first != -1
    count = 0
    for i, c in enumerate(string[first:]):
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count == 0:
            return i + first
    raise ValueError('No matching bracket')


def bracket_groups(string):
    """
    Split a string by its | separator, keeping the subgroups intact.
    """
    assert string[0] == '('
    groups = []
    current = []
    i = 1
    while i < len(string):
        c = string[i]
        if c == ')':
            pass
        elif c == '(':
            close = closing_bracket(string[i:])
            current.extend(list(string[i:i+close] + ')'))
            i += close
        elif c == '|':
            if current:
                groups.append(''.join(current))
                current = ['']
            else:
                groups.append('')
        else:
            current.append(c)
        i += 1
    if current:
        groups.append(''.join(current))
    return groups



def simulate(regex, pos):
    for i, d in enumerate(regex):
        if d not in move:
            break
        doors[pos].add(d)
        pos = move[d](pos)
    else:
        return
    if d == '(':
        regex = regex[i:]
        close = closing_bracket(regex)
        groups = bracket_groups(regex[:close])
        for group in groups:
            simulate(group, pos)
        simulate(regex[close+1:], pos)
    else:
        raise ValueError('What is', d)


if __name__ == '__main__':
    with open('input') as f:
        read = f.read().strip()[1:-1]

    simulate(read, (0, 0))

    distances = dijkstra()
    room, distance = max(distances.items(), key=lambda x: x[1])
    far_rooms = sum(d >= 1000 for d in distances.values())
    print('Furthest room:', room)
    print('Distance:', distance)
    print('Rooms over 1000:', far_rooms)
