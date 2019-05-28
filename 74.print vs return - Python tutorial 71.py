# 74.print vs return - Python tutorial 71
def add_three(a,b,c):
    return (a+b+c)
add_three(5,5,5)
print(add_three(6,6,6))
# both are same but in case of fuinctions return is better bcz
# often we use such functions that dont have to print anything
# we just use thier value in return in the code