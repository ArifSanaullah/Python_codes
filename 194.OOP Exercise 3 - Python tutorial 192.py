# 194.OOP Exercise 3 - Python tutorial 192

class Person:
    count_instance = 0
    def __init__(self,first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('arif','sanaullah', 25)
p2 = Person('arif','sanaullah', 25)
p3 = Person('arif','sanaullah', 25)
print(Person.count_instance)