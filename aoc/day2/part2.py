from guppy import hpy
from memory_profiler import profile


@profile
def main():
    result = {'depth': 0, 'forward': 0, 'aim': 0}
    with open('input.txt', 'r') as fp:
        for direction, amount in ((vals[0], int(vals[1])) for vals in (line.split(' ') for line in fp)):
            result['forward' if direction == 'forward' else 'aim'] += -amount if direction == 'up' else amount
            if direction == 'forward':
                result['depth'] += result['aim'] * amount

    print(result['depth'] * result['forward'])


if __name__ == '__main__':
    h = hpy()
    h.setref()
    main()
    print(h.heap())
