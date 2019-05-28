# 198.OOP Static Method - Python tutorial 196

class Person:
    count_instance = 0  # class variable/class attribute

    def __init__(self , first_name , last_name , age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls , string):
        first_name , last_name , age = string.split(",")
        return cls(first_name , last_name , age)

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} objects of {cls.__name__} class"
    @staticmethod
    def hello():
        return "static method called"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age > 18


p1 = Person('arif' , 'khan' , 21)
p2 = Person('arf' , 'han' , 17)
p3 = Person.from_string('arif,sanaullah,27')
print(Person.hello())