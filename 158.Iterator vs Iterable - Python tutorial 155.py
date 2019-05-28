# 158.Iterator vs Iterable - Python tutorial 155

numbers = [1,2,3,4,5,6] # iterables
sqrs = list(map(lambda a:a**2,numbers)) # iterators
print(sqrs)




# for i in sqrs:

# workinmg of for loop

# 1 call iter function
# 2 iter(numbers)--->iterators
# 3 next (iter(numbers))
#     print(i)


# practicfal working of for loop
numbers_iter = iter(numbers)

print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))


#