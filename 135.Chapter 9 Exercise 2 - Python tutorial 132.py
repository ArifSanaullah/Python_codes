# 135.Chapter 9 Exercise 2 - Python tutorial 132
def retturn_String(l):
    mylist  = [i for i in l if ((type(i)) == int or (type(i)) == float or (type(i)) == str)]
    return mylist
print(retturn_String([True, False, [1,2],{3,4},"abc",("false","ali"),1,2,2.5,3.7]))