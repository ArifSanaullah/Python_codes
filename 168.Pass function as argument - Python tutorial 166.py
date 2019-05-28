# 168.Pass function as argument - Python tutorial 166


def sqre(a):
    return a ** 2


l = [ 1 , 2 , 3 , 4 ]

print(list(map(sqre , l)))
k = [ 1 , 2 , 3 , 4 ]


def my_map(func , l):
    new_lst = [ ]
    for item in l:
        new_lst.append(func(item))
        return new_lst


print(my_map(sqre, l))
print(list(map(lambda a : a**2, l)))