# 88.Delete data from list - Python tutorial 85
fruits = ['mango', 'apple', 'orange', 'banana', 'guava', 'kiwi']
# pop method takes one or no argument. as if any arfument is passed it will remove selected index number
# else the last one in the list
print(f'this is the real list: {fruits}')
fruits.pop(2)
print(f'this is the pop method: {fruits}')
# del also does the same work as pop
del fruits[2]
print(f'this is the del method: {fruits}')
# remove method takes the item name as a argument not the index number with this we do not need to know about the
# index number it wi;; simply remove the typed item
fruits.remove('kiwi')
print(f'this is the remove method: {fruits}')