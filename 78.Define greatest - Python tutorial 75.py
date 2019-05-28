def greatest(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>a and b>c and b>d:
        return b
    elif c>a and c>b and c>d:
        return c
    else:
        return d
num1,num2,num3,num4 = input("insert 4 coma seperated numbers: ").split(",")
print(greatest(num1,num2,num3,num4))