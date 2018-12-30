from common import add_recipes


def endswith(recipes, pattern, double=False):
    if len(recipes) < len(pattern):
        return False

    end = recipes[-len(pattern):]
    if ''.join(map(str, end)) == pattern:
        return True

    if not double:
        return False

    end = recipes[-len(pattern)-1:-1]
    return ''.join(map(str, end)) == pattern


def sol2(target):
    recipes = [3, 7]
    first = 0
    second = 1
    double = add_recipes(recipes, first, second)
    while not endswith(recipes, target, double=double):
        double = add_recipes(recipes, first, second)
        first = (first + recipes[first] + 1) % len(recipes)
        second = (second + recipes[second] + 1) % len(recipes)

    return len(recipes) - len(target)


if __name__ == '__main__':
    with open('input') as f:
        target = f.read().strip()
    sol = sol2(target)
    print(sol)
