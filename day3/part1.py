# Binary arithmetic in Python is terrible. Using strings here instead.

from guppy import hpy
from memory_profiler import profile
from numpy import add
from functools import reduce, lru_cache


class BinDigitsCount:
    def __init__(self, digits):
        self.digits = digits

    def __add__(self, other):
        if not isinstance(other, self.__class__) or len(self) != len(other):
            raise ValueError('Cannot add')
        return BinDigitsCount(add(self.digits, other.digits))

    def __len__(self):
        return len(self.digits)

    def __repr__(self):
        return ''.join(map(lambda d: '1' if d > 0 else '0' if d < 0 else 'X', self.digits))

    @classmethod
    def from_bin_string(cls, string):
        return cls(tuple(map(lambda s: 1 if s == '1' else -1, string)))


@lru_cache
def gamma(bitcount):
    return int('0' + repr(bitcount), base=2)


@lru_cache
def epsilon(bitcount):
    return int('0' + ''.join(map(lambda d: '1' if d == '0' else '0' if d == '1' else 'X', repr(bitcount))), base=2)


@profile
def main():
    with open('input.txt', 'r') as fp:
        bin_count = reduce(lambda x, y: x + y, (BinDigitsCount.from_bin_string(line.strip()) for line in fp))
        print(bin_count)
        print('Gamma: %u Epsilon: %u' % (gamma(bin_count), epsilon(bin_count)))
        print('Result: %u' % (gamma(bin_count)*epsilon(bin_count)))


if __name__ == '__main__':
    h = hpy()
    h.setref()
    main()
    print(h.heap())
