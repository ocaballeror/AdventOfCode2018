def first_repeat():
    seen = set()
    acc = 0
    seen.add(acc)
    with open('input') as f:
        numbers = list(map(int, f))

    while True:
        for n in numbers:
            acc += n
            print(acc)
            if acc in seen:
                return acc
            seen.add(acc)


print('first is', first_repeat())
