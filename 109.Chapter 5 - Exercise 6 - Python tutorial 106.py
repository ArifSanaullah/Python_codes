# 109.Chapter 5 - Exercise 6 - Python tutorial 106

def lists_counter(l):
    count = 0
    for i in l:
        if type(i)==list:
            count += 1
    return count
a = [1,2,3,[1,2,3],[1,2,3],[1,1,3],[1,2,3],[1,2,3],[1,1,3]]
print(lists_counter(a))