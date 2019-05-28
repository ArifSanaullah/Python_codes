# 189.OOP Instance Methods - Python tutorial 187

# instance methods

l = [1,2,3]

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name } {self.last_name}"
    def is_18(self):
        return self.age>18
p1 = Person('arif','khan',22)
print(p1.full_name())
print(p1.is_18())
