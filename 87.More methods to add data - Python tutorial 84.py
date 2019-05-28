# 87.More methods to add data - Python tutorial 84
fruits1 = ['apple','mango']
fruits2 = ['banana','orange']
fruits1.insert(1,'guava')
print(f"this is insert function on string {fruits1}")
fruits = fruits1 + fruits2
print(f"this is string concatination {fruits}")
fruits1.extend(fruits2)
print(f"this is extend function on string {fruits1}")
fruits1.append(fruits2)
print(f"this is append function on string {fruits1}")
