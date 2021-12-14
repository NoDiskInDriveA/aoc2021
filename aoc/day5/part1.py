from collections import namedtuple, defaultdict
import re

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['start', 'end'])

MAX_DIM = 1000


def it_range(a, b):
    ret = range(a, b-1, -1) if (b < a) else range(a, b+1, 1)
    return ret


def increase_points_on_line(field, line: Line, allow_diagonal=False):
    if line.start.x != line.end.x:
        if line.start.y != line.end.y:
            if allow_diagonal:
                for (x, y) in zip(it_range(line.start.x, line.end.x), it_range(line.start.y, line.end.y)):
                    index = MAX_DIM * x + y
                    field[index] = field[index] + 1
        else:
            for x in it_range(line.start.x, line.end.x):
                index = MAX_DIM * x + line.start.y
                field[index] = field[index] + 1
    else:
        for y in it_range(line.start.y, line.end.y):
            index = MAX_DIM * line.start.x + y
            field[index] = field[index] + 1


def create_line(line):
    x1, y1, x2, y2 = re.split(',| -> ', line.strip())
    return Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))


def main():
    with open('input.txt') as fp:
        lines = (create_line(input_line) for input_line in fp)

        field = defaultdict(int)
        for line in lines:
            increase_points_on_line(field, line, False)

        print(len(list(filter(lambda v: v > 1, field.values()))))


if __name__ == '__main__':
    main()
