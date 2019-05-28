# 178.Decorators with arguments - Python tutorial 176

from functools import wraps

def only_allowed_dataType(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper_function(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            return "Invalid Argument"
        return wrapper_function
    return decorator

@only_allowed_dataType(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_join('arif ', 'khan','a '))