# 176.Exercise 1 solution - Python tutorial 174

from functools import wraps
import time


def time_calc(function):
    @wraps(function)
    def wrapper_function(*args , **kwargs):
        t_start = time.time()
        print(f"executing {function.__name__} function ...")
        returned_value = function(*args , **kwargs)
        t_end = time.time()
        total_time_consumed = t_end - t_start
        print(f"this {function.__name__} function took {total_time_consumed} secs to execute")
        return returned_value

    return wrapper_function


@time_calc
def square_finder(n):
    return [ i ** 2 for i in range(1 , n + 1) ]


print(square_finder(5))
