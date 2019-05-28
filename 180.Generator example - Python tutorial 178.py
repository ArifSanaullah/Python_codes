# 180.Generator example - Python tutorial 178

# create our first generator with generator function

# 1.) generator functtion
# 2.) generator comprehension------> after 2 3 lecturs

# define a function that print numbers from 1 to 10

def num(n):
    for i in range(1,n+1):
        yield i

numbers = num(10)
for num in numbers:
    print(num)
# for num in numbers:
#     print(num)

# memory ----->  list-----> [.............]
# memory ----->  genr-----> [single element which is required at the time]

# for number in (num(10)):
#     print(number)