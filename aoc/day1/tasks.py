from functools import reduce
from collections import namedtuple

Agg = namedtuple('Agg', ['old', 'incs'], defaults=[None, 0])


def sum_window(window_size):
    with open('input.txt', 'r') as fp:
        numbers = [int(line.strip()) for line in fp]
        print(reduce(
            lambda agg, val: Agg(old=(new := sum(val)), incs=agg.incs + int(agg.old is not None and new > agg.old)),
            (numbers[start:start + window_size] for start in range(0, len(numbers) - window_size + 1)),
            Agg()
        ).incs)


def main():
    sum_window(1)
    sum_window(3)


if __name__ == '__main__':
    main()
