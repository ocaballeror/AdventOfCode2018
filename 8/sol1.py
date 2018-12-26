def count_entries(numbers):
    """
    Recursive function.

    On each call, it returns the total value of the current node's metadata
    entries, and the offset, i.e. the amount of numbers that this node spans
    over.
    """
    nodes = numbers[0]
    mt_entries = numbers[1]

    total = 0
    offset = 2
    for _ in range(nodes):
        entries, value = count_entries(numbers[offset:])
        offset += entries
        total += value

    for entry in numbers[offset:offset+mt_entries]:
        total += entry
        offset += 1
    return offset, total


with open('input') as f:
    numbers = list(map(int, f.read().split()))

node_count, metadata_sum = count_entries(numbers)
print(metadata_sum)
