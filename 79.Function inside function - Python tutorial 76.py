# 79.Function inside function - Python tutorial 76
def is_greater(a,b):
    if a>b:
        return a
    else:
        return b
def greatest(a,b,c):
    if is_greater(a,b)>c:
        return is_greater(a,b)
    else:
        return c
def new_gratest(a,b,c,d):
    if greatest(a,b,c)> d:
        return (greatest(a,b,c))
    else:
        return (d)
print(new_gratest(801,100,51,5))