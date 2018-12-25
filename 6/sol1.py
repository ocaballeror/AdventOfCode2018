from collections import defaultdict
from common import manhattan
from common import all_points
from common import start_x, end_x, start_y, end_y


def nearest_point(coord):
    nearest = None
    smallest = float('inf')
    duplicate = False
    for point in all_points:
        distance = manhattan(point, coord)
        if distance == smallest:
            duplicate = True
        elif distance < smallest:
            duplicate = False
            smallest = distance
            nearest = point
    return nearest if not duplicate else None


def is_finite(point):
    x, y = point
    left = start_x, y
    right = end_x, y
    up = x, start_y
    down = x, end_y
    for test in (left, right, up, down):
        if nearest_point(test) == point:
            return False
    return True


def part1():
    valid_points = [p for p in all_points if is_finite(p)]
    area = defaultdict(int)
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            nearest = nearest_point((x, y))
            if nearest in valid_points:
                area[nearest] += 1

    return max(area.values())


print(part1())
