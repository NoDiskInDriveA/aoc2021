from collections import Counter


def pass_day(fish: dict):
    fish = {k-1: v for k, v in fish.items()}

    fish[6] = fish.get(6, 0) + fish.get(-1, 0)
    fish[8] = fish.get(-1, 0)
    fish.pop(-1, None)
    return fish


def main():
    with open('input.txt') as fp:
        fish = Counter([int(age) for age in fp.readline().strip().split(',')])
        for _ in range(0, 256):
            fish = pass_day(fish)
        print(sum(fish.values()))


if __name__ == '__main__':
    main()
