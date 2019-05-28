# 113.More about tuples - Python tutorial 110
#loopin in tuples
#tuple with onlyy one element
# tuple unpacking
# list inside tuple
# some fucntions that can be done with tuples
mixed = (1,2,3.5)
type(mixed)
#for i in mixed:
 #   print(i)
 #NOTE: we can use while loop too.
# this is only int not a tuple with one element ------>   nums = (1)
# tuple with one element is following:
num = (1,)
#print(type(num))
word = ('word',)
#print(type(word))



#tuples without paranthesis
name = ('arif','sana','ali','tania','danish')
(p1,p2,p3,p4,p5) = (name)
#print(p1)


# list inside a tuple
favorites = ('a','b',['arif','sanaullah'])
favorites[2].pop(0)
favorites[2].append("its me")
#print(favorites)

#min( max( sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))