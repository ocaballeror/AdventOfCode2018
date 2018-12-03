import re
from collections import defaultdict


covered = defaultdict(int)
for parsed in map(lambda i: i.split('@')[1].strip(), open('input')):
    left, top, width, height = map(int, re.sub(r'[,:x]', ' ', parsed).split())
    for x in range(left, left + width):
        for y in range(top, top + height):
            covered[(x, y)] += 1

print(len([k for k, v in covered.items() if v > 1]))
