# 171.Decorators Intro - Python tutorial 169

# decprators do increase the functionality of other functions

# @ is used for decorators

def decorator_function( any_funcion):

    quot = "this is awesome function...!!!"

    def wrapper_fucntion():
        str1 = any_funcion
        print (str1())
        return (f"{quot},{str1()}")

    return wrapper_fucntion


@decorator_function
def func1():
    string1 = ("this is function 1")
    return string1


@decorator_function
def func2():
    string2 = ("this is function 2")
    return string2

print(func1())
print(func2())
