# 187.OOP  Exercise 1 - Python tutorial 185

class Laptop:
    def __init__(self,brand_name,model,price):
        # instance variables
        self.brand_name = brand_name
        self.model = model
        self.price = price
        self.laptop_name = brand_name + ' ' + model


lap1 = Laptop('HP','probook6550b',18000)
lap2 = Laptop('Dell','iSport i3i',17000)

print(lap2.brand_name)
print(lap2.price)
print(lap1.laptop_name)