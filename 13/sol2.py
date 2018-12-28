from heapq import heappush

from common import simulate
from common import parse_input


def remove_cart(carts, x, y):
    """
    Remove one or more carts at the given coordinates. The carts array will
    keep its heap invariant.
    """
    new_carts = []
    for cart in carts:
        if cart[1] != x or cart[0] != y:
            heappush(new_carts, cart)
    return new_carts


def run(tracks, carts):
    while len(carts) > 1:
        carts, collisions = simulate(tracks, carts)
        for x, y in collisions:
            carts = remove_cart(carts, x, y)

    return carts


if __name__ == '__main__':
    tracks, carts = parse_input()
    carts = run(tracks, carts)
    last = carts[0]
    print('Last cart:', (last[1], last[0]))
