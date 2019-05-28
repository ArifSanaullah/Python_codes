fruits = ['mango','filter', 'mango', 'apple', 'orange', 'banana', 'guava', 'kiwi']
print(fruits.count('mango'))
#sort method sorts the original list while sorted function only sorts the list but our original list remains the same
print(sorted(fruits))
fruits.sort()
print(fruits)
print(fruits.reverse())
fruits_copy = fruits.copy()*2
print(fruits_copy)
fruits.clear()
print(fruits)