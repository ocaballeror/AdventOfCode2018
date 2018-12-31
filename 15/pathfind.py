import collections


def combine_state_units(state, units):
    """
    Overlap the units on top of the map.
    """
    state = [row.copy() for row in state]
    unit_coords = {(unit.x, unit.y): unit.side for unit in units}
    for y, row in enumerate(state):
        for x in range(len(row)):
            unit = unit_coords.get((x, y), None)
            if unit:
                state[y][x] = unit
    return state


def surrounding(point):
    if hasattr(point, 'x') and hasattr(point, 'y'):
        point = (point.x, point.y)
    directions = ((0, -1), (-1, 0), (1, 0), (0, 1))
    return [(point[0] + d[0], point[1] + d[1]) for d in directions]


def shortest_path(unit, targets, state):
    """
    Calculate the shortest path to the nearest target from the list of points
    specified as `targets`.

    Returns a tuple containing the nearest target, the next move needed to get
    there and the total distance of the path from the current node.
    """
    unit = (unit.x, unit.y)
    targets = set(s for t in targets for s in surrounding(t))
    to_visit = collections.deque([(unit, 0)])
    distances = {unit: (0, None)}
    occupied = set((x, y) for (y, row) in enumerate(state)
                   for (x, col) in enumerate(row) if col not in ('.', 'X'))
    targets.difference_update(occupied)
    seen = set()
    while to_visit:
        position, distance = to_visit.popleft()
        for neighbor in surrounding(position):
            if neighbor in occupied:
                continue

            candidate = (distance + 1, (position[1], position[0]))
            dist = distances.get(neighbor, None)
            if dist is None or \
                    candidate < (dist[0], (dist[1][1], dist[1][0])):
                distances[neighbor] = (distance + 1, position)

            if neighbor not in seen:
                if not any(neighbor == field[0] for field in to_visit):
                    to_visit.append((neighbor, distance + 1))
        seen.add(position)

    results = [(distance, position)
               for position, (distance, via) in distances.items()
               if position in targets]
    if not results:
        return None

    distance, target = min(results, key=lambda x: (x[0], (x[1][1], x[1][0])))
    closest = target
    while distances[closest][0] > 1:
        _, closest = distances[closest]
    return target, closest, distance


def get_enemies(unit, all_units, stateunits):
    """
    Get the list of possible enemies to target.
    If there are one or more enemies right in range, the returned list will
    contain only those, and exclude everything else.
    """
    coords = (unit.x, unit.y)
    candidates = [u for u in all_units if u.side not in (unit.side, 'X')]
    candidate_coords = {(c.x, c.y): c for c in candidates}
    enemies = set()

    for block in surrounding(coords):
        if block in candidate_coords:
            enemies.add(candidate_coords[block])
    if not enemies:
        for cand in candidates:
            for tx, ty in surrounding(cand):
                if (tx, ty) == coords or stateunits[ty][tx] == '.':
                    enemies.add(cand)
    return list(enemies)


def get_target(unit, all_units, state):
    coords = (unit.x, unit.y)
    stateunits = combine_state_units(state, all_units)
    enemies = get_enemies(unit, all_units, stateunits)
    enemy_coords = {(e.x, e.y): e for e in enemies}
    if not enemies:
        return

    if enemies[0] in surrounding(unit):
        target, move, distance = coords, coords, 0
    else:
        # if the list doesn't just contain adjacent enemies, find the best path
        # to the nearest.
        shortest = shortest_path(unit, enemy_coords.keys(), stateunits)
        if not shortest:
            return None
        target, move, distance = shortest

    if distance in (0, 1):
        # convert the list of coordinates to a list of Unit and get the target
        # with the lowest hp
        enemies_in_range = [enemy_coords[p]
                            for p in surrounding(target) if p in enemy_coords]
        target = min(enemies_in_range, key=lambda x: x.hp)

    return target, move, distance
