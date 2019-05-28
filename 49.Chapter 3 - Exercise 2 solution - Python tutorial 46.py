#48.Chapter 3 - Exercise 2 - Python tutorial 45
#watch coco movie code
name, age = input("please input your name and age seperated by a coma : ").split(",")
age = int(age)
if age >= 10 and ((name[0] == "a") or (name[0]=="A")):
    print('you can watch the coco movie')
else:
    print("you can not watch coco movie")