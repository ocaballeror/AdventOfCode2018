import os
import tempfile
from datetime import datetime
from datetime import timedelta
from collections import defaultdict

def chunks(fname):
    n = -1
    f = open(fname)
    lines = []
    for l in f:
        if 'Guard' in l:
            if n != -1 and lines:
                yield n, lines
            lines = []
            n = int(l.split()[3][1:])
        else:
            lines.append(l.strip())
    f.close()


def sort_input():
    tmp = tempfile.mktemp()
    os.system('sort input > ' + tmp)
    return tmp

def calculate_naps():
    naps = defaultdict(lambda: defaultdict(int))
    tmp = sort_input()
    for n, lines in chunks(tmp):
        asleep = None
        for line in lines:
            dt, msg = line.split(']')
            dt = datetime.strptime(dt, '[%Y-%m-%d %H:%M')
            if not asleep and 'asleep' in msg:
                asleep = dt
            elif asleep and 'wakes' in msg:
                while asleep < dt:
                    naps[n][asleep.minute] += 1
                    asleep += timedelta(minutes=1)
                asleep = None
    return naps
