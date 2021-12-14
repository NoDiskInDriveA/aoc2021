from itertools import count
from aoc.shared import Array2D

DIM = 10


def increase_neighbors(buffer, x, y):
    updated = False
    for dy in range(y - 1, y + 2):
        for dx in range(x - 1, x + 2):
            if dx == x and dy == y:
                continue
            dx_dy = buffer.get_xy(dx, dy)
            if dx_dy is None or dx_dy == 0:
                continue
            buffer.set_xy(dx, dy, buffer.get_xy(dx, dy) + 1)
            updated = True
    return updated


def simulate_step(buffer: Array2D):
    buffer.apply(lambda n: n + 1)
    while True:
        updated = False

        for y in range(0, buffer.dim):
            for x in range(0, buffer.dim):
                xy = buffer.get_xy(x, y)
                if xy > 9:
                    updated |= increase_neighbors(buffer, x, y)
                    buffer.set_xy(x, y, 0)

        if not updated:
            break

    return buffer.data.count(0)


def get_input() -> Array2D:
    with open('input.txt', 'r') as fp:
        buffer = Array2D(DIM)
        for line in fp:
            buffer.extend([int(c) for c in line.strip()])
    return buffer


def first_task():
    buffer = get_input()
    flashes = 0
    for s in range(0, 100):
        flashes += simulate_step(buffer)
    print('Flashes after 100 steps: %d' % flashes)


def second_task():
    buffer = get_input()
    buffer_length = len(buffer)
    for s in count(1, 1):
        if simulate_step(buffer) == buffer_length:
            print('First step where all flash: %d' % s)
            break


def main():
    first_task()
    second_task()


if __name__ == '__main__':
    main()
