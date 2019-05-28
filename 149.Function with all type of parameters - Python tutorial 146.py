# 149.Function with all type of parameters - Python tutorial 146


# argument passing of all types in functions is with this order and it is necessery to follow the order


# PADK
# parameters
# *arguments
# default arguments
# **kwargs

# exampele
def fun(name, *args, age = "unknown", **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)
fun("arif", 1,2,5,8, grade = "graduation",cgpa = "3.4")


# if we want to pass parameters and default parameters thenthe syntax will be:
def fun(name, age = "unknown"):
    print(name)
    print(age)
fun("arif")