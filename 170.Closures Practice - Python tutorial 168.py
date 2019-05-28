# 170.Closures Practice - Python tutorial 168

# square
# cube
# x**4

def to_power(power):
    """this function will take a number as power and second number to calculate the power of that number
    and will return number to the power given"""
    def calc_power(num):
        return num**power
    return calc_power

cube = to_power(3)
print(cube(5))

square = to_power(2)
print(square(5))