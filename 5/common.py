def read_input():
    with open('input') as f:
        content = f.read().strip()
    return content


def react_polymer(polymer):
    marked = list(polymer)
    size = len(marked)
    i = 0
    while i < size-1:
        if i < 0:
            i = 0

        if marked[i] != marked[i+1] and\
                marked[i].lower() == marked[i+1].lower():
            del marked[i]
            del marked[i]
            i -= 2
            size -= 2
        i += 1

    return size
