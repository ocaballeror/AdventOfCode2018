from itertools import chain
from common import tick
from common import read_input


if __name__ == '__main__':
    trees, lumber, clear = read_input()
    maxx = max(c[0] for c in chain(trees, lumber, clear)) + 1
    maxy = max(c[1] for c in chain(trees, lumber, clear)) + 1
    print(maxx, maxy)
    for minute in range(10):
        trees, lumber, clear = tick(trees, lumber, clear, maxx, maxy)
    res = len(trees) * len(lumber)
    print(f'{len(trees)} * {len(lumber)} = {res}')
