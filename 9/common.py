import re


def high_score(players, goal):
    marbles = [0]
    current_ball = 0
    current_player = 0
    scores = [0] * players

    for i in range(1, goal + 1):
        if i % 23 != 0:
            offset = ((current_ball + 2) % len(marbles))
            if offset == 0:
                offset = len(marbles)
            marbles.insert(offset, i)
            current_ball = offset
        else:
            current_ball -= 7
            if current_ball < 0:
                current_ball = len(marbles) + current_ball
            pop = marbles.pop(current_ball)
            scores[current_player] += (pop + i)
        current_player = (current_player + 1) % players

    return max(scores)


def parse_input():
    with open('input') as f:
        content = f.read()
        players, goal = re.findall(r'\d+', content)
        return int(players), int(goal)
