# 206.Raise errors - Python tutorial 204

def add(a , b):
    if (type(a) is int) and (type(b) is int):
        return a + b
    raise TypeError("oops wrong types of variable are given")


print(add('2' , '5'))
