OPEN = '([{<'
CLOSE = ')]}>'
POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def check_syntax(inp: str):
    stack = []
    for char in inp:
        if char in OPEN:
            stack.append(char)
        elif char in CLOSE:
            last_char = stack.pop()
            if OPEN.index(last_char) != CLOSE.index(char):
                return char
    return None


def main():
    with open('input.txt', 'r') as fp:
        points_sum = 0;
        for i, line in enumerate(fp):
            illegal = check_syntax(line)
            if illegal is not None:
                points_sum += POINTS[illegal]
                print('%d: Illegal char "%s" [%d points]' % (i, illegal, POINTS[illegal]))
            else:
                print('%d: Valid.' % (i,))
        print('Points: %s' % (points_sum,))


if __name__ == '__main__':
    main()
