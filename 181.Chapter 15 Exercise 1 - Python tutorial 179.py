# 181.Chapter 15 Exercise 1 - Python tutorial 179

def evens(n):
    for num in range(2,n+1,2):
        yield num


for i in evens(100):
    print(i)
