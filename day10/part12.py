from functools import reduce
from math import floor

OPEN = '([{<'
CLOSE = ')]}>'
POINTS_ILLEGAL = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
POINTS_COMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def parse_syntax(inp: str):
    stack = []
    for char in inp:
        if char in OPEN:
            stack.append(char)
        elif char in CLOSE:
            last_char = stack.pop()
            if OPEN.index(last_char) != CLOSE.index(char):
                raise ValueError(char)
    complete = ''
    for char in stack[::-1]:
        complete += CLOSE[OPEN.index(char)]

    return complete


def score_complete(inp: str):
    return reduce(lambda carry, char: carry * 5 + POINTS_COMPLETE[char], inp, 0)


def main():
    with open('input.txt', 'r') as fp:
        points_sum, compl_scores = 0, []
        for i, line in enumerate(fp):
            try:
                complete = parse_syntax(line)
                print('%d: Valid.' % (i,))
                compl_scores.append(score_complete(complete))
            except ValueError as e:
                illegal = str(e)
                points_sum += POINTS_ILLEGAL[illegal]
                print('%d: Illegal char "%s" [%d points]' % (i, illegal, POINTS_ILLEGAL[illegal]))

        print('Illegal sum: %d, Complete middle: %d' % (points_sum, sorted(compl_scores)[floor(len(compl_scores)/2)]))


if __name__ == '__main__':
    main()
