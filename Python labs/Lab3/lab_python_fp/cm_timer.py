from time import time, sleep
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.__start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        work_time = time() - self.__start_time
        print(f"time: {round(work_time, 2)}")


@contextmanager
def cm_timer_2():
    start_time = time()
    try:
        yield start_time
    finally:
        work_time = time() - start_time
        print(f"time: {round(work_time, 2)}")


# with cm_timer_2():
#     sleep(5.5)
