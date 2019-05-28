# 82.Fibonacci series program - Python tutorial 79
def fib(num):
    a=0
    b=1
    if num == 0:
        print(a)
    elif num==1:
        print(b)
    else:
        print(a,b, end=' ')
        for i in range(num-2):
            c=a+b
            a=b
            b=c
            print(b, end=" ")
fib(200)