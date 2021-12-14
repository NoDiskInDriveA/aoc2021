from collections.abc import Callable, Iterable
from typing import TypeVar


class Array2D:

    def __init__(self, dim, data=None):
        self.dim = dim
        self.data = data if data is not None else []

    def extend(self, lst: list):
        self.data.extend(lst)

    def get_xy(self, x, y, default=None):
        if (0 <= x < self.dim) and (0 <= y < self.dim):
            index = x + self.dim * y
            return self.data[index]
        return default

    def set_xy(self, x, y, data):
        if (0 <= x < self.dim) and (0 <= y < self.dim):
            index = x + self.dim * y
            self.data[index] = data

    def copy(self):
        return Array2D(self.dim, list(self.data))

    def apply(self, fn: Callable[[int], int]):
        self.data = [fn(n) for n in self.data]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        r = ''
        for y in range(0, self.dim):
            r += ' '.join([str(n).rjust(2, '0') for n in self.data[y * self.dim:(y + 1) * self.dim]]) + "\n"
        return r


T = TypeVar('T')


def partition(seq: Iterable[T], fn: Callable[[T], bool]) -> list[list[T]]:
    """
    Partitions an iterable into two, based on the application of fn on each item
    :param seq: iterable of T
    :param fn: function callable with T as argument, returns True if element goes into first partition, False otherwise
    :return: list of two lists containing the partitions
    """
    a, b = [], []
    for item in seq:
        (a if fn(item) else b).append(item)
    return [a, b]
