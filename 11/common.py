SIZE = 300


def calculate_power(coord, serial):
    x, y = coord
    rack = x + 10
    power = ((rack * y) + serial) * rack
    power = (power // 100) % 10
    return power - 5


def parse_input():
    with open('input') as f:
        serial = int(f.read())
    return serial


def compute_grid(serial):
    grid = [[calculate_power((x, y), serial) for y in range(SIZE)]
            for x in range(SIZE)]
    return grid
