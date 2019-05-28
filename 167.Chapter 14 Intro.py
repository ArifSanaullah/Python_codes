# 167.Chapter 14 Intro
# first we sill learn about function/closures in detail
# then finally we sill learn about decoraters


def square(a):
    return a**2

s = square
print(s(7))
print(s)
print(square)
print(s.__name__)
print(square.__name__)