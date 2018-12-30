from common import add_recipes


def print_status(recipes, first, second):
    out = ''
    for i, elem in enumerate(recipes):
        if i == first:
            surround = '()'
        elif i == second:
            surround = '[]'
        else:
            surround = '  '
        out += '{}{}{}'.format(surround[0], elem, surround[1])
    print(out)


def sol1(target):
    extra = 10

    recipes = [3, 7]
    first = 0
    second = 1
    # print_status(recipes, first, second)
    add_recipes(recipes, first, second)
    while len(recipes) < target + extra:
        # print_status(recipes, first, second)
        add_recipes(recipes, first, second)
        first = (first + recipes[first] + 1) % len(recipes)
        second = (second + recipes[second] + 1) % len(recipes)

    return ''.join(map(str, recipes[target:target+10]))


if __name__ == '__main__':
    with open('input') as f:
        target = int(f.read().strip())
    sol = sol1(target)
    print(sol)
