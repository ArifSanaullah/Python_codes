# 137.List comprehension with if else - Python tutorial 134
negative_or_square = [(i**2) if (i%2==0) else (-i) for i in range(1,11)]
print(negative_or_square)