from itertools import chain
from common import tick
from common import read_input


if __name__ == '__main__':
    MAX = 1000000000
    trees, lumber, clear = read_input()
    maxx = max(c[0] for c in chain(trees, lumber, clear)) + 1
    maxy = max(c[1] for c in chain(trees, lumber, clear)) + 1
    seen = set()
    pattern = []
    recording = False
    for minute in range(1, MAX):
        trees, lumber, clear = tick(trees, lumber, clear, maxx, maxy)
        res = len(trees) * len(lumber)
        if res in seen:
            if not recording:
                recording = True
                pattern = [res]
            else:
                if res == pattern[0]:
                    target = (MAX - minute) % len(pattern)
                    print(pattern[target])
                    break
                else:
                    pattern.append(res)
        else:
            recording = False
        print(res, res in seen)
        seen.add(res)
