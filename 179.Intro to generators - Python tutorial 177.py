# 179.Intro to generators - Python tutorial 177

# generators
# generators are iterators

# generators work on a single element in alist while list works on all elements
# generators are used when we are concerened with a single or two elements of list while lists are useed when we are conncerened
# with all elements of list

l = [1,2,3]   #iterable

# for i in l:
#     print(i)

# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))

# next(l)------>will give an error----->TypeError: 'list' object is not an iterator
# for num in map(lambda a:a**2,l): #iterator
#     print(num)

