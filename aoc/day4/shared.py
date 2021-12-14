import re
import numpy as np


class Board:

    def __init__(self, matrix):
        self.matrix = matrix
        self._update_win()

    def __repr__(self):
        return repr(self.matrix)

    @classmethod
    def create(cls, size, data):
        matrix = np.array(data, dtype=np.int32)
        assert matrix.shape == (size, size)
        return Board(matrix)

    def _update_win(self):
        self.won = np.any(np.all(self.matrix == -1, axis=0)) or np.any(np.all(self.matrix == -1, axis=1))
        pass

    def mark(self, number):
        self.matrix = np.where(self.matrix == number, -1, self.matrix)
        self._update_win()

    def sum(self):
        return np.sum(np.where(self.matrix > 0, self.matrix, 0))


def chunks(seq):
    last_index = 0
    for index in (k for k, v in enumerate(seq) if v.strip() == ''):
        if last_index != index:
            yield seq[last_index + 1:index]
            last_index = index


def read_input():
    with open('input.txt', 'r') as fp:
        drawn = (int(n) for n in fp.readline().strip().split(','))
        boards = []
        for c in chunks(fp.readlines()):
            boards.append(Board.create(len(c), [re.split('\\s+', line.strip()) for line in c]))
        return boards, drawn
