from common import calculate_naps

naps = calculate_naps()

best = 0
best_guard = -1
best_minute = -1
for guard, minutes in naps.items():
    total = sum(minutes.values())
    if total > best:
        best = total
        best_guard = guard
        best_minute = max(minutes, key=lambda x: minutes[x])

sol = best_guard * best_minute
print(f'{best_guard} * {best_minute} = {sol}')
