# 76.Chapter 4 Exercise 1 - Python tutorial 73
def is_greater(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
num_1,num_2=input("insert two numbers seperated by a coma: ").split(",")
greater = is_greater(num_1,num_2)
print(f'{greater} is greater')