# @print_function_Data

from functools import wraps
def print_func_Data(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        print(f"you are calling {function.__name__} function")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper_function

@print_func_Data
def add(a,b):
    """this function takes two args and adds them and returns sum"""
    return a+b

print(add(4,5))
# output
# you are calling functin
# dock
# sum