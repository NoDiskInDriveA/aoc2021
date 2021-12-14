# Giving up on using file pointers...

from guppy import hpy
from memory_profiler import profile


def rec_partition(lines, pred_fn, where=0):
    if len(lines) <= 1:
        return lines
    return rec_partition(
        pred_fn(
            list(filter(lambda line: line[where] == '0', lines)),
            list(filter(lambda line: line[where] == '1', lines))
        ),
        pred_fn,
        where + 1
    )


def pred_mcv(part_zero, part_one):
    return part_zero if (len(part_zero) > len(part_one)) else part_one


def pred_lcv(part_zero, part_one):
    return part_one if (len(part_one) < len(part_zero)) else part_zero


@profile
def main():
    with open('input.txt', 'r') as fp:
        lines = [line.strip() for line in fp.readlines()]

    ox = int(rec_partition(lines, pred_mcv).pop(), base=2)
    co = int(rec_partition(lines, pred_lcv).pop(), base=2)
    print('%u', ox*co)


if __name__ == '__main__':
    h = hpy()
    h.setref()
    main()
    print(h.heap())
