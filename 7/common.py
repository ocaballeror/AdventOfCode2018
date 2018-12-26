import re
from collections import defaultdict


def read_input():
    steps = defaultdict(list)
    with open('input') as f:
        for line in f:
            line = line.strip().lower()
            a, b = re.findall('step (.)', line)
            steps[b].append(a)
            if a not in steps:
                # create an entry for the newly mentioned step
                steps[a] = []
    steps = {k: steps[k] for k in sorted(steps.keys(), reverse=True)}
    return steps
