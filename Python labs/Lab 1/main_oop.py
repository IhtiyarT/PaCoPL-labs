from math import sqrt
from sys import argv


class BiSquareCalculator:
    def __init__(self):
        self.roots = set()
        self.a_coef = 0.0
        self.b_coef = 0.0
        self.c_coef = 0.0

    def get_coef(self, ind, promt):
        try:
            coef = argv[ind]
        except IndexError:
            coef = input(promt)

        while True:
            try:
                return float(coef)
            except ValueError:
                coef = input(promt)

    def get_coefs(self):
        self.a_coef = self.get_coef(1, "Enter coef a: ")
        self.b_coef = self.get_coef(2, "Enter coef b: ")
        self.c_coef = self.get_coef(3, "Enter coef c: ")

    def find_roots(self):
        try:
            sdisc = sqrt(self.b_coef * self.b_coef - 4 * self.a_coef * self.c_coef)

            x1 = (-self.b_coef + sdisc) / (2 * self.a_coef)
            if x1 > 0:
                self.roots.add(sqrt(x1))
                self.roots.add(-sqrt(x1))

            x2 = (-self.b_coef - sdisc) / (2 * self.a_coef)
            self.roots.add(sqrt(x2))
            self.roots.add(-sqrt(x2))
        except ValueError or TypeError:
            return

    def print_roots(self):
        if self.roots:
            print(self.roots)
        else:
            print("No roots")


def main():
    calc = BiSquareCalculator()
    calc.get_coefs()
    calc.find_roots()
    calc.print_roots()
    return 0


if __name__ == "__main__":
    main()
