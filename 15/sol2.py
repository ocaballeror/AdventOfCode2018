from common import Unit
from common import read_input
from common import tick


def sol2(state, units):
    elf_attack_power = 3
    ini_elves = len([u for u in units if u.side == 'E'])
    ini_units = [Unit(u.x, u.y, u.side) for u in units]
    while True:
        units = [Unit(u.x, u.y, u.side) for u in ini_units]
        for u in units:
            if u.side == 'E':
                u.attack_power = elf_attack_power

        rounds = 0
        while True:
            units, full_round = tick(state, units)
            if full_round:
                rounds += 1
            new_elves = len([u for u in units if u.side == 'E'])
            if new_elves < ini_elves:
                elf_attack_power += 1
                print(f'stopped attack {elf_attack_power} at round {rounds}')
                break
            if len(set(u.side for u in units)) == 1:
                print('Elves won with attack power', elf_attack_power)
                hitpoints = sum(u.hp for u in units)
                score = rounds * hitpoints
                return rounds, hitpoints, score


if __name__ == '__main__':
    gstate, gunits = read_input()
    grounds, ghp, gscore = sol2(gstate, gunits)
    print(f'Rounds: {grounds}, Total HP: {ghp}, Score: {gscore}')
