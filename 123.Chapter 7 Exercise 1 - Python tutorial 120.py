#123.Chapter 7 Exercise 1 - Python tutorial 120
def cube_finder(n):
    cube = dict()
    for i in range(1,n+1):
        cube[i] = i**3
    return cube
n = int(input("enter a number: "))
print(cube_finder(n))