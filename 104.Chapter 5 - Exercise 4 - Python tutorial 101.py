# 104.Chapter 5 - Exercise 4 - Python tutorial 101

def dev(l):
    even_list = []
    odd_list = []
    for i in l:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    output = [odd_list, even_list]
    return output
a = range(15)
print(dev(a))