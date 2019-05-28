# 97.More about lists - Python tutorial 94
numbers = list(range(1,11))
# actually the range function in list will create a list like this
# numbers = [1,2,3,4,5,6,7,8,9,10]
#print(numbers)

#print(numbers.pop())

def negativeList(l):
    negative = []
    for i in l:
        negative.append(i*i)
    return negative
print(negativeList(numbers))