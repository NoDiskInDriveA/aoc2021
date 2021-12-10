from functools import reduce
from collections import namedtuple
WINDOW_SIZE = 3
Agg = namedtuple('Agg', ['old', 'incs'], defaults=[None, 0])


def main():
    with open('input.txt', 'r') as fp:
        numbers = [int(line.strip()) for line in fp]
        print(reduce(
            lambda agg, val: Agg(old=(new := sum(val)), incs=agg.incs + int(agg.old is not None and new > agg.old)),
            (numbers[start:start + WINDOW_SIZE] for start in range(0, len(numbers) - WINDOW_SIZE + 1)),
            Agg()
        ).incs)


if __name__ == '__main__':
    main()
