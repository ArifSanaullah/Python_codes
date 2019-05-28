#48.Chapter 3 - Exercise 2 - Python tutorial 45
#watch coco movie code
name, age = input("please input your name and age seperated by a coma : ").split(",")
age = int(age)
if name[0] == "a" or "A":
    print("name is valid")
elif name[0] != "a" or "A":
    print("invalid name")
elif age>10:
    print("you can watch")
else:
    print("you can not watch")