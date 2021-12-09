from guppy import hpy
from memory_profiler import profile
from shared import read_input


def play_terribly(boards, numbers):
    last_board = None
    for number in numbers:
        for board in boards:
            board.mark(int(number))
            last_board = board
        boards = list(filter(lambda b: not b.won, boards))
        if len(boards) == 0:
            assert(last_board is not None)
            return last_board.sum()*number


@profile
def main():
    print(play_terribly(*read_input()))


if __name__ == '__main__':
    h = hpy()
    h.setref()
    main()
    print(h.heap())
