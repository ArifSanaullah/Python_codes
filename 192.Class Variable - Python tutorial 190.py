# 192.Class Variable - Python tutorial 190

# class variable

# instance variable already discussed----------> unique variables for an object. ------->
# a variable can be used by only one object

class circle:
    pi = 3.14

    def __init__(self , radius):
        self.radius = radius

    def calc_circumference(self):
        return 2 * circle.pi * self.radius


c = circle(4)
c1 = circle(6)
print(c.calc_circumference())
print(c1.calc_circumference())
