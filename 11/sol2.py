from itertools import product

import numpy as np
from common import parse_input
from common import compute_grid
from common import SIZE

try:
    from tqdm import trange
except ImportError:
    trange = range


def best_square(serial):
    grid = compute_grid(serial)
    sums = np.zeros((SIZE, SIZE, SIZE)).astype(int)
    best = None
    highest = -float('inf')
    for size in trange(1, SIZE + 1):
        for x, y in product(range(SIZE-size), repeat=2):
            power = sums[x, y, size-1] + sums[x+1, y+1, size-1] -\
                sums[x+1, y+1, size-2] + grid[x+size-1][y] + grid[x][y+size-1]
            sums[x, y, size] = power
            if power > highest:
                highest = power
                best = (x, y, size)
    return highest, best


if __name__ == '__main__':
    serial = parse_input()
    r = best_square(serial)
    print(r[1])
