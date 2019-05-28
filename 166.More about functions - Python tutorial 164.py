# 166.More about functions - Python tutorial 164

# what are doc strings
# how to write docstring
# how to see docstring
# what is help fucntion

def add(a,b):
    '''this function will take two numbers as input and return their sum'''
    return a+b
print(add.__doc__ )

# len,sum,max,min,sort,sorted,
print(len.__doc__)
print(sum.__doc__)
print(map.__doc__)
print(min.__doc__)
print(max.__doc__)
print(sorted.__doc__)
print(help(sum))