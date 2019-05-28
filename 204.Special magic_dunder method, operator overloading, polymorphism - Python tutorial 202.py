# 204.Special magic_dunder method, operator overloading, polymorphism - Python tutorial 202

# SPECIAL MAGIC METHODS
# operator overloading
# polymorphism - method overriding

class Phone:
    def __init__(self,brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def phone_name(self):
        return f"{self.brand} {self.model}"
#     __str__      ,__repr__

    def __str__(self):
        return f"{self.brand} {self.model} and price is  {self.price}"


    def __repr__(self):
        return f"phone ({self.brand} {self.model} {self.price})"

    def __len__(self):
        return len(self.phone_name())
    def __add__(self, other):
        return self.price + other.price





# l = [1,2,3]
# print(len(l))
# t = (1,2,3)
# print(len(t))
# s = "arif"
# print(len(s))
my_phone = Phone('nokia','3310',1500)
my_phone2 = Phone('noki','310',150)
print(my_phone+my_phone2)
# print(len(my_phone))
# print(repr(my_phone))
# print(my_phone.__repr__())


