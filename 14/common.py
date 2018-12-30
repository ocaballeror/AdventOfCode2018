def add_recipes(recipes, first, second):
    """
    Add the corresponding recipes to the list.

    Returns False if only one recipe was added and True otherwise.
    """
    total = recipes[first] + recipes[second]
    if total < 10:
        recipes.append(total)
        return False
    else:
        recipes.append(total // 10)
        recipes.append(total % 10)
        return True
