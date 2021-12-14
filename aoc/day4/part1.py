from guppy import hpy
from memory_profiler import profile
from shared import read_input


def play(boards, numbers):
    for number in numbers:
        for board in boards:
            board.mark(int(number))
            if board.won:
                return board.sum() * number


@profile
def main():
    print(play(*read_input()))


if __name__ == '__main__':
    h = hpy()
    h.setref()
    main()
    print(h.heap())
