# 132.Chapter 9 Exercise 1 - Python tutorial 129
def return_reverse(l):
    return [(i[::-1]) for i in l]
l = ['abc','def','ghi']
print(return_reverse(l))