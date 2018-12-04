from common import calculate_naps

naps = calculate_naps()

best = 0
best_guard = -1
best_minute = -1
for guard, minutes in naps.items():
    most = max(minutes, key=lambda x: minutes[x])
    if minutes[most] > best:
        best = minutes[most]
        best_guard = guard
        best_minute = most

sol = best_guard * best_minute
print(f'{best_guard} * {best_minute} = {sol}')
