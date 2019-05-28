# 173.Decorators part 3 - Python tutorial 171

from functools import wraps
def decorator_function(any_funcion):
    @wraps(any_funcion)
    def wrapper_fucntion(*args,**kwargs):
        """this is wrapper function"""
        print("this is awesome function...!!!")
        return any_funcion(*args,**kwargs)
    return (wrapper_fucntion)
@decorator_function
def add(a,b):
    """this is adding functioon"""
    return a+b
print(add.__doc__)
print(decorator_function.__doc__)