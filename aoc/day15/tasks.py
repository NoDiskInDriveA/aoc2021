from __future__ import annotations
from collections import defaultdict, namedtuple
from functools import reduce
from collections.abc import Callable
from math import inf, sqrt
from timeit import default_timer as timer

DIM = 100

XY = namedtuple('XY', ['x', 'y'])


def get_input() -> dict[XY, int]:
    with open('input.txt', 'r') as fp:
        d = {}
        for (y, line) in enumerate(fp):
            d.update({XY(x, y): int(letter) for (x, letter) in enumerate(line.strip())})

    return d


def get_other_input() -> dict[XY, int]:
    # TODO this is meh
    with open('input.txt', 'r') as fp:
        d = {}
        for (y, line) in enumerate(fp):
            for dx in range(0, 5):
                for dy in range(0, 5):
                    d.update({XY(x + (dx * DIM), y + (dy * DIM)): int(letter) + dx + dy if (
                                int(letter) + dx + dy < 10) else (int(letter) + dx + dy - 9) for (x, letter) in
                              enumerate(line.strip())})

    return d


def expand_neighbors(d: dict[XY, int], of: XY) -> list[XY]:
    return list(
        filter(lambda xy: xy in d, (XY(of.x + dx, of.y + dy) for (dx, dy) in [(0, 1), (0, -1), (-1, 0), (1, 0)])))


def total_path_cost(d, came_from, current):
    cost = 0
    while current in came_from:
        cost += d[current]
        current = came_from[current]
    return cost


def a_star(d: dict[XY, int], start: XY, end: XY, h: Callable[XY]):
    # TODO replace open_set with an appropriate priority queue
    open_set = set[XY]()
    came_from = dict()

    g_score = defaultdict(lambda: inf)
    f_score = defaultdict(lambda: inf)

    f_score[start] = h(start)
    g_score[start] = 0
    open_set.add(start)

    while len(open_set) > 0:
        current = reduce(lambda xy1, xy2: xy1 if f_score[xy1] < f_score[xy2] else xy2, open_set)

        if current == end:
            return total_path_cost(d, came_from, current)

        open_set.remove(current)
        for neighbor in expand_neighbors(d, current):
            tentative_g_score = g_score[current] + d[neighbor]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                open_set.add(neighbor)

    raise Exception('No path found')


def first_task():
    d = get_input()
    print(a_star(d, XY(0, 0), XY(DIM - 1, DIM - 1), lambda xy: 0))


def second_task():
    d = get_other_input()
    start = timer()
    print(a_star(d, XY(0, 0), XY(DIM * 5 - 1, DIM * 5 - 1), lambda xy: sqrt((499 - xy.x) ^ 2 + (499 - xy.y) ^ 2)))
    end = timer()
    print(end - start)
    start = timer()
    print(a_star(d, XY(0, 0), XY(DIM * 5 - 1, DIM * 5 - 1), lambda xy: 0))
    end = timer()
    print(end - start)


def main():
    # first_task()
    second_task()


if __name__ == '__main__':
    main()
