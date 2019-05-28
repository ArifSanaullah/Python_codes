# 177.Decorators Practice 2 - Python tutorial 175
from functools import wraps

def only_int(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        data_types = []
        if all([type(arg) == int for arg in args]):
            return function(*args,**kwargs)
        return "Invalid Argument"

        # for arg in args:
        #     data_types.append(type(arg) == int)
        # if all(data_types):
        #     return function(*args, **kwargs)
        # else:
        #     return "invalid argument"
    return wrapper_function

@only_int
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1,2,3,4))
print(add_all(1,2,3,4,[1,2]))