#57.Chapter 3 Exercise 4 - Python tutorial 54
num = input('please enter any 4 digit number : ')
length = len(num)
sum = 0
i = 0
while i < length:
    sum += int(num[i])
    i += 1
print(sum)