# 153.Lambda Expression - Python tutorial 150

# lambda expression,(anonymus fucntion)

def add(m , n):
    return m + n

# actually lambda experssion is not assigned any vairable name.
# is is used with built in funcions like map, reduce, filter etc
add2 = lambda a , b: a + b
print(add2(5,7))

mult = lambda a,b: a*b
print(mult(3,5))
# fucntions has names below statement will show you the name of funcoin
print(add)
# lambdas has no names below statements will show you this
print(add2)
print(mult)