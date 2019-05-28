# 172.Decorators Part 2 - Python tutorial 170

def decorator_function(any_funcion):
    def wrapper_fucntion(*args,**kwargs):
        print("this is awesome function...!!!")
        return any_funcion(*args,**kwargs)
    return (wrapper_fucntion)

@decorator_function
def func(a):
    print(f"this is function with argument {a}")
func()

@decorator_function
def add(a,b):
    return a+b
print(add(2,3))