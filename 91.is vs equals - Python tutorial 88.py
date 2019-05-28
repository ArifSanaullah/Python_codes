# 91.is vs equals - Python tutorial 88
fruits1 = [ 'orange','mango', 'mango', 'kiwi', 'guava', 'filter', 'banana', 'apple']
fruits2 = ['mango', 'kiwi', 'guava', 'filter']
fruits3 = ['mango', 'kiwi', 'guava', 'filter']
print(fruits1 == fruits2)
print(fruits2 == fruits3)
# "is" keyword cheks the location at which the lists are stored are those same or not while == cheks wether content of
# the list is same or not
print(fruits2 is fruits3)