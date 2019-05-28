# 144.- args with normal parameter -  Python tutorial 141

def multiply(num1 , *args):
    print(num1)
    print(args)
    multiple = 1
    for i in args:
        multiple *= i
    return multiple


print(multiply(10 , 2 , 3))
