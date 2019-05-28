# 151.Exercise 2 Solution - Python tutorial 148





def func(l, **kwargs):
    # s = str(l)
    if kwargs.get('reverse_str') == True:
        return[a[::-1] for a in l]
    else:
        return[a for a in l]


l = ['Arif Khan','123']
print(func(l, reverse_str = True))





def add(*args):
    total = 0
    for num in args:
        total += num
    return total

n = (1,2,1,3,5,6,8,10.5,0j)
print(add(*n))