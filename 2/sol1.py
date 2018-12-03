from collections import Counter
counts = {'2': 0, '3': 0}
for l in open('input'):
    c = Counter(l)
    counts['2'] += int(2 in c.values())
    counts['3'] += int(3 in c.values())

sol = counts['2'] * counts['3']
print(f'{counts["2"]} * {counts["3"]} = {sol}')
# print(counts['2'] * counts['3'])
