# 106.Chapter 5 - Exercise 5 - Python tutorial 103

def same_items(lst1,lst2):
    output = []
    for i in lst1:
        if i in lst2:
            output.append(i)
    return output
print(same_items([1,3,5,7],[2,4,1,3,7]))