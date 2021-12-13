class DisplaySolver:

    unambiguous = {
        2: 1,
        3: 7,
        4: 4,
        7: 8,
    }

    solved: dict
    unsolved: list
    displaying: list

    def __init__(self, unsolved, displayed):
        self.unsolved = unsolved
        self.displaying = displayed
        self.solved = {}
        self.find_unambiguous()
        self.find(3, 5, lambda cmb, slvd: len(cmb.union(slvd[1])) == 5)
        self.find(9, 6, lambda cmb, slvd: len(cmb.union(slvd[3])) == 6)
        self.find(0, 6, lambda cmb, slvd: len(cmb.union(slvd[1])) == 6)
        self.find(6, 6)
        self.find(5, 5, lambda cmb, slvd: len(cmb.union(slvd[6])) == 6)
        self.find(2, 5)

    def find_unambiguous(self):
        for combination in self.unsolved:
            ln = len(combination)
            if ln in self.unambiguous:
                self.solved[self.unambiguous[ln]] = combination

        for combination in self.solved.values():
            self.unsolved.remove(combination)

    def find(self, digit, length, constraint=lambda c, s: True):
        for combination in self.unsolved:
            if len(combination) == length:
                if constraint(combination, self.solved):
                    self.solved[digit] = combination
                    self.unsolved.remove(combination)
                    return

    def get_displayed_number(self):
        digits = ''
        for d in self.displaying:
            for s in self.solved:
                if self.solved[s] == d:
                    digits += str(s)
        return digits

    def get_displayed_segments(self):
        return ' '.join([''.join(sorted(list(d))) for d in self.displaying])

    def __repr__(self):
        return self.get_displayed_segments() + ' => ' + self.get_displayed_number()

    @classmethod
    def from_string(cls, observed, displayed):
        return cls(
            [set(o) for o in observed.split(' ')],
            [set(d) for d in displayed.split(' ')]
        )


def main():
    with open('input.txt', 'r') as fp:
        inp = (line.strip().split(' | ') for line in fp)
        simple_count, sum_all = 0, 0
        for display in (DisplaySolver.from_string(observed, displayed) for (observed, displayed) in inp):
            print(display)
            digits = display.get_displayed_number()
            simple_count += digits.count('1') + digits.count('4') + digits.count('7') + digits.count('8')
            sum_all += int(digits)

        print('Amount of 1,4,7,8: %d, Sum of numbers: %d' % (simple_count, sum_all))


if __name__ == '__main__':
    main()
