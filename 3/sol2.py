import re
from collections import defaultdict


all_ids = set()
covered = {}
for ide, parsed in map(lambda i: i.split('@'), open('input')):
    lonely = True
    ide, parsed = ide.strip(), parsed.strip()
    left, top, width, height = map(int, re.sub(r'[,:x]', ' ', parsed).split())
    for x in range(left, left + width):
        for y in range(top, top + height):
            if (x, y) in covered:
                lonely = False
                all_ids = all_ids.difference({covered[(x, y)]})
            covered[(x, y)] = ide
    if lonely:
        all_ids.add(ide)

print(all_ids)
