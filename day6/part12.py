from collections import Counter

BREED_TIMER_ADULT = 6
BREED_TIMER_OFFSPRING = BREED_TIMER_ADULT + 2


def pass_day(fish: dict):
    # could do this in place but...nah
    fish = {k-1: v for k, v in fish.items()}
    fish[BREED_TIMER_ADULT] = fish.get(BREED_TIMER_ADULT, 0) + fish.get(-1, 0)
    fish[BREED_TIMER_OFFSPRING] = fish.get(-1, 0)
    fish.pop(-1, None)
    return fish


def main():
    with open('input.txt') as fp:
        fish = Counter([int(timer) for timer in fp.readline().strip().split(',')])
        for _ in range(0, 80):
            fish = pass_day(fish)
        print(sum(fish.values()))
        for _ in range(80, 256):
            fish = pass_day(fish)
        print(sum(fish.values()))


if __name__ == '__main__':
    main()
