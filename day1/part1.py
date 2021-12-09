from guppy import hpy
from memory_profiler import profile


@profile
def main():
    old = None
    incs = 0
    with open('input.txt', 'r') as fp:
        for number in (int(line) for line in fp):
            if old is not None and old < number:
                incs += 1
            old = number

    print(incs)


if __name__ == '__main__':
    main()
    h = hpy()
    h.setref()
    print(h.heap())
