from collections import namedtuple
from functools import reduce

Point = namedtuple('Point', ['x', 'y'])
Fold = namedtuple('Fold', ['axis', 'position'])


def get_input() -> tuple[set[Point], list[Fold]]:
    with open('input.txt', 'r') as fp:
        points, folds = set(), list()
        for line in fp:
            if line.strip() == '':
                break
            points.add(Point(*[int(n) for n in line.strip().split(',')]))
        for line in fp:
            eq = line.strip().index('=')
            folds.append(Fold(line.strip()[eq - 1], int(line.strip()[eq + 1:])))
    return points, folds


def fold_x(points: set[Point], x: int) -> set[Point]:
    return set(map(lambda p: Point(2 * x - p.x if p.x >= x else p.x, p.y), points))


def fold_y(points: set[Point], y: int) -> set[Point]:
    return set(map(lambda p: Point(p.x, 2 * y - p.y if p.y >= y else p.y), points))


def fold(points: set[Point], f: Fold) -> set[Point]:
    if f.axis == 'x':
        return fold_x(points, f.position)
    elif f.axis == 'y':
        return fold_y(points, f.position)
    else:
        raise ValueError('Unknown axis %s' % f.axis)


def display_points(points: set[Point], scale_x: int = 1):
    (max_x, max_y) = reduce(lambda c, p: Point(max(c.x, p.x), max(c.y, p.y)), points)
    display = ''
    for y in range(0, max_y + 1):
        display += ''.join(
            ['▓' * scale_x if Point(x, y) in points else ' ' * scale_x for x in range(0, max_x + 1)]) + "\n"
    print(display)


def first_task():
    points, folds = get_input()
    for f in folds[0:1]:
        points = fold(points, f)
    print(len(points))


def second_task():
    points, folds = get_input()
    for f in folds:
        points = fold(points, f)
    display_points(points)


def main():
    first_task()
    second_task()


if __name__ == '__main__':
    main()
