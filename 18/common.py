def read_input():
    trees = set()
    lumber = set()
    clear = set()
    i = j = 0
    with open('input') as f:
        for i, line in enumerate(f):
            for j, block in enumerate(line):
                if block == '.':
                    clear.add((j, i))
                elif block == '|':
                    trees.add((j, i))
                elif block == '#':
                    lumber.add((j, i))
    return trees, lumber, clear


def adjacent(coord, maxx, maxy):
    """
    Return the list of points that are adjacent to this coord and are inside
    the height and width constraints
    """
    for movex, movey in ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                         (0, 1), (1, -1), (1, 0), (1, 1)):

        newx = coord[0] + movex
        newy = coord[1] + movey
        if 0 <= newx < maxx and 0 <= newy < maxy:
            yield (newx, newy)


def tick(trees, lumber, clear, maxx, maxy):
    """
    Calculate the transformations that will occur in one minute to the given
    set of blocks and return the new state of the forest
    """
    newtrees = set()
    newlumber = set()
    newclear = set()
    for x in range(maxx + 1):
        for y in range(maxy + 1):
            coord = (x, y)
            lumbercount = 0
            treecount = 0
            for c in adjacent(coord, maxx, maxy):
                if c in lumber:
                    lumbercount += 1
                elif c in trees:
                    treecount += 1
            if coord in clear:
                if treecount >= 3:
                    newtrees.add(coord)
                else:
                    newclear.add(coord)
            elif coord in trees:
                if lumbercount >= 3:
                    newlumber.add(coord)
                else:
                    newtrees.add(coord)
            elif coord in lumber:
                if lumbercount >= 1 and treecount >= 1:
                    newlumber.add(coord)
                else:
                    newclear.add(coord)
    return newtrees, newlumber, newclear
