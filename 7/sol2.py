from heapq import heapreplace

from common import read_input


dependencies = read_input()

WORKERS = 5
TIME = 60
now = 0
pending = set(dependencies.keys())
# workers is a heap with the time when the first task will end
workers = [-1] * WORKERS
completed = {k: float('inf') for k in dependencies}
while pending:
    free = workers[0]
    if now < free:
        now = free
    avail = lambda k: all(completed[d] <= now for d in dependencies[k])
    waiting = [k for k in pending if avail(k)]
    if not waiting:
        now += 1
        continue
    pick = min(waiting)
    pending.remove(pick)
    eta = ord(pick) - 96 + TIME
    heapreplace(workers, eta + now)
    completed[pick] = eta + now

print(max(completed.values()))
