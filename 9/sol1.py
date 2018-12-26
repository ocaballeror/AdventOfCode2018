import sys

from common import parse_input, high_score

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        args = list(map(int, sys.argv[1:]))
    else:
        args = parse_input()
    print(high_score(args[0], args[1]))
