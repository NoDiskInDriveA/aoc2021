from collections import Counter, defaultdict


def get_input() -> tuple[str, list[str], dict[str,str]]:
    with open('input.txt', 'r') as fp:
        first = fp.readline().strip()
        start = [first[i:i + 2] for i in range(0, len(first) - 1)]
        fp.readline()
        rules = {pattern: insert for (pattern, insert) in (line.strip().split(' -> ') for line in fp)}
        return first, start, rules


def simulate_step(pairs: dict[str, int], rules: dict[str,str]) -> dict[str, int]:
    nxt = Counter(pairs)
    for pair in list(pairs.keys()):
        if pair in rules:
            nxt[(pair[0] + rules[pair])] += pairs[pair]
            nxt[(rules[pair] + pair[1])] += pairs[pair]
            nxt[pair] -= pairs[pair]
    return nxt


def letter_count_maxmin_diff(pairs: dict[str, int], first_letter: str, last_letter: str):
    counter = defaultdict(int)

    # each letter from the sequence appears in exactly two pairs,
    # except for the first and last of the original input (which were never duplicated)
    counter.update({first_letter: 1, last_letter: 1})
    for pair, count in pairs.items():
        counter[pair[0]] += count
        counter[pair[1]] += count

    counter = counter.values()
    return int((max(counter) - min(counter)) / 2)


def run(steps):
    original, pair_count, rules = get_input()
    pairs = Counter(pair_count)

    for step in range(0, steps):
        pairs = simulate_step(pairs, rules)

    print(letter_count_maxmin_diff(pairs, original[0], original[-1]))


def first_task():
    run(10)


def second_task():
    run(40)


def main():
    first_task()
    second_task()


if __name__ == '__main__':
    main()
