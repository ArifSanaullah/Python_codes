# 102.Chapter 5 Exercise 3 - Python tutorial 99
# def o_list(l): # o_list = original_list
#    r_list = [] # r_list = reverted_list
#    for i in range(len(l)):
#        popped_item = l.pop()
#        r_list.append(popped_item)
#    return r_list

def abc(r):
    cba = []
    for i in r:
        cba.append(i[::-1])
    return cba
alpha = ["abc","def","ghi"]
print(abc(alpha))
