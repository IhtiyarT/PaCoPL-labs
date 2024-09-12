# def print_result(func):
#     def wrapped():
#         func_result = func()
#         print(func.__name__)
#         if isinstance(func_result, list):
#             for i in func_result:
#                 print(i)
#         elif isinstance(func_result, dict):
#             for key in func_result:
#                 print(f"{key} = {func_result[key]}")
#         else:
#             print(func_result)
#         return func_result
#     return wrapped


def print_result(func):
    def wrapped(arg):
        func_result = func(arg)
        print(func.__name__)
        print(func_result)
        return func_result
    return wrapped


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


# if __name__ == '__main__':
#     print('!!!!!!!!')
#     test_1()
#     test_2()
#     test_3()
#     test_4()
