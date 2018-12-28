from heapq import heapify, heappush, heappop


def parse_input():
    """
    Reads the input and returns separate lists for the map and the carts.
    """
    carts = []
    tracks = []
    with open('input') as f:
        for line in f:
            line = line.rstrip()
            track = []
            for i, c in enumerate(line):
                if c not in ('<', '>', '^', 'v'):
                    char = c
                else:
                    if i != 0 and tracks and i < len(tracks[-1]) and \
                            tracks[-1][i] in ('|', '+') and \
                            line[i-1] in ('-', '+'):
                        char = '+'
                    else:
                        if c in ('<', '>'):
                            char = '-'
                        else:
                            char = '|'
                    carts.append((len(tracks), i, c, 0))
                track.append(char)
            tracks.append(track)

    heapify(carts)
    return tracks, carts


movement = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1),
}

back_curve = {
    '>': 'v',
    '<': '^',
    '^': '<',
    'v': '>',
}

forward_curve = {
    '>': '^',
    '<': 'v',
    '^': '>',
    'v': '<',
}

turn_left = {
    '>': '^',
    '<': 'v',
    '^': '<',
    'v': '>',
}

turn_right = {
    '>': 'v',
    '<': '^',
    '^': '>',
    'v': '<',
}


def move(cart, tracks):
    y, x, direction, turn = cart
    delta_x, delta_y = movement[direction]
    x, y = x + delta_x, y + delta_y

    pos = tracks[y][x]
    if pos == '\\':
        direction = back_curve[direction]
    elif pos == '/':
        direction = forward_curve[direction]
    elif pos == '+':
        if turn == 0:
            direction = turn_left[direction]
        elif turn == 2:
            direction = turn_right[direction]
        turn = (turn + 1) % 3
    return y, x, direction, turn


def simulate(tracks, carts):
    """
    Move the carts one by one as specified by the problem.
    Note that the carts array is assumed to be heapified.

    Return the new list of carts and the list of collisions that ocurred.
    """
    collisions = set()
    spots = set((c[1], c[0]) for c in carts)
    new_carts = []
    while carts:
        cart = heappop(carts)
        y, x, = cart[0:2]
        if (x, y) in collisions:
            continue
        spots.remove((x, y))

        new_cart = move(cart, tracks)
        y, x = new_cart[0:2]
        if (x, y) in spots:
            collisions.add((x, y))
            spots.add((x, y))
            continue
        spots.add((x, y))
        heappush(new_carts, new_cart)

    carts = new_carts
    return carts, collisions


def draw(tracks, carts, collisions=None):
    tracks = [t.copy() for t in tracks]
    for cart in carts:
        y, x, direction, _ = cart
        tracks[y][x] = direction
    if not collisions:
        collisions = []
    for collision in collisions:
        x, y = collision
        tracks[y][x] = 'X'
    print('\n'.join(''.join(t) for t in tracks))
