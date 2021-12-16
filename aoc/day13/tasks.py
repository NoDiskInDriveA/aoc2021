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


def fold(points: set[Point], f: Fold) -> set[Point]:
    if f.axis == 'x':
        return set(map(lambda p: Point(2 * f.position - p.x if p.x >= f.position else p.x, p.y), points))
    elif f.axis == 'y':
        return set(map(lambda p: Point(p.x, 2 * f.position - p.y if p.y >= f.position else p.y), points))
    else:
        raise ValueError('Unknown axis %s' % f.axis)


def display_points(points: set[Point], scale_x: int = 1):
    (max_x, max_y) = reduce(lambda c, p: Point(max(c.x, p.x), max(c.y, p.y)), points)
    display = ''
    for y in range(0, max_y + 1):
        display += ''.join(
            ['▓' * scale_x if Point(x, y) in points else ' ' * scale_x for x in range(0, max_x + 1)]) + "\n"
    print(display)


def main():
    points, folds = get_input()
    points = fold(points, folds[0])
    print(len(points))
    for f in folds[1:]:
        points = fold(points, f)
    display_points(points)


if __name__ == '__main__':
    main()
