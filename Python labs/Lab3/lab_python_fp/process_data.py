import json
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from field import field
from gen_random import gen_random

path = "../data_light.json"

with open(path, encoding='utf8') as f:
    data = json.load(f)


@print_result
def f1(arg) -> list:
    return sorted([str(x) for x in Unique(field(arg, "job-name"), ignore_case=True)])


@print_result
def f2(arg: list):
    return list(filter(lambda x: x.startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    return [f"{job_name}, зарплата {salary} руб." for job_name, salary in zip(arg, salaries)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
