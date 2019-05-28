# 207.Error raise example 1 - Python tutorial 205

# notImplementedError
# abstract method


class Animal:
    def __init__(self , name):
        self.name = name

    def sound(self):
        raise NotImplementedError("you have to define this method in subclasses")


class Dog(Animal):
    def __init__(self , name , bread):
        super().__init__(name)
        self.bread = bread

    def sound(self):
        return "bhow bhow"


class Cat(Animal):
    def __init__(self , name , bread):
        super().__init__(name)
        self.bread = bread

    def sound(self):
        return "meow meow"


doggy = Dog('russion' , "fastfood")
print(doggy.sound())
