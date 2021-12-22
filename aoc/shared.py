from collections import defaultdict
from collections.abc import Callable, Iterable, Hashable
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
U = TypeVar('U', bound=Hashable)


def partition(seq: Iterable[T], fn: Callable[[T], U]) -> dict[U, list[T]]:
    """
    Partitions an iterable multiple lists, depending on the result of fn called on each item
    :param seq: iterable of T
    :param fn: function callable with T as argument, returns partition key
    :return: list of two lists containing the partitions
    """
    partitions = defaultdict(list)
    for item in seq:
        partitions[fn(item)].append(item)
    return dict(partitions)
