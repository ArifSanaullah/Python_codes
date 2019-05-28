# 98.Chapter 5 - Exercise 1 - Python tutorial 95
numbers = list(range(1,11))
def sqrList(l):
    sqr = []
    for i in l:
        sqr.append(i*i)
    return sqr
print(sqrList(numbers))