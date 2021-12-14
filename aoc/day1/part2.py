from guppy import hpy
from memory_profiler import profile


def file_window(file, size):
    lst = list()
    for _ in range(size):
        num = file.readline()
        if not num:
            raise ValueError('not enough values in file')
        lst.append(int(num))
    yield lst
    num = file.readline()
    index = 0
    while num:
        lst[index] = int(num)
        yield lst
        index = (index + 1) % size
        num = file.readline()


@profile
def main():
    old = None
    incs = 0
    with open('input.txt', 'r') as fp:
        for number in (sum(window) for window in file_window(fp, 3)):
            if old is not None and old < number:
                incs += 1
            old = number
    print(incs)


if __name__ == '__main__':
    h = hpy()
    h.setref()
    main()
    print(h.heap())
