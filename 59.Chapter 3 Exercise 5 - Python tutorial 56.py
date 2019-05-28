# 59.Chapter 3 Exercise 5 - Python tutorial 56
name = input('enter your name please ......: ')
length = len(name)
all_freq = {}
for i in  name:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq = 1
print('count of all characters in is :' )