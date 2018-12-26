from common import read_input


def pop_step(pop, steps):
    """
    Remove a step from the dictionary and all its appearances as a dependency
    for other steps.
    """
    for step, depends in steps.items():
        depends = [d for d in depends if d != pop]
        steps[step] = depends
    if pop in steps:
        del steps[pop]


def iterate_steps(steps):
    """
    Walk the list of steps and return them in order of dependency.
    """
    pop = None
    while steps:
        for step, depends in steps.items():
            if depends == []:
                pop = step
        if not pop:
            return
        pop_step(pop, steps)
        yield pop


def part1():
    steps = read_input()
    return ''.join(iterate_steps(steps))


print(part1())
