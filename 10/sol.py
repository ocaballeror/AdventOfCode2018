"""
Solution to day 10.

To my knowledge, it is impossible to guess when the letters have been formed,
so the only way to get the answer is to run this module and wait for something
coherent to appear on screen. I recommend piping this to tee to save the output
to a file.

For part 2, the amount of seconds elapsed is shown after every print.
"""
import re
import sys
import time
import itertools


def draw(start_x, end_x, start_y, end_y, points):
    valid = False
    out = [['.'] * (end_x - start_x) for _ in range(end_y - start_y)]
    for x, y in points:
        if start_x <= x < end_x and start_y <= y < end_y:
            out[y - start_y][x - start_x] = '#'
            valid = True

    if not valid:
        return ''
    return '\n'.join(''.join(l) for l in out)


def move(points, velocities):
    for point, speed in zip(points, velocities):
        point[0] += speed[0]
        point[1] += speed[1]


def is_valid(start_x, end_x, start_y, end_y, points):
    return any(start_x <= p[0] <= end_x or
               start_y <= p[1] <= end_y for p in points)


def maybe_draw(start_x, end_x, start_y, end_y, points):
    if not is_valid(start_x, end_x, start_y, end_y, points):
        return ''
    msg = draw(start_x, end_x, start_y, end_y, points)
    if not msg:
        return ''
    return msg


def parse_input():
    points = []
    velocities = []
    with open('input') as f:
        for line in f:
            data = tuple(map(int, re.findall(r'-?\d+', line)))
            points.append([data[0], data[1]])
            velocities.append((data[2], data[3]))
    return points, velocities


def simulate():
    points, velocities = parse_input()
    for second in itertools.count():
        msg = maybe_draw(0, 300, 0, 150, points)
        move(points, velocities)
        if not msg:
            continue
        sys.stdout.write(f'{msg}\nTime: {second}s\n')
        time.sleep(.1)


if __name__ == '__main__':
    simulate()
