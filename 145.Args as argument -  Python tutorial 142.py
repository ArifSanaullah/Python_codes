# 145.Args as argument -  Python tutorial 142

def multiply_nums(*args):
    multiply = 1
    for num in args:
        multiply *= num
    return multiply


# if we want to pass a list/tuple of args in function then we will use * before the name of list and then items of list will be
# treated as single else in output we will get a single list as we input into the function


a = (1.2,3,5,8,2.1)
print(multiply_nums(a))
print(multiply_nums(*a)) # this method is called list unpacking