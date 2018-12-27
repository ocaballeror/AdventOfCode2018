GENERATIONS_1 = 20
GENERATIONS_2 = 50000000000


def crop(graph):
    """
    Make a status line have exactly 3 dots at the beginning and 3 at the end.

    Return the updated status, plus the number of dots added at the start.
    """
    delta = 0
    while not graph.endswith('#...'):
        if graph.endswith('....'):
            graph = graph[:-1]
        else:
            graph += '.'
    while not graph.startswith('...#'):
        if graph.startswith('....'):
            graph = graph[1:]
            delta -= 1
        else:
            graph = '.' + graph
            delta += 1
    return graph, delta


def read_input():
    with open('input') as f:
        content = list(map(str.strip, f.readlines()))

    initial = content[0].split(':')[1].strip()
    initial = '.' * 3 + initial + '.' * 3

    rules = {}
    for line in content[2:]:
        case, _, result = line.split()
        rules[case] = result

    return initial, rules


def value(state, start):
    """
    Return the value of any given state.
    """
    total = 0
    for number, pot in enumerate(state):
        if pot == '#':
            total += (number - start)
    return total


def process(initial_state, rules, generations):
    start = 3
    state = initial_state
    # print(0, state)
    for i in range(1, generations + 1):
        newstate = ['.'] * len(state)
        for rule, result in rules.items():
            pos = state.find(rule)
            while pos != -1:
                newstate[pos + 2] = result
                pos = state.find(rule, pos + 1)
        newstate = ''.join(newstate)
        newstate, delta = crop(newstate)
        if newstate == state:
            # print('stopped at generation', i)
            # print('delta:', delta)
            start += delta * (generations - i + 1)
            break
        state = newstate
        start += delta
        # print(i, state)

    return value(state, start)


if __name__ == '__main__':
    initial, rules = read_input()
    part1 = process(initial, rules, GENERATIONS_1)
    part2 = process(initial, rules, GENERATIONS_2)
    print('Part 1:', part1)
    print('Part 2:', part2)
