# 190.OOP EXERCISE 2 - Python tutorial 188

class Laptop:
    disc_percent = 10
    def __init__(self,brand_name,model,price):
        # instance variables
        self.brand_name = brand_name
        self.model = model
        self.price = price
        self.laptop_name = brand_name + ' ' + model

    def off_percentage(self):
        return (self.price) - ((Laptop.disc_percent / 100) * self.price)

lap1 = Laptop('HP','probook6550b',18000)
lap2 = Laptop('Dell','iSport i3i',20000)

print(lap2.brand_name)
print(lap2.price)
print(lap1.laptop_name)
print(f"discounted rate for {lap2.brand_name} is : {lap2.off_percentage()}")
print(f"discounted rate is : {lap1.off_percentage()}")