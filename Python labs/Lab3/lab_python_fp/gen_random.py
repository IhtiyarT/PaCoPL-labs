from random import randint, seed
from time import time


def gen_random(num_count, begin, end):
    seed(time())
    result = []
    for i in range(num_count):
        result.append(randint(begin, end))
    return result


# print(gen_random(5, 1, 3))
