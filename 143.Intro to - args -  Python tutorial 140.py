# 143.Intro to - args -  Python tutorial 140
# *operator
# *args


# def total(a,b):
#     return a+b
# print(total(2,5))


# using *args operator we can insert as many argumens as we want into the funtion this all just bcz of " * " used
# before args not bcz of the word "args" used after " * ". "args" is just a variable name it can be replaced by any other
def all_total(*args):
    total = 0
    for nums in args:
        total += nums
    return total
print(all_total(1,2,3,3,4,5,8))