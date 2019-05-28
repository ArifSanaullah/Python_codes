# 84.Variable Scope - Python tutorial 81
x=6
def func():
    global x
    x=5
    return x
print(x)
print(func())
print(x)