# 100.Chapter 5 - Exercise 2 - Python tutorial 97
#def revert_list(l):
#    l.reverse()
#    return l
#numbers = [1,2,3,4,5,6]
#print(revert_list(numbers))


def o_list(l): # o_list = original_list
    r_list = [] # r_list = reverted_list
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list
n = [1,2,3,4,5,6]
print(o_list(n))
