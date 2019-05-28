# 196.OOP Class Methods - Python tutorial 194

class Person:
    count_instance = 0   #class variable/class attribute
    def __init__(self,first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return (f"you have created {cls.count_instance} objects of {cls.__name__} class")


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
        return self.age>18

p1 = Person('arif','khan',21)
p2 = Person('arf','han',17)
# "you have created 4 instances of Person class"

print(Person.count_instances())
print(Person.full_name(p1))
print(Person.is_above_18(p2))