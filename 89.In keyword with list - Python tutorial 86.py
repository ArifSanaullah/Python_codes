# 89.In keyword with list - Python tutorial 86
fruits = ['mango', 'apple', 'orange', 'banana', 'guava', 'kiwi']
add_fruit = input("enter the name of fruit you weant to add to list: ")
if add_fruit in fruits:
    print("the fruit you entered is already in the list")
else:
    fruits.insert(0,add_fruit)
print(fruits)