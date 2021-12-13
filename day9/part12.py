from collections import namedtuple
from functools import reduce

Coords = namedtuple('Coords', ['x', 'y'])


class Array2D:

    def __init__(self, dim):
        self.dim = dim
        self.data = []

    def extend(self, lst: list):
        self.data.extend(lst)

    def get_xy(self, x, y):
        if (0 <= x < self.dim) and (0 <= y < self.dim):
            index = x + self.dim * y
            return self.data[index]
        return 10


visited = set()


def rec_get_basin(buf, coords: Coords):
    if coords in visited:
        return {}

    visited.add(coords)
    xy = buf.get_xy(coords.x, coords.y)
    if xy >= 9:
        return {}

    return {coords} \
        .union(rec_get_basin(buf, Coords(coords.x - 1, coords.y))) \
        .union(rec_get_basin(buf, Coords(coords.x + 1, coords.y))) \
        .union(rec_get_basin(buf, Coords(coords.x, coords.y - 1))) \
        .union(rec_get_basin(buf, Coords(coords.x, coords.y + 1)))


def main():
    with open('input.txt', 'r') as fp:
        buf = Array2D(100)
        for line in fp.readlines():
            buf.extend([int(char) for char in line.strip()])

    risklevel_sum = 0
    basin_sizes = []
    for y in range(0, buf.dim):
        for x in range(0, buf.dim):
            xy = buf.get_xy(x, y)
            if buf.get_xy(x - 1, y) > xy and buf.get_xy(x + 1, y) > xy and \
                    buf.get_xy(x, y - 1) > xy and buf.get_xy(x, y + 1) > xy:
                risklevel_sum += xy + 1
                basin_sizes.append(len(rec_get_basin(buf, Coords(x, y))))

    print('Risklevel sum: %d, Basinity: %s' % (risklevel_sum, reduce(lambda c, s: c * s, sorted(basin_sizes)[-3:], 1)))


if __name__ == '__main__':
    main()
