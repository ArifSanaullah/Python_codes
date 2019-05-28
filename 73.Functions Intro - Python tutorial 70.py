# 73.Functions Intro - Python tutorial 70
# name = "sanaullah"
# print(len(name))


#a,b = [int(x) for x in input('enter two coma seperated numbers: ').split(',')]
#def add_two(a,b):
#    return a+b
#total = add_two(a,b)
#print(total)


first_name, last_name = input('enter your fist name and last name septerated by a coma: ').split(',')
def add_two(first_name, last_name):
    return (first_name + last_name)
print(add_two(first_name, last_name))