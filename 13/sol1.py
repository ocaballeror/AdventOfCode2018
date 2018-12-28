"""
DAY 13

The map is represented as an array, containing all the track pieces, using
their original character representation, with a few exceptions:
    1. The carts are removed from the map and stored in a separate array.
    # 2. Empty space is replace by an empty string for easier conversion to bool.
    3. Empty space at the end is removed.

The carts are stored as an array of tuples in the format:
    (y_position, x_position, direction, last_turn)
Where the direction is one of the four characters used to represent the cart in
the original example, and last_turn is an integer representing the action taken
in the last crossroad. 0 means it will turn left the next time, 1 straight and
2 left.

The y position is stored first so that we can use the carts array as a heap,
and get the upper most cart in an efficient way.
"""
import time

from common import draw
from common import simulate
from common import parse_input

def run(tracks, carts):
    while True:
        draw(tracks, carts)
        carts, collisions = simulate(tracks, carts)
        if collisions:
            return collisions
        time.sleep(.05)


if __name__ == '__main__':
    tracks, carts = parse_input()
    collision = run(tracks, carts)
    draw(tracks, carts, collision)
    if len(collision) == 1:
        collision = list(collision)[0]
    print('Collision at', collision)
