# 156.Map function- Python tutorial 153

# map functions

numbers = [ 1 , 2 , 3 , 4 , 5 ]


# with map function
def sqr(n):
    return n ** 2


sqrs = list(map(sqr , numbers))
print(sqrs)

# with lambda expression
sqrs2 = list(map(lambda n: n ** 2 , numbers))
print(sqrs2)

# with list comorehension
sqrs3 = list(i**2 for i in numbers)
print(sqrs3)