from functools import lru_cache
import math


def cost_fn_linear(to, positions):
    return sum([abs(p - to) for p in positions])


@lru_cache(maxsize=None)
def _cost_fn_sum_item(to, position):
    return int(abs(position - to) * (abs(position - to) + 1) / 2)


def cost_fn_sum(to, positions):
    return sum([_cost_fn_sum_item(to, p) for p in positions])


def brute_force(positions: list, cost_fn):
    result = []
    for where in range(min(positions), max(positions) + 1):
        result.append(cost_fn(where, positions))

    return min(result)


def bin_force(positions: list, cost_fn):
    return _bin_force(positions, cost_fn, min(positions), max(positions) + 1)


def _bin_force(positions: list, cost_fn, start: int, end: int):
    pivot = math.floor((end + start)/2)
    start_sum = cost_fn(start, positions)
    if start == end:
        return start_sum
    end_sum = cost_fn(end, positions)
    if start_sum < end_sum:
        return _bin_force(positions, cost_fn, start, pivot)
    else:
        return _bin_force(positions, cost_fn, pivot, end)


def main():
    with open('input.txt', 'r') as fp:
        positions = [int(pos) for pos in fp.readline().split(',')]
        # part 1
        print(brute_force(positions, cost_fn_linear))
        print(bin_force(positions, cost_fn_linear))
        # part 2
        print(brute_force(positions, cost_fn_sum))
        print(bin_force(positions, cost_fn_sum))


if __name__ == '__main__':
    main()
