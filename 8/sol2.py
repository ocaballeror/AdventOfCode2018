def get_value(numbers):
    nodes = numbers[0]
    mt_entries = numbers[1]

    total = 0
    offset = 2
    values = {}
    for i in range(nodes):
        entries, value = get_value(numbers[offset:])
        offset += entries
        values[i] = value

    for entry in numbers[offset:offset+mt_entries]:
        if nodes == 0:
            total += entry
        else:
            total += values.get(entry-1, 0)
        offset += 1
    return offset, total


with open('input') as f:
    numbers = list(map(int, f.read().strip().split()))

node_count, node_value = get_value(numbers)
print(node_value)
