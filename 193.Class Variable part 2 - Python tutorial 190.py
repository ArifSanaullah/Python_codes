# 193.Class Variable part 2 - Python tutorial 190

class Laptop:
    disc_percent = 10
    def __init__(self,brand_name,model,price):
        # instance variables
        self.brand_name = brand_name
        self.model = model
        self.price = price
        self.laptop_name = brand_name + ' ' + model

    def off_percentage(self):
        return (self.price) - ((self.disc_percent / 100) * self.price)
# Laptop.disc_percent = 0
lap1 = Laptop('HP','probook6550b',18000)
lap2 = Laptop('Dell','iSport i3i',20000)
lap2.disc_percent = 50

# let suppos that lap2 is conserved with 50% discount let see how it will be done



print(lap2.brand_name)
print(lap2.price)
print(lap1.laptop_name)
print(f"discounted rate of {lap2.brand_name} on {lap2.disc_percent} percent is : {lap2.off_percentage()}")
print(f"discounted rate is : {lap1.off_percentage()}")
print(lap2.__dict__)