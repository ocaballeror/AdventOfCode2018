from itertools import product
from common import compute_grid
from common import parse_input
from common import SIZE


def highest_power(grid, cell_size):
    best = None
    highest = -float('inf')
    for x, y in product(range(SIZE-cell_size), repeat=2):
        value = 0
        for i, j in product(range(cell_size), repeat=2):
            value += grid[x+i][y+j]
        if value > highest:
            highest = value
            best = (x, y)
    return best, highest


if __name__ == '__main__':
    serial = parse_input()
    grid = compute_grid(serial)
    print(highest_power(grid, 3)[0])
