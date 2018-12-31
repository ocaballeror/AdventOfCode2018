import time
from common import read_input
from common import tick
from common import draw_map


def sol1(state, units):
    rounds = 0
    while True:
        print(rounds, ':', sep='')
        draw_map(state, units)
        # time.sleep(1)
        units, full_round = tick(state, units)
        if full_round:
            rounds += 1
        if len(set(u.side for u in units)) == 1:
            hitpoints = sum(u.hp for u in units)
            score = rounds * hitpoints
            print(rounds, ':', sep='')
            draw_map(state, units)
            return rounds, hitpoints, score


if __name__ == '__main__':
    gstate, gunits = read_input()
    grounds, ghp, gscore = sol1(gstate, gunits)
    print(f'Rounds: {grounds}, Total HP: {ghp}, Score: {gscore}')
