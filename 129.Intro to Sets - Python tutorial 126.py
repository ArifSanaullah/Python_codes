# 129.Intro to Sets - Python tutorial 126
# sets are used to strea rando,ly items
# set can not store listz tuples or dicts inside themselves
# set can store any data typw like int float string etc
# repetition is not allowed in sets
# there is no indexing in sets
s = {1,2,3,2}
#print(s)
#print(s[1]) . to
# if we have a list of many items that are same then we can remove those same items by converting the list to set and
# converting the set back to list
l = [1,2,3,4,5,6,1,2,3,4,6,1,2,3,4,5,6]
#print(l)
s2 = list(set(l))
#print(s2)
#s.add(4)
#print(s)
#s.remove(3)
#print(s)
# if an item is not availablw in set then remove method will give an  error. to avoid this we can use discard method
s.discard(5)
print(s)
# we can make a copy of set
s3 = s.copy()
#print(s3)
