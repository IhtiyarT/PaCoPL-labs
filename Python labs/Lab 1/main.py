from math import sqrt
from sys import argv


def get_coef(ind: int, promt: str) -> float:
    try:
        coef = argv[ind]
    except IndexError:
        coef = input(promt)

    while True:
        try:
            return float(coef)
        except ValueError:
            coef = input(promt)


def get_result(a: float, b: float, c: float) -> set:

    result = set()
    try:
        sdisc = sqrt(b * b - 4 * a * c)

        x1 = (-b + sdisc) / (2 * a)
        if x1 > 0:
            result.add(sqrt(x1))
            result.add(-sqrt(x1))

        x2 = (-b - sdisc) / (2 * a)
        result.add(sqrt(x2))
        result.add(-sqrt(x2))
        return result
    except ValueError or TypeError:
        return result


def main():
    a = get_coef(1, "Enter coefficient a: ")
    b = get_coef(2, "Enter coefficient b: ")
    c = get_coef(3, "Enter coefficient c: ")
    result = get_result(a, b, c)
    if result:
        print(result)
    else:
        print("No roots found")


if __name__ == '__main__':
    main()
