from common import manhattan
from common import all_points
from common import start_x, end_x, start_y, end_y


def is_valid(coord):
    acc = 0
    for point in all_points:
        acc += manhattan(coord, point)
        if acc >= MAX:
            return False
    return True


def part2():
    good = []
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if is_valid((x, y)):
                good.append((x, y))
    return len(good)


MAX = 10000

print(part2())
