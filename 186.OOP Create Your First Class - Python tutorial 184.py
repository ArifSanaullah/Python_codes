# 186.OOP Create Your First Class - Python tutorial 184

# objectives
# what is class
# how to create class
# what is init method, constructer
# what are attributes,instance variables
# how to create our object

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print("init method/constructer is called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('arif', 'khan', 22)
p2 = Person('leonard', 'randy', 25)
print(p1.first_name)
print(p2.first_name)
